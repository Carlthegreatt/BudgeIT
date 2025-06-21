import unittest
from unittest.mock import Mock, MagicMock, patch, call
import sqlite3
import sys
import os
from contextlib import contextmanager

# Add the parent directory to the path so we can import from budgeit
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from budgeit.logic.auth_manager import AuthManager, DatabaseManager, get_db_connection
from PySide6.QtWidgets import QMessageBox, QLineEdit


class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures with in-memory database."""
        self.db_manager = DatabaseManager()
        # Override db_path to use in-memory database for testing
        # Force initialization to create tables
        self.db_manager._initialize_database()

    @patch("budgeit.logic.auth_manager.get_database_path")
    def test_database_manager_initialization(self, mock_get_db_path):
        """Test DatabaseManager initialization."""
        mock_get_db_path.return_value = "test_path.db"
        db_manager = DatabaseManager()

        self.assertEqual(db_manager.db_path, "test_path.db")
        self.assertIsNotNone(db_manager.report_date)
        mock_get_db_path.assert_called_once()

    def test_get_connection_context_manager(self):
        """Test database connection context manager."""
        with self.db_manager.get_connection() as conn:
            self.assertIsInstance(conn, sqlite3.Connection)
            # Test that connection is working
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            self.assertEqual(result[0], 1)


class TestAuthManager(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.mock_username_widget = Mock(spec=QLineEdit)
        self.mock_password_widget = Mock(spec=QLineEdit)
        self.mock_confirm_widget = Mock(spec=QLineEdit)
        self.mock_email_widget = Mock(spec=QLineEdit)

        # Create AuthManager with mocked database
        with patch("budgeit.logic.auth_manager.DatabaseManager") as mock_db_class:
            self.mock_db_manager = Mock()
            mock_db_class.return_value = self.mock_db_manager
            self.auth_manager = AuthManager(
                self.mock_username_widget,
                self.mock_password_widget,
                self.mock_confirm_widget,
                self.mock_email_widget,
            )
            self.auth_manager.db_manager = self.mock_db_manager

    def test_validate_signup_fields_empty_fields(self):
        """Test validation with empty fields."""
        is_valid, message = self.auth_manager._validate_signup_fields(
            "", "password123", "password123", "test@example.com"
        )

        self.assertFalse(is_valid)
        self.assertEqual(message, "All fields are required.")

    def test_validate_signup_fields_password_mismatch(self):
        """Test validation with password mismatch."""
        is_valid, message = self.auth_manager._validate_signup_fields(
            "testuser", "password123", "differentpassword", "test@example.com"
        )

        self.assertFalse(is_valid)
        self.assertEqual(message, "Passwords do not match.")

    def test_check_existing_user_username_exists(self):
        """Test checking existing user when username already exists."""
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.side_effect = [("existing_user",), None]

        mock_context_manager = MagicMock()
        mock_context_manager.__enter__.return_value = mock_connection
        mock_context_manager.__exit__.return_value = None
        self.mock_db_manager.get_connection.return_value = mock_context_manager

        exists, message = self.auth_manager._check_existing_user(
            "existing_user", "new@example.com"
        )

        self.assertFalse(exists)
        self.assertEqual(message, "Username already exists.")

    def test_check_existing_user_email_exists(self):
        """Test checking existing user when email already exists."""
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.side_effect = [None, ("existing@example.com",)]

        mock_context_manager = MagicMock()
        mock_context_manager.__enter__.return_value = mock_connection
        mock_context_manager.__exit__.return_value = None
        self.mock_db_manager.get_connection.return_value = mock_context_manager

        exists, message = self.auth_manager._check_existing_user(
            "newuser", "existing@example.com"
        )

        self.assertFalse(exists)
        self.assertEqual(message, "Email already exists.")

    def test_check_existing_user_new_user(self):
        """Test checking existing user with new credentials."""
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.side_effect = [None, None]

        mock_context_manager = MagicMock()
        mock_context_manager.__enter__.return_value = mock_connection
        mock_context_manager.__exit__.return_value = None
        self.mock_db_manager.get_connection.return_value = mock_context_manager

        exists, message = self.auth_manager._check_existing_user(
            "newuser", "new@example.com"
        )

        self.assertTrue(exists)
        self.assertEqual(message, "")

    def test_create_user_record(self):
        """Test creating a new user record."""
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = (123,)  # New user ID

        mock_context_manager = MagicMock()
        mock_context_manager.__enter__.return_value = mock_connection
        mock_context_manager.__exit__.return_value = None
        self.mock_db_manager.get_connection.return_value = mock_context_manager
        self.mock_db_manager.report_date = "2023-12"

        user_id = self.auth_manager._create_user_record(
            "testuser", "password123", "test@example.com"
        )

        self.assertEqual(user_id, 123)

        # Verify user insertion
        mock_cursor.execute.assert_any_call(
            "INSERT INTO users (username, password, email, account_setup) VALUES (?,?,?,?)",
            ("testuser", "password123", "test@example.com", False),
        )

    @patch("budgeit.logic.auth_manager.EmailSender")
    def test_signup_success(self, mock_email_sender):
        """Test successful signup process."""
        # Mock widgets
        self.mock_username_widget.text.return_value = "testuser"
        self.mock_password_widget.text.return_value = "password123"
        self.mock_confirm_widget.text.return_value = "password123"
        self.mock_email_widget.text.return_value = "test@example.com"

        # Mock email sender
        mock_email_instance = Mock()
        mock_email_sender.return_value = mock_email_instance
        mock_email_instance.send_email.return_value = True

        # Mock database operations
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.side_effect = [
            None,
            None,
            (123,),
        ]  # No existing user, new user ID

        mock_context_manager = MagicMock()
        mock_context_manager.__enter__.return_value = mock_connection
        mock_context_manager.__exit__.return_value = None
        self.mock_db_manager.get_connection.return_value = mock_context_manager
        self.mock_db_manager.report_date = "2023-12"

        result = self.auth_manager.signup(
            self.mock_username_widget,
            self.mock_password_widget,
            self.mock_confirm_widget,
            self.mock_email_widget,
        )

        self.assertTrue(result)
        mock_email_sender.assert_called_once_with("test@example.com", "testuser")
        mock_email_instance.send_email.assert_called_once()

    @patch("budgeit.logic.auth_manager.EmailSender")
    def test_signup_invalid_email(self, mock_email_sender):
        """Test signup with invalid email."""
        # Mock widgets
        self.mock_username_widget.text.return_value = "testuser"
        self.mock_password_widget.text.return_value = "password123"
        self.mock_confirm_widget.text.return_value = "password123"
        self.mock_email_widget.text.return_value = "invalid@example.com"

        # Mock email sender failure
        mock_email_instance = Mock()
        mock_email_sender.return_value = mock_email_instance
        mock_email_instance.send_email.return_value = False

        # Mock database operations for user checking
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.side_effect = [None, None]  # No existing user

        mock_context_manager = MagicMock()
        mock_context_manager.__enter__.return_value = mock_connection
        mock_context_manager.__exit__.return_value = None
        self.mock_db_manager.get_connection.return_value = mock_context_manager

        with patch("budgeit.logic.auth_manager.QMessageBox.warning") as mock_warning:
            result = self.auth_manager.signup(
                self.mock_username_widget,
                self.mock_password_widget,
                self.mock_confirm_widget,
                self.mock_email_widget,
            )

            self.assertFalse(result)
            mock_warning.assert_called_once()

    def test_signin_success(self):
        """Test successful signin process."""
        # Mock widgets
        self.mock_email_widget.text.return_value = "test@example.com"
        self.mock_password_widget.text.return_value = "password123"

        # Mock database operations
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = (123, "testuser")  # Valid user

        mock_context_manager = MagicMock()
        mock_context_manager.__enter__.return_value = mock_connection
        mock_context_manager.__exit__.return_value = None
        self.mock_db_manager.get_connection.return_value = mock_context_manager

        result = self.auth_manager.signin(
            self.mock_email_widget, self.mock_password_widget
        )

        self.assertEqual(result, 123)
        self.assertEqual(self.auth_manager.current_user_id, 123)

        # Verify widgets are cleared
        self.mock_email_widget.clear.assert_called_once()
        self.mock_password_widget.clear.assert_called_once()

    def test_signin_invalid_credentials(self):
        """Test signin with invalid credentials."""
        # Mock widgets
        self.mock_email_widget.text.return_value = "wrong@example.com"
        self.mock_password_widget.text.return_value = "wrongpassword"

        # Mock database operations
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None  # No matching user

        mock_context_manager = MagicMock()
        mock_context_manager.__enter__.return_value = mock_connection
        mock_context_manager.__exit__.return_value = None
        self.mock_db_manager.get_connection.return_value = mock_context_manager

        result = self.auth_manager.signin(
            self.mock_email_widget, self.mock_password_widget
        )

        self.assertFalse(result)
        self.assertIsNone(self.auth_manager.current_user_id)

    def test_signin_empty_fields(self):
        """Test signin with empty fields."""
        # Mock widgets with empty values
        self.mock_email_widget.text.return_value = ""
        self.mock_password_widget.text.return_value = "password123"

        result = self.auth_manager.signin(
            self.mock_email_widget, self.mock_password_widget
        )

        self.assertFalse(result)

    def test_signin_database_error(self):
        """Test signin with database error."""
        # Mock widgets
        self.mock_email_widget.text.return_value = "test@example.com"
        self.mock_password_widget.text.return_value = "password123"

        # Mock database error
        self.mock_db_manager.get_connection.side_effect = sqlite3.Error(
            "Database error"
        )

        result = self.auth_manager.signin(
            self.mock_email_widget, self.mock_password_widget
        )

        self.assertFalse(result)

    def test_create_initial_user_data(self):
        """Test creation of initial user data records."""
        mock_cursor = Mock()
        self.auth_manager.db_manager.report_date = "2023-12"

        self.auth_manager._create_initial_user_data(mock_cursor, 123)

        # Check that both user_data and remaining_budgets records are created
        self.assertEqual(mock_cursor.execute.call_count, 2)

        # Verify user_data insertion
        user_data_call = mock_cursor.execute.call_args_list[0]
        self.assertIn("INSERT INTO user_data", user_data_call[0][0])
        self.assertEqual(user_data_call[0][1][0], 123)  # user_id

        # Verify remaining_budgets insertion
        remaining_budgets_call = mock_cursor.execute.call_args_list[1]
        self.assertIn("INSERT INTO remaining_budgets", remaining_budgets_call[0][0])
        self.assertEqual(remaining_budgets_call[0][1][0], 123)  # user_id


class TestGetDbConnection(unittest.TestCase):
    """Test the get_db_connection context manager function."""

    @patch("budgeit.logic.auth_manager.DatabaseManager")
    def test_get_db_connection(self, mock_db_manager_class):
        """Test get_db_connection context manager."""
        # Mock DatabaseManager instance
        mock_db_manager = Mock()
        mock_db_manager_class.return_value = mock_db_manager

        # Mock connection context manager
        mock_connection = Mock()
        mock_context_manager = MagicMock()
        mock_context_manager.__enter__.return_value = mock_connection
        mock_context_manager.__exit__.return_value = None
        mock_db_manager.get_connection.return_value = mock_context_manager

        # Test the context manager
        with get_db_connection() as conn:
            self.assertEqual(conn, mock_connection)

        # Verify DatabaseManager was created and get_connection was called
        mock_db_manager_class.assert_called_once()
        mock_db_manager.get_connection.assert_called_once()


if __name__ == "__main__":
    unittest.main()
