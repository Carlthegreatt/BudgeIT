from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QSize
from PySide6.QtWidgets import QGraphicsOpacityEffect


class SidebarAnimation:
    def __init__(self, sidebar, duration=300):
        self.sidebar = sidebar
        self.duration = duration
        self.width_animation = QPropertyAnimation(sidebar, b"minimumWidth")
        self.width_animation.setDuration(duration)
        self.width_animation.setEasingCurve(QEasingCurve.OutCubic)

        self.opacity_effect = QGraphicsOpacityEffect(sidebar)
        self.sidebar.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation.setDuration(duration)
        self.opacity_animation.setEasingCurve(QEasingCurve.OutCubic)

    def expand(self, target_width):
        self.width_animation.setStartValue(self.sidebar.width())
        self.width_animation.setEndValue(target_width)
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(1.0)
        self.width_animation.start()
        self.opacity_animation.start()

    def collapse(self, target_width):
        self.width_animation.setStartValue(self.sidebar.width())
        self.width_animation.setEndValue(target_width)
        self.opacity_animation.setStartValue(1.0)
        self.opacity_animation.setEndValue(0.0)
        self.width_animation.start()
        self.opacity_animation.start()


class MenuTransitionAnimation:
    def __init__(self, widget, duration=300):
        self.widget = widget
        self.duration = duration
        self.opacity_effect = QGraphicsOpacityEffect(widget)
        self.widget.setGraphicsEffect(self.opacity_effect)

        self.fade_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_animation.setDuration(duration)
        self.fade_animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.slide_animation = QPropertyAnimation(widget, b"pos")
        self.slide_animation.setDuration(duration)
        self.slide_animation.setEasingCurve(QEasingCurve.OutQuad)

    def transition_in(self, start_pos, end_pos):
        self.widget.move(start_pos)
        self.slide_animation.setStartValue(start_pos)
        self.slide_animation.setEndValue(end_pos)

        self.fade_animation.setStartValue(0.0)
        self.fade_animation.setEndValue(1.0)

        self.slide_animation.start()
        self.fade_animation.start()

    def transition_out(self, start_pos, end_pos):
        self.slide_animation.setStartValue(start_pos)
        self.slide_animation.setEndValue(end_pos)

        self.fade_animation.setStartValue(1.0)
        self.fade_animation.setEndValue(0.0)

        self.slide_animation.start()
        self.fade_animation.start()


class DataRefreshAnimation:
    def __init__(self, widget, duration=500):
        self.widget = widget
        self.duration = duration
        self.opacity_effect = QGraphicsOpacityEffect(widget)
        self.widget.setGraphicsEffect(self.opacity_effect)

        self.fade_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_animation.setDuration(duration)
        self.fade_animation.setEasingCurve(QEasingCurve.InOutQuad)

    def refresh(self):
        self.fade_animation.setStartValue(1.0)
        self.fade_animation.setEndValue(0.3)
        self.fade_animation.start()

        # After fade out, fade back in
        self.fade_animation.finished.connect(self._fade_in)

    def _fade_in(self):
        self.fade_animation.setStartValue(0.3)
        self.fade_animation.setEndValue(1.0)
        self.fade_animation.start()
        self.fade_animation.finished.disconnect(self._fade_in)


class ButtonHoverAnimation:
    def __init__(self, button, duration=200):
        self.button = button
        self.duration = duration
        self.scale_animation = QPropertyAnimation(button, b"geometry")
        self.scale_animation.setDuration(duration)
        self.scale_animation.setEasingCurve(QEasingCurve.OutQuad)

        self.original_geometry = button.geometry()

    def enter_event(self):
        enlarged = self.original_geometry.adjusted(-2, -2, 2, 2)
        self.scale_animation.setStartValue(self.original_geometry)
        self.scale_animation.setEndValue(enlarged)
        self.scale_animation.start()

    def leave_event(self):
        self.scale_animation.setStartValue(self.button.geometry())
        self.scale_animation.setEndValue(self.original_geometry)
        self.scale_animation.start()
