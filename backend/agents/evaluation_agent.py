import subprocess
import re
import sys
from typing import Dict

def run_pytest(test_dir: str = "generated_tests") -> Dict:
    result = subprocess.run(
        [sys.executable, "-m", "pytest", test_dir, "-v"],
        capture_output=True,
        text=True,
        cwd=".",
        timeout=30
    )
    stdout = result.stdout
    stderr = result.stderr
    returncode = result.returncode

    # Debug – will appear in the backend terminal
    print("===== PYTEST STDOUT =====")
    print(stdout)
    print("===== PYTEST STDERR =====")
    print(stderr)
    print(f"===== RETURN CODE: {returncode} =====")

    passed = 0
    failed = 0
    passed_match = re.search(r'(\d+) passed', stdout)
    if passed_match:
        passed = int(passed_match.group(1))
    failed_match = re.search(r'(\d+) failed', stdout)
    if failed_match:
        failed = int(failed_match.group(1))

    total = passed + failed
    pass_rate = round(passed / total * 100, 2) if total else 0

    return {
        "total": total,
        "passed": passed,
        "pass_rate": pass_rate,
        "output": stdout[-500:] if stdout else stderr[-500:]
    }