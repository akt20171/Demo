# Python Code Review — `calculator.py`

**Version:** v1.0.0
**Date:** 2026-02-20
**Reviewer:** Claude Code (automated structured review)
**Files reviewed:**
- `calculator.py` (51 lines)
- `tests/test_calculator.py` (130 lines)

---

## STEP 1 — OVERVIEW

### Purpose / Responsibility
`calculator.py` is a beginner-friendly, single-file command-line calculator. It accepts user input interactively, performs addition or subtraction on two floating-point numbers, and loops until the user quits.

### Entry Point
```python
if __name__ == "__main__":   # pragma: no cover
    main()
```
The `main()` function drives the application loop. The `# pragma: no cover` marker correctly excludes the guard from coverage measurement.

### Key Dependencies
None — the module uses only Python builtins (`input`, `print`, `float`, `ValueError`). No third-party imports are present, which is ideal for a project of this scope.

### Functions at a Glance

| Function          | Responsibility                                      |
|-------------------|-----------------------------------------------------|
| `add(a, b)`       | Returns the sum of two numbers                      |
| `subtract(a, b)`  | Returns the difference of two numbers               |
| `get_number(prompt)` | Prompts the user and loops until a valid float is entered |
| `show_menu()`     | Prints the operation menu to stdout                 |
| `main()`          | Main REPL loop; dispatches to add/subtract          |

---

## STEP 2 — STRUCTURE & READABILITY

### Overall Assessment
The code is well-structured and readable. Functions are small and single-purpose. Variable names are clear. Spacing and indentation are consistent with PEP 8.

### Issues Found

#### 2.1 — No docstrings on any function (lines 1, 5, 9, 18, 26)

**Problem:** Every public function is missing a docstring. Without them, `help(calculator.add)` returns nothing useful, and the intent of parameters is not self-documented.

**Before:**
```python
def add(a, b):
    return a + b
```

**After (recommended):**
```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

---

#### 2.2 — No type annotations on any function (lines 1, 5, 9, 18, 26)

**Problem:** Function signatures carry no type information. Readers and tools (mypy, IDEs) cannot infer that `a` and `b` are numeric or that `get_number` returns a `float`.

**Before:**
```python
def get_number(prompt):
```

**After (recommended):**
```python
def get_number(prompt: str) -> float:
```

_(See also Step 5 for full type-hint coverage details.)_

---

#### 2.3 — Prompt alignment is cosmetic but could be a style inconsistency (lines 37–38)

**Observation (not a bug):** The two `get_number` prompts use trailing spaces to align the cursor:
```python
a = get_number("Enter first number:  ")
b = get_number("Enter second number: ")
```
This works, but the alignment relies on manual spacing. Not a PEP 8 violation; just worth noting if the prompts ever change.

---

### Positive Observations
- All lines are well within the 88-character limit.
- Consistent 4-space indentation throughout.
- Clear separation of concerns: I/O in `get_number`/`show_menu`/`main`, pure logic in `add`/`subtract`.
- `# pragma: no cover` on line 50 is correctly placed and justified.

---

## STEP 3 — CORRECTNESS & LOGIC

### Overall Assessment
The logic is correct for all standard inputs. Two minor edge cases exist that don't affect correctness per se but may surprise beginners.

### Issues Found

#### 3.1 — `float()` silently accepts special values: `"inf"`, `"nan"`, `"-inf"` (line 13)

**Problem:** Python's `float()` accepts string representations of IEEE 754 special values. A user who types `inf` passes validation and produces mathematically valid but potentially confusing results:

```
Enter first number:  inf
Enter second number: 1
  inf + 1.0 = inf
```

For a beginner-targeted calculator, this may be unexpected. A strict numeric validator could be added.

**Severity:** LOW — not a bug, but a UX gap.

**Recommended fix (optional):**
```python
def get_number(prompt: str) -> float:
    while True:
        user_input = input(prompt).strip()
        try:
            value = float(user_input)
            if not math.isfinite(value):
                raise ValueError
            return value
        except ValueError:
            print("  Invalid number. Please try again.")
```
_(Requires `import math`.)_

