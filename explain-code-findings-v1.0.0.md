# Code Explanation: `calculator.py` — v1.0.0

**Date:** 2026-02-20
**File:** `calculator.py`
**Author:** Claude Code Explainer

---

## 1. Analogy — The Vending Machine

Think of this calculator like a **vending machine**:

- The **menu screen** (`show_menu`) shows you what's available.
- You **press a button** (`choice = input(...)`) to pick what you want.
- The machine **asks for your coins** (`get_number`) — and keeps asking if you put in a banana instead of a coin.
- It **dispenses your result** (`add` or `subtract`) and shows it on a little display.
- You can keep using it or **press the exit button** (`q`) to walk away.

No matter how many times you use it, the vending machine loops back to the menu — just like `main()` loops with `while True`.

---

## 2. Program Flow Diagram

```
          ┌─────────────────────────────┐
          │     main()                  │
          │   "Welcome to Calculator"   │
          └──────────┬──────────────────┘
                     │
                     ▼
          ┌─────────────────────────────┐
    ┌────►│     show_menu()             │◄──────────────────┐
    │     │  Prints +, -, q options     │                   │
    │     └──────────┬──────────────────┘                   │
    │                │                                       │
    │                ▼                                       │
    │     ┌─────────────────────────────┐                   │
    │     │  choice = input(...)        │                   │
    │     └──────────┬──────────────────┘                   │
    │                │                                       │
    │        ┌───────┴──────────────────┐                   │
    │        │                          │                   │
    │        ▼                          ▼                   │
    │   choice == "q"         choice == "+" or "-"          │
    │        │                          │                   │
    │        ▼                          ▼                   │
    │   print("Goodbye!")      get_number(prompt)           │
    │   break ◄─── EXIT             ┌──┴──────────┐        │
    │                               │             │        │
    │                           a = float    b = float     │
    │                               └──┬──────────┘        │
    │                                  │                   │
    │                        ┌─────────┴──────────┐        │
    │                        │                    │        │
    │                        ▼                    ▼        │
    │                    add(a, b)        subtract(a, b)   │
    │                        │                    │        │
    │                        └─────────┬──────────┘        │
    │                                  │                   │
    │                          print(f"{a} op {b} = result")
    │                                  │                   │
    └──────────────────────────────────┴───────────────────┘
                           (loop again)
```

---

## 3. Step-by-Step Code Walkthrough

### `add(a, b)` — Lines 1–2

```python
def add(a, b):
    return a + b
```

The simplest possible function. Takes two numbers, returns their sum. No surprises — pure math, no side effects.

---

### `subtract(a, b)` — Lines 5–6

```python
def subtract(a, b):
    return a - b
```

Same shape as `add`. Subtracts `b` from `a`. Again, pure and simple.

---

### `get_number(prompt)` — Lines 9–15

```python
def get_number(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("  Invalid number. Please try again.")
```

This is the **input guard**. Here's what each line does:

| Line | What it does |
|------|-------------|
| `while True:` | Loop forever until we get a valid number |
| `input(prompt).strip()` | Show the prompt, read a line, remove leading/trailing spaces |
| `return float(user_input)` | Try to convert the text to a decimal number — if it works, return it and exit the loop |
| `except ValueError:` | If conversion fails (e.g., user typed "abc"), catch the error |
| `print("Invalid...")` | Tell the user and loop back to ask again |

The `while True` + `return` pattern is a classic "keep asking until valid" loop.

---

### `show_menu()` — Lines 18–23

```python
def show_menu():
    print("\n--- Simple Calculator ---")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  q : Quit")
    print("-------------------------")
```

Pure display code. Prints the menu to the terminal. The `\n` at the start adds a blank line for visual breathing room between loops.

---

### `main()` — Lines 26–47

```python
def main():
    print("Welcome to the Simple Calculator!")

    while True:
        show_menu()
        choice = input("Choose an operation: ").strip()

        if choice == "q":
            print("Goodbye!")
            break
        elif choice in ("+", "-"):
            a = get_number("Enter first number:  ")
            b = get_number("Enter second number: ")

            if choice == "+":
                result = add(a, b)
                print(f"  {a} + {b} = {result}")
            else:
                result = subtract(a, b)
                print(f"  {a} - {b} = {result}")
        else:
            print("  Invalid option. Please choose +, -, or q.")
```

This is the **brain** of the program:

1. Greet the user once.
2. Enter a `while True` loop — the calculator runs forever until the user quits.
3. Show the menu, then read a choice.
4. **Branch on choice:**
   - `"q"` → say goodbye, `break` out of the loop, program ends.
   - `"+"` or `"-"` → ask for two numbers, compute, display result.
   - Anything else → tell the user the choice was invalid, loop again.

The `f"  {a} + {b} = {result}"` lines use **f-strings** to neatly embed variable values in the output string.

---

### `if __name__ == "__main__":` — Lines 50–51

```python
if __name__ == "__main__":  # pragma: no cover
    main()
```

This guard means: **only run `main()` if this file is executed directly** — not when it's imported as a module (e.g., by the test suite).

The `# pragma: no cover` comment tells the coverage tool to ignore this line — it can't easily be tested in automated tests since it only runs when the script is launched directly.

---

## 4. Gotcha — Float Output Surprises

When you enter whole numbers like `1` and `2`, the result prints as **`1.0 + 2.0 = 3.0`** — not `3`.

Why? Because `get_number` converts everything to `float`. So `"1"` becomes `1.0`, and `add(1.0, 2.0)` returns `3.0`.

If you wanted `3` instead of `3.0`, you'd need to format the output — for example:

```python
# Display as int if the result is a whole number
display = int(result) if result == int(result) else result
```

But this is intentionally kept simple — `float` handles both integers and decimals without needing two separate code paths. It's a deliberate trade-off.

---

## Summary

| Function | Role | Key Pattern |
|----------|------|-------------|
| `add` | Pure math | Simple return |
| `subtract` | Pure math | Simple return |
| `get_number` | Input validation | `while True` + `try/except` |
| `show_menu` | Display | Side-effect only |
| `main` | Orchestrator | `while True` + branching |

The code follows a clean **separation of concerns**: math functions don't do I/O, input functions don't do math, and `main` ties everything together.
