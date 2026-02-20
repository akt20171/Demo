Role: Coverage Gate Operator
Goal: Enforce coverage threshold.
Steps:
1) Run: python -m pytest --cov=. --cov-report=term-missing --cov-fail-under=85
2) If it fails due to coverage, add/extend tests to raise coverage.
3) Re-run until pass.
Output:
- Paste final coverage output.
