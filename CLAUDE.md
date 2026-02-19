# Simple Calculator (Python CLI)

---

## 1️⃣ Mission

Build a beginner-friendly command-line calculator that:

- Supports addition and subtraction
- Validates numeric input
- Loops until user exits
- Is simple, readable, and fully tested

Clarity and correctness are more important than cleverness.

---

## 2️⃣ Technology Stack

- Python 3.11+
- pytest
- pytest-cov
- black
- ruff
- bandit
- pip-audit
- detect-secrets

---

## 3️⃣ Scope

### In Scope
- Addition (+)
- Subtraction (-)
- CLI interaction
- Input validation
- Unit tests
- Coverage enforcement

### Out of Scope
- GUI
- Web app
- Expression parsing (e.g., "2+2")
- Advanced math
- External frameworks

---

## 4️⃣ Architecture

Single file:

- `calculator.py`

Required functions:

- `add(a, b)`
- `subtract(a, b)`
- `get_number(prompt)`
- `show_menu()`
- `main()`

Tests:

- `tests/test_calculator.py`

Architecture rules:

- No global variables
- No unnecessary abstractions
- No advanced Python tricks
- Keep functions small and readable

---

# 🔁 5️⃣ Required Development Workflow

All changes MUST follow this order:

1. Plan
2. TDD Loop
3. Implementation
4. Lint & Format Gate
5. Test Gate
6. Coverage Gate
7. Security Audit (Code)
8. Dependency Vulnerability Scan
9. Secrets Scan
10. Security Review
11. Performance Review
12. Final Re-Validation

Skipping steps is not allowed.

---

# 🧪 6️⃣ Test-Driven Loop With AI (TDD Enforcement)

For any behavioral change:

1. Add or update tests FIRST (or alongside change)
2. Run:

       python -m pytest -q

3. If failing:
   - Diagnose root cause
   - Apply smallest correct fix
   - Re-run tests
4. Repeat until tests pass
5. Only then summarize changes

AI is a quality-enforcing partner, not just a code generator.

---

# 🧹 7️⃣ Lint & Formatting Gate

Run:

    python -m black .
    python -m ruff check .

All lint issues must be resolved before proceeding.

No warnings left unresolved.

---

# 🧪 8️⃣ Test Gate

Run:

    python -m pytest -q

All tests must pass.

No skipped tests unless justified.

---

# 📊 9️⃣ Coverage Enforcement

Run:

    python -m pytest --cov=. --cov-report=term-missing --cov-fail-under=85

Coverage must be ≥ 85%.

If below threshold:
- Add meaningful tests
- Re-run until satisfied

---

# 🔐 10️⃣ Security Audit (Static Code Scan)

Run:

    python -m bandit -r . -q

Rules:
- Fix real issues
- Justify false positives briefly
- No high-severity issues allowed

---

# 🛡 11️⃣ Dependency Vulnerability Scan

Run:

    python -m pip_audit

If vulnerabilities are found:
- Summarize affected packages
- Propose minimal safe upgrades
- Avoid unnecessary major version jumps
- Document reasoning

---

# 🔑 12️⃣ Secrets Scan

Run:

    python -m detect_secrets scan --all-files

If potential secrets detected:
- List file path + line number
- Recommend remediation
- Do NOT expose secret values

---

# 🛡 13️⃣ Security Reviewer (Manual Reasoning)

Verify:

- Input validation present
- No unsafe eval/exec
- No hardcoded secrets
- Safe file handling
- No unnecessary dependencies

If changes made:
- Re-run tests and bandit

---

# ⚡ 14️⃣ Performance Reviewer

Check for:

- Inefficient loops
- Repeated I/O
- Unnecessary data copying
- Obvious bottlenecks

Apply minimal improvements only.

If modified:
- Re-run tests

---

# ✅ 15️⃣ Final Validation

Before declaring complete:

Re-run:

    python -m ruff check .
    python -m pytest -q

Confirm:

- Lint clean
- Tests passing
- Coverage ≥ 85%
- No critical security issues
- Code remains beginner-readable

---

# 🏁 Definition of Done

A change is complete only if:

- Formatting clean
- Lint clean
- Tests pass
- Coverage ≥ 85%
- Bandit clean
- pip-audit clean or remediation documented
- No secrets detected
- No obvious performance issues
- Code remains simple and readable

Discipline over speed.
