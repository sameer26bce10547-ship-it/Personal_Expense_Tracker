from typing import List, Optional

from .models import Expense
from .storage import ExpenseStorage
from .validators import (
    validate_amount,
    validate_category,
    validate_date,
    validate_id,
)


class ExpenseManager:
    """Business logic for creating, reading, updating and deleting expenses."""

    def __init__(self, storage: ExpenseStorage):
        self.storage = storage
        self.expenses = storage.load()

    def _next_id(self) -> int:
        return max((e.expense_id for e in self.expenses), default=0) + 1

    def add(self, date: str, category: str, amount: str, note: str = "") -> Expense:
        expense = Expense(
            expense_id=self._next_id(),
            date=validate_date(date),
            category=validate_category(category),
            amount=validate_amount(amount),
            note=note.strip(),
        )
        self.expenses.append(expense)
        self.storage.save(self.expenses)
        return expense

    def list_all(self) -> List[Expense]:
        return sorted(self.expenses, key=lambda e: (e.date, e.expense_id), reverse=True)

    def get(self, expense_id: str) -> Optional[Expense]:
        record_id = validate_id(expense_id)
        return next((e for e in self.expenses if e.expense_id == record_id), None)

    def delete(self, expense_id: str) -> bool:
        record_id = validate_id(expense_id)
        old_count = len(self.expenses)
        self.expenses = [e for e in self.expenses if e.expense_id != record_id]
        changed = len(self.expenses) != old_count
        if changed:
            self.storage.save(self.expenses)
        return changed

    def update(self, expense_id: str, date: str, category: str,
               amount: str, note: str = "") -> Expense:
        record_id = validate_id(expense_id)
        expense = self.get(str(record_id))
        if expense is None:
            raise ValueError("Expense ID was not found.")

        expense.date = validate_date(date)
        expense.category = validate_category(category)
        expense.amount = validate_amount(amount)
        expense.note = note.strip()
        self.storage.save(self.expenses)
        return expense
