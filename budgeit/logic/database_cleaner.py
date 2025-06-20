import sqlite3
from contextlib import contextmanager
from datetime import datetime
from .database_manager import get_database_path


class DatabaseCleaner:
    """Utility class for cleaning and resetting database data"""

    def __init__(self, db_path: str = None):
        self.__db_path = db_path if db_path else get_database_path()

    @contextmanager
    def __get_connection(self):
        """Get database connection context manager"""
        conn = sqlite3.connect(self.__db_path)
        try:
            yield conn
        finally:
            conn.close()

    def reset_all_data(self) -> bool:
        """
        NUCLEAR OPTION: Completely clears ALL data from ALL tables.
        This will remove all users, transactions, budgets, and user data.
        USE WITH EXTREME CAUTION!
        """
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()

                # Delete all data from all tables (order matters due to foreign keys)
                cursor.execute("DELETE FROM transactions")
                cursor.execute("DELETE FROM remaining_budgets")
                cursor.execute("DELETE FROM user_data")
                cursor.execute("DELETE FROM users")
                cursor.execute("DELETE FROM meta")

                # Reset auto-increment sequences
                cursor.execute("DELETE FROM sqlite_sequence")

                conn.commit()
                print("✅ All database data has been reset successfully!")
                return True
        except Exception as e:
            print(f"❌ Error resetting all data: {e}")
            return False

    def clean_user_data(self, user_id: int) -> bool:
        """
        Remove all data for a specific user including:
        - User account
        - All transactions
        - All budget data
        - All user data records
        """
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()

                # Delete all user-related data (order matters due to foreign keys)
                cursor.execute("DELETE FROM transactions WHERE user_id = ?", (user_id,))
                cursor.execute(
                    "DELETE FROM remaining_budgets WHERE user_id = ?", (user_id,)
                )
                cursor.execute("DELETE FROM user_data WHERE user_id = ?", (user_id,))
                cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))

                conn.commit()
                print(
                    f"✅ All data for user_id {user_id} has been removed successfully!"
                )
                return True
        except Exception as e:
            print(f"❌ Error cleaning user data: {e}")
            return False

    def clean_transactions_only(self, user_id: int = None) -> bool:
        """
        Remove transaction data only (keeps users and budget settings)
        If user_id is provided, only cleans transactions for that user
        """
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()

                if user_id:
                    cursor.execute(
                        "DELETE FROM transactions WHERE user_id = ?", (user_id,)
                    )
                    print(f"✅ Transactions for user_id {user_id} have been cleaned!")
                else:
                    cursor.execute("DELETE FROM transactions")
                    print("✅ All transactions have been cleaned!")

                conn.commit()
                return True
        except Exception as e:
            print(f"❌ Error cleaning transactions: {e}")
            return False

    def reset_monthly_budgets(self, user_id: int, report_date: str = None) -> bool:
        """
        Reset remaining budgets to zero for a specific user and month
        If report_date is not provided, uses current month
        """
        if not report_date:
            report_date = datetime.today().strftime("%Y-%m")

        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()

                cursor.execute(
                    """UPDATE remaining_budgets SET 
                       remaining_monthly_budget = 0, 
                       remaining_food_budget = 0, 
                       remaining_utilities_budget = 0, 
                       remaining_health_wellness_budget = 0, 
                       remaining_personal_lifestyle_budget = 0, 
                       remaining_education_budget = 0, 
                       remaining_transportation_budget = 0, 
                       remaining_miscellaneous_budget = 0 
                       WHERE user_id = ? AND report_date = ?""",
                    (user_id, report_date),
                )

                conn.commit()
                print(
                    f"✅ Monthly budgets reset for user_id {user_id} for {report_date}!"
                )
                return True
        except Exception as e:
            print(f"❌ Error resetting monthly budgets: {e}")
            return False

    def clean_old_data(self, months_to_keep: int = 12) -> bool:
        """
        Remove data older than specified months
        Keeps recent data based on months_to_keep parameter
        """
        try:
            from dateutil.relativedelta import relativedelta

            cutoff_date = datetime.today() - relativedelta(months=months_to_keep)
            cutoff_str = cutoff_date.strftime("%Y-%m")

            with self.__get_connection() as conn:
                cursor = conn.cursor()

                # Delete old transactions
                cursor.execute(
                    "DELETE FROM transactions WHERE transaction_date < ?",
                    (cutoff_str + "-01",),
                )

                # Delete old budget data
                cursor.execute(
                    "DELETE FROM remaining_budgets WHERE report_date < ?", (cutoff_str,)
                )

                # Delete old user data
                cursor.execute(
                    "DELETE FROM user_data WHERE report_date < ?", (cutoff_str,)
                )

                conn.commit()
                print(f"✅ Data older than {months_to_keep} months has been cleaned!")
                return True
        except Exception as e:
            print(f"❌ Error cleaning old data: {e}")
            return False

    def vacuum_database(self) -> bool:
        """
        Optimize database by reclaiming space and defragmenting
        Should be run after cleaning operations
        """
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("VACUUM")
                print("✅ Database has been optimized!")
                return True
        except Exception as e:
            print(f"❌ Error vacuuming database: {e}")
            return False

    def get_database_stats(self) -> dict:
        """Get statistics about the current database state"""
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()

                stats = {}

                # Count users
                cursor.execute("SELECT COUNT(*) FROM users")
                stats["users"] = cursor.fetchone()[0]

                # Count transactions
                cursor.execute("SELECT COUNT(*) FROM transactions")
                stats["transactions"] = cursor.fetchone()[0]

                # Count user_data records
                cursor.execute("SELECT COUNT(*) FROM user_data")
                stats["user_data_records"] = cursor.fetchone()[0]

                # Count remaining_budgets records
                cursor.execute("SELECT COUNT(*) FROM remaining_budgets")
                stats["remaining_budget_records"] = cursor.fetchone()[0]

                # Get database file size
                cursor.execute("PRAGMA page_count")
                page_count = cursor.fetchone()[0]
                cursor.execute("PRAGMA page_size")
                page_size = cursor.fetchone()[0]
                stats["database_size_bytes"] = page_count * page_size

                return stats
        except Exception as e:
            print(f"❌ Error getting database stats: {e}")
            return {}

    def backup_database(self, backup_path: str) -> bool:
        """Create a backup of the current database"""
        try:
            import shutil

            shutil.copy2(self.__db_path, backup_path)
            print(f"✅ Database backed up to: {backup_path}")
            return True
        except Exception as e:
            print(f"❌ Error creating backup: {e}")
            return False


