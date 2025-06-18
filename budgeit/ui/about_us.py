from PySide6.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPixmap, QColor, QPainter, QBrush, QCursor
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QGraphicsDropShadowEffect)
from PySide6.QtWidgets import QGraphicsOpacityEffect
from PySide6.QtCore import QTimer
import sys

class HoverableImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._original_geometry = None

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor("#982761"))
        self.shadow.setOffset(0, 0)
        self.setGraphicsEffect(self.shadow)

        self._animation = QPropertyAnimation(self, b"geometry")
        self._animation.setDuration(200)
        self._animation.setEasingCurve(QEasingCurve.OutQuad)

    def enterEvent(self, event):
        if not self._original_geometry:
            self._original_geometry = self.geometry()

        enlarged = self._original_geometry.adjusted(-5, -5, 5, 5)
        self._animation.stop()
        self._animation.setStartValue(self.geometry())
        self._animation.setEndValue(enlarged)
        self._animation.start()

        self.shadow.setBlurRadius(30)
        self.shadow.setColor(QColor("#c8195b"))

        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.stop()
        self._animation.setStartValue(self.geometry())
        self._animation.setEndValue(self._original_geometry)
        self._animation.start()

        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor("#982761"))

        super().leaveEvent(event)

class Team_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 680)
        Dialog.setStyleSheet("""
            QLabel {
                font-family: 'Segoe UI';
            }
            QLabel[name] {
                font: 700 12pt 'Segoe UI';
                color: #000000;
            }
            QLabel[role] {
                font: 700 9pt 'Segoe UI';
                color: #982761;
            }
        """)

        self.logo_label = QLabel(Dialog)
        self.logo_label.setGeometry(QRect(20, 10, 60, 50)) 
        self.logo_label.setPixmap(QPixmap("logo.png").scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo_label.setScaledContents(True)

        self.label_meet = QLabel(Dialog)
        self.label_meet.setGeometry(QRect(260, 20, 150, 35))
        self.label_meet.setStyleSheet("font: 700 18pt 'Inter'; color: #000000;")
        self.label_meet.setAlignment(Qt.AlignRight)
        self.label_meet.setText("MEET THE")

        self.label_team = QLabel(Dialog)
        self.label_team.setGeometry(QRect(415, 20, 200, 35))
        self.label_team.setStyleSheet("font: 700 18pt 'Inter'; color: #BF5473;")
        self.label_team.setAlignment(Qt.AlignLeft)
        self.label_team.setText("TEAM")

        members = [
            (20, 70, "Ayesha Zhyrile Infante", "Project Manager", "Ayesha.jpg", "ayeshainfante@gmail.com", "https://www.facebook.com/ayeshazhyrile.infante.7/"),
            (440, 70, "Carl Blancaflor", "Lead Engineer", "Carl.jpg", "blancaflorcarlferros@gmail.com", "https://www.facebook.com/BlancaflorCarl"),
            (20, 270, "Janreb Payton", "Senior Developer", "Payton.jpg", "janrebcornelpayton@gmail.com", "https://www.facebook.com/janrebcornel.payton"),
            (440, 270, "Risha Villones", "Quality & Test Engineer", "Risha.jpg", "Vrishamay@gmail.com", "https://www.facebook.com/risha.villones.2024"),
            (20, 480, "Erika Asio", "Junior Developer", "Erika.jpg", "asioerika12@gmail.com", "https://www.facebook.com/ErikaAsio036"),
            (439, 480, "Jan Randolph Santos", "Junior Developer", "Randolph.jpg", "santoschinkit@gmail.com", "https://www.facebook.com/SantosRaandoolph")
        ]

        for x, y, name, role, image_path, email, fb_link in members:
            image_label = HoverableImageLabel(Dialog)
            image_label.setGeometry(QRect(x, y, 121, 121))
            image_label.setPixmap(self.getRoundedImage(image_path, 121))
            image_label.setScaledContents(True)

            name_label = QLabel(Dialog)
            name_label.setGeometry(QRect(x + 140, y + 20, 200, 20))
            name_label.setObjectName("name")
            name_label.setProperty("name", True)
            name_label.setText(name)

            role_label = QLabel(Dialog)
            role_label.setGeometry(QRect(x + 140, y + 45, 200, 16))
            role_label.setObjectName("role")
            role_label.setProperty("role", True)
            role_label.setText(role)

            email_label = QLabel(Dialog)
            email_label.setGeometry(QRect(x + 140, y + 65, 300, 20))
            email_label.setOpenExternalLinks(True)
            email_label.setStyleSheet("font: 9pt 'Segoe UI'; color: #5555ff;")
            email_label.setText(f"<a href='mailto:{email}'>{email}</a>")

            fb_icon = QLabel(Dialog)
            fb_icon.setGeometry(QRect(x + 140, y + 90, 20, 20))
            fb_icon.setPixmap(QPixmap("fb icon.png").scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            fb_icon.setCursor(QCursor(Qt.PointingHandCursor))
            fb_icon.setToolTip("View Facebook Profile")
            fb_icon.link = fb_link
            fb_icon.mousePressEvent = lambda event, url=fb_link: self.openFbLink(url)
            

    def openFbLink(self, url):
        import webbrowser
        webbrowser.open(url)

    def getRoundedImage(self, path, size):
        original = QPixmap(path).scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        rounded = QPixmap(size, size)
        rounded.fill(Qt.transparent)

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(original))
        painter.setPen(QColor("#982761"))
        painter.drawEllipse(0, 0, size - 1, size - 1)
        painter.end()

        return rounded

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
