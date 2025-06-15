from PySide6.QtWidgets import *
from PySide6.QtCore import *


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        self.collapsed_width = 50
        self.expanded_width = 200

        self.setFixedWidth(self.collapsed_width)
        self.setStyleSheet("background-color: #2c3e50;")
        self.setMouseTracking(True)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(QToolButton(self))

        layout.addWidget(QLabel("⚙️", self))
        layout.addWidget(QLabel("📊", self))

        for label in self.findChildren(QLabel):
            label.setStyleSheet("color: white; font-size: 18px; padding: 10px;")

    def enterEvent(self, event):
        self.animate_width(self.expanded_width)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animate_width(self.collapsed_width)
        super().leaveEvent(event)

    def animate_width(self, target_width):
        self.animation = QPropertyAnimation(self, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(self.width())
        self.animation.setEndValue(target_width)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.start()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hover Sidebar Example")
        self.resize(800, 500)

        self.sidebar = Sidebar()

        content = QLabel("Main Content Area")
        content.setStyleSheet("font-size: 20px; padding: 20px;")

        layout = QHBoxLayout(self)
        layout.addWidget(self.sidebar)
        layout.addWidget(content)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