---

#### 3.2 — No `KeyboardInterrupt` handling in `main()` or `get_number()` (lines 10, 29)

**Problem:** If the user presses Ctrl+C during an `input()` call, Python raises `KeyboardInterrupt`, which propagates uncaught and prints a traceback. A friendlier experience would be:

```python
def main():
    print("Welcome to the Simple Calculator!")
    try:
        while True:
            ...
    except KeyboardInterrupt:
        print("\nGoodbye!")
```

**Severity:** LOW — not a logic error; purely a UX polish issue.

---

### Positive Observations
- `add` and `subtract` are correct for all numeric inputs (integers, floats, negatives, large numbers).
- `get_number` correctly loops on invalid input, uses `.strip()` to handle whitespace, and catches only `ValueError` (not a bare `except`).
- `main` correctly handles all three branches: `+`, `-`, `q`, and invalid input.
- No off-by-one errors. No unreachable code (the `else` on line 46 is reachable via any non-`+`/`-`/`q` input).

---

## STEP 4 — PYTHONIC STYLE

### Overall Assessment
The code is clean and idiomatic. No anti-patterns detected.

### Issues Found

None of the common anti-patterns are present:

| Anti-pattern                    | Present? | Note                         |
|---------------------------------|----------|------------------------------|
| `range(len(...))` loop          | No       |                              |
| Mutable default argument        | No       |                              |
| String concatenation in loop    | No       | f-strings used correctly     |
| Bare `except` clause            | No       | `except ValueError` is specific |
| Redundant type checks           | No       |                              |
| Global variables                | No       | All state passed as arguments |
| Manual index iteration          | No       |                              |

### Positive Observations
- f-strings used throughout (lines 42, 45) — modern and readable.
- `.strip()` applied to all user input (lines 11, 31) — defensive and correct.
- `choice in ("+", "-")` (line 36) uses a tuple membership test — idiomatic.
- The `while True: ... break` pattern in `main()` is appropriate here.

---

## STEP 5 — TYPE HINTS & DOCUMENTATION

### Type Hint Coverage

| Function              | Parameters typed? | Return typed? |
|-----------------------|-------------------|---------------|
| `add(a, b)`           | No                | No            |
| `subtract(a, b)`      | No                | No            |
| `get_number(prompt)`  | No                | No            |
| `show_menu()`         | No                | No            |
| `main()`              | No                | No            |

**Recommended complete annotations:**
```python
def add(a: float, b: float) -> float: ...
def subtract(a: float, b: float) -> float: ...
def get_number(prompt: str) -> float: ...
def show_menu() -> None: ...
def main() -> None: ...
```

### Docstring Coverage

No function has a docstring. Recommended minimal docstrings:

```python
def add(a: float, b: float) -> float:
    """Return the sum of a and b."""

def subtract(a: float, b: float) -> float:
    """Return a minus b."""

def get_number(prompt: str) -> float:
    """Prompt the user until a valid finite float is entered and return it."""

def show_menu() -> None:
    """Print the available calculator operations to stdout."""

def main() -> None:
    """Run the interactive calculator REPL until the user quits."""
```

---

## STEP 6 — SECURITY CONCERNS

### Overall Assessment
No security concerns for a local CLI tool of this scope. The static analysis tool `bandit` found zero issues.

### Findings

| # | Severity | Line | Finding |
|---|----------|------|---------|
| 1 | LOW      | 13   | `float()` accepts `"inf"` / `"nan"` — not a vulnerability but an unvalidated special case |

**Detail:**

There is no use of `eval()`, `exec()`, `subprocess`, `os.system`, `pickle`, `yaml.load()`, hardcoded secrets, or unsafe file-path construction. Input is parsed exclusively through `float()`, which is safe — it cannot execute code or cause injection.

The only observation (LOW severity) is that `float("inf")` and `float("nan")` pass the `ValueError` guard silently. For a calculator aimed at beginners, rejecting non-finite values may be preferable UX. See Step 3.1 for the recommended guard using `math.isfinite()`.

