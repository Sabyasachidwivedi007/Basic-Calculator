import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error! Square root of negative number."
    return math.sqrt(a)


def calculator():
    print("\n===== BASIC PYTHON CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Square Root (√)")
    print("8. Exit")

    while True:
        choice = input("\nEnter your choice (1-8): ")

        if choice == "8":
            print("Calculator closed. Thank you!")
            break

        if choice == "7":
            num = float(input("Enter number: "))
            print("Result:", square_root(num))
            continue

        if choice in ["1", "2", "3", "4", "5", "6"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            elif choice == "4":
                print("Result:", divide(num1, num2))
            elif choice == "5":
                print("Result:", modulus(num1, num2))
            elif choice == "6":
                print("Result:", power(num1, num2))
        else:
            print("Invalid choice! Please select between 1 to 8.")


if __name__ == "__main__":
    calculator()
