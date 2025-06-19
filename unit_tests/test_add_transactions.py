import unittest
from unittest.mock import Mock, MagicMock, patch, call
import sqlite3
import sys
import os

# Add the parent directory to the path so we can import from budgeit
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from budgeit.logic.add_transactions import (
    TransactionData,
    BudgetData,
    TransactionDatabase,
    TransactionValidator,
    BudgetManager,
    UIManager,
    TransactionService,
    AddTransactions,
    DatabaseInterface,
)
from PySide6.QtCore import QDate
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QMessageBox


class TestTransactionData(unittest.TestCase):
    def test_transaction_data_creation(self):
        """Test TransactionData dataclass creation and to_dict method."""
        transaction = TransactionData(
            user_id=1,
            amount=100.50,
            description="Test transaction",
            category="Food",
            date="2023-01-01",
        )

        self.assertEqual(transaction.user_id, 1)
        self.assertEqual(transaction.amount, 100.50)
        self.assertEqual(transaction.description, "Test transaction")
        self.assertEqual(transaction.category, "Food")
        self.assertEqual(transaction.date, "2023-01-01")

        expected_dict = {
            "user_id": 1,
            "amount": 100.50,
            "description": "Test transaction",
            "category": "Food",
            "date": "2023-01-01",
        }
        self.assertEqual(transaction.to_dict(), expected_dict)


class TestBudgetData(unittest.TestCase):
    def test_budget_data_creation(self):
        """Test BudgetData dataclass creation."""
        budget = BudgetData(
            remaining_category_budget=500.0,
            remaining_monthly_savings=1000.0,
            remaining_monthly_budget=2000.0,
        )

        self.assertEqual(budget.remaining_category_budget, 500.0)
        self.assertEqual(budget.remaining_monthly_savings, 1000.0)
        self.assertEqual(budget.remaining_monthly_budget, 2000.0)


class TestTransactionValidator(unittest.TestCase):
    def test_validate_input_valid(self):
        """Test validation with valid input."""
        is_valid, message, amount = TransactionValidator.validate_input(
            "100.50", "Test description"
        )

        self.assertTrue(is_valid)
        self.assertEqual(message, "")
        self.assertEqual(amount, 100.50)

    def test_validate_input_with_peso_sign(self):
        """Test validation with peso sign and commas."""
        is_valid, message, amount = TransactionValidator.validate_input(
            "₱1,500.75", "Test description"
        )

        self.assertTrue(is_valid)
        self.assertEqual(message, "")
        self.assertEqual(amount, 1500.75)

    def test_validate_input_empty_amount(self):
        """Test validation with empty amount."""
        is_valid, message, amount = TransactionValidator.validate_input(
            "", "Test description"
        )

        self.assertFalse(is_valid)
        self.assertEqual(message, "Please fill in both amount and description fields.")
        self.assertIsNone(amount)

    def test_validate_input_empty_description(self):
        """Test validation with empty description."""
        is_valid, message, amount = TransactionValidator.validate_input("100.50", "")

        self.assertFalse(is_valid)
        self.assertEqual(message, "Please fill in both amount and description fields.")
        self.assertIsNone(amount)

    def test_validate_input_invalid_amount(self):
        """Test validation with invalid amount."""
        is_valid, message, amount = TransactionValidator.validate_input(
            "invalid", "Test description"
        )

        self.assertFalse(is_valid)
        self.assertEqual(message, "Please enter a valid number for the amount.")
        self.assertIsNone(amount)

    def test_validate_input_negative_amount(self):
        """Test validation with negative amount."""
        is_valid, message, amount = TransactionValidator.validate_input(
            "-100", "Test description"
        )

        self.assertFalse(is_valid)
        self.assertEqual(message, "Amount must be greater than zero.")
        self.assertIsNone(amount)

    def test_validate_input_zero_amount(self):
        """Test validation with zero amount."""
        is_valid, message, amount = TransactionValidator.validate_input(
            "0", "Test description"
        )

        self.assertFalse(is_valid)
        self.assertEqual(message, "Amount must be greater than zero.")
        self.assertIsNone(amount)


