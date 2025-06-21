import sqlite3
from .database_manager import get_database_path


class UserDataManager:
    def __init__(self):
        self.__connect = sqlite3.connect(get_database_path())
        self.__cursor = self.__connect.cursor()
        self.__current_user_id = None
        self.__current_email = None
        self._create_tables()

    @property
    def current_user_id(self):
        """Get the current user ID."""
        return self.__current_user_id

    @property
    def current_email(self):
        """Get the current user email."""
        return self.__current_email

    def _create_tables(self):
        """Create necessary database tables if they don't exist"""
        self.__cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
               user_id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT UNIQUE NOT NULL,
               password TEXT NOT NULL,
               email TEXT UNIQUE NOT NULL)"""
        )

        self.__cursor.execute(
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
        self.__connect.commit()

    def signup(self, username, password, confirm_password, email):
        if not all([username, password, confirm_password, email]):
            print("All fields are required.")
            return False

        if password != confirm_password:
            print("Passwords do not match.")
            return False

        self.__cursor.execute(
            "SELECT username FROM users WHERE username = ?", (username,)
        )
        if self.__cursor.fetchone():
            print("Username already exists.")
            return False

        self.__cursor.execute("SELECT email FROM users WHERE email = ?", (email,))
        if self.__cursor.fetchone():
            print("Email already exists.")
            return False

        try:
            self.__cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (?,?,?)",
                (username, password, email),
            )
            self.__connect.commit()

            self.__cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
            result = self.__cursor.fetchone()
            if result:
                self.__current_user_id = result[0]
                self.__current_email = email
                print(f"Registration successful. User ID: {self.current_user_id}")

            return True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False

    def signin(self, email, password):
        if not all([email, password]):
            print("Email and password are required.")
            return False

        try:
            self.__cursor.execute(
                "SELECT user_id, username FROM users WHERE email = ? AND password = ?",
                (email, password),
            )
            data = self.__cursor.fetchone()
            if data:
                self.__current_user_id = data[0]
                self.__current_email = email
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
        if not self.__current_user_id:
            print("Please log in first.")
            return False

        self.__cursor.execute(
            "SELECT data_id FROM user_data WHERE user_id = ?",
            (self.__current_user_id,),
        )
        if self.__cursor.fetchone():
            print("User budget data already exists. Use update method to modify.")
            return False

        self.__cursor.execute(
            "INSERT INTO user_data (user_id, monthly_income, monthly_budget, food_budget, utilities_budget, health_wellness_budget, personal_lifestyle_budget, education_budget, transportation_budget, miscellaneous_budget) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (
                self.__current_user_id,
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
        self.__connect.commit()
        print(f"Budget data added successfully for user ID: {self.__current_user_id}")
        return True

    def get_user_data(self):
        if not self.__current_user_id:
            print("Please log in first.")
            return None

        self.__cursor.execute(
            "SELECT * FROM user_data WHERE user_id = ?",
            (self.__current_user_id,),
        )
        return self.__cursor.fetchone()

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
        if not self.__current_user_id:
            print("Please log in first.")
            return False

        self.__cursor.execute(
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
                self.__current_user_id,
            ),
        )
        self.__connect.commit()
        print(f"Budget data updated successfully for user ID: {self.__current_user_id}")
        return True

    def signout(self):
        self.__current_user_id = None
        self.__current_email = None
        print("Logged out successfully.")

    def close_connection(self):
        """Close the database connection"""
        if self.__connect:
            self.__connect.close()
