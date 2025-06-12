from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QGraphicsOpacityEffect,
)
from PySide6.QtCore import QPropertyAnimation, QTimer, Qt, QEasingCurve, QPoint


class FadePopup(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            "color: black; font: 500 14px 'Inter'; background: transparent;"
        )
        self.adjustSize()
        self.setVisible(False)

        # Set opacity effect
        self.opacity = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity)
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
        self.move_anim = QPropertyAnimation(self, b"pos")
        self.move_anim.setDuration(500)
        self.move_anim.setEasingCurve(QEasingCurve.OutQuad)

    def show_popup(self, text, x, y):
        self.setText(text)
        self.adjustSize()
        self.move(x, y)
        self.setVisible(True)
        self.opacity.setOpacity(0)

        # Set up move animation
        current_pos = self.pos()
        end_pos = QPoint(current_pos.x(), current_pos.y() - 30)
        self.move_anim.setStartValue(current_pos)
        self.move_anim.setEndValue(end_pos)

        # Start both animations
        self.fade_in.start()
        self.move_anim.start()

        # After animations finish, start fade out
        self.fade_in.finished.connect(self.start_fade_out)

    def start_fade_out(self):
        self.fade_out.start()
        self.fade_out.finished.connect(lambda: self.setVisible(False))


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Popup Demo")
#         self.setFixedSize(400, 300)

#         # Main layout
#         layout = QVBoxLayout(self)

#         # Create popup
#         self.popup = FadePopup(self)

#         # Buttons
#         self.button1 = QPushButton("Add Transaction")
#         self.button1.clicked.connect(lambda: self.show_popup("Transaction added!"))
#         layout.addWidget(self.button1)

#         self.button2 = QPushButton("Save Changes")
#         self.button2.clicked.connect(lambda: self.show_popup("Changes saved!"))
#         layout.addWidget(self.button2)

#     def show_popup(self, text):
#         # Calculate center position
#         x = (self.width() - self.popup.width()) // 2
#         y = self.height() // 2
#         self.popup.show_popup(text, x, y)
