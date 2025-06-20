import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from .user_sign import SignEntry
from .features import Features_ui
from .about_us import Team_Dialog
from ..assets.images import images_rc
from .faq_window import Faq
import os
import ctypes


class LandingPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.about_us_dialog = None
        self.features_dialog = None
        self.faq_dialog = None
        self.setupUi()
        self.setup_animations()
        self.setWindowTitle(" ")

    def setupUi(self):

        title_icon = QIcon()
        title_icon.addFile(
            ":/budgeIT_logo.png",
            QSize(),
            QIcon.Mode.Active,
            QIcon.State.On,
        )
        self.setWindowIcon(title_icon)
        from ..utils.path_helper import get_asset_path

        font_path = get_asset_path("fonts", "Roboto.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            if font_families:
                app_font = QFont(font_families[0])
                QApplication.setFont(app_font)
            else:
                print("Font loaded, but no families found.")
        else:
            print("Failed to load font.")

        if not self.objectName():
            self.setObjectName("MainWindow")
        self.resize(1000, 640)
        self.setMinimumSize(QSize(1000, 640))
        self.setStyleSheet("background-color:rgb(234, 234, 234)")

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setMinimumSize(QSize(0, 60))
        self.widget_3.setMaximumSize(QSize(16777215, 60))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(40, 0, 40, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Logo
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.label_2.setMinimumSize(QSize(91, 35))
        self.label_2.setMaximumSize(QSize(91, 35))
        self.label_2.setPixmap(QPixmap(":/logomax.png"))
        self.label_2.setScaledContents(True)
        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_6 = QToolButton(self.widget_3)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_6.setMinimumSize(QSize(80, 30))
        self.toolButton_6.setMaximumSize(QSize(80, 30))
        self.toolButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toolButton_6.setStyleSheet(self.get_nav_button_style())
        self.toolButton_6.setText("About us")
        self.toolButton_6.clicked.connect(lambda: self.open_about_us())
        self.horizontalLayout.addWidget(self.toolButton_6)

        self.toolButton_9 = QToolButton(self.widget_3)
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_9.setMinimumSize(QSize(80, 30))
        self.toolButton_9.setMaximumSize(QSize(80, 30))
        self.toolButton_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toolButton_9.setStyleSheet(self.get_nav_button_style())
        self.toolButton_9.setText("Features")
        self.toolButton_9.clicked.connect(lambda: self.open_features())
        self.horizontalLayout.addWidget(self.toolButton_9)

        self.toolButton_7 = QToolButton(self.widget_3)
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_7.setMinimumSize(QSize(80, 30))
        self.toolButton_7.setMaximumSize(QSize(80, 30))
        self.toolButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toolButton_7.setStyleSheet(self.get_nav_button_style())
        self.toolButton_7.setText("FAQ")
        self.horizontalLayout.addWidget(self.toolButton_7)
        self.toolButton_7.clicked.connect(lambda: self.open_faq())

        self.toolButton_5 = QToolButton(self.widget_3)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_5.setMinimumSize(QSize(80, 30))
        self.toolButton_5.setMaximumSize(QSize(80, 30))
        self.toolButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toolButton_5.setStyleSheet(self.get_signup_button_style())
        self.toolButton_5.setText("Sign up")
        self.toolButton_5.clicked.connect(lambda: self.sign_entry())
        self.horizontalLayout.addWidget(self.toolButton_5)

        self.toolButton_8 = QToolButton(self.widget_3)
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_8.setMinimumSize(QSize(80, 30))
        self.toolButton_8.setMaximumSize(QSize(80, 30))
        self.toolButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toolButton_8.setStyleSheet(self.get_signin_button_style())
        self.toolButton_8.setText("Sign in")
        self.toolButton_8.clicked.connect(lambda: self.sign_entry(show_signin=True))
        self.horizontalLayout.addWidget(self.toolButton_8)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.verticalSpacer = QSpacerItem(
            20, 142, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )
        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 40)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.user = QLabel(self.widget_2)
        self.user.setObjectName("user")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies(["Roboto"])
        font.setBold(True)
        font.setItalic(False)
        self.user.setFont(font)
        self.user.setStyleSheet(
            'color: rgb(108, 68, 100);\nfont: 700 45px "Roboto";\nbackground-color: transparent'
        )
        self.user.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.user.setText("Smart finance tracking")
        self.verticalLayout_2.addWidget(self.user)

        self.user_6 = QLabel(self.widget_2)
        self.user_6.setObjectName("user_6")
        sizePolicy.setHeightForWidth(self.user_6.sizePolicy().hasHeightForWidth())
        self.user_6.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies(["Roboto"])
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        self.user_6.setFont(font1)
        self.user_6.setStyleSheet(
            'color: rgb(108, 68, 100);\nfont: 600 35px "Roboto";\nbackground-color: transparent'
        )
        self.user_6.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.user_6.setText("Starts with BudgeIT")
        self.verticalLayout_2.addWidget(self.user_6)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.user_2 = QLabel(self.widget_2)
        self.user_2.setObjectName("user_2")
        sizePolicy.setHeightForWidth(self.user_2.sizePolicy().hasHeightForWidth())
        self.user_2.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies(["Roboto"])
        font2.setBold(False)
        font2.setItalic(False)
        self.user_2.setFont(font2)
        self.user_2.setStyleSheet(
            'color: rgb(167, 83, 115);\nfont: 400 25px "Roboto";\nbackground-color: transparent'
        )
        self.user_2.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.user_2.setText("Your personal budget companion")
        self.verticalLayout_3.addWidget(self.user_2)

        self.toolButton_3 = QToolButton(self.widget_2)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(140, 40))
        self.toolButton_3.setMaximumSize(QSize(140, 40))
        self.toolButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toolButton_3.setStyleSheet(self.get_cta_button_style())
        self.toolButton_3.setText("Get Started")
        self.toolButton_3.clicked.connect(lambda: self.handle_get_started())
        self.verticalLayout_3.addWidget(self.toolButton_3)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(
            20, 141, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )
        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        self.widget.setMinimumSize(QSize(0, 60))
        self.widget.setStyleSheet(
            """
QWidget {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 #ff9a9e,
        stop: 0.5 #fad0c4,
        stop: 1 rgb(244, 212, 212)
    );
}
"""
        )

        self.verticalLayout_8.addWidget(self.widget)
        self.widget.raise_()
        self.verticalLayout.addWidget(self.widget_2)

        self.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(self)

    def get_nav_button_style(self):
        return """
        QToolButton {
            background-color: transparent;
            color: rgb(212, 106, 146);
            border: none;
            border-radius: 5px;
            font: 600 12px "Roboto";
        }
        QToolButton:hover {
            color: rgb(198, 99, 137);
        }
        QToolButton:pressed {
            color: rgb(144, 72, 101);
        }
        """

    def get_signup_button_style(self):
        return """
        QToolButton {
            background-color: transparent;
            color: rgb(212, 106, 146);
            border: 2px solid rgb(212, 106, 146);
            border-radius: 5px;
            font: 600 12px "Roboto";
        }
        QToolButton:hover {
            border-color: rgb(198, 99, 137);
            color: rgb(198, 99, 137);
        }
        QToolButton:pressed {
            border-color: rgb(144, 72, 101);
            color: rgb(144, 72, 101);
        }
        """

    def get_signin_button_style(self):
        return """
        QToolButton {
            background-color: rgb(212, 106, 146);
            color: white;
            border: none;
            border-radius: 5px;
            font: 600 12px "Roboto";
        }
        QToolButton:hover {
            background-color: rgb(179, 89, 124);
        }
        QToolButton:pressed {
            background-color: rgb(144, 72, 101);
        }
        """

    def get_cta_button_style(self):
        return """
        QToolButton {
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(254, 161, 163),
                stop: 1 rgb(246, 211, 206)
            );
            color: white;
            border: none;
            border-radius: 5px;
            font: 500 14px "Roboto";
        }
        QToolButton:hover {
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(230, 146, 149),
                stop: 1 rgb(220, 190, 185)
            );
        }
        QToolButton:pressed {
            background-color: rgb(144, 72, 101);
        }
        """

    def setup_animations(self):
        self.header_opacity = QGraphicsOpacityEffect()
        self.title_opacity = QGraphicsOpacityEffect()
        self.subtitle_opacity = QGraphicsOpacityEffect()
        self.description_opacity = QGraphicsOpacityEffect()
        self.cta_opacity = QGraphicsOpacityEffect()
        self.footer_opacity = QGraphicsOpacityEffect()

        self.widget_3.setGraphicsEffect(self.header_opacity)
        self.user.setGraphicsEffect(self.title_opacity)
        self.user_6.setGraphicsEffect(self.subtitle_opacity)
        self.user_2.setGraphicsEffect(self.description_opacity)
        self.toolButton_3.setGraphicsEffect(self.cta_opacity)
        self.widget.setGraphicsEffect(self.footer_opacity)

        self.header_opacity.setOpacity(0)
        self.title_opacity.setOpacity(0)
        self.subtitle_opacity.setOpacity(0)
        self.description_opacity.setOpacity(0)
        self.cta_opacity.setOpacity(0)
        self.footer_opacity.setOpacity(0)

        self.initial_user_pos = QPoint(-300, self.user.y())
        self.initial_user6_pos = QPoint(-250, self.user_6.y())
        self.initial_user2_pos = QPoint(-200, self.user_2.y())
        self.initial_cta_pos = QPoint(-150, self.toolButton_3.y())

        self.header_fade = QPropertyAnimation(self.header_opacity, b"opacity")
        self.header_fade.setDuration(800)
        self.header_fade.setStartValue(0)
        self.header_fade.setEndValue(1)
        self.header_fade.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.title_fade = QPropertyAnimation(self.title_opacity, b"opacity")
        self.title_fade.setDuration(1000)
        self.title_fade.setStartValue(0)
        self.title_fade.setEndValue(1)
        self.title_fade.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.subtitle_fade = QPropertyAnimation(self.subtitle_opacity, b"opacity")
        self.subtitle_fade.setDuration(1000)
        self.subtitle_fade.setStartValue(0)
        self.subtitle_fade.setEndValue(1)
        self.subtitle_fade.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.description_fade = QPropertyAnimation(self.description_opacity, b"opacity")
        self.description_fade.setDuration(1000)
        self.description_fade.setStartValue(0)
        self.description_fade.setEndValue(1)
        self.description_fade.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.cta_fade = QPropertyAnimation(self.cta_opacity, b"opacity")
        self.cta_fade.setDuration(1000)
        self.cta_fade.setStartValue(0)
        self.cta_fade.setEndValue(1)
        self.cta_fade.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.footer_fade = QPropertyAnimation(self.footer_opacity, b"opacity")
        self.footer_fade.setDuration(800)
        self.footer_fade.setStartValue(0)
        self.footer_fade.setEndValue(1)
        self.footer_fade.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.title_slide = QPropertyAnimation(self.user, b"pos")
        self.title_slide.setDuration(1200)
        self.title_slide.setEasingCurve(QEasingCurve.Type.OutQuart)

        self.subtitle_slide = QPropertyAnimation(self.user_6, b"pos")
        self.subtitle_slide.setDuration(1200)
        self.subtitle_slide.setEasingCurve(QEasingCurve.Type.OutQuart)

        self.description_slide = QPropertyAnimation(self.user_2, b"pos")
        self.description_slide.setDuration(1200)
        self.description_slide.setEasingCurve(QEasingCurve.Type.OutQuart)

        self.cta_slide = QPropertyAnimation(self.toolButton_3, b"pos")
        self.cta_slide.setDuration(1200)
        self.cta_slide.setEasingCurve(QEasingCurve.Type.OutQuart)

    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(100, self.start_animations)

    def start_animations(self):
        actual_user_pos = self.user.pos()
        actual_user6_pos = self.user_6.pos()
        actual_user2_pos = self.user_2.pos()
        actual_cta_pos = self.toolButton_3.pos()

        self.title_slide.setStartValue(QPoint(-300, actual_user_pos.y()))
        self.title_slide.setEndValue(actual_user_pos)

        self.subtitle_slide.setStartValue(QPoint(-250, actual_user6_pos.y()))
        self.subtitle_slide.setEndValue(actual_user6_pos)

        self.description_slide.setStartValue(QPoint(-200, actual_user2_pos.y()))
        self.description_slide.setEndValue(actual_user2_pos)

        self.cta_slide.setStartValue(QPoint(-150, actual_cta_pos.y()))
        self.cta_slide.setEndValue(actual_cta_pos)

        self.user.move(-300, actual_user_pos.y())
        self.user_6.move(-250, actual_user6_pos.y())
        self.user_2.move(-200, actual_user2_pos.y())
        self.toolButton_3.move(-150, actual_cta_pos.y())

        self.header_fade.start()

        QTimer.singleShot(
            200, lambda: (self.title_fade.start(), self.title_slide.start())
        )

        QTimer.singleShot(
            400, lambda: (self.subtitle_fade.start(), self.subtitle_slide.start())
        )

        QTimer.singleShot(
            600, lambda: (self.description_fade.start(), self.description_slide.start())
        )

        QTimer.singleShot(800, lambda: (self.cta_fade.start(), self.cta_slide.start()))

        QTimer.singleShot(1000, self.footer_fade.start)

    def handle_get_started(self):
        self.sign_entry()

    def sign_entry(self, show_signin=False):
        window = SignEntry(self)
        if show_signin:
            window.stackedWidget.setCurrentIndex(1)
        else:
            window.stackedWidget.setCurrentIndex(0)
        window.setWindowModality(Qt.ApplicationModal)
        window.show()

    def open_features(self):
        if self.features_dialog and self.features_dialog.isVisible():
            self.features_dialog.close()
            self.features_dialog = None
            return

        dialog = QDialog(self)

        ui = Features_ui()
        ui.setupUi(dialog)
        dialog.setWindowModality(Qt.ApplicationModal)
        self.features_dialog = dialog
        dialog.show()

    def open_about_us(self):
        if self.about_us_dialog and self.about_us_dialog.isVisible():
            self.about_us_dialog.close()
            self.about_us_dialog = None
            return

        self.about_us_dialog = Team_Dialog(self)
        self.about_us_dialog.setWindowModality(Qt.ApplicationModal)
        self.about_us_dialog.show()

    def open_faq(self):
        if self.faq_dialog and self.faq_dialog.isVisible():
            self.faq_dialog.close()
            self.faq_dialog = None
            return

        self.faq_dialog = Faq(self)
        self.faq_dialog.setWindowModality(Qt.ApplicationModal)
        self.faq_dialog.show()
