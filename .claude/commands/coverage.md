description: Enforce coverage threshold (>=85%) and raise coverage by adding tests if needed
allowed-tools: Bash, Read, Write
prompt: |
  Enforce coverage threshold.

  Run:
    python -m pytest --cov=. --cov-report=term-missing --cov-fail-under=85

  If coverage fails:
  - Add or improve meaningful tests (avoid nonsense assertions).
  - Prefer testing core functions and edge cases.
  - Re-run the coverage command until it passes.

  At the end:
  - paste the final coverage output
  - list which tests were added/updated
