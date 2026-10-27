
import json
expenses = []

def add_expense():
    name = input("Name of the Expense: ")
    try:
        amount = float(input("Amount (₹): "))

        if amount <= 0:
            print("Amount should be greater than zero.")
            return

    except ValueError:
        print("Invalid amount! please enter only numbers.")
        return

    print("Categories: Food, Travel, Shopping, Other")
    category = input("Expense ki category: ").title()

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses()
    print("Expense successfully added!")

def save_expenses():
    with open("expenses.json","w") as file:
        json.dump(expenses,file,indent=4)
    print("Expenses saved successfully")    

def load_expenses():
    global expenses
    try:
        with open("expenses.json","r") as file:
            expenses=json.load(file)
    except FileNotFoundError:
        expenses=[]
    print("Expenses loaded successfully")    

def show_expenses():
    if not expenses:
        print("there is no expenses.")
        return

    for expense in expenses:
        print(
            expense["name"],
            "- ₹",
            expense["amount"],
            "| Category :",expense["category"]
        )

def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total spending: ₹", total)

def delete_expense():
    if not expenses:
        print("There is no expenses .")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            i, ".",
            expense["name"],
            "- ₹", expense["amount"],
            "| Category:", expense["category"]
        )

    try:
        choice = int(input("Write the expense number to delete: "))
    except ValueError:
        print("Invalid input! Please enter number.")
        return

    if choice < 1 or choice > len(expenses):
        print("Invalid expense number!")
        return

    deleted = expenses.pop(choice - 1)
    save_expenses()

    print(deleted["name"], "successfully deleted!")


def edit_expense():
    if not expenses:
        print("There are no expenses.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            i, ".",
            expense["name"],
            "- ₹", expense["amount"],
            "| Category:", expense["category"]
        )

    try:
        choice = int(input("Enter expense number to edit: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        return

    if choice < 1 or choice > len(expenses):
        print("Invalid expense number!")
        return

    expense = expenses[choice - 1]

    new_name = input("Enter new name (press Enter to keep old): ")
    if new_name.strip():
        expense["name"] = new_name

    new_amount = input("Enter new amount (press Enter to keep old): ")

    if new_amount.strip():
        try:
            amount = float(new_amount)

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

            expense["amount"] = amount

        except ValueError:
            print("Invalid amount!")
            return

    print("Categories: Food, Travel, Shopping, Other")
    new_category = input("Enter new category (press Enter to keep old): ")

    if new_category.strip():
        expense["category"] = new_category.title()

    save_expenses()
    print("Expense successfully updated!")

load_expenses()
while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Show total spending")
    print("4. Exit")
    print("5. Save expenses")
    print("6. Delete expense")
    print("7. Edit expenses")

    choice = input("choose your option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Thank you!")
    elif choice == "5":
        save_expenses()
    elif choice == "6":
        delete_expense()
    elif choice == "7":
        edit_expense()

        break
    else:
        print("Invalid option, try again.")
