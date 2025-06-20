import sqlite3
from ..utils.email_automation import EmailSender
from PySide6.QtWidgets import QMessageBox
from contextlib import contextmanager
from datetime import datetime
from .database_manager import get_database_path


class DatabaseManager:
    def __init__(self):
        self.db_path = get_database_path()
        self.report_date = datetime.today().strftime("%Y-%m")
        self._initialize_database()

    @contextmanager
    def get_connection(self):
        connection = sqlite3.connect(self.db_path)
        try:
            yield connection
        finally:
            connection.close()

    def _initialize_database(self):
        with self.get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users(
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    account_setup INTEGER NOT NULL
                )
            """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS user_data(
                    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    monthly_savings INTEGER NOT NULL,
                    monthly_expenses INTEGER NOT NULL,
                    monthly_income INTEGER NOT NULL,
                    monthly_budget INTEGER NOT NULL,
                    food_budget INTEGER NOT NULL,
                    utilities_budget INTEGER NOT NULL,
                    health_wellness_budget INTEGER NOT NULL,
                    personal_lifestyle_budget INTEGER NOT NULL,
                    education_budget INTEGER NOT NULL,
                    transportation_budget INTEGER NOT NULL,
                    miscellaneous_budget INTEGER NOT NULL,
                    report_date TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS remaining_budgets(
                    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    remaining_income INTEGER NOT NULL,
                    remaining_monthly_savings INTEGER NOT NULL,
                    remaining_monthly_budget INTEGER NOT NULL,
                    remaining_food_budget INTEGER NOT NULL,
                    remaining_utilities_budget INTEGER NOT NULL,
                    remaining_health_wellness_budget INTEGER NOT NULL,
                    remaining_personal_lifestyle_budget INTEGER NOT NULL,
                    remaining_education_budget INTEGER NOT NULL,
                    remaining_transportation_budget INTEGER NOT NULL,
                    remaining_miscellaneous_budget INTEGER NOT NULL,
                    report_date TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS transactions(
                    data_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    transaction_date TEXT NOT NULL,
                    amount REAL NOT NULL,
                    description TEXT NOT NULL,
                    category TEXT NOT NULL
                )
            """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS meta (
                    key TEXT PRIMARY KEY,
                    value TEXT
                )
            """
            )

            connection.commit()


class AuthManager:
    def __init__(
        self, username_line=None, password_line=None, confirm_line=None, email_line=None
    ):
        self.db_manager = DatabaseManager()
        self.username_line_widget = username_line
        self.password_line_widget = password_line
        self.confirm_line_widget = confirm_line
        self.email_line_widget = email_line
        self.current_user_id = None

    def _validate_signup_fields(self, username, password, confirm_password, email):
        if not all([username, password, confirm_password, email]):
            return False, "All fields are required."

        if password != confirm_password:
            return False, "Passwords do not match."

        return True, ""

    def _check_existing_user(self, username, email):
        with self.db_manager.get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
            if cursor.fetchone():
                return False, "Username already exists."

            cursor.execute("SELECT email FROM users WHERE email = ?", (email,))
            if cursor.fetchone():
                return False, "Email already exists."

        return True, ""

    def _create_user_record(self, username, password, email):
        with self.db_manager.get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO users (username, password, email, account_setup) VALUES (?,?,?,?)",
                (username, password, email, False),
            )

            cursor.execute("SELECT rowid FROM users ORDER BY rowid DESC LIMIT 1")
            user_id = cursor.fetchone()[0]

            self._create_initial_user_data(cursor, user_id)
            connection.commit()

            return user_id

    def _create_initial_user_data(self, cursor, user_id):
        report_date = self.db_manager.report_date

        cursor.execute(
            """
            INSERT INTO user_data (
                user_id, monthly_savings, monthly_expenses, monthly_income, 
                monthly_budget, food_budget, utilities_budget, health_wellness_budget, 
                personal_lifestyle_budget, education_budget, transportation_budget, 
                miscellaneous_budget, report_date
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
            (user_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, report_date),
        )

        cursor.execute(
            """
            INSERT INTO remaining_budgets (
                user_id, remaining_income, remaining_monthly_savings, 
                remaining_monthly_budget, remaining_food_budget, remaining_utilities_budget, 
                remaining_health_wellness_budget, remaining_personal_lifestyle_budget, 
                remaining_education_budget, remaining_transportation_budget, 
                remaining_miscellaneous_budget, report_date
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """,
            (user_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, report_date),
        )

    def signup(self, username_line, password_line, confirm_line, email_line):
        username = username_line.text().strip()
        password = password_line.text().strip()
        confirm_password = confirm_line.text().strip()
        email = email_line.text().strip()

        is_valid, error_message = self._validate_signup_fields(
            username, password, confirm_password, email
        )
        if not is_valid:
            print(error_message)
            return False

        exists, error_message = self._check_existing_user(username, email)
        if not exists:
            print(error_message)
            return False

        try:
            if EmailSender(email, username).send_email():
                self._create_user_record(username, password, email)
                print("Registration successful.")
                return True
            else:
                QMessageBox.warning(
                    None, "Invalid Email", "Please check your email and try again."
                )
                return False

        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False

    def signin(self, email_widget, password_widget):
        email = email_widget.text().strip()
        password = password_widget.text().strip()

        if not all([email, password]):
            print("Email and password are required.")
            return False

        try:
            with self.db_manager.get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT user_id, username FROM users WHERE email = ? AND password = ?",
                    (email, password),
                )
                data = cursor.fetchone()

                if data:
                    self.current_user_id = data[0]
                    print(f"Signin successful. Welcome {data[1]} (ID: {data[0]})")

                    email_widget.clear()
                    password_widget.clear()

                    return self.get_current_user()
                else:
                    print("Invalid email or password.")
                    return False

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def get_current_user(self):
        return self.current_user_id


@contextmanager
def get_db_connection():
    db_manager = DatabaseManager()
    with db_manager.get_connection() as connection:
        yield connection
