import os
from pathlib import Path

root_dir = Path(__file__).resolve().parent
os.chdir(root_dir)

print(f"Path.cwd(): {Path.cwd()}")
print(f"Path(__file__): {Path(__file__).resolve().parent }")


print(
    "\n================================================================ MyPy ================================================================="
)
# mypy only checks the code by default and does not apply any changes.
os.system("mypy --exclude venv .")


print(
    "\n================================================================ Black ================================================================"
)
os.system("black --check --exclude venv .")  # --check


print(
    "\n================================================================ Flake8 ================================================================"
)
# flake8 only checks the code by default and does not apply any changes.
os.system("flake8 --exclude venv .")


print(
    "\n============================================================ ISORT - diff ============================================================"
)
os.system("isort --diff --skip venv .")  # --check-only
print(
    "\n============================================================ ISORT - check ============================================================"
)
os.system("isort --check --skip venv .")  # --check-only
