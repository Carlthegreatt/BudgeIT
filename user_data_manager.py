import sqlite3
from AuthorizationManager import AuthManager

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


class UserDataManager(AuthManager):
    def __init__(self, connect, cursor):
        super().__init__(connect, cursor)
        self.current_user_id = None  # Track currently logged in user
        self.current_email = None

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
        # Check if user is logged in
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

username = "car"
email = "car@gmail.com"
password = "09082005"
confirm_password = "09082005"


def signin(email, password):
    user_manager = UserDataManager(connect, cursor)
    if user_manager.signin(email, password):
        # Add budget data for the logged-in user
        user_manager.add_user_data()
        # Retrieve and display user data
        data = user_manager.get_user_data()
        if data:
            print(f"User budget data: {data}")


def signup(username, password, confirm_password, email):
    user_manager = UserDataManager(connect, cursor)
    if user_manager.signup(username, password, confirm_password, email):
        print("User signuped successfully.")
    else:
        print("User registration failed.")


def signout():
    user_manager = UserDataManager(connect, cursor)
    user_manager.signout()


# signup(username, password, confirm_password, email)
signin(email, password)
# signout()

signin("carl1@gmail.com", "0908005")
