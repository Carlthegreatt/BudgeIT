from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QScrollArea,
    QLabel,
    QGraphicsOpacityEffect,
)
from PySide6.QtCore import (
    QPropertyAnimation,
    QPoint,
    QEasingCurve,
    QParallelAnimationGroup,
    Qt,
    QTimer,
)


class FadeSlideScrollArea(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scroll-triggered Fade + Slide In")
        self.resize(500, 500)

        layout = QVBoxLayout(self)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        layout.addWidget(self.scroll_area)

        # Container for scroll content
        self.container = QWidget()
        self.vbox = QVBoxLayout(self.container)

        self.labels = []

        for i in range(30):
            label = QLabel(f"Item {i + 1}")
            label.setStyleSheet(
                "font-size: 18px; padding: 12px; background: #eee; margin: 5px;"
            )
            self.vbox.addWidget(label)
            self.labels.append(label)

            # Store placeholder for animations
            label._animated = False
            label._opacity = QGraphicsOpacityEffect()
            label.setGraphicsEffect(label._opacity)
            label._opacity.setOpacity(0.0)

        self.scroll_area.setWidget(self.container)

        # Track which labels have animated
        self.animated = set()

        # Connect scroll
        self.scroll_area.verticalScrollBar().valueChanged.connect(self.check_visibility)

        # Delay initial visibility check to allow layout setup
        QTimer.singleShot(200, self.check_visibility)

    def check_visibility(self):
        viewport = self.scroll_area.viewport()
        scroll_pos = self.scroll_area.verticalScrollBar().value()
        viewport_bottom = scroll_pos + viewport.height()

        for i, widget in enumerate(self.labels):
            widget_top = widget.y()
            widget_bottom = widget.y() + widget.height()

            if widget_bottom >= scroll_pos and widget_top <= viewport_bottom:
                if not widget._animated:
                    self.animate_widget(widget)
                    widget._animated = True

    def animate_widget(self, widget):
        # Opacity animation
        fade_anim = QPropertyAnimation(widget.graphicsEffect(), b"opacity")
        fade_anim.setDuration(500)
        fade_anim.setStartValue(0.0)
        fade_anim.setEndValue(1.0)

        # Position animation
        original_pos = widget.pos()
        start_pos = original_pos - QPoint(30, 0)

        slide_anim = QPropertyAnimation(widget, b"pos")
        slide_anim.setDuration(500)
        slide_anim.setStartValue(start_pos)
        slide_anim.setEndValue(original_pos)
        slide_anim.setEasingCurve(QEasingCurve.OutCubic)

        # Run animations in parallel
        group = QParallelAnimationGroup()
        group.addAnimation(fade_anim)
        group.addAnimation(slide_anim)
        group.start()

        # Prevent GC
        widget._anim_group = group


if __name__ == "__main__":
    app = QApplication([])
    window = FadeSlideScrollArea()
    window.show()
    app.exec()
