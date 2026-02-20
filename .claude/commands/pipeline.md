description: Full disciplined pipeline (TDD → lint → tests → coverage → security → perf → final validation)
allowed-tools: Bash, Read, Write
prompt: |
  You are the orchestrator. Follow CLAUDE.md strictly.
  Execute the full pipeline in exact order.

  ==================================================
  1️⃣ PLAN
  ==================================================
  - Produce a short plan (max 10 bullets)
  - List impacted files
  - List edge cases
  - No code yet

  ==================================================
  2️⃣ TDD LOOP (TEST-FIRST BEHAVIOR)
  ==================================================
  - If change affects behavior:
      • Add or update tests FIRST in tests/test_calculator.py
  - Run: python -m pytest -q

  If tests fail:
      1) Diagnose root cause
      2) Apply smallest correct fix (prefer fixing code)
      3) Re-run: python -m pytest -q
      4) Repeat until all tests pass

  ==================================================
  3️⃣ IMPLEMENTATION (if not fully covered above)
  ==================================================
  - Implement minimal required changes
  - Keep beginner-readable
  - No unnecessary abstractions

  ==================================================
  4️⃣ LINT & FORMAT GATE
  ==================================================
  - Run: python -m black .
  - Run: python -m ruff check .

  If lint errors appear:
      • Fix them
      • Re-run ruff until clean

  ==================================================
  5️⃣ TEST GATE (RE-VALIDATE)
  ==================================================
  - Run: python -m pytest -q
  - Must be fully green

  ==================================================
  6️⃣ COVERAGE ENFORCEMENT (>=85%)
  ==================================================
  - Run:
      python -m pytest --cov=. --cov-report=term-missing --cov-fail-under=85

  If coverage fails:
      • Add meaningful tests
      • Re-run until threshold satisfied

  ==================================================
  7️⃣ SECURITY AUDIT (STATIC CODE)
  ==================================================
  - Run: python -m bandit -r . -q

  If findings exist:
      • Fix real issues
      • Justify false positives briefly
      • Re-run bandit

  ==================================================
  8️⃣ DEPENDENCY VULNERABILITY SCAN
  ==================================================
  - Run: python -m pip_audit

  If vulnerabilities found:
      • Summarize affected packages
      • Propose minimal safe upgrades
      • Avoid major version jumps unless necessary

  ==================================================
  9️⃣ SECRETS SCAN
  ==================================================
  - Run: python -m detect_secrets scan --all-files

  If potential secrets found:
      • List file path + line number
      • Recommend remediation
      • Do NOT expose secret contents

  ==================================================
  🔟 SECURITY REVIEW (MANUAL REASONING)
  ==================================================
  Verify:
      • Input validation exists
      • No unsafe eval/exec
      • No hardcoded secrets
      • No unsafe file handling

  If changes made:
      • Re-run tests and bandit

  ==================================================
  1️⃣1️⃣ PERFORMANCE REVIEW
  ==================================================
  Check for:
      • Inefficient loops
      • Unnecessary copies
      • Repeated I/O
      • Obvious bottlenecks

  Apply minimal improvements only.

  If changed:
      • Re-run tests

  ==================================================
  1️⃣2️⃣ FINAL VALIDATION
  ==================================================
  Re-run:
      python -m ruff check .
      python -m pytest -q

  Ensure:
      • Lint clean
      • Tests pass
      • Coverage >= 85%
      • No critical security issues
      • Code remains beginner-friendly

  ==================================================
  FINAL OUTPUT MUST INCLUDE:
  ==================================================
  - Plan (from step 1)
  - Files changed
  - Final outputs of:
      • ruff
      • pytest
      • coverage
      • bandit
      • pip-audit
      • detect-secrets
  - Short 5-bullet summary of changes
