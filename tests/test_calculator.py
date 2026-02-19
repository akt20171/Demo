import calculator

# --- add() ---


def test_add_integers():
    assert calculator.add(2, 3) == 5


def test_add_floats():
    assert calculator.add(2.5, 0.5) == 3.0


def test_add_negative_numbers():
    assert calculator.add(-4, -6) == -10


def test_add_large_numbers():
    assert calculator.add(1_000_000, 2_000_000) == 3_000_000


# --- subtract() ---


def test_subtract_integers():
    assert calculator.subtract(10, 4) == 6


def test_subtract_negative_result():
    assert calculator.subtract(3, 10) == -7


def test_subtract_negative_numbers():
    assert calculator.subtract(-5, -3) == -2


def test_subtract_large_numbers():
    assert calculator.subtract(1_000_000, 999_999) == 1


# --- get_number() ---


def test_get_number_valid(monkeypatch):
    # Simulate user typing "5" at the prompt
    monkeypatch.setattr("builtins.input", lambda _: "5")
    assert calculator.get_number("Enter: ") == 5.0


def test_get_number_float(monkeypatch):
    # Simulate user typing a decimal number
    monkeypatch.setattr("builtins.input", lambda _: "3.14")
    assert calculator.get_number("Enter: ") == 3.14


def test_get_number_invalid_then_valid(monkeypatch, capsys):
    # Simulate user typing "abc" then "2.5"
    inputs = iter(["abc", "2.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = calculator.get_number("Enter: ")
    assert result == 2.5

    # Confirm an error message was printed
    out = capsys.readouterr().out
    assert "Invalid number" in out


def test_get_number_empty_string_then_valid(monkeypatch, capsys):
    # Simulate user pressing Enter (empty input) then typing a valid number
    inputs = iter(["", "7"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = calculator.get_number("Enter: ")
    assert result == 7.0

    # Confirm an error message was printed
    out = capsys.readouterr().out
    assert "Invalid number" in out


# --- show_menu() ---


def test_show_menu_output(capsys):
    calculator.show_menu()
    out = capsys.readouterr().out
    assert "Simple Calculator" in out
    assert "+" in out
    assert "-" in out
    assert "Quit" in out


# --- main() ---


def test_main_quit(monkeypatch, capsys):
    # User immediately quits
    monkeypatch.setattr("builtins.input", lambda _: "q")
    calculator.main()
    out = capsys.readouterr().out
    assert "Goodbye" in out


def test_main_addition(monkeypatch, capsys):
    # User picks +, enters 3 and 4, then quits
    inputs = iter(["+", "3", "4", "q"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator.main()
    out = capsys.readouterr().out
    assert "3.0 + 4.0 = 7.0" in out


def test_main_subtraction(monkeypatch, capsys):
    # User picks -, enters 10 and 3, then quits
    inputs = iter(["-", "10", "3", "q"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator.main()
    out = capsys.readouterr().out
    assert "10.0 - 3.0 = 7.0" in out


def test_main_invalid_option(monkeypatch, capsys):
    # User picks an invalid option, then quits
    inputs = iter(["x", "q"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator.main()
    out = capsys.readouterr().out
    assert "Invalid option" in out
