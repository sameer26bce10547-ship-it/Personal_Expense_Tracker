# UML / Design Diagrams

## Use Case Diagram

```text
                +-------------------------+
                |    Expense Tracker      |
                |                         |
User ---------->| Add Expense             |
 |-------------->| View Expenses          |
 |-------------->| Update Expense         |
 |-------------->| Delete Expense         |
 |-------------->| View Reports           |
 |-------------->| Exit                   |
                +-------------------------+
```

## Class / Component Diagram

```text
+-------------------+
| Expense           |
+-------------------+
| expense_id        |
| date              |
| category          |
| amount            |
| note              |
+-------------------+
          ^
          |
+-------------------+        +-------------------+
| ExpenseManager    |------->| ExpenseStorage    |
+-------------------+        +-------------------+
| add               |        | load              |
| list_all          |        | save              |
| get               |        +-------------------+
| update            |
| delete            |
+---------+---------+
          |
          +------------------+
          |                  |
          v                  v
+-------------------+  +-------------------+
| validators.py     |  | reports.py        |
+-------------------+  +-------------------+
```

## ER / Storage Design

Although this project does not use a relational database, the JSON record structure is:

```text
Expense
--------------------------------
expense_id : integer (key)
date       : string YYYY-MM-DD
category   : string
amount     : float
note       : string
```

The JSON file contains an array of these records.
