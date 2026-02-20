# Python Code Review — `calculator.py`

**Skill:** `.claude/skills/py-code-reviewer.md`
**Reviewed:** `calculator.py`
**Date:** 2026-02-20

---

## Step 1 — Overview

| Item | Detail |
|------|--------|
| **Purpose** | Beginner-friendly interactive CLI calculator supporting addition and subtraction |
| **Entry point** | `if __name__ == "__main__"` → `main()` (line 50–51) |
| **Dependencies** | None — uses only Python built-in functions (`input`, `print`, `float`) |
| **Module size** | 51 lines, 5 functions |

The script presents a looping menu, accepts an operation choice, reads two numbers,
computes the result, and prints it. Loops until the user enters `q`.

---

## Step 2 — Structure & Readability

**Functions and responsibilities:**

| Function | Responsibility |
|----------|---------------|
| `add(a, b)` | Pure arithmetic — returns `a + b` |
| `subtract(a, b)` | Pure arithmetic — returns `a - b` |
| `get_number(prompt)` | Input loop — validates and returns a float |
| `show_menu()` | Displays the operation menu |
| `main()` | Orchestrates the full interactive loop |

**Findings:**

| # | Line | Issue | Recommendation |
|---|------|-------|----------------|
| 1 | 19–23 | `show_menu()` uses 5 separate `print()` calls | Acceptable for readability; a single `print("""...""")` would be marginally cleaner but is not required |
| 2 | 37–38 | Alignment spaces in prompts (`"Enter first number:  "`) are intentional but undocumented | Add a brief inline comment if the alignment is intentional |

No PEP 8 violations. All lines are well within 88 characters. Naming is clear and
consistent throughout. No global variables. No unnecessary abstractions.

**Rating: 5 / 5**

---

## Step 3 — Correctness & Logic

**Findings:**

| # | Line | Observation |
|---|------|-------------|
| 1 | 1–2 | `add(a, b)` correctly returns `a + b` for all numeric inputs including floats and negatives |
| 2 | 5–6 | `subtract(a, b)` correctly returns `a - b` |
| 3 | 9–15 | `get_number` retries indefinitely on invalid input and returns the first valid float — correct behaviour |
| 4 | 33–47 | `main` handles all three branches (`q`, `+`/`-`, invalid) with no unreachable paths |
| 5 | 13 | Returns `float` — whole-number input `2` is returned as `2.0`. Cosmetically noticeable in output (`2.0 + 3.0 = 5.0`) but arithmetically correct |
| 6 | 42, 45 | f-string display shows floats as-is; `1.0 + 2.0 = 3.0` may surprise users who typed integers — not a bug, a UX note |

No logic bugs, off-by-one errors, or unreachable code paths found.

**Rating: 5 / 5**

---

## Step 4 — Pythonic Style

**Findings:**

| # | Line | Pattern | Assessment |
|---|------|---------|------------|
| 1 | 10 | `while True` + `return` inside `try` | Correct Python idiom for input-retry loops ✅ |
| 2 | 11 | `.strip()` applied to `input()` result | Good defensive habit ✅ |
| 3 | 14 | Catches only `ValueError`, not bare `except` | Correct narrow exception handling ✅ |
| 4 | 36 | `choice in ("+", "-")` membership test | Idiomatic ✅ |
| 5 | 40–45 | `if/else` inside validated `elif` branch | Clean dispatch logic ✅ |
| 6 | 50 | `# pragma: no cover` on `__main__` guard | Correct coverage exclusion ✅ |

No anti-patterns found. Code is fully idiomatic for its scope and beginner-friendly.

**Rating: 5 / 5**

---

## Step 5 — Type Hints & Documentation

**Type hint coverage:** None — no function has parameter or return annotations.

**Docstring coverage:** None — no function has a docstring.

**Missing annotations:**

```python
# Current
def add(a, b):
    return a + b

# Recommended
def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b
```

```python
# Current
def subtract(a, b):
    return a - b

# Recommended
def subtract(a: float, b: float) -> float:
    """Return the difference of a and b (a - b)."""
    return a - b
```

```python
# Current
def get_number(prompt):
    ...

# Recommended
def get_number(prompt: str) -> float:
    """Prompt the user repeatedly until a valid float is entered, then return it."""
    ...
```

```python
# Current
def show_menu():
    ...

# Recommended
def show_menu() -> None:
    """Print the calculator operation menu."""
    ...
```

