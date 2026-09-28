from expense_tracker.cli import run
from expense_tracker.expense_manager import ExpenseManager
from expense_tracker.storage import ExpenseStorage


def main():
    storage = ExpenseStorage("data/expenses.json")
    manager = ExpenseManager(storage)
    run(manager)


if __name__ == "__main__":
    main()
