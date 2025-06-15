#!/usr/bin/env python3
"""
Test script to demonstrate the new modern animations in BudgeIT
"""

import sys
from PySide6.QtWidgets import QApplication
from main import BudgetApp


def test_animations():
    """Test the animation features"""
    app = QApplication(sys.argv)

    # Mock user ID for testing (replace with actual user authentication)
    test_user_id = 1

    # Create the main application window
    window = BudgetApp(test_user_id)
    window.show()

    return app.exec()


if __name__ == "__main__":
    test_animations()
