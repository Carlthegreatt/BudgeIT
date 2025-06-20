#!/usr/bin/env python3
"""
Build script for BudgeIT application
This script ensures all necessary files are included in the exe build
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def clean_build():
    """Clean previous build artifacts"""
    dirs_to_clean = ["build", "dist", "__pycache__"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Cleaned {dir_name}")


def check_requirements():
    """Check if all required packages are installed"""
    required_packages = ["PySide6", "pyinstaller"]
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package.lower().replace("-", "_"))
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print(f"Missing required packages: {', '.join(missing_packages)}")
        print("Please install them using: pip install " + " ".join(missing_packages))
        return False
    return True


def build_exe():
    """Build the executable using PyInstaller"""
    if not check_requirements():
        return False

    print("Starting build process...")

    # Clean previous builds
    clean_build()

    # Run PyInstaller
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--clean",
        "--noconfirm",
        "BudgeIT.spec",
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Build completed successfully!")
        print(f"Executable created at: {os.path.abspath('dist/BudgeIT.exe')}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error: {e}")
        print(f"Error output: {e.stderr}")
        return False


def verify_build():
    """Verify that the build was successful"""
    exe_path = Path("dist/BudgeIT.exe")
    if exe_path.exists():
        print(f"✅ Executable found: {exe_path.absolute()}")
        print(f"📁 File size: {exe_path.stat().st_size / 1024 / 1024:.1f} MB")
        return True
    else:
        print("❌ Executable not found!")
        return False


if __name__ == "__main__":
    print("🔧 BudgeIT Build Script")
    print("=" * 30)

    if build_exe():
        if verify_build():
            print("🎉 Build process completed successfully!")
            print("\n📝 Notes:")
            print("- Test the executable thoroughly before distribution")
            print("- The first run might be slower due to unpacking")
            print("- Database will be created in user's temp directory")
        else:
            print("⚠️  Build completed but executable verification failed")
    else:
        print("💥 Build process failed")
        sys.exit(1)
