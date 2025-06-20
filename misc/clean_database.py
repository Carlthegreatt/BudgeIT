#!/usr/bin/env python3
"""
BudgeIT Database Cleaning Script

This script provides various options to clean and maintain the BudgeIT database.
Run this script from the project root directory.

Usage:
    python clean_database.py

IMPORTANT: Always backup your database before running any cleaning operations!
"""

import sys
import os

# Add the budgeit package to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "budgeit"))

from budgeit.logic.database_cleaner import DatabaseCleaner


def show_current_database_info():
    """Display current database statistics"""
    cleaner = DatabaseCleaner()
    stats = cleaner.get_database_stats()

    print("\n" + "=" * 50)
    print("📊 CURRENT DATABASE STATISTICS")
    print("=" * 50)
    print(f"👥 Users: {stats.get('users', 0)}")
    print(f"💰 Transactions: {stats.get('transactions', 0)}")
    print(f"📈 User Data Records: {stats.get('user_data_records', 0)}")
    print(f"📊 Budget Records: {stats.get('remaining_budget_records', 0)}")

    size_bytes = stats.get("database_size_bytes", 0)
    size_mb = size_bytes / (1024 * 1024)
    print(f"💾 Database Size: {size_mb:.2f} MB ({size_bytes:,} bytes)")
    print("=" * 50)


def create_backup():
    """Create a backup of the current database"""
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"accounts_backup_{timestamp}.db"
    backup_path = os.path.join(".", backup_filename)

    cleaner = DatabaseCleaner()
    if cleaner.backup_database(backup_path):
        print(f"✅ Backup created: {backup_filename}")
        return backup_path
    else:
        print("❌ Failed to create backup!")
        return None


def main():
    print("🧹 BudgeIT Database Cleaner")
    print("=" * 40)

    # Show current database stats
    show_current_database_info()

    print("\n🛠️  CLEANING OPTIONS:")
    print("1. 🔄  Create database backup")
    print("2. 🧹  Clean all transactions (keep users & settings)")
    print("3. 👤  Remove specific user data")
    print("4. 📅  Reset monthly budgets for user")
    print("5. 🗓️   Clean old data (keep recent months)")
    print("6. 🗑️   RESET ALL DATA (DANGER!)")
    print("7. ⚡  Optimize database (VACUUM)")
    print("8. 📊  Show database statistics only")
    print("0. ❌  Exit")

    while True:
        try:
            choice = input("\n🔢 Enter your choice (0-8): ").strip()

            if choice == "0":
                print("👋 Goodbye!")
                break

            elif choice == "1":
                # Create backup
                backup_path = create_backup()

            elif choice == "2":
                # Clean all transactions
                confirm = input(
                    "⚠️  This will delete ALL transactions. Continue? (y/N): "
                )
                if confirm.lower() == "y":
                    cleaner = DatabaseCleaner()
                    cleaner.clean_transactions_only()
                    show_current_database_info()
                else:
                    print("Operation cancelled.")

            elif choice == "3":
                # Remove specific user
                try:
                    user_id = int(input("Enter user_id to remove: "))
                    confirm = input(
                        f"⚠️  This will delete ALL data for user_id {user_id}. Continue? (y/N): "
                    )
                    if confirm.lower() == "y":
                        cleaner = DatabaseCleaner()
                        cleaner.clean_user_data(user_id)
                        show_current_database_info()
                    else:
                        print("Operation cancelled.")
                except ValueError:
                    print("❌ Please enter a valid user_id number.")

            elif choice == "4":
                # Reset monthly budgets
                try:
                    user_id = int(input("Enter user_id: "))
                    report_date = input(
                        "Enter report date (YYYY-MM) or press Enter for current month: "
                    ).strip()
                    if not report_date:
                        report_date = None

                    cleaner = DatabaseCleaner()
                    cleaner.reset_monthly_budgets(user_id, report_date)
                    show_current_database_info()
                except ValueError:
                    print("❌ Please enter a valid user_id number.")

            elif choice == "5":
                # Clean old data
                try:
                    months = int(
                        input("How many recent months to keep? (default: 12): ") or "12"
                    )
                    confirm = input(
                        f"⚠️  This will delete data older than {months} months. Continue? (y/N): "
                    )
                    if confirm.lower() == "y":
                        cleaner = DatabaseCleaner()
                        cleaner.clean_old_data(months)
                        show_current_database_info()
                    else:
                        print("Operation cancelled.")
                except ValueError:
                    print("❌ Please enter a valid number of months.")

            elif choice == "6":
                # Nuclear option - reset all data
                print("🚨 DANGER ZONE 🚨")
                print("This will completely wipe ALL data from the database!")
                print("- All users will be deleted")
                print("- All transactions will be deleted")
                print("- All budgets and settings will be deleted")
                print("- This action CANNOT be undone!")

                confirm1 = input(
                    "\nDo you understand the consequences? (type 'I UNDERSTAND'): "
                )
                if confirm1 == "I UNDERSTAND":
                    confirm2 = input("Type 'DELETE EVERYTHING' to proceed: ")
                    if confirm2 == "DELETE EVERYTHING":
                        # Create automatic backup before nuclear option
                        print("Creating automatic backup before deletion...")
                        backup_path = create_backup()
                        if backup_path:
                            cleaner = DatabaseCleaner()
                            cleaner.reset_all_data()
                            show_current_database_info()
                        else:
                            print("❌ Cannot proceed without backup!")
                    else:
                        print("Operation cancelled.")
                else:
                    print("Operation cancelled.")

            elif choice == "7":
                # Vacuum database
                print("🔧 Optimizing database...")
                cleaner = DatabaseCleaner()
                cleaner.vacuum_database()
                show_current_database_info()

            elif choice == "8":
                # Show stats only
                show_current_database_info()

            else:
                print("❌ Invalid choice. Please select 0-8.")

        except KeyboardInterrupt:
            print("\n\n👋 Operation cancelled by user. Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
