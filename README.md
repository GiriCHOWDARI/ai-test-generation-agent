# AI-Powered Test Generation Agent

An intelligent multi-agent QA automation platform that automatically generates, validates, executes, and evaluates `pytest` test suites from FastAPI applications using local Large Language Models.

Built for autonomous API testing, developer productivity, and AI-assisted software engineering workflows.

> Fully local • Zero API cost • Autonomous test generation • Live evaluation dashboard

---

## 🚀 Overview

This project transforms FastAPI backend code into executable pytest suites through an AI-driven multi-agent pipeline.

The system:

* parses FastAPI routes,
* builds structured prompts,
* generates tests using local LLMs,
* validates generated code,
* executes pytest automatically,
* and visualizes pass/fail metrics through a modern React dashboard.

Unlike basic AI code generators, this platform includes:

* validation layers,
* automated execution,
* evaluation metrics,
* and real-time frontend observability.

---

## ✨ Features

* 🤖 AI-powered pytest generation from FastAPI routes
* 🧠 Local LLM execution using Ollama (DeepSeek / Kimi)
* 🛡️ AST-based syntax validation
* 📊 Automated pass/fail evaluation metrics
* 🧹 Embedding-based duplicate test removal
* ⚙️ Modular multi-agent architecture
* 📡 Live React dashboard with logs and analytics
* 🔍 Route extraction and prompt engineering pipeline
* 🧪 Automated pytest execution
* 💻 Fully local development workflow

---

## 🏗️ System Architecture

```text
FastAPI Source Code
        ↓
Parser Agent
        ↓
Prompt Builder Agent
        ↓
LLM Generation Agent
        ↓
Validation Agent (AST + Pydantic)
        ↓
Deduplication Agent
        ↓
File Writer Agent
        ↓
Evaluation Agent (pytest)
        ↓
React Dashboard
```

---

## 🧠 Multi-Agent Pipeline

### 1. Parser Agent

Extracts:

* routes
* HTTP methods
* endpoint paths

from uploaded FastAPI source files.

---

### 2. Prompt Builder Agent

Constructs optimized prompts for the LLM including:

* happy paths
* invalid inputs
* edge cases
* boundary conditions

---

### 3. LLM Generation Agent

Uses local coding models through Ollama to generate:

* pytest suites
* assertions
* API request tests
* validation tests

---

### 4. Validation Agent

Ensures generated code is executable using:

* Python AST parsing
* syntax verification
* markdown cleanup

---

### 5. Deduplication Agent

Uses embeddings via `sentence-transformers` to remove redundant tests.

---

### 6. Evaluation Agent

Runs generated tests using:

```bash
python -m pytest generated_tests -v
```

and extracts:

* total tests
* passed tests
* failed tests
* pass rate
* execution logs

---

## 🖥️ Dashboard Features

The React dashboard provides:

* project upload
* AI pipeline visualization
* generation logs
* evaluation metrics
* recent job tracking
* pass/fail analytics
* configuration controls

---

## 📦 Tech Stack

| Layer            | Technology                |
| ---------------- | ------------------------- |
| Backend          | FastAPI, Uvicorn          |
| AI Orchestration | LangChain                 |
| LLM Runtime      | Ollama                    |
| Models           | DeepSeek-Coder, Kimi      |
| Validation       | Pydantic, AST             |
| Testing          | pytest                    |
| Embeddings       | sentence-transformers     |
| Frontend         | React, Vite, Tailwind CSS |
| Version Control  | Git & GitHub              |

---

# 📁 Project Structure

