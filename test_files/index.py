from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QProgressBar,
    QPushButton,
)
from PySide6.QtCore import QPropertyAnimation


class AnimatedProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar Smooth Animation")

        self.layout = QVBoxLayout()
        self.progress = QProgressBar()
        self.progress.setValue(0)
        self.layout.addWidget(self.progress)

        self.button = QPushButton("Animate")
        self.button.clicked.connect(self.animate_progress)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def animate_progress(self):
        self.animation = QPropertyAnimation(self.progress, b"value")
        self.animation.setDuration(2000)  # 2 seconds
        self.animation.setStartValue(0)
        self.animation.setEndValue(100)
        self.animation.start()


app = QApplication([])
window = AnimatedProgressBar()
window.show()
app.exec()
