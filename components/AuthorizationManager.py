import sqlite3


connect = sqlite3.connect("accounts.db")
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
    data_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    monthly_income INTEGER NOT NULL,
    monthly_budget INTEGER NOT NULL,
    food_budget INTEGER NOT NULL,
    utilities_budget INTEGER NOT NULL,
    health_wellness_budget INTEGER NOT NULL,
    personal_lifestyle_budget INTEGER NOT NULL,
    education_budget INTEGER NOT NULL,
    transportation_budget INTEGER NOT NULL,
    miscellaneous_budget INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
    )"""
)


class AuthManager:
    def __init__(self, username_line, password_line, confirm_line, email_line):
        # Get database connection
        self.connect = sqlite3.connect("accounts.db")
        self.cursor = self.connect.cursor()
        self.username_line_widget = username_line
        self.password_line_widget = password_line
        self.confirm_line_widget = confirm_line
        self.email_line_widget = email_line

    def signup(self, username_line, password_line, confirm_line, email_line):
        # Get values from UI elements
        username = username_line.text().strip()
        password = password_line.text().strip()
        confirm_password = confirm_line.text().strip()
        email = email_line.text().strip()

        # Validation
        if not all([username, password, confirm_password, email]):
            print("All fields are required.")
            return False

        # Debug password matching
        print(f"Password length: {len(password)}")
        print(f"Confirm password length: {len(confirm_password)}")
        print(f"Passwords match: {password == confirm_password}")

        # Strip whitespace and normalize case for comparison
        password = password.strip()
        confirm_password = confirm_password.strip()

        if password != confirm_password:
            print("Passwords do not match.")
            return False

        # Check if username already exists
        self.cursor.execute(
            "SELECT username FROM users WHERE username = ?", (username,)
        )
        if self.cursor.fetchone():
            print("Username already exists.")
            return False

        # Check if email already exists
        self.cursor.execute("SELECT email FROM users WHERE email = ?", (email,))
        if self.cursor.fetchone():
            print("Email already exists.")
            return False

        try:
            self.cursor.execute(
                "INSERT INTO users (username, password, email, account_setup) VALUES (?,?,?,?)",
                (username, password, email, True),
            )
            self.connect.commit()

            self.cursor.execute("SELECT rowid FROM users ORDER BY rowid DESC LIMIT 1")
            row = self.cursor.fetchone()
            last_id = row[0] if row else None

            self.cursor.execute(
                "INSERT INTO user_data (user_id, monthly_income, monthly_budget, food_budget, utilities_budget, health_wellness_budget, personal_lifestyle_budget, education_budget, transportation_budget, miscellaneous_budget) VALUES (?,?,?,?,?,?,?,?,?,?)",
                (last_id, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            )
            self.connect.commit()
            print("Registration successful.")

            return True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            self.cursor.close()
            self.connect.close()

    def signin(self, email_widget, password_widget):
        # Get values from UI elements
        email = email_widget.text().strip()
        password = password_widget.text().strip()

        # Validation
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
            print("from budgetapp")
            return self.current_user_id
        return None
