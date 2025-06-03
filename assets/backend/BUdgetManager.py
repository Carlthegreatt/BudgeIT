from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, List, Union
import mysql.connector
from mysql.connector import Error


@dataclass
class Transaction(ABC):
    """Abstract base transaction class"""
    amount: float
    category: str
    date: str  
    description: str 
    
    @abstractmethod
    def __post_init__(self):
        pass

    def display_info(self) -> str:
        return f"{self.date} | {self.category}: ${self.amount:.2f} - {self.description}"

@dataclass
class Expense(Transaction):
    """Expense transaction (negative amount)"""
    def __post_init__(self):
        self.amount = -abs(self.amount)

@dataclass
class Income(Transaction):
    """Income transaction (positive amount)"""
    def __post_init__(self):
        self.amount = abs(self.amount)

        
class BudgetManager:
    def __init__(self, db_config: dict):
        self.db_config = db_config
        self.connection = None
        self._connect()
        self._initialize_tables()
        self.transactions: list[Transaction] = []
        self.monthly_budget = 0.0
        self._load_initial_data()

    def _connect(self):
        """For MySQL connection"""
        try:
            self.connection = mysql.connector.connect(
                host=self.db_config['host'],
                user=self.db_config['user'],
                password=self.db_config['password'],
                database=self.db_config['database']
            )
        except Error as e:
            raise ConnectionError(f"Failed to connect to database: {e}")

    def _initialize_tables(self):
        """Create tables if don't exist"""
        try:
            cursor = self.connection.cursor()
            
            # Create budget_settings table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS budget_settings (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    monthly_budget DECIMAL(10,2) NOT NULL DEFAULT 0.00
                )
            """)
            
            # Create transactions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    amount DECIMAL(10,2) NOT NULL,
                    category VARCHAR(50) NOT NULL,
                    description TEXT,
                    date DATE NOT NULL
                )
            """)
            
            self.connection.commit()
        except Error as e:
            raise RuntimeError(f"Failed to initialize tables: {e}")
        finally:
            cursor.close()

    def _load_initial_data(self):
        """Load all transactions from database as list"""
        try:
            cursor = self.connection.cursor()
            # Load budget
            cursor.execute("SELECT monthly_budget FROM budget_settings LIMIT 1")
            result = cursor.fetchone()
            if result:
                self.monthly_budget = float(result[0])

            # Load transactions
            cursor.execute("SELECT amount, category, description, date FROM transactions")
            self.transactions = []
            for amount, category, description, date in cursor.fetchall():
                date_str = date.strftime("%Y-%m-%d") if hasattr(date, "strftime") else str(date)
                if amount < 0:
                    trx = Expense(abs(amount), category, date_str, description)
                else:
                    trx = Income(amount, category, date_str, description)
                self.transactions.append(trx)
        except Error as e:
            print(f"Warning: Error loading initial data - {e}")
        finally:
            cursor.close()

    def add_transaction(self, transaction: Transaction) -> bool:
        """Adds transaction with validation"""
        print("Inserting:", transaction.amount, transaction.category, transaction.description, transaction.date)
        try:
            # Validate date
            if not transaction.date:
                print("Error: Transaction date cannot be empty")
                return False
                
            cursor = self.connection.cursor()
            query = """
            INSERT INTO transactions 
                (amount, category, description, date)
            VALUES (%s, %s, %s, %s)
            """
        
            cursor.execute(query, (
                transaction.amount,
                transaction.category,
                transaction.description,
                transaction.date
            ))
            self.connection.commit()
            return True
        except Error as e:
            print(f"Error adding transaction: {e}")
            return False
        finally:
            cursor.close()

    def get_formatted_transactions(self) -> List[Dict]:
        """Converts Transaction objects to dictionary format for DataManager"""
        return [{
            "Date": t.date,
            "Category": t.category,
            "Description": t.description,
            "Amount": t.amount,
            "Type": "expense" if isinstance(t, Expense) else "income"
        } for t in self.transactions]

    def set_budget(self, amount: float) -> bool:
        """Set/update monthly budget"""
        try:
            cursor = self.connection.cursor()
            query = """
            INSERT INTO budget_settings (monthly_budget)
            VALUES (%s)
            ON DUPLICATE KEY UPDATE monthly_budget = VALUES(monthly_budget)
            """
            cursor.execute(query, (amount,))
            self.connection.commit()
            self.monthly_budget = amount
            return True
        except Error as e:
            print(f"Error setting budget: {e}")
            return False
        finally:
            cursor.close()

    def get_summary(self) -> Dict[str, Union[str, float, Dict[str, float]]]:
        """Returns a monthly budget summary"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            current_month = datetime.now().strftime("%B %Y")
            
            # Get income total (positive amounts)
            cursor.execute("""
                SELECT SUM(amount) as total_income
                FROM transactions
                WHERE amount > 0
                AND MONTH(date) = MONTH(CURRENT_DATE())
                AND YEAR(date) = YEAR(CURRENT_DATE())
            """)
            total_income = float(cursor.fetchone()['total_income'] or 0.0)
            
            # Get expense total (negative amounts)
            cursor.execute("""
                SELECT SUM(amount) as total_expenses
                FROM transactions
                WHERE amount < 0
                AND MONTH(date) = MONTH(CURRENT_DATE())
                AND YEAR(date) = YEAR(CURRENT_DATE())
            """)
            total_expenses = abs(float(cursor.fetchone()['total_expenses'] or 0.0))
            
            # Get category breakdown (absolute values)
            cursor.execute("""
                SELECT category, ABS(SUM(amount)) as amount 
                FROM transactions 
                WHERE amount < 0
                AND MONTH(date) = MONTH(CURRENT_DATE())
                AND YEAR(date) = YEAR(CURRENT_DATE())
                GROUP BY category
            """)
            categories = {row['category']: row['amount'] for row in cursor.fetchall()}
            
            return {
                "period": current_month,
                "total_income": total_income,
                "total_expenses": total_expenses,   
                "remaining_budget": self.monthly_budget - total_expenses,
                "categories": categories
            }
        except Error as e:
            raise RuntimeError(f"Failed to generate summary: {e}") from e
        finally:
            cursor.close()

    def get_statistics(self) -> Dict[str, Union[int, float, Dict[str, float]]]:
        """Returns detailed transaction statistics"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            # Get all transactions for stats
            cursor.execute("""
                SELECT 
                    COUNT(*) as total_count,
                    SUM(amount) as total_amount,
                    MAX(CASE WHEN amount > 0 THEN amount ELSE NULL END) as max_income,
                    MAX(CASE WHEN amount < 0 THEN amount ELSE NULL END) as max_expense
                FROM transactions
            """)
            stats = cursor.fetchone()

            largest_income = float(stats['max_income'] or 0.0)
            largest_expense = abs(float(stats['max_expense'] or 0.0))  # Take absolute value for display
            
            if not stats['total_count']:
                return {
                    "total_transactions": 0,
                    "average_transaction": 0.0,
                    "largest_income": 0.0,
                    "largest_expense": 0.0,
                    "category_distribution": {}
                }
            
            # Get category distribution
            cursor.execute("""
                SELECT 
                    category,
                    SUM(amount) as amount 
                FROM transactions 
                WHERE amount < 0
                GROUP BY category
            """)
            category_dist = {row['category']: row['amount'] for row in cursor.fetchall()}
            
            return {
                "total_transactions": stats['total_count'],
                "average_transaction": round(float(stats['total_amount']) / stats['total_count'], 2),
                "largest_income": float(stats['max_income']),
                "largest_expense": abs(float(stats['max_expense'])),
                "category_distribution": category_dist
            }
        except Error as e:
            raise RuntimeError(f"Failed to generate statistics: {e}") from e
        finally:
            cursor.close()

    def close(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def __del__(self):
        """Destructor to ensure connection is closed"""
        self.close()



'''
HEHE copy paste nalangs muna (may binago ako sa get_graph)
'''



from datetime import datetime
from matplotlib import pyplot as plt
from collections import defaultdict

class DataManager:
    def __init__(self, budget_manager: BudgetManager):
        self.budget_manager = budget_manager
        self._transactions = self.budget_manager.get_formatted_transactions()

    def get_report(self, period: str) -> dict:
        """Validation for empty transactions"""
        if not self._transactions:
            return {
                "Period": period,
                "Total_spent": 0.0,
                "Category": {}
            }

        filtered = []
        for transaction in self._transactions:
            try:
                transaction_date = datetime.strptime(transaction["Date"], "%Y-%m-%d")
                if transaction_date.strftime("%B %Y") == period:
                    filtered.append(transaction)
            except (KeyError, ValueError):
                continue  # Skip malformed entries

        report_trx = defaultdict(float)
        total = 0.0
        
        for transaction in filtered:
            try:
                report_trx[transaction["Category"]] += transaction["Amount"]
                total += transaction["Amount"]
            except KeyError:
                continue

        return {
            "Period": period,
            "Total_spent": total,
            "Category": dict(report_trx)
        }

    def get_statistics(self, total_income: float) -> dict:
        """Added complete empty data handling"""
        if not self._transactions:
            return {
                "Total Expenses": 0,
                "Total Income": total_income,
                "Average transaction": "0.00",
                "Largest Transaction": ("N/A", 0),
                "Smallest Transaction": ("N/A", 0),
                "Category Percentage and amount": {}
            }

        total_expense = 0.0
        trx_cnt = []
        trx_cat_total = defaultdict(float)
        
        for transaction in self._transactions:
            try:
                amount = float(transaction["Amount"])
                if amount < 0:  # Only count expenses (negative ule)
                    total_expense += abs(amount)
                    trx_cnt.append((transaction["Category"], abs(amount)))
                    trx_cat_total[transaction["Category"]] += abs(amount)
            except (KeyError, ValueError):
                continue

        trx_cat_ptg = {
            category: (f"{(amount/total_income)*100:.1f}%", amount)
            for category, amount in trx_cat_total.items()
        }

        return {
            "Total Expenses": total_expense,
            "Total Income": total_income,
            "Average transaction": f"{total_expense/len(trx_cnt):.2f}" if trx_cnt else "0.00",
            "Largest Transaction": max(trx_cnt, key=lambda x: x[1]) if trx_cnt else ("N/A", 0),
            "Smallest Transaction": min(trx_cnt, key=lambda x: x[1]) if trx_cnt else ("N/A", 0),
            "Category Percentage and amount": trx_cat_ptg
        }

    def generate_graph(self, total_income: float) -> None:
        """Generate graphs with better error handling"""
        try:
            if not self._transactions:
                print("No transactions to visualize")
                return

            # Get expense data only with proper date validation
            expenses = []
            for t in self._transactions:
                if t.get("Type") != "expense":
                    continue
                    
                # Skip transactions na may missing/invalid dates
                if not t.get("Date"):
                    continue
                    
                try:
                    date = datetime.strptime(t["Date"], "%Y-%m-%d")
                    expenses.append({
                        "Date": date,
                        "Amount": float(abs(t["Amount"])),
                        "Category": t["Category"]
                    })
                except (ValueError, TypeError):
                    continue

            if not expenses:
                print("No valid expense data to visualize")
                return

            # Prepare data
            categories = defaultdict(float)
            for t in expenses:
                categories[t["Category"]] += abs(float(t["Amount"]))

            if not categories:
                print("No expense categories found to plot")
                return

            # Create figures
            plt.figure(figsize=(12, 10))
            
            # Bar Chart
            plt.subplot(2, 2, 1)
            plt.bar(categories.keys(), categories.values())
            plt.title("Spending by Category")
            plt.xticks(rotation=45)
            
            # Pie Chart
            plt.subplot(2, 2, 2)
            plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
            plt.title("Spending Distribution")
            
            # Time Series - parsed datetime objects
            plt.subplot(2, 1, 2)
            dates = [t["Date"] for t in expenses]  # Already datetime objects
            amounts = [t["Amount"] for t in expenses]
            plt.plot(dates, amounts, 'o-')
            plt.title("Spending Over Time")
            plt.gcf().autofmt_xdate()
            
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"Failed to generate graphs: {e}")


