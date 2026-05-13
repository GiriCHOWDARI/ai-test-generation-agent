import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from schemas import GeneratedTest
from agents.parser_agent import extract_routes
from agents.prompt_builder_agent import build_prompt
from agents.llm_agent import generate_tests
from agents.validation_agent import validate_syntax
from agents.dedup_agent import remove_duplicates
from agents.file_writer_agent import write_test_files
from agents.evaluation_agent import run_pytest

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- In‑memory state ----
stats = {
    "generated_tests": 0,
    "runnable_tests": 0,
    "pass_rate": 0,
    "api_routes": 0,
}

pipeline_steps = [
    "Source Parser", "Prompt Builder", "LLM Generation",
    "Pydantic Validation", "AST Verification", "Duplicate Filtering",
    "File Writer", "Evaluation Harness"
]

jobs = []
logs = []
latest_source_code: str = ""
latest_filename: str = ""

# ---- Helper: strip markdown fences from LLM output ----
def extract_python_code(text: str) -> str:
    text = text.strip()
    if text.startswith("```python"):
        text = text[len("```python"):]
    elif text.startswith("```"):
        text = text[len("```"):]
    if text.endswith("```"):
        text = text[:-len("```")]
    return text.strip()

# ---- API endpoints ----
@app.get("/api/stats")
async def get_stats():
    return stats

@app.get("/api/pipeline")
async def get_pipeline():
    return pipeline_steps

@app.get("/api/jobs")
async def get_jobs():
    return jobs

@app.get("/api/logs")
async def get_logs():
    return logs

@app.post("/api/upload")
async def upload_project(file: UploadFile = File(...)):
    global latest_source_code, latest_filename
    content = await file.read()
    latest_source_code = content.decode("utf-8")
    latest_filename = file.filename

    # Optional debug print
    print("=" * 40)
    print("UPLOADED FILE CONTENT (first 300 chars):")
    print(latest_source_code[:300])
    print(f"Total length: {len(latest_source_code)} chars")
    print("=" * 40)

    routes = extract_routes(latest_source_code)
    stats["api_routes"] = len(routes)
    print(f"Extracted routes: {len(routes)}")

    return {
        "status": "success",
        "filename": file.filename,
        "routes_found": stats["api_routes"],
        "message": "File uploaded. Click 'Generate Tests' to run the pipeline."
    }

@app.post("/api/generate")
async def generate_from_uploaded():
    global latest_source_code, latest_filename, stats, jobs, logs
    if not latest_source_code:
        return {"status": "error", "message": "No file uploaded. Use 'Upload Project' first."}

    logs.clear()

    # 1. Parse routes
    routes = extract_routes(latest_source_code)
    if not routes:
        return {"status": "error", "message": "No FastAPI routes found in uploaded file."}
    stats["api_routes"] = len(routes)
    logs.append(f"[INFO] {len(routes)} routes extracted.")

    # 2. Determine module name for import
    module_name = latest_filename.replace(".py", "") if latest_filename else "app"

    # 3. Build prompt
    prompt = build_prompt(routes, module_name)
    logs.append("[INFO] Prompt built.")

    # 4. Generate tests via LLM
    try:
        raw_code = generate_tests(prompt)
    except Exception as e:
        logs.append(f"[ERROR] LLM call failed: {e}")
        return {"status": "error", "message": "LLM generation failed."}
    logs.append("[INFO] LLM generation completed.")

    # Debug: print raw output
    print("===== RAW LLM OUTPUT =====")
    print(raw_code)
    print("=========================")

    # 5. Clean output (remove markdown fences)
    clean_code = extract_python_code(raw_code)

    # 6. Validate syntax
    validation = validate_syntax(clean_code)
    if not validation.valid:
        logs.append(f"[ERROR] Syntax invalid: {validation.error}")
        return {"status": "error", "message": f"Syntax error: {validation.error}"}
    logs.append("[SUCCESS] AST validation passed.")

    # 7. Dedup (simplified – treat whole output as one test)
    test_name = "generated_test"
    tests = [GeneratedTest(code=clean_code, route="all", test_name=test_name)]
    tests = remove_duplicates(tests)
    logs.append(f"[INFO] {len(tests)} tests after dedup.")

    # 8. Write test files
    write_test_files(tests)
    logs.append("[SUCCESS] Test files written.")

    # 9. Run pytest (using python -m pytest internally)
    eval_result = run_pytest()
    # 🔍 TEMPORARY DEBUG – shows exactly what the evaluation returned
    print("EVAL RESULT:", eval_result)

    stats["generated_tests"] = eval_result.get("total", 0)
    stats["runnable_tests"] = eval_result.get("passed", 0)
    stats["pass_rate"] = eval_result.get("pass_rate", 0)
    logs.append(f"[RESULT] Pass rate: {stats['pass_rate']}%")

    # 10. Add job record
    job = {
        "project": latest_filename or "uploaded_file.py",
        "model": os.getenv("OLLAMA_MODEL", "unknown"),
        "status": "Completed",
        "tests": stats["generated_tests"],
        "passRate": f"{stats['pass_rate']}%"
    }
    jobs.append(job)

    return {"status": "success", "stats": stats}