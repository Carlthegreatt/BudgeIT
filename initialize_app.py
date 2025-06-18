import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings
from core.user_sign import SignEntry
from core.main import BudgetApp
from core.landing_page import LandingPage


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
            except (ValueError, TypeError):

                self.settings.remove("remember_me")
                self.settings.remove("saved_user_id")
                window = LandingPage()
        else:
            window = LandingPage()

        window.show()
        sys.exit(self.app.exec())


def main():
    # Import resource files to ensure they're loaded
    import assets.images.images_rc

    app = Main()


if __name__ == "__main__":
    main()
