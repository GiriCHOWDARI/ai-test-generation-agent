import os
from typing import List
from schemas import GeneratedTest

def write_test_files(tests: List[GeneratedTest], output_dir: str = "generated_tests"):
    os.makedirs(output_dir, exist_ok=True)
    for test in tests:
        filename = f"test_{test.test_name}.py"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(test.code)