import ast
from schemas import ValidationResult

def validate_syntax(code: str) -> ValidationResult:
    try:
        ast.parse(code)
        return ValidationResult(valid=True)
    except SyntaxError as e:
        return ValidationResult(valid=False, error=str(e))