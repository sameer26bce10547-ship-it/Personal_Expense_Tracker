# Test Cases

| ID | Test | Input | Expected Result |
|---|---|---|---|
| T01 | Add valid expense | Date, category, positive amount | Record saved |
| T02 | Invalid date | 2026/09/01 | Validation error |
| T03 | Negative amount | -10 | Validation error |
| T04 | Empty category | blank | Validation error |
| T05 | Update record | Existing ID + new values | Record changed |
| T06 | Delete record | Existing ID | Record removed |
| T07 | Missing ID | Unknown ID | No crash; not found message |
| T08 | Reporting | Multiple records | Correct totals |
| T09 | Persistence | Save then reload | Records remain available |
