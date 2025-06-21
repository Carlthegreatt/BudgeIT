import os
import sys


def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_database_path():
    """Get the correct database path for both dev and exe environments"""
    import shutil

    try:
        # In exe environment (PyInstaller bundle)
        base_path = sys._MEIPASS

        # Get user's AppData/Local directory
        if os.name == "nt":  # Windows
            user_data_dir = os.path.join(
                os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "BudgeIT"
            )
        else:  # Linux/Mac
            user_data_dir = os.path.join(os.path.expanduser("~"), ".budgeit")

        os.makedirs(user_data_dir, exist_ok=True)
        db_path = os.path.join(user_data_dir, "accounts.db")

        # Always use the current development database for the most up-to-date state
        # Find the development database
        dev_db_candidates = [
            # Try relative to the current working directory
            os.path.join(os.getcwd(), "budgeit", "accounts.db"),
            # Try relative to script location
            os.path.join(
                os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                "budgeit",
                "accounts.db",
            ),
        ]

        dev_db_path = None
        for candidate in dev_db_candidates:
            if os.path.exists(candidate):
                dev_db_path = candidate
                break

        # Copy the latest development database if it exists and is newer
        if dev_db_path and os.path.exists(dev_db_path):
            if not os.path.exists(db_path) or os.path.getmtime(
                dev_db_path
            ) > os.path.getmtime(db_path):
                shutil.copy2(dev_db_path, db_path)
                print(f"Database updated from development: {dev_db_path} -> {db_path}")
        elif not os.path.exists(db_path):
            # Create a new database if none exists
            _create_fresh_database(db_path)
            print(f"Created fresh database: {db_path}")

    except Exception as e:
        # In development environment
        current_dir = os.path.dirname(os.path.abspath(__file__))
        budgeit_dir = os.path.dirname(current_dir)
        db_path = os.path.join(budgeit_dir, "accounts.db")
        print(f"Using development database: {db_path}")

    return db_path


def _create_fresh_database(db_path):
    """Create a fresh database with proper schema"""
    import sqlite3

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create users table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT,
            date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    # Create other necessary tables
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            amount REAL,
            transaction_date DATE,
            description TEXT,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user_data (
            data_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            report_date TEXT,
            category TEXT,
            budget_amount REAL,
            spent_amount REAL DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS remaining_budgets (
            budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            report_date TEXT,
            category TEXT,
            remaining_budget REAL,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS meta (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """
    )

    conn.commit()
    conn.close()


def get_asset_path(asset_type, filename):
    """Get path to assets (fonts, images, icons)"""
    return get_resource_path(os.path.join("budgeit", "assets", asset_type, filename))
