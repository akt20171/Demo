description: Run unit tests and fix failures until all pass
allowed-tools: Bash, Read, Write
prompt: |
  Run: python -m pytest -q

  If tests fail:
  - Identify the failing test(s)
  - Fix the correct thing (code or tests)
  - Re-run: python -m pytest -q
  - Repeat until all tests pass

  At the end:
  - paste the final pytest output
  - summarize what was fixed (max 5 bullets)
