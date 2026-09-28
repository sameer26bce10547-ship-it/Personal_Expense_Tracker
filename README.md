# Personal Expense Tracker

## 1. Project Overview

Personal Expense Tracker is a simple command-line Python application for recording and analyzing daily expenses. It uses a JSON file for local storage, so it does not require a database server or third-party Python packages.

The project demonstrates modular Python programming, CRUD operations, input validation, persistent storage, reporting, and automated testing.

## 2. Main Features

1. Add an expense
2. List saved expenses
3. Update an expense
4. Delete an expense
5. Generate spending reports by category and month
6. Validate dates, amounts, categories, and IDs
7. Persist data locally in JSON
8. Run automated unit tests

## 3. Functional Modules

- **Expense Management:** Create, read, update, and delete expense records.
- **Data Validation & Storage:** Validate input and safely save/load JSON data.
- **Reporting:** Calculate total spending and summaries by category/month.

## 4. Technology

- Python 3.9+
- Standard library only
- JSON for local persistence
- `unittest` for testing

No external packages are required.

## 5. Project Structure

```text
expense-tracker/
├── main.py
├── requirements.txt
├── README.md
├── statement.md
├── .gitignore
├── data/
│   └── expenses.json
├── expense_tracker/
│   ├── __init__.py
│   ├── cli.py
│   ├── expense_manager.py
│   ├── models.py
│   ├── reports.py
│   ├── storage.py
│   └── validators.py
├── tests/
│   └── test_expense_tracker.py
└── docs/
    ├── architecture.md
    ├── workflow.md
    ├── uml.md
    └── test_cases.md
```

## 6. Environment Setup

### Windows

Install Python 3.9 or newer and make sure `python` works:

```bash
python --version
```

### Linux/macOS

```bash
python3 --version
```

## 7. Installation

Clone/download this repository and open a terminal in the repository root.

There are no third-party dependencies. The `requirements.txt` file is intentionally empty.

Optional virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

## 8. Run the Project

From the repository root:

```bash
python main.py
```

The program creates `data/expenses.json` automatically when the first expense is saved.

## 9. Testing

Run:

```bash
python -m unittest discover -s tests -v
```

Expected result: all tests should pass.

## 10. Example Workflow

1. Select `1` to add an expense.
2. Enter a date such as `2026-09-28`.
3. Enter a category such as `Food`.
4. Enter an amount such as `250`.
5. Select `2` to list records.
6. Select `5` to view category/month reports.
7. Select `3` or `4` to update/delete records.

## 11. Error Handling

Invalid dates, empty categories, invalid amounts, invalid IDs, malformed stored JSON, and missing records are handled with user-readable error messages.

## 12. Design Documentation

See the `docs/` directory for the architecture, workflow, UML diagrams, and test cases.

## 13. Project Report

A report suitable for the VITyarthi project requirements is included as `Project_Report.pdf`.

## 14. Version Control

For submission, initialize Git, commit the project, create a **public** GitHub repository, and push the project.

```bash
git init
git add .
git commit -m "Initial project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

Submit only the repository root URL, for example:

`https://github.com/YOUR_USERNAME/YOUR_REPO`

Do not submit `/tree/main/` or `/blob/main/` URLs.