```text
ai-test-generation-agent/
│
├── backend/
│   ├── agents/
│   │   ├── parser_agent.py
│   │   ├── prompt_builder_agent.py
│   │   ├── llm_agent.py
│   │   ├── validation_agent.py
│   │   ├── dedup_agent.py
│   │   ├── file_writer_agent.py
│   │   └── evaluation_agent.py
│   │
│   ├── generated_tests/
│   ├── schemas.py
│   ├── sample.py
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

# ⚡ Installation

## 1. Clone Repository

```bash
git clone https://github.com/GiriCHOWDARI/ai-test-generation-agent.git
cd ai-test-generation-agent
```

---

# 🔧 Backend Setup

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama

Download and install:

[Ollama Official Website](https://ollama.com?utm_source=chatgpt.com)

---

## Pull Local Coding Model

```bash
ollama pull deepseek-coder:6.7b-instruct-q4_K_M
```

Optional models:

* Kimi K2.6
* CodeLlama
* DeepSeek-Coder-V2

---

# ▶️ Run Backend

```bash
uvicorn main:app --reload
```

Backend runs at:

```text
http://localhost:8000
```

---

# 🎨 Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

# 🧪 Optional Sample API

To test live evaluation metrics:

```bash
cd backend
uvicorn sample:app --port 8001
```

---

# 📝 Usage

## Step 1 — Upload FastAPI File

Upload a FastAPI source file from the dashboard.

Example:

```python
@app.post("/users")
async def create_user(user: UserCreate):
```

---

## Step 2 — Generate Tests

Click:

```text
Generate Tests
```

The pipeline automatically:

* extracts routes,
* builds prompts,
* generates pytest code,
* validates syntax,
* removes duplicates,
* executes pytest,
* and updates dashboard metrics.

---

# 📊 Example Results

| Metric          | Value |
| --------------- | ----- |
| Generated Tests | 6     |
| Runnable Tests  | 6     |
| Pass Rate       | 100%  |

Development benchmark:

* ~78% valid runnable generation on unseen API routes

---

# 🔍 Example Generated Tests

```python
def test_create_user_success():
    ...

def test_create_user_invalid_payload():
    ...

def test_create_user_missing_fields():
    ...
```

---

# 🛡️ Validation Pipeline

Generated code passes through:

* markdown stripping
* AST parsing
* syntax verification
* duplicate filtering

before execution.

---

# 🧠 Current Capabilities

✅ FastAPI route parsing
✅ AI-generated pytest suites
✅ Automated evaluation
✅ React monitoring dashboard
✅ Local LLM execution
✅ Pass/fail analytics
✅ Embedding-based deduplication

---

# ⚠️ Current Limitations

* Regex-based parser (currently partial)
* Single-file FastAPI support
* Limited schema extraction
* No coverage metrics yet
* No sandboxed execution
* Basic AST validation only

---

# 🚀 Future Enhancements

* AST-based FastAPI analyzer
* Multi-file project parsing
* WebSocket live log streaming
* Coverage reporting
* Mutation testing
* Docker sandbox execution
* CI/CD integration
* Security-focused test generation
* Fine-tuned coding models
* Flask/Django support

---

## 🖥️ Dashboard Preview
<img width="1920" height="1080" alt="Screenshot 2026-05-14 001618" src="https://github.com/user-attachments/assets/0a3cf622-5283-43ae-a77f-2db38013e047" />
<img width="1920" height="1080" alt="Screenshot 2026-05-14 001556" src="https://github.com/user-attachments/assets/b5428f8a-3dd8-40fd-aa92-74208dbc15de" />
<img width="1920" height="1080" alt="Screenshot 2026-05-14 001609" src="https://github.com/user-attachments/assets/afdb245f-26a7-40e3-8304-2f6ea8e422e0" />

# 💼 Portfolio / Resume Highlight

> Developed an autonomous AI-powered QA automation platform capable of generating, validating, executing, and evaluating pytest suites from FastAPI applications using local LLMs and multi-agent orchestration.

---

# 📄 License

MIT License

---

# 👨‍💻 Author

GitHub Repository:

[ai-test-generation-agent Repository](https://github.com/GiriCHOWDARI/ai-test-generation-agent?utm_source=chatgpt.com)
