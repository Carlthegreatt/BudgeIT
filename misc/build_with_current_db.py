#!/usr/bin/env python3
"""
Enhanced Build Script for BudgeIT

This script ensures that the current database state is preserved when building
the executable, so your latest data is included in the built application.

Usage:
    python build_with_current_db.py
"""

import os
import sys
import shutil
import subprocess
from datetime import datetime


def backup_current_database():
    """Create a backup of the current database state"""
    current_db = os.path.join("budgeit", "accounts.db")
    if os.path.exists(current_db):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"accounts_backup_before_build_{timestamp}.db"
        shutil.copy2(current_db, backup_path)
        print(f"✅ Current database backed up to: {backup_path}")
        return backup_path
    else:
        print("❌ No current database found to backup")
        return None


def clean_build_directory():
    """Clean previous build artifacts"""
    dirs_to_clean = ["build", "dist"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"🧹 Cleaning {dir_name} directory...")
            try:
                shutil.rmtree(dir_name)
                print(f"✅ {dir_name} directory cleaned")
            except Exception as e:
                print(f"❌ Failed to clean {dir_name}: {e}")


def update_user_database_before_build():
    """Update the user's database location with current state before building"""
    # This ensures the executable will use the most current database
    current_db = os.path.join("budgeit", "accounts.db")
    if not os.path.exists(current_db):
        print("❌ No current database found!")
        return False

    # Get user data directory
    if os.name == "nt":  # Windows
        user_data_dir = os.path.join(
            os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "BudgeIT"
        )
    else:  # Linux/Mac
        user_data_dir = os.path.join(os.path.expanduser("~"), ".budgeit")

    os.makedirs(user_data_dir, exist_ok=True)
    user_db_path = os.path.join(user_data_dir, "accounts.db")

    # Copy current database to user location
    try:
        shutil.copy2(current_db, user_db_path)
        print(f"✅ Updated user database: {user_db_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to update user database: {e}")
        return False


def build_executable():
    """Build the executable using PyInstaller"""
    print("🔨 Building executable with PyInstaller...")

    try:
        # Run PyInstaller with the spec file
        result = subprocess.run(
            [sys.executable, "-m", "PyInstaller", "--clean", "BudgeIT.spec"],
            check=True,
            capture_output=True,
            text=True,
        )

        print("✅ Executable built successfully!")
        print(f"📁 Output directory: {os.path.abspath('dist')}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        print(f"Error output: {e.stderr}")
        return False


def create_installer():
    """Create an installer if the executable was built successfully"""
    exe_path = os.path.join("dist", "BudgeIT.exe")
    if os.path.exists(exe_path):
        print("🎁 Creating installer...")

        # Create installer directory
        installer_dir = os.path.join("dist", "installer")
        os.makedirs(installer_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        installer_name = f"BudgeIT_v1.1_{timestamp}.exe"
        installer_path = os.path.join(installer_dir, installer_name)

        # For now, just copy the exe (you can enhance this with a proper installer later)
        try:
            shutil.copy2(exe_path, installer_path)
            print(f"✅ Installer created: {installer_path}")
            return installer_path
        except Exception as e:
            print(f"❌ Failed to create installer: {e}")
            return None
    else:
        print("❌ Executable not found, skipping installer creation")
        return None


def validate_build():
    """Validate that the build was successful"""
    exe_path = os.path.join("dist", "BudgeIT.exe")
    if os.path.exists(exe_path):
        size_mb = os.path.getsize(exe_path) / (1024 * 1024)
        print(f"✅ Build validation passed!")
        print(f"📁 Executable: {exe_path}")
        print(f"📏 Size: {size_mb:.1f} MB")
        return True
    else:
        print("❌ Build validation failed - executable not found!")
        return False


def main():
    print("🚀 BudgeIT Build Script with Current Database")
    print("=" * 50)

    # Step 1: Backup current database
    print("\n1️⃣ Backing up current database...")
    backup_path = backup_current_database()

    # Step 2: Clean build directory
    print("\n2️⃣ Cleaning build directories...")
    clean_build_directory()

    # Step 3: Update user database location
    print("\n3️⃣ Updating user database with current state...")
    if not update_user_database_before_build():
        print("❌ Failed to update user database, continuing anyway...")

    # Step 4: Build executable
    print("\n4️⃣ Building executable...")
    if not build_executable():
        print("❌ Build failed! Exiting.")
        return 1

    # Step 5: Validate build
    print("\n5️⃣ Validating build...")
    if not validate_build():
        print("❌ Build validation failed!")
        return 1

    # Step 6: Create installer
    print("\n6️⃣ Creating installer...")
    installer_path = create_installer()

    # Summary
    print("\n" + "=" * 50)
    print("🎉 BUILD COMPLETE!")
    print("=" * 50)
    print(f"✅ Executable: dist/BudgeIT.exe")
    if installer_path:
        print(f"✅ Installer: {installer_path}")
    if backup_path:
        print(f"💾 Database backup: {backup_path}")

    print("\n📝 IMPORTANT NOTES:")
    print("• The executable now uses your current database state")
    print("• Database will be stored in user's AppData/Local/BudgeIT/")
    print("• Future updates will preserve existing user data")
    print("• Always test the executable before distributing")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n👋 Build cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
