import tempfile
import unittest
from pathlib import Path

from expense_tracker.expense_manager import ExpenseManager
from expense_tracker.reports import category_summary, monthly_summary, total_expenses
from expense_tracker.storage import ExpenseStorage


class ExpenseTrackerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        data_file = Path(self.temp_dir.name) / "expenses.json"
        self.manager = ExpenseManager(ExpenseStorage(str(data_file)))

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_and_reload(self):
        self.manager.add("2026-09-01", "Food", "120.50", "Lunch")
        self.assertEqual(len(self.manager.list_all()), 1)

        reloaded = ExpenseManager(self.manager.storage)
        self.assertEqual(reloaded.list_all()[0].amount, 120.50)

    def test_update_and_delete(self):
        expense = self.manager.add("2026-09-02", "Travel", "500", "Bus")
        updated = self.manager.update(
            str(expense.expense_id), "2026-09-03", "Travel", "550", "Train"
        )
        self.assertEqual(updated.amount, 550.0)
        self.assertTrue(self.manager.delete(str(expense.expense_id)))
        self.assertEqual(self.manager.list_all(), [])

    def test_reports(self):
        self.manager.add("2026-09-01", "Food", "100")
        self.manager.add("2026-09-15", "Food", "50")
        self.manager.add("2026-08-20", "Books", "200")

        self.assertEqual(total_expenses(self.manager.list_all()), 350.0)
        self.assertEqual(category_summary(self.manager.list_all())["Food"], 150.0)
        self.assertEqual(monthly_summary(self.manager.list_all())["2026-09"], 150.0)

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.manager.add("2026-09-01", "Food", "-5")


if __name__ == "__main__":
    unittest.main()