---

## STEP 7 — PERFORMANCE OBSERVATIONS

### Overall Assessment
No performance concerns. The code performs minimal, straightforward operations.

| Check                               | Finding                  |
|-------------------------------------|--------------------------|
| Repeated computation inside loops   | None                     |
| Unnecessary list copies             | None                     |
| Missing O(1) lookup (set/dict)      | N/A — no search required |
| Blocking I/O                        | `input()` is inherently blocking but correct for a CLI |

The `show_menu()` function calls `print()` four times. This could be a single `print()` with a multi-line string, but the performance difference is negligible and readability is acceptable either way.

---

## STEP 8 — TESTABILITY

### Overall Assessment
Excellent. The test suite is well-designed and achieves **100% branch coverage** on `calculator.py`.

### Testability Strengths
- `add` and `subtract` are **pure functions** — same input always yields same output, no setup needed.
- `get_number` isolates `input()` behind a parameter, making monkeypatching trivial.
- `main()` is testable despite being a REPL because it terminates on `"q"`.
- `capsys` and `monkeypatch` fixtures are used correctly and consistently.
- Tests are named descriptively (`test_add_negative_numbers`, `test_main_invalid_option`).

### Suggested Additional Test Cases

These are not gaps (coverage is already 100%) but would add regression protection for the edge cases identified in this review:

**1. Reject special float strings in `get_number`** *(if Step 3.1 guard is added)*
```python
def test_get_number_rejects_inf(monkeypatch, capsys):
    inputs = iter(["inf", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = calculator.get_number("Enter: ")
    assert result == 5.0
    assert "Invalid number" in capsys.readouterr().out
```

**2. Test whitespace-only input is rejected**
```python
def test_get_number_whitespace_then_valid(monkeypatch, capsys):
    inputs = iter(["   ", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = calculator.get_number("Enter: ")
    assert result == 3.0
    assert "Invalid number" in capsys.readouterr().out
```

**3. Test negative number input in `main` addition**
```python
def test_main_addition_with_negatives(monkeypatch, capsys):
    inputs = iter(["+", "-3", "-4", "q"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator.main()
    out = capsys.readouterr().out
    assert "-3.0 + -4.0 = -7.0" in out
```

---

## STEP 9 — SUMMARY SCORECARD

| Category            | Rating (1–5) | Key Finding                                          |
|---------------------|:------------:|------------------------------------------------------|
| Structure           |      4       | Well-organised; only gap is missing docstrings       |
| Correctness         |      4       | All paths correct; `inf`/`nan` is an unguarded edge  |
| Pythonic Style      |      5       | Clean, idiomatic — no anti-patterns found            |
| Type Hints & Docs   |      2       | No type annotations or docstrings anywhere           |
| Security            |      5       | Bandit clean; no real vulnerabilities for this scope |
| Performance         |      5       | Trivial code; no inefficiencies                      |
| Testability         |      5       | 100% coverage, monkeypatch used correctly throughout |

**Overall: 4.3 / 5**

---

## STEP 10 — PRIORITISED ACTION LIST

| Priority | Severity | Finding                                                                 | Location      |
|----------|----------|-------------------------------------------------------------------------|---------------|
| 1        | MEDIUM   | Add type hints to all five function signatures                          | Lines 1,5,9,18,26 |
| 2        | MEDIUM   | Add docstrings to all five public functions                             | Lines 1,5,9,18,26 |
| 3        | LOW      | Guard `get_number` against special float values (`inf`, `nan`, `-inf`) | Line 13       |
| 4        | LOW      | Handle `KeyboardInterrupt` in `main()` for graceful Ctrl+C exit        | Line 29       |
| 5        | INFO     | Consider collapsing `show_menu()` into a single multi-line `print()`   | Lines 19–23   |

---

> **Overall direction:** This is clean, well-tested, beginner-friendly code that meets its stated goals. Adding type hints and docstrings is the single most impactful next step — it will make the module self-documenting and IDE-friendly with minimal effort. Well done!
