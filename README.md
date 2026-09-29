## PERSONAL EXPENSE TRACKER

## 1.PROJECT SUMMARY

This application responsible to keep tracks of personal monetary expense of daily basis of an user. It uses a JSON file for local storage, so it does not require database server.

This project illustrates modular Python programming, management of CRUD operations, and more.

## 2. MAIN FEATURES

1. Include a payment.
2. Write down the expenses you already saved.
3. Revise an expense.
4. Erase an expenditure.
5. Create reports by type and by month.
6. Check dates, amounts, categories and ids. 
7. Save data locally in JSON.
8. Execute repeated unit tests automatically.

## 3.FUNCTIONAL MODULES

Expense Management: Perform CRUD operations on expense records
Ensure entered data is valid and save/load that data in JSON file properly.
You could say: Summary of spending According to Category/month.

## 4.TECHNOLOGY

- Python 3.9 and newer.
- Only Standard Library.
- A JSON file for local storage.

-   
Testing with Unittest

External packages are not needed.

## 5. PROJECT STRUCTURE

expense-tracker/.
Main file
requirements file
Readme document
statement markdown
.gitignore file
data folder
it’s JSON file.
└── expense_tracker/
init.py file
CLI File
expense manager Python
models.py file
reports python file
File storage.py
     └── validators.py
Tests Folder
test_expense_tracker.py.
documents folder
architecture document
workflow  Markdown file
uml markdown
test file
```.
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

## 7.Installation

Clone or download this repository and open a terminal in the repository root.

There is no third-party dependencies. The requirements.txt file is intentionally empty.

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

## 8.Run the Project

From the repository root:

```bash
python main.py
```

The program  automatically creates `data/expenses.json`  when the first expense is saved.

## 9.Testing

Run:

```bash
python -m unittest discover -s tests -v
```

Expected result:all tests should pass.

## 10.Example Workflow

1. Select `1` to add an expense.
2. Enter a date such as `2026-09-28`.
3. Enter a category such as `Food`.
4. Enter an amount such as `250`.
5. Select `2` to list records.
6. Select `5` to view category/month reports.
7. Select `3`or `4`to update/delete records.

## 11.Error Handling

Invalid dates, empty categories, invalid amounts, invalid IDs, malformed stored JSON, and missing records are handled with user-readable error messages.

## 12.Design Documentation

See the `docs/` directory for the architecture,workflow, UML diagrams, and test cases.

## 13.Project Report

A suitable report for the VITyarthi project requirements is included as `Project_Report.pdf`.

## 14.Version Control

For submission,initialize Git, commit the project, create a **public** GitHub repository, and push the project.

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