# Test :>
# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'MYSQl_105(+-)',
    'database': 'BudgetManager'
}

def main():
    try:
        # Initialize budget manager
        budget_manager = BudgetManager(db_config)
        
        # Set monthly budget
        budget_manager.set_budget(3000.00)
        print(f"Monthly budget set to: ${budget_manager.monthly_budget:.2f}")
        
        # Sample transactions
        current_date = datetime.now().strftime("%Y-%m-%d")
        transactions = [
            Income(2500.00, "Food", current_date, "Dinner with friends"),
            Expense(1200.00, "Utilities", current_date, "Water bills"),
            Expense(300.00, "Education", current_date, "1st sem tuition"),
            Expense(150.00, "Transportation", current_date, "Bus to work"),
            Income(500.00, "Health and Wellness", current_date, "Gym membership")
        ]
        
        for trx in transactions:
            budget_manager.add_transaction(trx)
            print(f"Added transaction: {trx.display_info()}")
        
        # Get summary
        summary = budget_manager.get_summary()
        print("\n=== Monthly Summary ===")
        print(f"Period: {summary['period']}")
        print(f"Income: ${summary['total_income']:.2f}")
        print(f"Expenses: ${summary['total_expenses']:.2f}")
        print(f"Remaining: ${summary['remaining_budget']:.2f}")
        print("Category breakdown:")
        for category, amount in summary['categories'].items():
            print(f"- {category}: ${amount:.2f}")
        
        # Get statistics
        stats = budget_manager.get_statistics()
        print("\n=== Statistics ===")
        print(f"Total transactions: {stats['total_transactions']}")
        print(f"Average transaction: ${stats['average_transaction']:.2f}")
        print(f"Largest income: ${stats['largest_income']:.2f}")
        print(f"Largest expense: ${stats['largest_expense']:.2f}")
        
        # Generate visual report
        data_manager = DataManager(budget_manager)
        print("\nGenerating visual reports...")
        data_manager.generate_graph(summary['total_income'])
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'budget_manager' in locals():
            budget_manager.close()

if __name__ == "__main__":
    main()


