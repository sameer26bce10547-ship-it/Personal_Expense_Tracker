from collections import defaultdict
from typing import Dict, List

from .models import Expense


def total_expenses(expenses: List[Expense]) -> float:
    return round(sum(e.amount for e in expenses), 2)


def category_summary(expenses: List[Expense]) -> Dict[str, float]:
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense.category] += expense.amount
    return dict(sorted(
        ((category, round(amount, 2)) for category, amount in summary.items()),
        key=lambda item: item[1],
        reverse=True,
    ))


def monthly_summary(expenses: List[Expense]) -> Dict[str, float]:
    summary = defaultdict(float)
    for expense in expenses:
        month = expense.date[:7]
        summary[month] += expense.amount
    return dict(sorted(
        ((month, round(amount, 2)) for month, amount in summary.items()),
        reverse=True,
    ))
