#!/usr/bin/env python3
"""
Debug script for BudgeIT application
This script helps debug executable build issues
"""

import sys
import os
import traceback


def debug_imports():
    """Test critical imports that might fail in executable"""
    imports_to_test = [
        "PySide6.QtWidgets",
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtSql",
        "sqlite3",
        "matplotlib.pyplot",
        "matplotlib.backends.backend_qt5agg",
    ]

    print("Testing critical imports...")
    for import_name in imports_to_test:
        try:
            __import__(import_name)
            print(f"✅ {import_name} - OK")
        except ImportError as e:
            print(f"❌ {import_name} - FAILED: {e}")
        except Exception as e:
            print(f"⚠️  {import_name} - ERROR: {e}")


def debug_resources():
    """Test resource loading"""
    print("\nTesting resource access...")

    # Test if we're in PyInstaller bundle
    if hasattr(sys, "_MEIPASS"):
        print(f"✅ Running in PyInstaller bundle: {sys._MEIPASS}")

        # Test critical paths
        test_paths = [
            "budgeit/assets/fonts/Roboto.ttf",
            "budgeit/assets/icons/favicon.ico",
            "budgeit/accounts.db",
        ]

        for path in test_paths:
            full_path = os.path.join(sys._MEIPASS, path)
            if os.path.exists(full_path):
                print(f"✅ Resource found: {path}")
            else:
                print(f"❌ Resource missing: {path}")
                print(f"   Full path: {full_path}")
    else:
        print("⚠️  Not running in PyInstaller bundle (development mode)")


def debug_database():
    """Test database functionality"""
    print("\nTesting database access...")
    try:
        from budgeit.utils.path_helper import get_database_path

        db_path = get_database_path()
        print(f"✅ Database path resolved: {db_path}")

        if os.path.exists(db_path):
            print("✅ Database file exists")
        else:
            print("❌ Database file missing")

        # Test SQLite connection
        import sqlite3

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"✅ Database tables: {[table[0] for table in tables]}")
        conn.close()

    except Exception as e:
        print(f"❌ Database test failed: {e}")
        traceback.print_exc()


def debug_application():
    """Test application startup"""
    print("\nTesting application startup...")
    try:
        from PySide6.QtWidgets import QApplication

        app = QApplication([])
        print("✅ QApplication created successfully")

        # Test resource imports
        try:
            from budgeit.assets.images import images_rc

            print("✅ Images resource loaded")
        except Exception as e:
            print(f"❌ Images resource failed: {e}")

        try:
            from budgeit.assets.icons import icons_rc

            print("✅ Icons resource loaded")
        except Exception as e:
            print(f"❌ Icons resource failed: {e}")

        app.quit()

    except Exception as e:
        print(f"❌ Application startup failed: {e}")
        traceback.print_exc()


def main():
    print("🔧 BudgeIT Executable Debug Tool")
    print("=" * 50)

    debug_imports()
    debug_resources()
    debug_database()
    debug_application()

    print("\n" + "=" * 50)
    print("🏁 Debug complete!")

    # Keep console open if running as executable
    if hasattr(sys, "_MEIPASS"):
        input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
