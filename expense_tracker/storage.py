import json
from pathlib import Path
from typing import List

from .models import Expense


class ExpenseStorage:
    """Handles persistent JSON storage for expenses."""

    def __init__(self, file_path: str = "data/expenses.json"):
        self.file_path = Path(file_path)

    def load(self) -> List[Expense]:
        if not self.file_path.exists():
            return []
        try:
            raw = json.loads(self.file_path.read_text(encoding="utf-8"))
            return [Expense.from_dict(item) for item in raw]
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            raise RuntimeError(
                f"Could not read data file '{self.file_path}'."
            ) from exc

    def save(self, expenses: List[Expense]) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        payload = [expense.to_dict() for expense in expenses]
        temp_path = self.file_path.with_suffix(".tmp")
        temp_path.write_text(
            json.dumps(payload, indent=2),
            encoding="utf-8",
        )
        temp_path.replace(self.file_path)
