import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QScrollArea,
    QVBoxLayout, QGroupBox, QLabel, QMainWindow
)


class ScrollableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrollable GroupBoxes")
        self.resize(400, 300)

        # Main widget for the window
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # Create the scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Widget that will contain the scrollable content
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # Add multiple group boxes to the scroll layout
        for i in range(10):
            group_box = QGroupBox(f"Group {i + 1}")
            group_layout = QVBoxLayout()
            group_layout.addWidget(QLabel(f"This is content for group {i + 1}."))
            group_box.setLayout(group_layout)
            group_box.setMinimumHeight(80)  # Prevent shrinking too much
            scroll_layout.addWidget(group_box)

        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)

        # Add scroll area to main layout
        main_layout.addWidget(scroll_area)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrollableWindow()
    window.show()
    sys.exit(app.exec())
