from datetime import datetime


def validate_date(value: str) -> str:
    """Validate and normalize date in YYYY-MM-DD format."""
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("Date must use YYYY-MM-DD format.") from exc
    return value


def validate_category(value: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError("Category cannot be empty.")
    if len(value) > 30:
        raise ValueError("Category must be 30 characters or fewer.")
    return value.title()


def validate_amount(value: str) -> float:
    try:
        amount = float(value)
    except ValueError as exc:
        raise ValueError("Amount must be a number.") from exc
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if amount > 1_000_000:
        raise ValueError("Amount is too large.")
    return round(amount, 2)


def validate_id(value: str) -> int:
    try:
        record_id = int(value)
    except ValueError as exc:
        raise ValueError("ID must be an integer.") from exc
    if record_id <= 0:
        raise ValueError("ID must be positive.")
    return record_id
