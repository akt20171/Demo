# Simple Calculator (Python CLI)

## Mission

Build a beginner-friendly command-line calculator that:
- Supports addition and subtraction
- Validates input
- Loops until user quits

Keep everything simple and readable.

---

## Stack

- Python 3.11+
- Standard library only
- pytest for testing

---

## Scope

IN SCOPE:
- + and - only
- CLI menu
- Input validation
- Loop for repeated calculations

OUT OF SCOPE:
- Multiplication/division
- GUI
- Web app
- Expression parsing like "2+2"

---

## Architecture

Single file:
- calculator.py

Functions required:
- add(a, b)
- subtract(a, b)
- get_number(prompt)
- show_menu()
- main()

Tests:
- tests/test_calculator.py

---

# 🔁 Required Multi-Agent Workflow

All changes MUST follow this sequence:

1️⃣ Planner  
- Produce a short plan (5–8 steps)
- List edge cases
- List files impacted
- No code yet

2️⃣ Implementer  
- Implement calculator.py
- Follow CLAUDE.md rules strictly
- Keep code beginner-friendly

3️⃣ Test Writer  
- Create/update tests/test_calculator.py
- Cover:
  - add()
  - subtract()
  - get_number() validation
- Tests must be readable

4️⃣ Test Runner & Fixer  
- Run: python -m pytest -q
- Fix failures
- Rerun until all tests pass
- Do not stop at first failure

5️⃣ Reviewer  
- Review code and tests
- Ensure simplicity
- Remove unnecessary complexity
- Improve clarity only if needed

Skipping any step is not allowed.

---

# 🧪 Testing Policy (Strict Gate)

Definition of Done:

- All tests pass
- No skipped tests unless justified
- No unhandled exceptions
- No crashes on invalid input
- Code remains beginner-readable

If tests fail:
- Fix code or tests
- Rerun until green

---

# 🛡 Safety & Simplicity Rules

- No external libraries except pytest
- No advanced Python features
- No clever tricks
- No global variables
- No unnecessary abstractions

Prefer clarity over compactness.

---

# ▶ How to Run

Run calculator:
    python calculator.py

Run tests:
    python -m pytest -q
