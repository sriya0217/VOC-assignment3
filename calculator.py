import math

def calculator():
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '7':
            print("🔚 Exiting calculator. Goodbye!")
            break

        if choice == '6':
            num = float(input("Enter number: "))
            print(f"√{num} = {math.sqrt(num)}")
            continue

        # For all other options
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print(f"➕ Result: {num1 + num2}")
        elif choice == '2':
            print(f"➖ Result: {num1 - num2}")
        elif choice == '3':
            print(f"✖️ Result: {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("❌ Cannot divide by zero!")
            else:
                print(f"➗ Result: {num1 / num2}")
        elif choice == '5':
            print(f"{num1}^{num2} = {math.pow(num1, num2)}")
        else:
            print("❗ Invalid choice. Please try again.")

calculator()
