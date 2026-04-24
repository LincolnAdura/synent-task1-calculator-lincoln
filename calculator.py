# ============================================
# Synent Technologies - Python Internship
# Task 1: Simple Calculator (CLI)
# Developer: Lincoln Adura
# ============================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    print("============================================")
    print("   Synent Technologies - Simple Calculator  ")
    print("============================================")

    while True:
        print("\nSelect Operation:")
        print("  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (*)")
        print("  4. Division       (/)")
        print("  5. Exit")
        print("--------------------------------------------")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please select a valid option (1-5).")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
            operator = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operator = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operator = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operator = "/"

        print(f"\nResult: {num1} {operator} {num2} = {result}")
        print("--------------------------------------------")

# Entry point
if __name__ == "__main__":
    calculator()