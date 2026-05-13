from typing import List
from schemas import RouteInfo

def build_prompt(routes: List[RouteInfo], module_name: str = "app") -> str:
    route_descriptions = []
    for route in routes:
        route_descriptions.append(f"{route.method} {route.path}")

    prompt = f"""
You are a code generator that outputs ONLY valid Python code.
Do NOT include any explanation, markdown formatting, or code fences.
Output must start directly with 'import' or 'from'.
Write pytest test cases for the following FastAPI routes.

Import the FastAPI app using: from {module_name} import app
Use TestClient from fastapi.testclient.

Include:
- Happy path
- Invalid input (missing fields, wrong types)
- Edge cases (empty body, extremely large values)
- Authentication failures (where applicable)

Routes:
{chr(10).join(route_descriptions)}
"""
    return prompt