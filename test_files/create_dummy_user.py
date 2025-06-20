import sqlite3
import random
import datetime
from dateutil.relativedelta import relativedelta


class DummyUserCreator:
    def __init__(self, db_name="budgeit/accounts.db"):
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

        # Expanded and more diverse transaction descriptions for each category
        self.transaction_descriptions = {
            "Food": [
                "Grocery shopping at supermarket",
                "Fine dining restaurant",
                "Local coffee shop",
                "Fast food drive-through",
                "Food delivery service",
                "Organic market shopping",
                "Bakery pastries",
                "Fresh seafood purchase",
                "Specialty cheese shop",
                "Wine and spirits",
                "Street food vendor",
                "Meal prep ingredients",
                "International cuisine",
                "Farmers market",
                "Protein supplements",
                "Gourmet chocolate",
                "Ice cream parlor",
                "Juice bar smoothie",
                "Catering for event",
                "Cooking class supplies",
                "BBQ and grilling",
                "Healthy snack box",
                "Premium tea collection",
                "Artisan bread",
                "Late night food order",
            ],
            "Utilities": [
                "Electricity bill - summer peak",
                "Water and sewage bill",
                "High-speed internet package",
                "Natural gas heating",
                "Mobile phone plan",
                "Premium cable package",
                "Waste management fee",
                "Home security system",
                "Property insurance premium",
                "HOA monthly dues",
                "Streaming service bundle",
                "Cloud storage subscription",
                "VPN service",
                "Energy bill - winter heating",
                "Satellite TV service",
                "Home warranty plan",
                "Smart home devices",
                "Solar panel maintenance",
                "Utility deposit",
                "Emergency repair service",
            ],
            "Health & Wellness": [
                "Annual physical exam",
                "Prescription medications",
                "Premium gym membership",
                "Vitamin supplements",
                "Dental cleaning",
                "Eye examination",
                "Blood work lab tests",
                "Physical therapy session",
                "Mental health counseling",
                "Health insurance premium",
                "Massage therapy",
                "Chiropractic treatment",
                "Yoga class membership",
                "Personal trainer sessions",
                "Specialized medical equipment",
                "Alternative medicine treatment",
                "Nutritionist consultation",
                "Wellness retreat",
                "Medical emergency visit",
                "Preventive health screening",
                "Skincare products",
                "Sports injury treatment",
                "Meditation app subscription",
                "Health monitoring device",
                "Emergency medical expense",
            ],
            "Personal & Lifestyle": [
                "Designer clothing purchase",
                "Concert tickets",
                "Movie theater outing",
                "Weekend getaway",
                "Hobby supplies",
                "Personal grooming",
                "Birthday gift",
                "Magazine subscriptions",
                "Beauty salon treatment",
                "Sports equipment",
                "Books and audiobooks",
                "Gaming console",
                "Art supplies",
                "Musical instrument",
                "Photography gear",
                "Home decoration",
                "Jewelry purchase",
                "Spa day treatment",
                "Social event hosting",
                "Premium software license",
                "Craft supplies",
                "Collectibles purchase",
                "Party planning",
                "Personal styling service",
                "Luxury watch",
                "Weekend activities",
                "Social club membership",
            ],
            "Education": [
                "University tuition payment",
                "Professional certification",
                "Online course enrollment",
                "Academic textbooks",
                "Educational software",
                "Workshop attendance fee",
                "Conference registration",
                "Training materials",
                "Skill development course",
                "Language learning app",
                "Professional exam fee",
                "Research materials",
                "Educational equipment",
                "Seminar participation",
                "Academic conference travel",
                "Professional development",
                "Industry certification",
                "Continuing education",
                "Educational consulting",
                "Student loan payment",
                "Academic supplies",
                "Online learning platform",
                "Professional coaching",
                "Skills assessment",
                "Educational technology",
            ],
            "Transportation": [
                "Premium gasoline fill-up",
                "Public transit monthly pass",
                "Ride-sharing service",
                "Vehicle maintenance service",
                "Airport parking fee",
                "Highway tolls",
                "Comprehensive car insurance",
                "Vehicle registration renewal",
                "Premium tire replacement",
                "Oil change and tune-up",
                "Car wash and detailing",
                "Parking meter fees",
                "Long-distance travel",
                "Vehicle repair service",
                "Auto parts purchase",
                "Roadside assistance",
                "Fuel efficiency upgrade",
                "Vehicle inspection",
                "Transportation for emergency",
                "Car rental service",
                "Motorcycle maintenance",
                "Bicycle purchase",
                "Public parking garage",
                "Vehicle accessories",
                "Professional driving course",
            ],
            "Miscellaneous": [
                "Bank service fees",
                "ATM withdrawal fees",
                "Charitable donations",
                "Home repairs",
                "Professional services",
                "Legal consultation",
                "Tax preparation service",
                "Insurance claims",
                "Investment fees",
                "Emergency fund contribution",
                "Pet care expenses",
                "Veterinary bills",
                "Travel insurance",
                "Safety equipment",
                "Professional tools",
                "Business expenses",
                "Consulting services",
                "Equipment rental",
                "Maintenance contracts",
                "Miscellaneous fees",
                "Professional memberships",
                "Industry subscriptions",
                "Unexpected expenses",
                "Service charges",
                "Administrative fees",
            ],
        }

        # Different spending profiles for variety
        self.spending_profiles = {
            "conservative": {
                "income_range": (45000, 75000),
                "savings_rate": (0.15, 0.25),
                "food_weight": 0.30,
                "utilities_weight": 0.25,
                "discretionary_spending": 0.20,
            },
            "moderate": {
                "income_range": (60000, 100000),
                "savings_rate": (0.10, 0.20),
                "food_weight": 0.28,
                "utilities_weight": 0.20,
                "discretionary_spending": 0.35,
            },
            "lifestyle": {
                "income_range": (80000, 150000),
                "savings_rate": (0.08, 0.18),
                "food_weight": 0.25,
                "utilities_weight": 0.15,
                "discretionary_spending": 0.45,
            },
            "high_earner": {
                "income_range": (120000, 250000),
                "savings_rate": (0.20, 0.35),
                "food_weight": 0.20,
                "utilities_weight": 0.12,
                "discretionary_spending": 0.50,
            },
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

    def get_seasonal_multiplier(self, month):
        """Get seasonal spending multiplier"""
        seasonal_multipliers = {
            1: 0.85,  # January - post-holiday recovery
            2: 0.90,  # February - low spending
            3: 0.95,  # March - moderate
            4: 1.05,  # April - spring activities
            5: 1.10,  # May - spring/summer prep
            6: 1.15,  # June - vacation season
            7: 1.20,  # July - peak summer
            8: 1.15,  # August - summer activities
            9: 1.00,  # September - back to school
            10: 1.05,  # October - fall activities
            11: 1.25,  # November - holiday prep
            12: 1.40,  # December - holiday season
        }
        return seasonal_multipliers.get(month, 1.0)

    def generate_monthly_budget_data(
        self, user_id, year, month, profile_name="moderate"
    ):
        """Generate realistic monthly budget data with profile variation"""
        profile = self.spending_profiles[profile_name]

        # Base monthly income with variation
        income_min, income_max = profile["income_range"]
        base_income = random.randint(income_min, income_max)

        # Add monthly variation (±10%)
        monthly_variation = random.uniform(0.90, 1.10)
        monthly_income = int(base_income * monthly_variation)

        # Monthly savings based on profile
        savings_min, savings_max = profile["savings_rate"]
        savings_rate = random.uniform(savings_min, savings_max)
        monthly_savings = max(0, int(monthly_income * savings_rate))

        # Get seasonal multiplier
        seasonal_multiplier = self.get_seasonal_multiplier(month)

        # Monthly budget (remaining income after savings, adjusted for season)
        available_for_spending = monthly_income - monthly_savings
        monthly_budget = max(0, int(available_for_spending * seasonal_multiplier))

        # Distribute budget across categories with profile-based weighting
        food_weight = profile["food_weight"] * random.uniform(0.8, 1.2)
        utilities_weight = profile["utilities_weight"] * random.uniform(0.9, 1.1)

        food_budget = max(
            0, int(monthly_budget * food_weight * random.uniform(0.20, 0.40))
        )
        utilities_budget = max(
            0, int(monthly_budget * utilities_weight * random.uniform(0.15, 0.30))
        )
        health_wellness_budget = max(
            0, int(monthly_budget * random.uniform(0.05, 0.20))
        )
        personal_lifestyle_budget = max(
            0, int(monthly_budget * random.uniform(0.10, 0.30))
        )
        education_budget = max(0, int(monthly_budget * random.uniform(0.02, 0.15)))
        transportation_budget = max(0, int(monthly_budget * random.uniform(0.10, 0.25)))

        # Miscellaneous gets the remainder
        allocated = (
            food_budget
            + utilities_budget
            + health_wellness_budget
            + personal_lifestyle_budget
            + education_budget
            + transportation_budget
        )
        miscellaneous_budget = max(0, monthly_budget - allocated)

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

    def generate_large_expense(self, category):
        """Generate occasional large expenses"""
        large_expenses = {
            "Food": ("Catering for large event", random.uniform(3000, 8000)),
            "Utilities": ("HVAC system repair", random.uniform(2000, 6000)),
            "Health & Wellness": (
                "Emergency medical procedure",
                random.uniform(5000, 15000),
            ),
            "Personal & Lifestyle": ("Luxury vacation", random.uniform(4000, 12000)),
            "Education": (
                "Professional certification course",
                random.uniform(2000, 8000),
            ),
            "Transportation": ("Major car repair", random.uniform(3000, 10000)),
            "Miscellaneous": ("Home renovation", random.uniform(5000, 20000)),
        }
        return large_expenses.get(
            category, ("Large expense", random.uniform(1000, 5000))
        )

    def generate_transactions_for_month(self, user_id, year, month, budgets):
        """Generate realistic and varied transactions for a specific month"""
        transactions = []
        total_expenses = 0

        # Vary number of transactions significantly (10-60 transactions)
        base_transactions = random.randint(15, 45)
        seasonal_modifier = self.get_seasonal_multiplier(month)
        num_transactions = max(
            10, int(base_transactions * seasonal_modifier * random.uniform(0.7, 1.3))
        )

        # Category spending tracking
        category_spending = {category: 0 for category in self.categories}

        # 10% chance of having a large expense this month
        has_large_expense = random.random() < 0.10
        if has_large_expense:
            large_category = random.choice(self.categories)
            large_desc, large_amount = self.generate_large_expense(large_category)

            day = random.randint(1, 28)
            transaction_date = f"{year}-{month:02d}-{day:02d}"

            transactions.append(
                (user_id, transaction_date, large_amount, large_desc, large_category)
            )
            category_spending[large_category] += large_amount
            total_expenses += large_amount

        # Generate regular transactions
        for _ in range(num_transactions):
            # Random day in the month
            day = random.randint(1, 28)
            transaction_date = f"{year}-{month:02d}-{day:02d}"

            # Choose category with varied weights
            category_weights = {
                "Food": 35,
                "Utilities": 12,
                "Transportation": 18,
                "Personal & Lifestyle": 20,
                "Health & Wellness": 8,
                "Miscellaneous": 12,
                "Education": 5,
            }

            category = random.choices(
                list(category_weights.keys()), weights=list(category_weights.values())
            )[0]

            # Determine amount based on category with much wider ranges
            budget_key = (
                category.lower().replace(" & ", "_").replace(" ", "_") + "_budget"
            )
            remaining_budget = max(
                0, budgets.get(budget_key, 5000) - category_spending[category]
            )

            if remaining_budget <= 10:
                continue

            # Generate amount with much more variation
            if category == "Food":
                # Range from small snacks to expensive meals
                choices = [
                    random.uniform(15, 150),  # 60% - regular meals
                    random.uniform(150, 500),  # 30% - expensive meals
                    random.uniform(500, 1200),  # 10% - very expensive
                ]
                weights = [6, 3, 1]
                amount = random.choices(choices, weights=weights)[0]
            elif category == "Utilities":
                # Utilities can vary significantly
                amount = random.uniform(200, min(4000, remaining_budget * 0.8))
            elif category == "Transportation":
                # Transportation varies a lot
                choices = [
                    random.uniform(10, 100),  # Small trips
                    random.uniform(100, 400),  # Regular expenses
                    random.uniform(400, 1500),  # Larger expenses
                ]
                weights = [4, 3, 1]
                amount = random.choices(choices, weights=weights)[0]
            elif category == "Health & Wellness":
                # Health expenses can be very varied
                choices = [
                    random.uniform(20, 200),  # Regular items
                    random.uniform(200, 800),  # Medical visits
                    random.uniform(800, 3000),  # Procedures/equipment
                ]
                weights = [5, 3, 1]
                amount = random.choices(choices, weights=weights)[0]
            elif category == "Education":
                # Education can be expensive
                amount = random.uniform(100, min(6000, remaining_budget * 0.9))
            elif category == "Personal & Lifestyle":
                # Very wide range for lifestyle
                choices = [
                    random.uniform(25, 200),  # Regular purchases
                    random.uniform(200, 800),  # Medium purchases
                    random.uniform(800, 3000),  # Luxury items
                ]
                weights = [6, 3, 1]
                amount = random.choices(choices, weights=weights)[0]
            else:  # Miscellaneous
                # Miscellaneous can be anything
                amount = random.uniform(20, min(2500, remaining_budget * 0.7))

            # Apply seasonal variation to amounts
            seasonal_multiplier = self.get_seasonal_multiplier(month)
            amount *= random.uniform(0.7, seasonal_multiplier)

            # Ensure amount is positive and doesn't exceed remaining budget
            amount = max(1, min(round(amount, 2), remaining_budget))

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
        self,
        username="dummy_user",
        email="dummy@example.com",
        password="dummy123",
        profile="moderate",
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
            print(f"Using spending profile: {profile}")

            while current_date <= end_date:
                year = current_date.year
                month = current_date.month

                print(f"Processing {year}-{month:02d}...")

                # Generate monthly budget data with profile
                budgets = self.generate_monthly_budget_data(
                    user_id, year, month, profile
                )

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
            print(f"   - Spending profile: {profile}")
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
    print("🚀 Creating dummy users with 3 years of varied transaction data...")

    # Create multiple users with different profiles
    users_to_create = [
        ("demo_conservative", "conservative@budgeit.com", "demo123", "conservative"),
        ("demo_moderate", "moderate@budgeit.com", "demo123", "moderate"),
        ("demo_lifestyle", "lifestyle@budgeit.com", "demo123", "lifestyle"),
        ("demo_high_earner", "high_earner@budgeit.com", "demo123", "high_earner"),
    ]

    for username, email, password, profile in users_to_create:
        print(f"\n{'='*50}")
        print(f"Creating user: {username} with {profile} profile")
        print(f"{'='*50}")

        creator = DummyUserCreator()
        success = creator.create_three_years_data(username, email, password, profile)

        if success:
            print(f"✅ {username} created successfully!")
        else:
            print(f"❌ Failed to create {username}")

    print("\n🎉 All dummy users creation completed!")
    print("\nYou can now log in with any of these accounts:")
    for username, email, password, profile in users_to_create:
        print(f"  Username: {username} | Password: {password} | Profile: {profile}")


if __name__ == "__main__":
    main()
