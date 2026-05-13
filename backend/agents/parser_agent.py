import re
from typing import List
from schemas import RouteInfo

def extract_routes(source_code: str) -> List[RouteInfo]:
    routes = []
    # Match @app.get("/path"), @app.post("/path"), etc.
    pattern = r'@app\.(get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)[\'"]'
    for match in re.finditer(pattern, source_code):
        method = match.group(1).upper()
        path = match.group(2)
        routes.append(RouteInfo(
            path=path,
            method=method,
            params=[],
            request_model=None
        ))
    return routes