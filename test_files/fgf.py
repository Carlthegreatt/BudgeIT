import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGroupBox,
    QLabel,
    QPushButton,
    QGraphicsDropShadowEffect,
)
from PySide6.QtGui import QColor


def apply_shadow(widget, blur=20, x_offset=0, y_offset=5, color="#555"):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(blur)
    shadow.setXOffset(x_offset)
    shadow.setYOffset(y_offset)
    shadow.setColor(QColor(color))
    widget.setGraphicsEffect(shadow)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GroupBox with Layout and Shadow")
        self.setStyleSheet(
            "background-color: #f0f0f0;"
        )  # Lighter background for contrast

        main_layout = QVBoxLayout(self)

        group_box = QGroupBox("User Info")
        group_box.setStyleSheet(
            """
            QGroupBox {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 8px;
                margin-top: 20px;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 4px;
                background-color: transparent;
            }
        """
        )

        group_layout = QVBoxLayout(group_box)
        group_layout.addWidget(QLabel("Name: John Doe"))
        group_layout.addWidget(QLabel("Age: 30"))
        group_layout.addWidget(QPushButton("Submit"))

        apply_shadow(group_box)  # Apply the shadow

        main_layout.addWidget(group_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(350, 250)
    window.show()
    sys.exit(app.exec())