```python
# Current
def main():
    ...

# Recommended
def main() -> None:
    """Run the interactive calculator loop until the user quits."""
    ...
```

**Rating: 2 / 5** — All functionality is correct, but zero type hints and zero
docstrings means the code is not self-documenting for tooling (mypy, IDE
autocomplete, help()).

---

## Step 6 — Security Concerns

| # | Severity | Line | Finding | Recommendation |
|---|----------|------|---------|----------------|
| 1 | ✅ NONE | 11 | `input()` result passed only to `float()` | Safe — `float()` rejects non-numeric strings with `ValueError` |
| 2 | ✅ NONE | 31 | Menu choice compared by string equality only | Safe — no code execution from user input |
| 3 | ✅ NONE | All | No `eval`, `exec`, `subprocess`, `os.system` | Clean |
| 4 | ✅ NONE | All | No hardcoded secrets, passwords, or API keys | Clean |
| 5 | ✅ NONE | All | No file I/O, network calls, or external dependencies | Clean |
| 6 | ✅ NONE | All | No use of `pickle`, `yaml.load()`, or unsafe deserializers | Clean |

No security issues found.

**Rating: 5 / 5**

---

## Step 7 — Performance Observations

| # | Line | Observation |
|---|------|-------------|
| 1 | 10 | `while True` input-retry loop exits immediately on valid input — not a busy-wait |
| 2 | 29 | Main `while True` loop has no redundant computation inside it |
| 3 | 19–23 | Five `print()` calls in `show_menu()` — negligible cost for a CLI tool |
| 4 | All | No data structures, copies, or collections used — nothing to optimise |

No performance issues for this scope.

**Rating: 5 / 5**

---

## Step 8 — Testability

| # | Function | Testability | Notes |
|---|----------|-------------|-------|
| 1 | `add` | Excellent | Pure function — no mocking needed |
| 2 | `subtract` | Excellent | Pure function — no mocking needed |
| 3 | `get_number` | Good | Requires `unittest.mock.patch("builtins.input")` |
| 4 | `show_menu` | Good | Requires `capsys` or `unittest.mock.patch("builtins.print")` |
| 5 | `main` | Excluded | `# pragma: no cover` — correct decision for integration-level function |

**Suggested high-value unit test cases:**

1. **`test_add_negative_numbers`** — verify `add(-3, -2) == -5`
2. **`test_get_number_invalid_then_valid`** — mock `input` to return `"abc"` first,
   then `"5"`, assert return value is `5.0`
3. **`test_get_number_float_string`** — mock `input` to return `"3.14"`, assert
   return value is `3.14`
4. **`test_show_menu_output`** — capture stdout and assert it contains
   `"Simple Calculator"`, `"+"`, `"-"`, and `"q"`

**Rating: 4 / 5** — Pure functions are trivially testable; `main()` is reasonably
excluded; `show_menu()` stdout capture test would close the last coverage gap.

---

## Step 9 — Summary Scorecard

| Category            | Rating (1–5) | Key Finding                                          |
|---------------------|:------------:|------------------------------------------------------|
| Structure           |      5       | Small, focused functions; no global state            |
| Correctness         |      5       | No logic bugs; edge cases handled correctly          |
| Pythonic Style      |      5       | Idiomatic loops, membership tests, exception handling|
| Type Hints & Docs   |      2       | No type annotations or docstrings on any function    |
| Security            |      5       | No unsafe operations; safe input handling throughout |
| Performance         |      5       | No inefficiencies for this scope                     |
| Testability         |      4       | Pure functions easy to test; I/O correctly excluded  |

**Overall: 4.4 / 5**

Rating guide: 1 = needs major work · 3 = acceptable · 5 = excellent

---

## Step 10 — Prioritised Action List

1. **[MEDIUM]** Add type hints to all 5 functions — lines 1, 5, 9, 18, 26
2. **[MEDIUM]** Add one-line docstrings to `add`, `subtract`, `get_number`,
   `show_menu`, `main` — improves IDE support and `help()` output
3. **[LOW]** Consider formatting float results with `f"{result:g}"` to display
   `3` instead of `3.0` for whole-number inputs — cosmetic UX improvement
4. **[LOW]** Add a `show_menu` stdout capture test to close the last coverage gap

---

This is a disciplined, beginner-friendly script that correctly follows the CLAUDE.md
architecture spec. The main growth area is adding type annotations and docstrings to
bring it to production-grade readability — the core logic needs no changes.
