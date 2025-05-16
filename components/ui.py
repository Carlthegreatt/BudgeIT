from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor


class ShadowEffect:
    def __init__(
        self, blur_radius=20, x_offset=40, y_offset=20, color=QColor(0, 0, 0, 160)
    ):
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setBlurRadius(blur_radius)
        self.effect.setOffset(x_offset, y_offset)
        self.effect.setColor(color)

    def apply_to(self, widget):
        widget.setGraphicsEffect(self.effect)
