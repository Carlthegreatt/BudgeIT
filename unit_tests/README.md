# Unit Tests for BudgeIT

This directory contains unit tests for the BudgeIT application.

## Running Tests

### Run All Tests
```bash
cd unit_tests
python -m unittest discover -v
```

### Run Specific Test File
```bash
cd unit_tests
python -m unittest test_add_transactions.py -v
```

### Run Specific Test Class
```bash
cd unit_tests
python -m unittest test_add_transactions.TestTransactionValidator -v
```

### Run Specific Test Method
```bash
cd unit_tests
python -m unittest test_add_transactions.TestTransactionValidator.test_validate_input_valid -v
```

## Test Coverage

### test_add_transactions.py
Tests for the `budgeit/logic/add_transactions.py` module:

- **TransactionData**: Tests for the transaction data dataclass
- **BudgetData**: Tests for the budget data dataclass  
- **TransactionValidator**: Tests for input validation logic
- **BudgetManager**: Tests for budget processing and validation
- **UIManager**: Tests for UI interaction methods
- **TransactionService**: Tests for the main transaction service
- **TransactionDatabase**: Tests for database operations with in-memory database
- **AddTransactions**: Tests for the main transaction addition class

### test_auth_manager.py
Tests for the `budgeit/logic/auth_manager.py` module:

- **DatabaseManager**: Tests for database initialization, connection management, and table creation
- **AuthManager**: Tests for user authentication, signup/signin processes, and user management
- **get_db_connection**: Tests for the database connection context manager function

Key test areas covered:
- Database table creation and structure validation
- User signup validation (field validation, duplicate checking, email verification)
- User signin authentication (credential validation, error handling)
- Database connection management and error handling
- User data initialization for new accounts

## Dependencies

The tests use Python's built-in `unittest` framework and `unittest.mock` for mocking dependencies. External dependencies like PySide6 are mocked to avoid UI dependencies during testing.

## Test Structure

- Each test class corresponds to a class in the main application
- Tests use descriptive names explaining what they test
- Mock objects are used to isolate units under test
- Database tests use in-memory SQLite for isolation
- Exception handling and edge cases are covered 