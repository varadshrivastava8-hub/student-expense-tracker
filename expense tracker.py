import json
import os
from datetime import date

FILE_NAME = "expenses.json"


def load_expenses():
    """Load saved expenses from the JSON file (if it exists)."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    """Save the expenses list to the JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses):
    """Take input from the user and add a new expense."""
    try:
        amount = float(input("Amount (Rs): "))
    except ValueError:
        print("Please enter a valid number.")
        return
    category = input("Category (food/travel/books/other): ").lower()
    note = input("Note: ")
    expenses.append({
        "date": str(date.today()),
        "amount": amount,
        "category": category,
        "note": note
    })
    save_expenses(expenses)
    print("Expense added!")


def view_expenses(expenses):
    """Display all expenses in a table."""
    if not expenses:
        print("No expenses yet.")
        return
    print("\nDate        Category   Amount   Note")
    print("-" * 45)
    for e in expenses:
        print(f"{e['date']}  {e['category']:<9}  {e['amount']:<7}  {e['note']}")


def show_summary(expenses):
    """Show category-wise totals and the overall total."""
    if not expenses:
        print("No expenses yet.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    print("\n--- Summary ---")
    for category, total in totals.items():
        print(f"{category}: Rs {total}")
    print(f"Total spent: Rs {sum(totals.values())}")


def main():
    expenses = load_expenses()
    while True:
        print("\n===== Student Expense Tracker =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Summary")
        print("4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
