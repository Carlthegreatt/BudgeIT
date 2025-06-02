import sqlite3

connect = sqlite3.connect("accounts.db")
cursor = connect.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
               user_id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT UNIQUE NOT NULL,
               password TEXT NOT NULL,
               email TEXT UNIQUE NOT NULL)"""
)


class AuthManager:
    def __init__(self, username_line, password_line, confirm_line, email_line):
        # Get database connection
        self.connect = sqlite3.connect("accounts.db")
        self.cursor = self.connect.cursor()

        # Store UI element references
        self.username_line_widget = username_line
        self.password_line_widget = password_line
        self.confirm_line_widget = confirm_line
        self.email_line_widget = email_line

    def signup(self):
        # Get values from UI elements
        username = self.username_line_widget.text().strip()
        password = self.password_line_widget.text().strip()
        confirm_password = self.confirm_line_widget.text().strip()
        email = self.email_line_widget.text().strip()

        # Validation
        if not all([username, password, confirm_password, email]):
            print("All fields are required.")
            return False

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
                "INSERT INTO users (username, password, email) VALUES (?,?,?)",
                (username, password, email),
            )
            self.connect.commit()
            print("Registration successful.")

            # Clear form fields
            self.username_line_widget.clear()
            self.password_line_widget.clear()
            self.confirm_line_widget.clear()
            self.email_line_widget.clear()

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

        # Get fresh database connection for signin
        connect = sqlite3.connect("accounts.db")
        cursor = connect.cursor()

        try:
            cursor.execute(
                "SELECT user_id, username FROM users WHERE email = ? AND password = ?",
                (email, password),
            )
            data = cursor.fetchone()
            if data:
                self.current_user_id = data[0]
                self.current_email = email
                print(f"Signin successful. Welcome {data[1]} (ID: {data[0]})")

                # Clear form fields
                email_widget.clear()
                password_widget.clear()

                return True
            else:
                print("Invalid email or password.")
                return False
        finally:
            cursor.close()
            connect.close()
