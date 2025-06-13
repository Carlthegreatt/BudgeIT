from PySide6.QtCore import QPropertyAnimation


class ProgressBarAnimator:
    def __init__(self, progress_bar, duration=2000):
        """
        Initialize the ProgressBarAnimator.

        Args:
            progress_bar: The QProgressBar instance to animate
            duration: Animation duration in milliseconds (default: 2000ms)
        """
        self.progress_bar = progress_bar
        self.duration = duration
        self.animation = None

    def animate(self, start_value=0, end_value=100):
        """
        Animate the progress bar from start_value to end_value.

        Args:
            start_value: Starting value (default: 0)
            end_value: Ending value (default: 100)
        """
        self.animation = QPropertyAnimation(self.progress_bar, b"value")
        self.animation.setDuration(self.duration)
        self.animation.setStartValue(start_value)
        self.animation.setEndValue(end_value)
        self.animation.start()

    def stop(self):
        """Stop the current animation if it's running."""
        if self.animation and self.animation.state() == QPropertyAnimation.Running:
            self.animation.stop()
