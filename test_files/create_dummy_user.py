import sqlite3
import random
import datetime
from dateutil.relativedelta import relativedelta


class DummyUserCreator:
    def __init__(self, db_name="accounts.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        # Categories available in the system
        self.categories = [
            "Food",
            "Utilities",
            "Health & Wellness",
            "Personal & Lifestyle",
            "Education",
            "Transportation",
            "Miscellaneous",
        ]

        # Sample transaction descriptions for each category
        self.transaction_descriptions = {
            "Food": [
                "Grocery shopping",
                "Restaurant meal",
                "Coffee shop",
                "Fast food",
                "Lunch delivery",
                "Dinner out",
                "Snacks",
                "Bakery items",
                "Fruits and vegetables",
                "Meat and dairy",
            ],
            "Utilities": [
                "Electricity bill",
                "Water bill",
                "Internet bill",
                "Gas bill",
                "Phone bill",
                "Cable TV",
                "Trash collection",
                "Home insurance",
                "Property tax",
                "HOA fees",
            ],
            "Health & Wellness": [
                "Doctor visit",
                "Pharmacy",
                "Gym membership",
                "Vitamins",
                "Dental care",
                "Eye exam",
                "Medical tests",
                "Physical therapy",
                "Wellness supplements",
                "Health insurance",
            ],
            "Personal & Lifestyle": [
                "Clothing",
                "Entertainment",
                "Movies",
                "Hobbies",
                "Personal care",
                "Gifts",
                "Subscriptions",
                "Beauty products",
                "Sports equipment",
                "Books and magazines",
            ],
            "Education": [
                "Tuition fees",
                "Books",
                "Online courses",
                "Supplies",
                "Certification",
                "Workshop",
                "Training materials",
                "Software licenses",
                "Educational tools",
                "Exam fees",
            ],
            "Transportation": [
                "Gas",
                "Public transport",
                "Uber/Taxi",
                "Car maintenance",
                "Parking",
                "Tolls",
                "Car insurance",
                "Vehicle registration",
                "Tire replacement",
                "Oil change",
            ],
            "Miscellaneous": [
                "Bank fees",
                "ATM fees",
                "Donations",
                "Repairs",
                "Cleaning supplies",
                "Office supplies",
                "Pet care",
                "Travel",
                "Emergency expenses",
                "Other",
            ],
        }

    def create_dummy_user(
        self, username="dummy_user", email="dummy@example.com", password="dummy123"
    ):
        """Create a dummy user in the database"""
        try:
            # Check if user already exists
            self.cursor.execute(
                "SELECT user_id FROM users WHERE username = ? OR email = ?",
                (username, email),
            )
            if self.cursor.fetchone():
                print(
                    f"User {username} already exists. Removing existing user first..."
                )
                self.remove_existing_user(username, email)

            # Insert user
            self.cursor.execute(
                "INSERT INTO users (username, password, email, account_setup) VALUES (?, ?, ?, ?)",
                (
                    username,
                    password,
                    email,
                    1,
                ),  # account_setup = 1 means setup is complete
            )

            # Get the user_id
            user_id = self.cursor.lastrowid
            print(f"Created user: {username} with ID: {user_id}")

            return user_id

        except sqlite3.Error as e:
            print(f"Error creating user: {e}")
            return None

    def remove_existing_user(self, username, email):
        """Remove existing user and all related data"""
        try:
            # Get user_id first
            self.cursor.execute(
                "SELECT user_id FROM users WHERE username = ? OR email = ?",
                (username, email),
            )
            result = self.cursor.fetchone()
            if result:
                user_id = result[0]

                # Delete from all related tables
                self.cursor.execute(
                    "DELETE FROM transactions WHERE user_id = ?", (user_id,)
                )
                self.cursor.execute(
                    "DELETE FROM remaining_budgets WHERE user_id = ?", (user_id,)
                )
                self.cursor.execute(
                    "DELETE FROM user_data WHERE user_id = ?", (user_id,)
                )
                self.cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))

                print(f"Removed existing user data for user_id: {user_id}")

        except sqlite3.Error as e:
            print(f"Error removing existing user: {e}")

    def generate_monthly_budget_data(self, user_id, year, month):
        """Generate realistic monthly budget data"""
        # Base monthly income (random between 50,000-120,000)
        monthly_income = random.randint(50000, 120000)

        # Monthly savings (10-20% of income)
        monthly_savings = max(0, int(monthly_income * random.uniform(0.10, 0.20)))

        # Monthly budget (70-80% of income after savings)
        monthly_budget = max(
            0, int((monthly_income - monthly_savings) * random.uniform(0.70, 0.80))
        )

        # Distribute budget across categories - ensure all are positive
        food_budget = max(0, int(monthly_budget * random.uniform(0.25, 0.35)))
        utilities_budget = max(0, int(monthly_budget * random.uniform(0.15, 0.25)))
        health_wellness_budget = max(
            0, int(monthly_budget * random.uniform(0.08, 0.15))
        )
        personal_lifestyle_budget = max(
            0, int(monthly_budget * random.uniform(0.10, 0.20))
        )
        education_budget = max(0, int(monthly_budget * random.uniform(0.05, 0.12)))
        transportation_budget = max(0, int(monthly_budget * random.uniform(0.15, 0.25)))
        miscellaneous_budget = max(
            0,
            monthly_budget
            - (
                food_budget
                + utilities_budget
                + health_wellness_budget
                + personal_lifestyle_budget
                + education_budget
                + transportation_budget
            ),
        )

        report_date = f"{year}-{month:02d}"

        # Insert user_data
        self.cursor.execute(
            """
            INSERT INTO user_data (
                user_id, monthly_savings, monthly_expenses, monthly_income, monthly_budget,
                food_budget, utilities_budget, health_wellness_budget, personal_lifestyle_budget,
                education_budget, transportation_budget, miscellaneous_budget, report_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                user_id,
                monthly_savings,
                0,
                monthly_income,
                monthly_budget,
                food_budget,
                utilities_budget,
                health_wellness_budget,
                personal_lifestyle_budget,
                education_budget,
                transportation_budget,
                miscellaneous_budget,
                report_date,
            ),
        )

        return {
            "food_budget": food_budget,
            "utilities_budget": utilities_budget,
            "health_wellness_budget": health_wellness_budget,
            "personal_lifestyle_budget": personal_lifestyle_budget,
            "education_budget": education_budget,
            "transportation_budget": transportation_budget,
            "miscellaneous_budget": miscellaneous_budget,
            "monthly_budget": monthly_budget,
            "monthly_savings": monthly_savings,
            "monthly_income": monthly_income,
        }

    def generate_transactions_for_month(self, user_id, year, month, budgets):
        """Generate realistic transactions for a specific month"""
        transactions = []
        total_expenses = 0

        # Number of transactions per month (random between 15-45)
        num_transactions = random.randint(15, 45)

        # Category spending tracking
        category_spending = {category: 0 for category in self.categories}

        # Generate transactions
        for _ in range(num_transactions):
            # Random day in the month
            day = random.randint(1, 28)  # Use 28 to avoid month-end issues
            transaction_date = f"{year}-{month:02d}-{day:02d}"

            # Choose category (weighted towards Food and Utilities)
            category_weights = {
                "Food": 30,
                "Utilities": 15,
                "Transportation": 15,
                "Personal & Lifestyle": 15,
                "Health & Wellness": 10,
                "Miscellaneous": 10,
                "Education": 5,
            }

            category = random.choices(
                list(category_weights.keys()), weights=list(category_weights.values())
            )[0]

            # Determine amount based on category and remaining budget
            budget_key = (
                category.lower().replace(" & ", "_").replace(" ", "_") + "_budget"
            )
            remaining_budget = max(
                0, budgets.get(budget_key, 5000) - category_spending[category]
            )

            if remaining_budget <= 0:
                continue

            # Generate amount based on category with proper bounds
            if category == "Food":
                max_amount = min(1500, remaining_budget)
                amount = random.uniform(50, max(50, max_amount))
            elif category == "Utilities":
                max_amount = min(3000, remaining_budget)
                amount = random.uniform(500, max(500, max_amount))
            elif category == "Transportation":
                max_amount = min(2000, remaining_budget)
                amount = random.uniform(100, max(100, max_amount))
            elif category == "Health & Wellness":
                max_amount = min(2500, remaining_budget)
                amount = random.uniform(200, max(200, max_amount))
            elif category == "Education":
                max_amount = min(5000, remaining_budget)
                amount = random.uniform(300, max(300, max_amount))
            elif category == "Personal & Lifestyle":
                max_amount = min(3000, remaining_budget)
                amount = random.uniform(100, max(100, max_amount))
            else:  # Miscellaneous
                max_amount = min(2000, remaining_budget)
                amount = random.uniform(50, max(50, max_amount))

            # Ensure amount is positive and doesn't exceed remaining budget
            amount = max(0, min(round(amount, 2), remaining_budget))

            # Skip if amount is 0 or very small
            if amount < 1:
                continue

            # Random description for the category
            description = random.choice(self.transaction_descriptions[category])

            transactions.append(
                (user_id, transaction_date, amount, description, category)
            )
            category_spending[category] += amount
            total_expenses += amount

        return transactions, total_expenses

    def update_remaining_budgets(self, user_id, year, month, budgets, total_expenses):
        """Update remaining budgets after generating transactions"""
        report_date = f"{year}-{month:02d}"

        # Calculate remaining amounts - ensure all values are non-negative
        remaining_monthly_budget = max(0, budgets["monthly_budget"] - total_expenses)
        remaining_monthly_savings = max(
            0,
            (
                budgets["monthly_savings"]
                - (total_expenses - budgets["monthly_budget"])
                if total_expenses > budgets["monthly_budget"]
                else budgets["monthly_savings"]
            ),
        )
        # Ensure remaining income cannot be negative
        remaining_income = max(0, budgets["monthly_income"] - total_expenses)

        # Individual category remaining budgets (simplified - set to 0 for realism)
        self.cursor.execute(
            """
            INSERT INTO remaining_budgets (
                user_id, remaining_income, remaining_monthly_savings, remaining_monthly_budget,
                remaining_food_budget, remaining_utilities_budget, remaining_health_wellness_budget,
                remaining_personal_lifestyle_budget, remaining_education_budget,
                remaining_transportation_budget, remaining_miscellaneous_budget, report_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                user_id,
                remaining_income,
                remaining_monthly_savings,
                remaining_monthly_budget,
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

    def update_monthly_expenses(self, user_id, year, month, total_expenses):
        """Update the monthly expenses in user_data table"""
        report_date = f"{year}-{month:02d}"

        # Ensure total_expenses is not negative
        total_expenses = max(0, total_expenses)

        self.cursor.execute(
            """
            UPDATE user_data 
            SET monthly_expenses = ? 
            WHERE user_id = ? AND report_date = ?
        """,
            (total_expenses, user_id, report_date),
        )

    def create_three_years_data(
        self, username="dummy_user", email="dummy@example.com", password="dummy123"
    ):
        """Create a dummy user with 3 years of transaction data"""
        try:
            # Create the user
            user_id = self.create_dummy_user(username, email, password)
            if not user_id:
                return False

            # Generate data for the last 3 years
            end_date = datetime.date.today()
            start_date = end_date - relativedelta(years=3)

            current_date = start_date
            transaction_count = 0

            print(f"Generating data from {start_date} to {end_date}")

            while current_date <= end_date:
                year = current_date.year
                month = current_date.month

                print(f"Processing {year}-{month:02d}...")

                # Generate monthly budget data
                budgets = self.generate_monthly_budget_data(user_id, year, month)

                # Generate transactions for the month
                transactions, total_expenses = self.generate_transactions_for_month(
                    user_id, year, month, budgets
                )

                # Insert transactions
                self.cursor.executemany(
                    """
                    INSERT INTO transactions (user_id, transaction_date, amount, description, category)
                    VALUES (?, ?, ?, ?, ?)
                """,
                    transactions,
                )

                transaction_count += len(transactions)

                # Update monthly expenses
                self.update_monthly_expenses(user_id, year, month, total_expenses)

                # Update remaining budgets
                self.update_remaining_budgets(
                    user_id, year, month, budgets, total_expenses
                )

                # Move to next month
                current_date = current_date + relativedelta(months=1)

            # Commit all changes
            self.connection.commit()

            print(f"\n✅ Successfully created dummy user '{username}' with:")
            print(f"   - User ID: {user_id}")
            print(f"   - Total transactions: {transaction_count}")
            print(f"   - Data span: {start_date} to {end_date}")
            print(f"   - Database: {self.db_name}")

            return True

        except Exception as e:
            print(f"❌ Error creating dummy user data: {e}")
            self.connection.rollback()
            return False

        finally:
            self.cursor.close()
            self.connection.close()


def main():
    """Main function to create dummy user data"""
    print("🚀 Creating dummy user with 3 years of transaction data...")

    # Create the dummy user creator
    creator = DummyUserCreator()

    # Create the user with 3 years of data
    success = creator.create_three_years_data(
        username="demo_user", email="demo@budgeit.com", password="demo123"
    )

    if success:
        print("\n🎉 Dummy user creation completed successfully!")
        print("\nYou can now log in with:")
        print("  Username: demo_user")
        print("  Password: demo123")
        print("  Email: demo@budgeit.com")
    else:
        print("\n❌ Failed to create dummy user data.")


if __name__ == "__main__":
    main()
