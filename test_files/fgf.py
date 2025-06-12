from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QGraphicsOpacityEffect,
)
from PySide6.QtCore import QPropertyAnimation, QTimer, Qt, QEasingCurve, QPoint


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fade-In Popup Text")
        self.setFixedSize(400, 300)

        # Main layout (for button)
        layout = QVBoxLayout(self)

        # Button
        self.button = QPushButton("Show Message")
        self.button.clicked.connect(self.show_popup)
        layout.addWidget(self.button)

        # Create the label for popup (not in layout, just floating on window)
        self.popup = QLabel("This is a popup!", self)
        self.popup.setStyleSheet(
            "color: black; font-size: 16px; background: transparent;"
        )
        self.popup.adjustSize()
        self.popup.setVisible(False)  # Start hidden

        # Set opacity effect
        self.opacity = QGraphicsOpacityEffect(self.popup)
        self.popup.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(0)

        # Fade in animation
        self.fade_in = QPropertyAnimation(self.opacity, b"opacity")
        self.fade_in.setDuration(500)
        self.fade_in.setStartValue(0)
        self.fade_in.setEndValue(1)
        self.fade_in.setEasingCurve(QEasingCurve.InOutQuad)

        # Fade out animation
        self.fade_out = QPropertyAnimation(self.opacity, b"opacity")
        self.fade_out.setDuration(500)
        self.fade_out.setStartValue(1)
        self.fade_out.setEndValue(0)
        self.fade_out.setEasingCurve(QEasingCurve.InOutQuad)

        # Move animation
        self.move_anim = QPropertyAnimation(self.popup, b"pos")
        self.move_anim.setDuration(500)
        self.move_anim.setEasingCurve(QEasingCurve.OutQuad)

    def show_popup(self):
        # Set initial position in the center
        x = (self.width() - self.popup.width()) // 2
        y = self.height() // 2
        self.popup.move(x, y)
        self.popup.setVisible(True)
        self.opacity.setOpacity(0)

        # Start fade-in
        self.fade_in.start()

        # After delay, start fade-out and move-up
        QTimer.singleShot(1500, self.fade_and_move)

    def fade_and_move(self):
        # Current and new position (move up by 30px)
        current_pos = self.popup.pos()
        end_pos = QPoint(current_pos.x(), current_pos.y() - 30)

        self.move_anim.setStartValue(current_pos)
        self.move_anim.setEndValue(end_pos)

        self.fade_out.start()
        self.move_anim.start()

        # Hide after animation finishes
        self.fade_out.finished.connect(lambda: self.popup.setVisible(False))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
