from .expense_manager import ExpenseManager
from .reports import category_summary, monthly_summary, total_expenses


def print_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return
    print("\nID   Date        Category              Amount       Note")
    print("-" * 70)
    for e in expenses:
        print(f"{e.expense_id:<4} {e.date:<11} {e.category:<20} "
              f"{e.amount:>9.2f}   {e.note}")


def prompt_add(manager):
    print("\nAdd Expense")
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    amount = input("Amount: ")
    note = input("Note (optional): ")
    expense = manager.add(date, category, amount, note)
    print(f"Added expense #{expense.expense_id}.")


def prompt_update(manager):
    print("\nUpdate Expense")
    expense_id = input("Expense ID: ")
    current = manager.get(expense_id)
    if current is None:
        print("Expense ID was not found.")
        return
    print("Press Enter to keep the current value.")
    date = input(f"Date [{current.date}]: ") or current.date
    category = input(f"Category [{current.category}]: ") or current.category
    amount = input(f"Amount [{current.amount:.2f}]: ") or str(current.amount)
    note = input(f"Note [{current.note}]: ")
    if note == "":
        note = current.note
    manager.update(expense_id, date, category, amount, note)
    print("Expense updated.")


def prompt_delete(manager):
    expense_id = input("\nExpense ID to delete: ")
    if manager.delete(expense_id):
        print("Expense deleted.")
    else:
        print("Expense ID was not found.")


def show_reports(manager):
    expenses = manager.list_all()
    print(f"\nTotal spending: {total_expenses(expenses):.2f}")

    print("\nBy category:")
    for category, amount in category_summary(expenses).items():
        print(f"  {category:<20} {amount:>10.2f}")

    print("\nBy month:")
    for month, amount in monthly_summary(expenses).items():
        print(f"  {month:<20} {amount:>10.2f}")


def run(manager):
    while True:
        print(
            "\n=== Expense Tracker ===\n"
            "1. Add expense\n"
            "2. List expenses\n"
            "3. Update expense\n"
            "4. Delete expense\n"
            "5. View reports\n"
            "6. Exit"
        )
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                prompt_add(manager)
            elif choice == "2":
                print_expenses(manager.list_all())
            elif choice == "3":
                prompt_update(manager)
            elif choice == "4":
                prompt_delete(manager)
            elif choice == "5":
                show_reports(manager)
            elif choice == "6":
                print("Goodbye.")
                return
            else:
                print("Please choose 1-6.")
        except (ValueError, RuntimeError) as exc:
            print(f"Error: {exc}")
