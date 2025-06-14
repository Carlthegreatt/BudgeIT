import sqlite3

# Remove the import of AuthManager since we'll implement our own auth methods
# from AuthorizationManager import AuthManager

# Use the same database as AuthManager for consistency
connect = sqlite3.connect("accounts.db")
cursor = connect.cursor()

# Fixed table schema - removed duplicate email/password, added foreign key reference
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

# Ensure users table exists (same as in AuthorizationManager)
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
               user_id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT UNIQUE NOT NULL,
               password TEXT NOT NULL,
               email TEXT UNIQUE NOT NULL)"""
)


class UserDataManager:
    def __init__(self, connect, cursor):
        self.connect = connect
        self.cursor = cursor
        self.current_user_id = None  # Track currently logged in user
        self.current_email = None

    def signup(self, username, password, confirm_password, email):
        """Register a new user"""
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

            # Get the newly created user's ID
            self.cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
            result = self.cursor.fetchone()
            if result:
                self.current_user_id = result[0]
                self.current_email = email
                print(f"Registration successful. User ID: {self.current_user_id}")

            return True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False

    def signin(self, email, password):
        """Sign in an existing user"""
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
                self.current_email = email
                print(f"Signin successful. Welcome {data[1]} (ID: {data[0]})")
                return True
            else:
                print("Invalid email or password.")
                return False
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def add_user_data(
        self,
        monthly_income=0,
        monthly_budget=0,
        food_budget=0,
        utilities_budget=0,
        health_wellness_budget=0,
        personal_lifestyle_budget=0,
        education_budget=0,
        transportation_budget=0,
        miscellaneous_budget=0,
    ):
        if not self.current_user_id:
            print("Please log in first.")
            return False

        # Check if user already has budget data
        self.cursor.execute(
            "SELECT data_id FROM user_data WHERE user_id = ?",
            (self.current_user_id,),
        )
        if self.cursor.fetchone():
            print("User budget data already exists. Use update method to modify.")
            return False

        # Insert new budget data for the current user
        self.cursor.execute(
            "INSERT INTO user_data (user_id, monthly_income, monthly_budget, food_budget, utilities_budget, health_wellness_budget, personal_lifestyle_budget, education_budget, transportation_budget, miscellaneous_budget) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (
                self.current_user_id,
                monthly_income,
                monthly_budget,
                food_budget,
                utilities_budget,
                health_wellness_budget,
                personal_lifestyle_budget,
                education_budget,
                transportation_budget,
                miscellaneous_budget,
            ),
        )
        self.connect.commit()
        print(f"Budget data added successfully for user ID: {self.current_user_id}")
        return True

    def get_user_data(self):
        """Get budget data for current user"""
        if not self.current_user_id:
            print("Please log in first.")
            return None

        self.cursor.execute(
            "SELECT * FROM user_data WHERE user_id = ?",
            (self.current_user_id,),
        )
        return self.cursor.fetchone()

    def update_user_data(
        self,
        monthly_income,
        monthly_budget,
        food_budget,
        utilities_budget,
        health_wellness_budget,
        personal_lifestyle_budget,
        education_budget,
        transportation_budget,
        miscellaneous_budget,
    ):
        """Update existing budget data for current user"""
        if not self.current_user_id:
            print("Please log in first.")
            return False

        self.cursor.execute(
            """UPDATE user_data SET 
            monthly_income = ?, monthly_budget = ?, food_budget = ?, 
            utilities_budget = ?, health_wellness_budget = ?, 
            personal_lifestyle_budget = ?, education_budget = ?, 
            transportation_budget = ?, miscellaneous_budget = ?
            WHERE user_id = ?""",
            (
                monthly_income,
                monthly_budget,
                food_budget,
                utilities_budget,
                health_wellness_budget,
                personal_lifestyle_budget,
                education_budget,
                transportation_budget,
                miscellaneous_budget,
                self.current_user_id,
            ),
        )
        self.connect.commit()
        print(f"Budget data updated successfully for user ID: {self.current_user_id}")
        return True

    def signout(self):
        """Clear current user session"""
        self.current_user_id = None
        self.current_email = None
        print("Logged out successfully.")


# Example usage with proper session management

username = "cal"
email = "ca1@gmail.com"
password = "09082005"
confirm_password = "09082005"


user_manager = UserDataManager(connect, cursor)
user_manager.signup(username, password, confirm_password, email)
