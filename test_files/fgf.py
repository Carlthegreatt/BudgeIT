from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtCore import QFile, QPropertyAnimation, QEasingCurve, QSize
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        ui_file = QFile("main.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.setCentralWidget(self.ui)

        # Widgets
        self.sidebar = self.ui.findChild(QWidget, "sidebar")
        self.toggle_button = self.ui.findChild(QWidget, "toggleButton")
        self.full_content = self.ui.findChild(QWidget, "fullSidebarContent")
        self.mini_content = self.ui.findChild(QWidget, "miniSidebarContent")

        # State
        self.sidebar_expanded = True
        self.expanded_width = 200
        self.collapsed_width = 50

        # Init view
        self.mini_content.setVisible(False)

        self.toggle_button.clicked.connect(self.toggle_sidebar)

    def toggle_sidebar(self):
        self.sidebar_expanded = not self.sidebar_expanded

        width = self.expanded_width if self.sidebar_expanded else self.collapsed_width

        # Animate width change
        animation = QPropertyAnimation(self.sidebar, b"maximumWidth")
        animation.setDuration(250)
        animation.setStartValue(self.sidebar.width())
        animation.setEndValue(width)
        animation.setEasingCurve(QEasingCurve.InOutCubic)
        animation.start()

        # Toggle contents
        self.full_content.setVisible(self.sidebar_expanded)
        self.mini_content.setVisible(not self.sidebar_expanded)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
