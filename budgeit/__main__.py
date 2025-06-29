import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings
from .ui.user_sign import SignEntry
from .ui.main_window import BudgetApp
from .ui.landing_page import LandingPage
import sqlite3


class Main:
    def __init__(self, user_id=None):
        self.app = QApplication(sys.argv)
        self.settings = QSettings("MyCompany", "MyApp")
        self.user_id = user_id

        remember_me = self.settings.value("remember_me", False, type=bool)
        saved_user_id = self.settings.value("saved_user_id", "", type=str)

        if remember_me and saved_user_id:
            try:
                window = BudgetApp(int(saved_user_id))
            except (ValueError, TypeError, sqlite3.OperationalError) as e:
                print(e)
                self.settings.clear()
                self.settings.remove("remember_me")
                self.settings.remove("saved_user_id")
                window = LandingPage()
        else:
            window = LandingPage()

        window.show()
        sys.exit(self.app.exec())


def main():
    try:
        # Import resource files
        from .assets.images import images_rc
        from .assets.icons import icons_rc

        print("Resources loaded successfully")

        app = Main()
    except Exception as e:
        print(f"Application failed to start: {e}")
        import traceback

        traceback.print_exc()

        # Keep console open for debugging if in executable
        import sys

        if hasattr(sys, "_MEIPASS"):
            input("\nPress Enter to exit...")
        sys.exit(1)


if __name__ == "__main__":
    main()
