import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings
from user_sign import SignEntry
from main_window import BudgetApp
from landing_page import LandingPage


class Main:
    def __init__(self, user_id=None):
        self.app = QApplication(sys.argv)
        self.settings = QSettings("MyCompany", "MyApp")  # Unique identifiers
        self.user_id = user_id

        # No need to track landing page session since it's always shown first

        # Check if user should be automatically logged in
        remember_me = self.settings.value("remember_me", False, type=bool)
        saved_user_id = self.settings.value("saved_user_id", "", type=str)

        if remember_me and saved_user_id:
            # User is already logged in, go directly to main app
            try:
                window = BudgetApp(int(saved_user_id))
            except (ValueError, TypeError):
                # Invalid user_id, clear settings and show landing page
                self.settings.remove("remember_me")
                self.settings.remove("saved_user_id")
                window = LandingPage()
        else:
            # Show landing page first for new users
            window = LandingPage()

        window.show()
        sys.exit(self.app.exec())


def main():
    """Entry point for the application"""
    app = Main()


if __name__ == "__main__":
    main()
