import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumSize(400, 300)

        self.drag_pos = None  # For dragging the window

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Custom title bar
        title_bar = QWidget()
        title_bar.setFixedHeight(30)
        title_bar.setStyleSheet("background-color: #444; color: white;")

        title_layout = QHBoxLayout(title_bar)
        title_layout.setContentsMargins(8, 0, 8, 0)

        self.title_label = QLabel("My App")
        title_layout.addWidget(self.title_label)

        title_layout.addStretch()

        btn_minimize = QPushButton("-")
        btn_minimize.setFixedSize(20, 20)
        btn_minimize.setStyleSheet("background: none; color: white; border: none;")
        btn_minimize.clicked.connect(self.showMinimized)

        btn_close = QPushButton("x")
        btn_close.setFixedSize(20, 20)
        btn_close.setStyleSheet("background: none; color: white; border: none;")
        btn_close.clicked.connect(self.close)

        title_layout.addWidget(btn_minimize)
        title_layout.addWidget(btn_close)

        main_layout.addWidget(title_bar)

        # Your main content
        content = QLabel("Hello!")
        content.setAlignment(Qt.AlignCenter)
        content.setStyleSheet("font-size: 16px;")
        main_layout.addWidget(content)

        # Mouse events for dragging the window
        title_bar.mousePressEvent = self.mousePressEvent
        title_bar.mouseMoveEvent = self.mouseMoveEvent

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_pos:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
            self.drag_pos = event.globalPosition().toPoint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
