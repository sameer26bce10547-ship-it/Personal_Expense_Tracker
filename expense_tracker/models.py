from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class Expense:
    """Represents one expense record."""
    expense_id: int
    date: str
    category: str
    amount: float
    note: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Expense":
        return Expense(
            expense_id=int(data["expense_id"]),
            date=str(data["date"]),
            category=str(data["category"]),
            amount=float(data["amount"]),
            note=str(data.get("note", "")),
        )