class TestBudgetManager(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.mock_database = Mock(spec=DatabaseInterface)
        self.budget_manager = BudgetManager(self.mock_database)

    @patch("budgeit.logic.add_transactions.QMessageBox.question")
    def test_process_transaction_sufficient_budget(self, mock_question):
        """Test processing transaction with sufficient budget."""
        # Setup
        budget_data = BudgetData(
            remaining_category_budget=500.0,
            remaining_monthly_savings=1000.0,
            remaining_monthly_budget=2000.0,
        )
        self.mock_database.get_remaining_budget.return_value = budget_data
        self.mock_database.update_category_budget.return_value = True
        self.mock_database.update_monthly_savings.return_value = True
        self.mock_database.update_monthly_budget.return_value = True

        # Execute
        success, message = self.budget_manager.process_transaction_budget_impact(
            user_id=1, amount=100.0, category="Food", report_date="2023-01"
        )

        # Assert
        self.assertTrue(success)
        self.assertEqual(message, "Transaction processed successfully.")
        self.mock_database.update_category_budget.assert_called_once_with(
            1, "2023-01", "Food", 100.0
        )
        self.mock_database.update_monthly_savings.assert_called_once_with(
            1, "2023-01", 100.0
        )
        self.mock_database.update_monthly_budget.assert_called_once_with(
            1, "2023-01", 100.0
        )
        mock_question.assert_not_called()

    @patch("budgeit.logic.add_transactions.QMessageBox.question")
    def test_process_transaction_insufficient_category_budget_user_cancels(
        self, mock_question
    ):
        """Test processing transaction with insufficient category budget where user cancels."""
        # Setup
        budget_data = BudgetData(
            remaining_category_budget=50.0,
            remaining_monthly_savings=1000.0,
            remaining_monthly_budget=2000.0,
        )
        self.mock_database.get_remaining_budget.return_value = budget_data
        mock_question.return_value = QMessageBox.No

        # Execute
        success, message = self.budget_manager.process_transaction_budget_impact(
            user_id=1, amount=100.0, category="Food", report_date="2023-01"
        )

        # Assert
        self.assertFalse(success)
        self.assertEqual(message, "Transaction cancelled by user.")
        mock_question.assert_called_once()

    @patch("budgeit.logic.add_transactions.QMessageBox.question")
    def test_process_transaction_no_budget_data(self, mock_question):
        """Test processing transaction when budget data is not available."""
        # Setup
        self.mock_database.get_remaining_budget.return_value = None

        # Execute
        success, message = self.budget_manager.process_transaction_budget_impact(
            user_id=1, amount=100.0, category="Food", report_date="2023-01"
        )

        # Assert
        self.assertFalse(success)
        self.assertEqual(message, "Unable to retrieve budget information.")
        mock_question.assert_not_called()


class TestUIManager(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.mock_amount_edit = Mock()
        self.mock_description_edit = Mock()
        self.mock_category_combo = Mock()

        self.ui_manager = UIManager(
            self.mock_amount_edit, self.mock_description_edit, self.mock_category_combo
        )

    def test_get_input_data(self):
        """Test getting input data from UI components."""
        # Setup
        self.mock_amount_edit.text.return_value = "  100.50  "
        self.mock_description_edit.text.return_value = "  Test description  "
        self.mock_category_combo.currentText.return_value = "Food"

        # Execute
        amount_text, description, category = self.ui_manager.get_input_data()

        # Assert
        self.assertEqual(amount_text, "100.50")
        self.assertEqual(description, "Test description")
        self.assertEqual(category, "Food")

    def test_clear_inputs(self):
        """Test clearing UI inputs."""
        # Execute
        self.ui_manager.clear_inputs()

        # Assert
        self.mock_amount_edit.clear.assert_called_once()
        self.mock_description_edit.clear.assert_called_once()
        self.mock_category_combo.setCurrentIndex.assert_called_once_with(0)

    @patch("budgeit.logic.add_transactions.QMessageBox.warning")
    def test_show_error(self, mock_warning):
        """Test showing error message."""
        UIManager.show_error("Test Title", "Test Message")
        mock_warning.assert_called_once_with(None, "Test Title", "Test Message")

    @patch("budgeit.logic.add_transactions.QMessageBox.critical")
    def test_show_critical_error(self, mock_critical):
        """Test showing critical error message."""
        UIManager.show_critical_error("Test Title", "Test Message")
        mock_critical.assert_called_once_with(None, "Test Title", "Test Message")


class TestTransactionService(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.mock_database = Mock(spec=DatabaseInterface)
        self.mock_budget_manager = Mock()
        self.transaction_service = TransactionService(
            self.mock_database, self.mock_budget_manager
        )

    @patch("budgeit.logic.add_transactions.UIManager.show_error")
    def test_add_transaction_invalid_input(self, mock_show_error):
        """Test adding transaction with invalid input."""
        # Execute
        success = self.transaction_service.add_transaction(
            1, "", "Test description", "Food"
        )

        # Assert
        self.assertFalse(success)
        mock_show_error.assert_called_once()

    @patch("budgeit.logic.add_transactions.QDate")
    @patch("budgeit.logic.add_transactions.UIManager.show_error")
    def test_add_transaction_budget_failure(self, mock_show_error, mock_qdate):
        """Test adding transaction when budget processing fails."""
        # Setup
        mock_date = Mock()
        mock_date.toString.side_effect = ["2023-01-01", "2023-01"]
        mock_qdate.currentDate.return_value = mock_date

        self.mock_budget_manager.process_transaction_budget_impact.return_value = (
            False,
            "Budget error",
        )

        # Execute
        success = self.transaction_service.add_transaction(
            1, "100.50", "Test description", "Food"
        )

        # Assert
        self.assertFalse(success)
        mock_show_error.assert_called_once_with("Budget Error", "Budget error")

    @patch("budgeit.logic.add_transactions.QDate")
    @patch("budgeit.logic.add_transactions.UIManager.show_critical_error")
    def test_add_transaction_database_insert_failure(
        self, mock_show_critical_error, mock_qdate
    ):
        """Test adding transaction when database insert fails."""
        # Setup
        mock_date = Mock()
        mock_date.toString.side_effect = ["2023-01-01", "2023-01"]
        mock_qdate.currentDate.return_value = mock_date

        self.mock_budget_manager.process_transaction_budget_impact.return_value = (
            True,
            "Success",
        )
        self.mock_database.insert_transaction.return_value = False

        # Execute
        success = self.transaction_service.add_transaction(
            1, "100.50", "Test description", "Food"
        )

        # Assert
        self.assertFalse(success)
        mock_show_critical_error.assert_called_once_with(
            "Error", "Failed to add transaction to database."
        )

    @patch("budgeit.logic.add_transactions.QDate")
    def test_add_transaction_success(self, mock_qdate):
        """Test successful transaction addition."""
        # Setup
        mock_date = Mock()
        mock_date.toString.side_effect = ["2023-01-01", "2023-01"]
        mock_qdate.currentDate.return_value = mock_date

        self.mock_budget_manager.process_transaction_budget_impact.return_value = (
            True,
            "Success",
        )
        self.mock_database.insert_transaction.return_value = True
        self.mock_database.update_monthly_expenses.return_value = True

        # Execute
        success = self.transaction_service.add_transaction(
            1, "100.50", "Test description", "Food"
        )

        # Assert
        self.assertTrue(success)
        self.mock_database.insert_transaction.assert_called_once()
        self.mock_database.update_monthly_expenses.assert_called_once_with(
            1, "2023-01", 100.50
        )


class TestTransactionDatabase(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures with in-memory database."""
        # Create a shared in-memory database
        self.conn = sqlite3.connect(":memory:")
        self.transaction_db = TransactionDatabase(":memory:")

        # Patch the database connection method to use our test connection
        self.original_get_connection = (
            self.transaction_db._TransactionDatabase__get_connection
        )
        self.transaction_db._TransactionDatabase__get_connection = lambda: self.conn

        # Create test tables
        cursor = self.conn.cursor()
        # Create remaining_budgets table
        cursor.execute(
            """
            CREATE TABLE remaining_budgets (
                user_id INTEGER,
                report_date TEXT,
                remaining_food_budget REAL,
                remaining_utilities_budget REAL,
                remaining_health_wellness_budget REAL,
                remaining_personal_lifestyle_budget REAL,
                remaining_education_budget REAL,
                remaining_transportation_budget REAL,
                remaining_miscellaneous_budget REAL,
                remaining_monthly_savings REAL,
                remaining_monthly_budget REAL
            )
        """
        )
        # Create user_data table
        cursor.execute(
            """
            CREATE TABLE user_data (
                user_id INTEGER,
                report_date TEXT,
                monthly_expenses REAL
            )
        """
        )
        # Insert test data
        cursor.execute(
            """
            INSERT INTO remaining_budgets VALUES 
            (1, '2023-01', 500.0, 300.0, 200.0, 150.0, 100.0, 250.0, 100.0, 1000.0, 2000.0)
        """
        )
        cursor.execute(
            """
            INSERT INTO user_data VALUES (1, '2023-01', 0.0)
        """
        )
        self.conn.commit()

    def tearDown(self):
        """Clean up test fixtures."""
        self.transaction_db._TransactionDatabase__get_connection = (
            self.original_get_connection
        )
        self.conn.close()

    def test_get_remaining_budget_success(self):
        """Test successful budget retrieval."""
        budget_data = self.transaction_db.get_remaining_budget(1, "2023-01", "Food")

        self.assertIsNotNone(budget_data)
        self.assertEqual(budget_data.remaining_category_budget, 500.0)
        self.assertEqual(budget_data.remaining_monthly_savings, 1000.0)
        self.assertEqual(budget_data.remaining_monthly_budget, 2000.0)

    def test_get_remaining_budget_invalid_category(self):
        """Test budget retrieval with invalid category."""
        budget_data = self.transaction_db.get_remaining_budget(
            1, "2023-01", "InvalidCategory"
        )

        self.assertIsNone(budget_data)

    def test_update_category_budget_success(self):
        """Test successful category budget update."""
        success = self.transaction_db.update_category_budget(
            1, "2023-01", "Food", 100.0
        )

        self.assertTrue(success)

        # Verify the update
        budget_data = self.transaction_db.get_remaining_budget(1, "2023-01", "Food")
        self.assertEqual(budget_data.remaining_category_budget, 400.0)

    def test_insert_transaction_success(self):
        """Test successful transaction insertion."""
        transaction = TransactionData(
            user_id=1,
            amount=100.50,
            description="Test transaction",
            category="Food",
            date="2023-01-01",
        )

        success = self.transaction_db.insert_transaction(transaction)
        self.assertTrue(success)

        # Verify the insertion
        cursor = self.conn.cursor()
        result = cursor.execute(
            "SELECT * FROM transactions WHERE user_id = ? AND description = ?",
            (1, "Test transaction"),
        ).fetchone()

        self.assertIsNotNone(result)
        self.assertEqual(result[3], 100.50)  # amount
        self.assertEqual(result[4], "Test transaction")  # description
        self.assertEqual(result[5], "Food")  # category


class TestAddTransactions(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.mock_amount_edit = Mock()
        self.mock_description_edit = Mock()
        self.mock_category_combo = Mock()
        self.mock_model = Mock(spec=QStandardItemModel)
        self.mock_database = Mock(spec=DatabaseInterface)

        self.add_transactions = AddTransactions(
            user_id=1,
            amount_edit=self.mock_amount_edit,
            description_edit=self.mock_description_edit,
            category_combo=self.mock_category_combo,
            model=self.mock_model,
            database=self.mock_database,
        )

    @patch("budgeit.logic.add_transactions.UIManager.show_critical_error")
    def test_add_entry_exception_handling(self, mock_show_critical_error):
        """Test exception handling in add_entry method."""
        # Setup to raise an exception
        self.mock_amount_edit.text.side_effect = Exception("Test exception")

        # Execute
        success = self.add_transactions.add_entry()

        # Assert
        self.assertFalse(success)
        mock_show_critical_error.assert_called_once()


if __name__ == "__main__":
    unittest.main()
