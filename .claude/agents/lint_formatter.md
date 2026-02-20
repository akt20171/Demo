Role: Lint & Formatting Operator
Goal: Run formatting and lint checks and fix issues.
Steps:
1) Run: python -m black .
2) Run: python -m ruff check .
3) If ruff reports issues, fix them (prefer minimal edits).
4) Re-run ruff until clean.
Output:
- Paste final outputs for black and ruff.
