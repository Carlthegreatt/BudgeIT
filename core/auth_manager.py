import sqlite3
from components.emailautomation import EmailSender
from PySide6.QtWidgets import QMessageBox
from contextlib import contextmanager
from datetime import datetime


@contextmanager
def get_db_connection():
    connect = sqlite3.connect("accounts.db")
    try:
        yield connect
    finally:
        connect.close()


with get_db_connection() as connect:
    report_date = datetime.today().strftime("%Y-%m")

    cursor = connect.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users(
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   account_setup INTEGER NOT NULL)"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS user_data(
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
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS remaining_budgets(
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
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS transactions(
            data_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            transaction_date TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL
        )"""
    )

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS meta (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """
    )

    connect.commit()


class AuthManager:
    def __init__(self, username_line, password_line, confirm_line, email_line):
        self.connect = sqlite3.connect("accounts.db")
        self.cursor = self.connect.cursor()
        self.username_line_widget = username_line
        self.password_line_widget = password_line
        self.confirm_line_widget = confirm_line
        self.email_line_widget = email_line

    def __del__(self):
        if hasattr(self, "cursor"):
            self.cursor.close()
        if hasattr(self, "connect"):
            self.connect.close()

    def signup(self, username_line, password_line, confirm_line, email_line):
        username = username_line.text().strip()
        password = password_line.text().strip()
        confirm_password = confirm_line.text().strip()
        email = email_line.text().strip()

        if not all([username, password, confirm_password, email]):
            print("All fields are required.")
            return False

        print(f"Password length: {len(password)}")
        print(f"Confirm password length: {len(confirm_password)}")
        print(f"Passwords match: {password == confirm_password}")

        password = password.strip()
        confirm_password = confirm_password.strip()

        if password != confirm_password:
            print("Passwords do not match.")
            return False

        self.cursor.execute(
            "SELECT username FROM users WHERE username = ?", (username,)
        )
        if self.cursor.fetchone():
            print("Username already exists.")
            return False

        self.cursor.execute("SELECT email FROM users WHERE email = ?", (email,))
        if self.cursor.fetchone():
            print("Email already exists.")
            return False

        try:
            if EmailSender(email, username).send_email():
                with get_db_connection() as connect:
                    cursor = connect.cursor()
                    cursor.execute(
                        "INSERT INTO users (username, password, email, account_setup) VALUES (?,?,?,?)",
                        (username, password, email, False),
                    )
                    connect.commit()

                    cursor.execute(
                        "SELECT rowid FROM users ORDER BY rowid DESC LIMIT 1"
                    )
                    row = cursor.fetchone()
                    last_id = row[0] if row else None

                    cursor.execute(
                        "INSERT INTO user_data (user_id, monthly_savings, monthly_expenses, monthly_income, monthly_budget, food_budget, utilities_budget, health_wellness_budget, personal_lifestyle_budget, education_budget, transportation_budget, miscellaneous_budget, report_date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            last_id,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            report_date,
                        ),
                    )

                    cursor.execute(
                        "INSERT INTO remaining_budgets (user_id, remaining_income, remaining_monthly_savings, remaining_monthly_budget, remaining_food_budget, remaining_utilities_budget, remaining_health_wellness_budget, remaining_personal_lifestyle_budget, remaining_education_budget, remaining_transportation_budget, remaining_miscellaneous_budget, report_date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                        (last_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, report_date),
                    )

                    connect.commit()
                print("Registration successful.")
                return True
            else:
                QMessageBox.warning(
                    None,
                    "Invalid Email",
                    "Please check your email and try again.",
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
            self.cursor.execute(
                "SELECT user_id, username FROM users WHERE email = ? AND password = ?",
                (email, password),
            )
            data = self.cursor.fetchone()
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
        if hasattr(self, "current_user_id"):
            return self.current_user_id
        return None
