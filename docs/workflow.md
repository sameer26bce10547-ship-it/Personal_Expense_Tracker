# Process Workflow

```text
Start
  |
  v
Load JSON data
  |
  v
Display menu
  |
  +--> Add --> Validate --> Save --> Menu
  |
  +--> List -------------> Display -> Menu
  |
  +--> Update --> Validate --> Save -> Menu
  |
  +--> Delete -----------> Save --> Menu
  |
  +--> Reports ----------> Calculate -> Display -> Menu
  |
  +--> Exit --> End
```

## Sequence Example: Add Expense

```text
User -> CLI: enter expense details
CLI -> Manager: add(date, category, amount, note)
Manager -> Validators: validate fields
Validators --> Manager: valid values
Manager -> Storage: save(expenses)
Storage --> Manager: saved
Manager --> CLI: created Expense
CLI --> User: success message
```
