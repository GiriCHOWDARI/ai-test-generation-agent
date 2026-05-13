from pydantic import BaseModel
from typing import List, Optional

class RouteInfo(BaseModel):
    path: str
    method: str
    params: List[str] = []
    request_model: Optional[str] = None

class GeneratedTest(BaseModel):
    code: str
    route: str
    test_name: str

class ValidationResult(BaseModel):
    valid: bool
    error: Optional[str] = None