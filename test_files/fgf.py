from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QLabel,
)
from PySide6.QtCore import QSettings


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login with Remember Me")

        # UI
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.remember_checkbox = QCheckBox("Remember Me")

        self.login_button = QPushButton("Login")
        self.status_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.remember_checkbox)
        layout.addWidget(self.login_button)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

        # Load saved settings
        self.settings = QSettings("YourCompany", "YourApp")
        self.load_credentials()

        # Connect signals
        self.login_button.clicked.connect(self.login)

    def load_credentials(self):
        if self.settings.value("remember", False, type=bool):
            self.username_input.setText(self.settings.value("username", ""))
            self.password_input.setText(self.settings.value("password", ""))
            self.remember_checkbox.setChecked(True)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        remember = self.remember_checkbox.isChecked()

        # Do your actual login check here (e.g., DB check)
        if username == "admin" and password == "1234":
            self.status_label.setText("Login successful!")

            if remember:
                self.settings.setValue("username", username)
                self.settings.setValue("password", password)
                self.settings.setValue("remember", True)
            else:
                self.settings.setValue("username", "")
                self.settings.setValue("password", "")
                self.settings.setValue("remember", False)
        else:
            self.status_label.setText("Login failed!")


if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec()
