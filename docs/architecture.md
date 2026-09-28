# System Architecture

```text
+----------------------+
|      User / CLI      |
+----------+-----------+
           |
           v
+----------------------+
|       cli.py         |
| Input + menu output  |
+----------+-----------+
           |
           v
+----------------------+
|  expense_manager.py  |
| Business operations  |
+-----+------------+---+
      |            |
      v            v
+-----------+  +-----------+
|validators |  | reports   |
+-----------+  +-----------+
      |
      v
+----------------------+
|      storage.py      |
| JSON persistence     |
+----------+-----------+
           |
           v
+----------------------+
| data/expenses.json   |
+----------------------+
```

## Layers

1. **Presentation layer:** `cli.py`
2. **Business layer:** `expense_manager.py`
3. **Domain layer:** `models.py`
4. **Utility/reporting layer:** `validators.py`, `reports.py`
5. **Persistence layer:** `storage.py`

The layered structure keeps user interaction, business logic, validation, reporting, and persistence separate.
