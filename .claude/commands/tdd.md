description: TDD loop (tests → run → fix → rerun until green)
allowed-tools: Bash, Read, Write
prompt: |
  Follow a strict TDD-style loop for the requested change.

  0) Confirm scope
     - Follow CLAUDE.md
     - Keep changes minimal and beginner-friendly

  1) Tests-first (or tests alongside the change)
     - If the change affects behavior, create or update tests in:
       tests/test_calculator.py
     - Prefer small, readable unit tests.

  2) Run tests
     - Run: python -m pytest -q

  3) Fix loop
     - If tests fail:
       a) Identify the failing test(s) and root cause
       b) Apply the smallest correct fix (prefer fixing code; fix tests only if the test is wrong)
       c) Re-run: python -m pytest -q
       d) Repeat until all tests pass

  4) Final output
     - Paste the final pytest output
     - Summarize changes in 5 bullets max
