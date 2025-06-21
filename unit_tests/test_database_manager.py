import unittest
import sqlite3
import os
from unittest.mock import patch
from datetime import datetime
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from budgeit.logic.database_manager import get_database_path, get_db_connection, check_monthly_reset

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.test_db = "test_accounts.db"
        # Clean up any existing test database
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def tearDown(self):
        # Clean up after tests
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_get_database_path(self):
        path = get_database_path()
        self.assertTrue(path.endswith('accounts.db'))
        self.assertTrue(os.path.dirname(path).endswith('budgeit'))

    def test_get_db_connection(self):
        # Test with default database
        with get_db_connection(self.test_db) as conn:
            self.assertIsInstance(conn, sqlite3.Connection)
            # Verify connection is active
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE test (id INTEGER)")
            conn.commit()

        # Verify connection is closed after context
        with self.assertRaises(sqlite3.ProgrammingError):
            conn.execute("SELECT 1")

    @patch('budgeit.logic.database_manager.datetime')
    def test_check_monthly_reset_same_month(self, mock_datetime):
        # Set up initial state
        mock_datetime.today.return_value = datetime(2023, 6, 15)
        
        with get_db_connection(self.test_db) as conn:
            # First run to set up the initial state
            check_monthly_reset(1)
            
            # Check again in the same month
            result = check_monthly_reset(1)
            self.assertFalse(result)

    @patch('budgeit.logic.database_manager.datetime')
    def test_check_monthly_reset_new_month(self, mock_datetime):
        # Set up initial state
        mock_datetime.today.return_value = datetime(2023, 6, 15)
        with get_db_connection(self.test_db) as conn:
            check_monthly_reset(1)

        # Change current date to next month
        mock_datetime.today.return_value = datetime(2023, 7, 1)
        result = check_monthly_reset(1)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()