from PySide6.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPixmap, QColor, QPainter, QCursor, QPainterPath, QRegion
from PySide6.QtWidgets import (QDialog, QLabel, QGraphicsDropShadowEffect)
import os
import webbrowser

class HoverableImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._original_geometry = None
        self.setMask(QRegion(0, 0, 121, 121, QRegion.Ellipse))

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
        enlarged = self._original_geometry.adjusted(-3, -3, 3, 3)

        self._animation.stop()
        self._animation.setStartValue(self.geometry())
        self._animation.setEndValue(enlarged)
        self._animation.start()

        self.setMask(QRegion(0, 0, enlarged.width(), enlarged.height(), QRegion.Ellipse))
        
        self.shadow.setBlurRadius(30)
        self.shadow.setColor(QColor("#c8195b"))
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.stop()
        self._animation.setStartValue(self.geometry())
        self._animation.setEndValue(self._original_geometry)
        self._animation.start()

        self.setMask(QRegion(0, 0, self._original_geometry.width(), self._original_geometry.height(), QRegion.Ellipse))
       
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor("#982761"))
        super().leaveEvent(event)

class Team_Dialog(QDialog):
    def __init__(self, parent=None):  
        super().__init__(parent)       
        self.setWindowTitle("Meet the Team")
        self.resize(750, 680)
        self.setStyleSheet("""
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
        self.setupUi()

    def setupUi(self):
        self.logo_label = QLabel(self)
        self.logo_label.setGeometry(QRect(20, 10, 60, 50))
        self.logo_label.setPixmap(QPixmap("assets/images/logomin.png").scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo_label.setScaledContents(True)

        label_meet = QLabel("MEET THE", self)
        label_meet.setGeometry(QRect(260, 20, 150, 35))
        label_meet.setStyleSheet("font: 700 18pt 'Inter'; color: #000000;")
        label_meet.setAlignment(Qt.AlignRight)

        label_team = QLabel("TEAM", self)
        label_team.setGeometry(QRect(415, 20, 200, 35))
        label_team.setStyleSheet("font: 700 18pt 'Inter'; color: #BF5473;")
        label_team.setAlignment(Qt.AlignLeft)

        print("[DEBUG] __file__ path:", __file__)

        image_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "images"))


        print("[DEBUG] image_dir:", image_dir)

        test_path = os.path.join(image_dir, "Ayesha.jpg")
        print("[DEBUG] Test image path:", test_path)
        print("[DEBUG] Test image exists:", os.path.exists(test_path))
  
        members = [
            (20, 70, "Ayesha Zhyrile Infante", "Project Manager", "Ayesha.jpg", "ayeshainfante@gmail.com", "https://www.facebook.com/ayeshazhyrile.infante.7/"),
            (440, 70, "Carl Blancaflor", "Lead Engineer", "Carl.jpg", "blancaflorcarlferros@gmail.com", "https://www.facebook.com/BlancaflorCarl"),
            (20, 270, "Janreb Payton", "Senior Developer", "Payton.jpg", "janrebcornelpayton@gmail.com", "https://www.facebook.com/janrebcornel.payton"),
            (440, 270, "Risha Villones", "Quality & Test Engineer", "Risha.jpg", "Vrishamay@gmail.com", "https://www.facebook.com/risha.villones.2024"),
            (20, 480, "Erika Asio", "Junior Developer", "Erika.jpg", "asioerika12@gmail.com", "https://www.facebook.com/ErikaAsio036"),
            (439, 480, "Jan Randolph Santos", "Junior Developer", "Randolph.jpg", "santoschinkit@gmail.com", "https://www.facebook.com/SantosRaandoolph")
        ]

        for x, y, name, role, image_file, email, fb_link in members:
            image_label = HoverableImageLabel(self)
            image_label.setGeometry(QRect(x, y, 121, 121))

            full_image_path = os.path.join(image_dir, image_file)
            print("[DEBUG] Expected image path:", full_image_path)
            image_label.setPixmap(self.getRoundedImage(full_image_path, 121))
            image_label.setScaledContents(True)
            image_label.setStyleSheet("border: none; background: transparent;")
            image_label.setPixmap(QPixmap(full_image_path).scaled(121, 121, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            image_label.setMask(QRegion(0, 0, 121, 121, QRegion.Ellipse))


            name_label = QLabel(name, self)
            name_label.setGeometry(QRect(x + 140, y + 20, 200, 20))
            name_label.setObjectName("name")
            name_label.setProperty("name", True)

            role_label = QLabel(role, self)
            role_label.setGeometry(QRect(x + 140, y + 45, 200, 16))
            role_label.setObjectName("role")
            role_label.setProperty("role", True)

            email_label = QLabel(self)
            email_label.setGeometry(QRect(x + 140, y + 65, 300, 20))
            email_label.setOpenExternalLinks(True)
            email_label.setStyleSheet("font: 9pt 'Segoe UI'; color: #5555ff;")
            email_label.setText(f"<a href='mailto:{email}'>{email}</a>")

            fb_icon = QLabel(self)
            fb_icon.setGeometry(QRect(x + 140, y + 90, 20, 20))
            fb_icon.setPixmap(QPixmap("assets/images/fb icon.png").scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            fb_icon.setCursor(QCursor(Qt.PointingHandCursor))
            fb_icon.setToolTip("View Facebook Profile")
            fb_icon.mousePressEvent = lambda event, url=fb_link: self.openFbLink(url)

    def openFbLink(self, url):
        webbrowser.open(url)

    def getPlaceholderPixmap(self, size):
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.lightGray)
        painter = QPainter(pixmap)
        painter.setPen(Qt.black)
        painter.drawText(pixmap.rect(), Qt.AlignCenter, "No Image")
        painter.end()
        return pixmap

    def getRoundedImage(self, full_image_path, size):
        original = QPixmap(full_image_path)
        if original.isNull():
            return self.getPlaceholderPixmap(size)

        high_res_size = size * 3  
        original = original.scaled(high_res_size, high_res_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        rounded = QPixmap(high_res_size, high_res_size)
        rounded.fill(Qt.transparent)  

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        path = QPainterPath()
        path.addEllipse(0, 0, size, size)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, original)
        painter.end()

        region = QRegion(0, 0, size, size, QRegion.Ellipse)
        label = QLabel()  # Assuming this is the QLabel you're using for images
        label.setPixmap(rounded)
        label.setMask(region)

        return rounded.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)


        


