description: Format + lint the repo (black + ruff) and fix until clean
allowed-tools: Bash, Read, Write
prompt: |
  Run formatting and lint checks and fix issues until clean.

  1) Run: python -m black .
  2) Run: python -m ruff check .

  If ruff reports issues:
  - Fix them with minimal edits (prefer readability).
  - Re-run: python -m ruff check . until clean.

  At the end:
  - paste the final outputs from black and ruff.
