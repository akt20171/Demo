def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def get_number(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("  Invalid number. Please try again.")


def show_menu():
    print("\n--- Simple Calculator ---")
    print("  1. Add (+)")
    print("  2. Subtract (-)")
    print("  q. Quit")
    print("-------------------------")


def main():
    print("Welcome to the Simple Calculator!")

    while True:
        show_menu()
        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break
        elif choice in ("1", "2"):
            a = get_number("Enter first number:  ")
            b = get_number("Enter second number: ")

            if choice == "1":
                result = add(a, b)
                print(f"  {a} + {b} = {result}")
            else:
                result = subtract(a, b)
                print(f"  {a} - {b} = {result}")
        else:
            print("  Invalid option. Please choose 1, 2, or q.")


if __name__ == "__main__":
    main()
