from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import Qt
import sys


class RoundedDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Remove title bar and window frame
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)

        # Enable translucent background
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set fixed size (for demonstration)
        self.setFixedSize(400, 300)

        # Apply stylesheet with border-radius
        self.setStyleSheet(
            """
            QDialog {
                background-color: white;
                border-radius: 20px;
            }
        """
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = RoundedDialog()
    dialog.show()
    sys.exit(app.exec())
