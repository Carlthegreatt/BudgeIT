#!/usr/bin/env python3
"""
BudgeIT Database Unlock Utility

This script helps resolve database lock issues by:
1. Checking for running processes that might have the database locked
2. Safely closing any open connections
3. Backing up the database
4. Optimizing the database to prevent corruption

Usage:
    python unlock_database.py
"""

import sys
import os
import sqlite3
import shutil
import time
from datetime import datetime

# Add the budgeit package to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def get_database_path():
    """Get the database path"""
    try:
        from budgeit.utils.path_helper import get_database_path as _get_db_path

        return _get_db_path()
    except ImportError:
        # Fallback to default path
        return os.path.join(os.path.dirname(__file__), "budgeit", "accounts.db")


def check_database_lock(db_path):
    """Check if database is locked"""
    try:
        conn = sqlite3.connect(db_path, timeout=1.0)
        conn.execute("BEGIN IMMEDIATE;")
        conn.rollback()
        conn.close()
        return False  # Not locked
    except sqlite3.OperationalError as e:
        if "database is locked" in str(e).lower():
            return True  # Locked
        else:
            print(f"Database error: {e}")
            return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def backup_database(db_path):
    """Create a backup of the database"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{db_path}.backup_{timestamp}"
        shutil.copy2(db_path, backup_path)
        print(f"✅ Backup created: {backup_path}")
        return backup_path
    except Exception as e:
        print(f"❌ Failed to create backup: {e}")
        return None


def force_unlock_database(db_path):
    """Force unlock the database by various methods"""
    print("🔓 Attempting to unlock database...")

    methods_tried = []

    # Method 1: Try connecting with different timeouts
    try:
        for timeout in [1, 5, 10, 30]:
            conn = sqlite3.connect(db_path, timeout=timeout)
            conn.execute("BEGIN IMMEDIATE;")
            conn.rollback()
            conn.close()
            methods_tried.append(f"Timeout {timeout}s - SUCCESS")
            print(f"✅ Database unlocked using timeout method ({timeout}s)")
            return True
    except Exception as e:
        methods_tried.append(f"Timeout method - FAILED: {e}")

    # Method 2: Try WAL mode reset
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA journal_mode=DELETE;")
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.close()
        methods_tried.append("WAL reset - SUCCESS")
        print("✅ Database unlocked using WAL reset")
        return True
    except Exception as e:
        methods_tried.append(f"WAL reset - FAILED: {e}")

    # Method 3: Vacuum
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("VACUUM;")
        conn.close()
        methods_tried.append("VACUUM - SUCCESS")
        print("✅ Database unlocked using VACUUM")
        return True
    except Exception as e:
        methods_tried.append(f"VACUUM - FAILED: {e}")

    print("❌ Failed to unlock database. Methods tried:")
    for method in methods_tried:
        print(f"   - {method}")

    return False


def optimize_database(db_path):
    """Optimize database to prevent future locks"""
    try:
        print("🔧 Optimizing database...")
        conn = sqlite3.connect(db_path)

        # Set optimized pragmas
        conn.execute("PRAGMA synchronous=NORMAL;")
        conn.execute("PRAGMA cache_size=10000;")
        conn.execute("PRAGMA temp_store=MEMORY;")
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA wal_autocheckpoint=1000;")

        # Analyze tables for better query performance
        conn.execute("ANALYZE;")

        conn.close()
        print("✅ Database optimized")
        return True
    except Exception as e:
        print(f"❌ Failed to optimize database: {e}")
        return False


def kill_python_processes():
    """Kill other Python processes that might be using the database"""
    import subprocess

    try:
        if os.name == "nt":  # Windows
            # Get current process ID
            current_pid = os.getpid()

            # Find all python processes
            result = subprocess.run(
                ["tasklist", "/FI", "IMAGENAME eq python.exe", "/FO", "CSV"],
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:
                lines = result.stdout.strip().split("\n")[1:]  # Skip header
                for line in lines:
                    if line:
                        parts = line.strip('"').split('","')
                        if len(parts) >= 2:
                            pid = int(parts[1])
                            if pid != current_pid:
                                try:
                                    subprocess.run(
                                        ["taskkill", "/PID", str(pid), "/F"],
                                        capture_output=True,
                                    )
                                    print(f"✅ Killed Python process PID: {pid}")
                                except:
                                    pass
        else:  # Unix-like
            subprocess.run(["pkill", "-f", "python.*budgeit"], capture_output=True)

        return True
    except Exception as e:
        print(f"❌ Failed to kill processes: {e}")
        return False


def main():
    print("🔓 BudgeIT Database Unlock Utility")
    print("=" * 40)

    db_path = get_database_path()
    print(f"📁 Database path: {db_path}")

    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return

        # Check if database is locked
    is_locked = check_database_lock(db_path)
    if not is_locked:
        print("✅ Database is not locked!")

        # Still optimize it
        optimize_database(db_path)
        return

    print("🔒 Database is locked!")

    # Create backup first
    backup_path = backup_database(db_path)
    if not backup_path:
        print("❌ Cannot proceed without backup!")
        return

    # Try to unlock
    print("\n🔄 Attempting to unlock database...")

    # Option 1: Kill other Python processes
    print("\n1️⃣ Killing other Python processes...")
    kill_python_processes()
    time.sleep(2)

    if not check_database_lock(db_path):
        print("✅ Database unlocked after killing processes!")
        optimize_database(db_path)
        return

    # Option 2: Force unlock
    print("\n2️⃣ Force unlocking database...")
    if force_unlock_database(db_path):
        optimize_database(db_path)
        return

    # If all fails, suggest manual intervention
    print("\n❌ Could not unlock database automatically.")
    print("\n🛠️  Manual steps to try:")
    print("1. Close all BudgeIT application windows")
    print("2. Restart your computer")
    print("3. Delete any .db-wal or .db-shm files in the budgeit folder")
    print("4. If desperate, restore from backup:")
    print(f'   copy "{backup_path}" "{db_path}"')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Operation cancelled by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback

        traceback.print_exc()