def main():
    """Example usage of the DatabaseCleaner"""
    cleaner = DatabaseCleaner()

    print("=== Database Statistics ===")
    stats = cleaner.get_database_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\n=== Available Cleaning Options ===")
    print("1. Reset ALL data (DANGER!)")
    print("2. Clean specific user data")
    print("3. Clean all transactions only")
    print("4. Reset monthly budgets")
    print("5. Clean old data (older than X months)")
    print("6. Vacuum/optimize database")
    print("7. Create database backup")

    choice = input("\nEnter your choice (1-7): ").strip()

    if choice == "1":
        confirm = input("⚠️  This will DELETE ALL DATA! Type 'YES' to confirm: ")
        if confirm == "YES":
            cleaner.reset_all_data()
        else:
            print("Operation cancelled.")

    elif choice == "2":
        user_id = int(input("Enter user_id to clean: "))
        cleaner.clean_user_data(user_id)

    elif choice == "3":
        cleaner.clean_transactions_only()

    elif choice == "4":
        user_id = int(input("Enter user_id: "))
        cleaner.reset_monthly_budgets(user_id)

    elif choice == "5":
        months = int(input("Keep data for how many months? "))
        cleaner.clean_old_data(months)

    elif choice == "6":
        cleaner.vacuum_database()

    elif choice == "7":
        backup_path = input("Enter backup file path: ")
        cleaner.backup_database(backup_path)

    print("\n=== Updated Database Statistics ===")
    stats = cleaner.get_database_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
