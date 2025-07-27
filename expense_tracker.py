import json

def add_expense(file_path):
    amount = float(input("Enter expense amount: ₹"))
    category = input("Enter category: ")
    expense = {"amount": amount, "category": category}

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(expense)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print("Expense added successfully!")

def view_expenses(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            print("\n--- Your Expenses ---")
            for i, expense in enumerate(data, 1):
                print(f"{i}. ₹{expense['amount']} - {expense['category']}")
    except FileNotFoundError:
        print("No expenses found.")

def main():
    file_path = "expenses.json"

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(file_path)
        elif choice == "2":
            view_expenses(file_path)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
