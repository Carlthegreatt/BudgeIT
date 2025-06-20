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

        # If database doesn't exist in user directory, copy it from bundle
        if not os.path.exists(db_path):
            template_db = os.path.join(base_path, "budgeit", "accounts.db")
            if os.path.exists(template_db):
                shutil.copy2(template_db, db_path)
                print(f"Database copied to: {db_path}")
            else:
                print(f"Template database not found at: {template_db}")

    except Exception as e:
        # In development environment
        current_dir = os.path.dirname(os.path.abspath(__file__))
        budgeit_dir = os.path.dirname(current_dir)
        db_path = os.path.join(budgeit_dir, "accounts.db")
        print(f"Using development database: {db_path}")

    return db_path


def get_asset_path(asset_type, filename):
    """Get path to assets (fonts, images, icons)"""
    return get_resource_path(os.path.join("budgeit", "assets", asset_type, filename))
