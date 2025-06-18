from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..logic.auth_manager import AuthManager
from .main_window import BudgetApp
from ..logic.account_setup import AccountSetup
import sys
from ..utils.emailautomation import EmailSender
import os


class SignEntry(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(" ")
        self.setWindowTitle(" ")
        self.load_saved_credentials()

    def setupUi(self, MainWindow):

        title_icon = QIcon()
        title_icon.addFile(
            ":/budgeIT_logo.png",
            QSize(),
            QIcon.Mode.Active,
            QIcon.State.On,
        )
        self.setWindowIcon(title_icon)
        font_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "assets", "fonts", "Roboto.ttf"
        )
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

        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(900, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_3 = QHBoxLayout(self.page)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.page)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet(
            "QWidget {\n"
            "    background: qlineargradient(\n"
            "        x1: 1, y1: 1, x2:1, y2: 0,\n"
            "        stop: 0 rgb(255, 129, 135),\n"
            "        stop: 0.5 rgb(250, 192, 181),\n"
            "        stop: 1 rgb(244, 212, 212)\n"
            "    );\n"
            "}\n"
            ""
        )
        self.verticalLayout_22 = QVBoxLayout(self.widget)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.logomin_1 = QLabel(self.widget)
        self.logomin_1.setObjectName("logomin_1")
        self.logomin_1.setMinimumSize(QSize(40, 30))
        self.logomin_1.setMaximumSize(QSize(40, 30))
        self.logomin_1.setStyleSheet("background-color: transparent")
        self.logomin_1.setPixmap(QPixmap(":/logomin.png"))
        self.logomin_1.setScaledContents(True)

        self.verticalLayout_22.addWidget(self.logomin_1)

        self.verticalSpacer_9 = QSpacerItem(
            20, 222, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_22.addItem(self.verticalSpacer_9)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 70)
        self.horizontalSpacer_13 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.label_17.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            'font: 600 30px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_20.addWidget(self.label_17)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.label_18.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            'font: 500 20px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_20.addWidget(self.label_18)

        self.horizontalLayout_16.addLayout(self.verticalLayout_20)

        self.horizontalSpacer_14 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_16.addItem(self.horizontalSpacer_14)

        self.verticalLayout_22.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_8 = QSpacerItem(
            20, 222, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_22.addItem(self.verticalSpacer_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")

        self.verticalLayout_22.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setMinimumSize(QSize(500, 0))
        self.widget_2.setMaximumSize(QSize(500, 16777215))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_17 = QVBoxLayout(self.widget_2)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalSpacer_3 = QSpacerItem(
            20, 93, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_17.addItem(self.verticalSpacer_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, -1, 10)
        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 40px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_13.addWidget(self.label_12)

        self.verticalLayout_6.addLayout(self.verticalLayout_13)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.username_label = QLabel(self.widget_2)
        self.username_label.setObjectName("username_label")
        self.username_label.setStyleSheet(
            "color: rgb(166, 166, 166);\n"
            'font:500 12px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout.addWidget(self.username_label)

        self.username_line = QLineEdit(self.widget_2)
        self.username_line.setObjectName("username_line")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.username_line.sizePolicy().hasHeightForWidth()
        )
        self.username_line.setSizePolicy(sizePolicy1)
        self.username_line.setMinimumSize(QSize(250, 35))
        self.username_line.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: transparent;\n"
            "    border: 1px solid #dcdcdc;\n"
            "    border-radius: 10px;\n"
            "    padding-left: 14px;\n"
            '    font: 500 12px "Roboto";\n'
            "    color: rgb(108, 68, 103)\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border: 1px solid rgb(255, 157, 160); /* Blue border on focus */\n"
            "    background-color: #ffffff;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            'QLineEdit[echoMode="1"] { /* For password fields */\n'
            "    letter-spacing: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::placeholder {\n"
            '	font: 500 15px "Roboto";\n'
            "    color: #999999;\n"
            "}\n"
            ""
        )
        self.username_line.setEchoMode(QLineEdit.EchoMode.Normal)
        self.username_line.setDragEnabled(True)
        self.username_line.setReadOnly(False)
        self.username_line.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.username_line)

        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.email_label = QLabel(self.widget_2)
        self.email_label.setObjectName("email_label")
        self.email_label.setStyleSheet(
            "color: rgb(166, 166, 166);\n"
            'font:500 12px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_2.addWidget(self.email_label)

        self.email_line = QLineEdit(self.widget_2)
        self.email_line.setObjectName("email_line")
        sizePolicy1.setHeightForWidth(self.email_line.sizePolicy().hasHeightForWidth())
        self.email_line.setSizePolicy(sizePolicy1)
        self.email_line.setMinimumSize(QSize(250, 35))
        self.email_line.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: transparent;\n"
            "    border: 1px solid #dcdcdc;\n"
            "    border-radius: 10px;\n"
            "    padding-left: 14px;\n"
            '    font: 500 12px "Roboto";\n'
            "    color: rgb(108, 68, 103)\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border: 1px solid rgb(255, 157, 160); /* Blue border on focus */\n"
            "    background-color: #ffffff;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            'QLineEdit[echoMode="1"] { /* For password fields */\n'
            "    letter-spacing: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::placeholder {\n"
            "    color: #999999;\n"
            "}\n"
            ""
        )
        self.email_line.setEchoMode(QLineEdit.EchoMode.Normal)
        self.email_line.setDragEnabled(True)
        self.email_line.setReadOnly(False)
        self.email_line.setClearButtonEnabled(False)

        self.verticalLayout_2.addWidget(self.email_line)

        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.password_label = QLabel(self.widget_2)
        self.password_label.setObjectName("password_label")
        self.password_label.setStyleSheet(
            "color: rgb(166, 166, 166);\n"
            'font:500 12px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_3.addWidget(self.password_label)

        self.password_line = QLineEdit(self.widget_2)
        self.password_line.setObjectName("password_line")
        self.password_line.setMinimumSize(QSize(250, 35))
        self.password_line.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: transparent;\n"
            "    border: 1px solid #dcdcdc;\n"
            "    border-radius: 10px;\n"
            "    padding-left: 14px;\n"
            '    font: 400 7px "Roboto";\n'
            "    color:rgb(108, 68, 103)\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border: 1px solid rgb(255, 157, 160); /* Blue border on focus */\n"
            "    background-color: #ffffff;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            'QLineEdit[echoMode="1"] { /* For password fields */\n'
            "    letter-spacing: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::placeholder {\n"
            "    color: #999999;\n"
            "}\n"
            ""
        )
        self.password_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_line.setClearButtonEnabled(False)

        self.verticalLayout_3.addWidget(self.password_line)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.confirm_label = QLabel(self.widget_2)
        self.confirm_label.setObjectName("confirm_label")
        self.confirm_label.setStyleSheet(
            "color: rgb(166, 166, 166);\n"
            'font:500 12px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_4.addWidget(self.confirm_label)

        self.confirm_line = QLineEdit(self.widget_2)
        self.confirm_line.setObjectName("confirm_line")
        self.confirm_line.setMinimumSize(QSize(250, 35))
        self.confirm_line.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: transparent;\n"
            "    border: 1px solid #dcdcdc;\n"
            "    border-radius: 10px;\n"
            "    padding-left: 14px;\n"
            '    font: 400 7px "Roboto";\n'
            "    color: rgb(108, 68, 103)\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border: 1px solid rgb(255, 157, 160); /* Blue border on focus */\n"
            "    background-color: #ffffff;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            'QLineEdit[echoMode="1"] { /* For password fields */\n'
            "    letter-spacing: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::placeholder {\n"
            "    color: #999999;\n"
            "}\n"
            ""
        )
        self.confirm_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_line.setClearButtonEnabled(False)

        self.verticalLayout_4.addWidget(self.confirm_line)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 3, -1, -1)
        self.terms_checkbox = QCheckBox(self.widget_2)
        self.terms_checkbox.setObjectName("terms_checkbox")
        self.terms_checkbox.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.terms_checkbox.setStyleSheet(
            "\n"
            "QCheckBox{\n"
            "color: rgb(166, 166, 166);\n"
            'font:500 10px "Roboto";\n'
            "background-color: transparent;\n"
            "}\n"
            "\n"
            "QCheckBox::indicator {\n"
            "    \n"
            "	rgb(212, 212, 212)\n"
            "}\n"
            "\n"
            ""
        )
        self.terms_checkbox.setTristate(False)

        self.horizontalLayout_2.addWidget(self.terms_checkbox)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.signup_btn = QToolButton(self.widget_2)
        self.signup_btn.setObjectName("signup_btn")
        sizePolicy1.setHeightForWidth(self.signup_btn.sizePolicy().hasHeightForWidth())
        self.signup_btn.setSizePolicy(sizePolicy1)
        self.signup_btn.setMinimumSize(QSize(0, 35))
        self.signup_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signup_btn.setStyleSheet(
            "/* Base style for QToolButton */\n"
            "QToolButton {\n"
            "\n"
            "    \n"
            "    background: qlineargradient(\n"
            "        x1: 0, y1: 0, x2: 1, y2: 1,\n"
            "        stop: 0 rgb(253, 129, 130),\n"
            "        stop: 1 rgb(246, 211, 206)\n"
            "    );\n"
            "\n"
            "\n"
            "    color: white;               /* White text */\n"
            "    border: none;\n"
            "    border-radius: 10px;\n"
            "   \n"
            '    font: 500 12px "Roboto";\n'
            "   \n"
            "\n"
            "}\n"
            "\n"
            "/* Hover state */\n"
            "QToolButton:hover {\n"
            "    background-color: rgb(230, 146, 149)\n"
            "}\n"
            "\n"
            "/* Pressed state */\n"
            "QToolButton:pressed {\n"
            "    background-color: rgb(144, 72, 101)\n"
            "}\n"
            "\n"
            "/* Disabled state */\n"
            "QToolButton:disabled {\n"
            "    background-color: #A6A6A6;  /* Gray background when disabled */\n"
            "    color: #666666;\n"
            "}\n"
            "\n"
            "/* Optional: Different style for Sign Up button */\n"
            "QToolButton#signUpButton {\n"
            "    background-color: #28A745;  /* Green */\n"
            "}\n"
            "\n"
            "QToolButton#signUpButton:hover {\n"
            "    background-color: #1E7E34;\n"
            "}\n"
            "\n"
            "QToolButton#signUpButton:pressed {\n"
            "    background-color: #155D27;\n"
            "}\n"
            ""
        )
        self.signup_btn.clicked.connect(lambda: signup_success())
        self.verticalLayout_6.addWidget(self.signup_btn)

        self.verticalLayout_14.addLayout(self.verticalLayout_6)

        self.horizontalLayout_8.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.verticalLayout_17.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, -1, 5)
        self.label_19 = QLabel(self.widget_2)
        self.label_19.setObjectName("label_19")
        self.label_19.setMaximumSize(QSize(133, 16777215))
        self.label_19.setStyleSheet(
            "color: rgb(159, 159, 159);\n"
            'font: 400 11px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.horizontalLayout_12.addWidget(self.label_19)

        self.signin_btn_existing = QToolButton(self.widget_2)
        self.signin_btn_existing.setObjectName("signin_btn_existing")
        self.signin_btn_existing.setMinimumSize(QSize(20, 0))
        self.signin_btn_existing.setMaximumSize(QSize(50, 16777215))
        self.signin_btn_existing.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signin_btn_existing.setStyleSheet(
            "/* Default style */\n"
            "QToolButton {\n"
            "    background-color: transparent;\n"
            "    color: rgb(153, 97, 146);\n"
            '    font: 500 11px "Roboto";\n'
            "}\n"
            "\n"
            "/* Hover effect: darker border */\n"
            "QToolButton:hover {\n"
            "    border-color: rgb(198, 99, 137)\n"
            "}\n"
            "\n"
            "/* Pressed effect: even darker border */\n"
            "QToolButton:pressed {\n"
            "    border-color: rgb(144, 72, 101)\n"
            "}\n"
            "\n"
            "/* Disabled state */\n"
            "QToolButton:disabled {\n"
            "    border-color: #CCCCCC;\n"
            "    color: #CCCCCC;\n"
            "}\n"
            ""
        )
        self.signin_btn_existing.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1)
        )

        self.horizontalLayout_12.addWidget(self.signin_btn_existing)

        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.verticalLayout_17.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_4 = QSpacerItem(
            20, 47, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_17.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_5 = QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.page_2)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setMinimumSize(QSize(500, 0))
        self.widget_3.setMaximumSize(QSize(500, 16777215))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_16 = QVBoxLayout(self.widget_3)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalSpacer_2 = QSpacerItem(
            20, 149, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_16.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, -1, -1, 10)
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 40px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_21.addWidget(self.label_7)

        self.verticalLayout_7.addLayout(self.verticalLayout_21)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.signin_email_lbl = QLabel(self.widget_3)
        self.signin_email_lbl.setObjectName("signin_email_lbl")
        self.signin_email_lbl.setStyleSheet(
            "color:rgb(166, 166, 166);\n"
            'font:500 12px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_10.addWidget(self.signin_email_lbl)

        self.signin_email_line = QLineEdit(self.widget_3)
        self.signin_email_line.setObjectName("signin_email_line")
        sizePolicy1.setHeightForWidth(
            self.signin_email_line.sizePolicy().hasHeightForWidth()
        )
        self.signin_email_line.setSizePolicy(sizePolicy1)
        self.signin_email_line.setMinimumSize(QSize(250, 35))
        self.signin_email_line.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: transparent;\n"
            "    border: 1px solid #dcdcdc;\n"
            "    border-radius: 10px;\n"
            "    padding-left: 14px;\n"
            '    font: 500 12px "Roboto";\n'
            "    color: rgb(108, 68, 103)\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border: 1px solid rgb(255, 157, 160); /* Blue border on focus */\n"
            "    background-color: #ffffff;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            'QLineEdit[echoMode="1"] { /* For password fields */\n'
            "    letter-spacing: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::placeholder {\n"
            "    color: #999999;\n"
            "}\n"
            ""
        )
        self.signin_email_line.setEchoMode(QLineEdit.EchoMode.Normal)
        self.signin_email_line.setDragEnabled(True)
        self.signin_email_line.setReadOnly(False)
        self.signin_email_line.setClearButtonEnabled(False)

        self.verticalLayout_10.addWidget(self.signin_email_line)

        self.verticalLayout_7.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.signin_password_lbl = QLabel(self.widget_3)
        self.signin_password_lbl.setObjectName("signin_password_lbl")
        self.signin_password_lbl.setStyleSheet(
            "color: rgb(166, 166, 166);\n"
            'font:500 12px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_11.addWidget(self.signin_password_lbl)

        self.signin_password_line = QLineEdit(self.widget_3)
        self.signin_password_line.setObjectName("signin_password_line")
        self.signin_password_line.setMinimumSize(QSize(250, 35))
        self.signin_password_line.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: transparent;\n"
            "    border: 1px solid #dcdcdc;\n"
            "    border-radius: 10px;\n"
            "    padding-left: 14px;\n"
            '    font: 400 7px "Roboto";\n'
            "    color:rgb(108, 68, 103)\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border: 1px solid rgb(255, 157, 160); /* Blue border on focus */\n"
            "    background-color: #ffffff;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            'QLineEdit[echoMode="1"] { /* For password fields */\n'
            "    letter-spacing: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::placeholder {\n"
            "    color: #999999;\n"
            "}\n"
            ""
        )
        self.signin_password_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.signin_password_line.setClearButtonEnabled(False)

        self.verticalLayout_11.addWidget(self.signin_password_line)

        self.verticalLayout_7.addLayout(self.verticalLayout_11)

        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 3, -1, -1)
        self.remember_checkbox = QCheckBox(self.widget_3)
        self.remember_checkbox.setObjectName("remember_checkbox")
        self.remember_checkbox.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.remember_checkbox.setStyleSheet(
            "\n"
            "QCheckBox{\n"
            "color: rgb(166, 166, 166);\n"
            'font:500 10px "Roboto";\n'
            "background-color: transparent;\n"
            "}\n"
            "\n"
            "QCheckBox::indicator {\n"
            "    \n"
            "	rgb(212, 212, 212)\n"
            "}\n"
            "\n"
            ""
        )
        self.remember_checkbox.setTristate(False)

        self.horizontalLayout_4.addWidget(self.remember_checkbox)

        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.signin_btn = QToolButton(self.widget_3)
        self.signin_btn.setObjectName("signin_btn")
        sizePolicy1.setHeightForWidth(self.signin_btn.sizePolicy().hasHeightForWidth())
        self.signin_btn.setSizePolicy(sizePolicy1)
        self.signin_btn.setMinimumSize(QSize(0, 35))
        self.signin_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signin_btn.setStyleSheet(
            "/* Base style for QToolButton */\n"
            "QToolButton {\n"
            "\n"
            "    \n"
            "    background: qlineargradient(\n"
            "        x1: 0, y1: 0, x2: 1, y2: 1,\n"
            "        stop: 0 rgb(253, 129, 130),\n"
            "        stop: 1 rgb(246, 211, 206)\n"
            "    );\n"
            "\n"
            "\n"
            "    color: white;               /* White text */\n"
            "    border: none;\n"
            "    border-radius: 10px;\n"
            "   \n"
            '    font: 500 12px "Roboto";\n'
            "   \n"
            "\n"
            "}\n"
            "\n"
            "/* Hover state */\n"
            "QToolButton:hover {\n"
            "    background-color: rgb(230, 146, 149)\n"
            "}\n"
            "\n"
            "/* Pressed state */\n"
            "QToolButton:pressed {\n"
            "    background-color: rgb(144, 72, 101)\n"
            "}\n"
            "\n"
            "/* Disabled state */\n"
            "QToolButton:disabled {\n"
            "    background-color: #A6A6A6;  /* Gray background when disabled */\n"
            "    color: #666666;\n"
            "}\n"
            "\n"
            "/* Optional: Different style for Sign Up button */\n"
            "QToolButton#signUpButton {\n"
            "    background-color: #28A745;  /* Green */\n"
            "}\n"
            "\n"
            "QToolButton#signUpButton:hover {\n"
            "    background-color: #1E7E34;\n"
            "}\n"
            "\n"
            "QToolButton#signUpButton:pressed {\n"
            "    background-color: #155D27;\n"
            "}\n"
            ""
        )

        def validate_signin():
            # Validate email and password fields are not empty
            if (
                not self.signin_email_line.text().strip()
                or not self.signin_password_line.text().strip()
            ):
                QMessageBox.warning(
                    None,
                    "Invalid Input",
                    "Please fill in both email and password fields.",
                )
                return

            auth_manager = AuthManager(None, None, None, None)

            user_id = auth_manager.signin(
                self.signin_email_line, self.signin_password_line
            )
            if user_id:
                remember = self.remember_checkbox.isChecked()

                settings = QSettings("MyCompany", "MyApp")
                settings.setValue("remember_me", remember)

                if remember:
                    settings.setValue("saved_email", self.signin_email_line.text())
                    settings.setValue("saved_user_id", str(user_id))
                else:
                    settings.remove("saved_email")
                    settings.remove("saved_user_id")

                print(f"Signin successful, user ID: {user_id}")

                from .main_window import BudgetApp

                self.main_app = BudgetApp(user_id)
                self.main_app.show()

                if hasattr(self, "parent") and self.parent():
                    self.parent().close()
                self.close()

            else:
                QMessageBox.warning(
                    None,
                    "Invalid Input",
                    "Invalid credentials. Please try again.",
                )

        def signup_success():
            if (
                not self.email_line.text().strip()
                or not self.password_line.text().strip()
                or not self.username_line.text().strip()
                or not self.confirm_line.text().strip()
            ):
                QMessageBox.warning(
                    None,
                    "Invalid Input",
                    "Please fill in both email and password fields.",
                )
                return

            auth_manager = AuthManager(None, None, None, None)
            if auth_manager.signup(
                self.username_line,
                self.password_line,
                self.confirm_line,
                self.email_line,
            ):

                QMessageBox.information(
                    None,
                    "Signup successful",
                    "You have successfully signed up. Please sign in to continue.",
                )

                self.stackedWidget.setCurrentIndex(1)
                self.signin_email_line.setText(self.email_line.text())  # Pre-fill email
                self.signin_password_line.clear()

        self.signin_btn.clicked.connect(validate_signin)

        self.verticalLayout_9.addWidget(self.signin_btn)

        self.verticalLayout_15.addLayout(self.verticalLayout_9)

        self.horizontalLayout_6.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.verticalSpacer_5 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.horizontalLayout_6.addItem(self.verticalSpacer_5)

        self.verticalLayout_16.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 15)
        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, -1, 5)
        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName("label_16")
        self.label_16.setMaximumSize(QSize(133, 16777215))
        self.label_16.setStyleSheet(
            "color:rgb(159, 159, 159);\n"
            'font: 400 11px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.horizontalLayout_9.addWidget(self.label_16)

        self.signup_existing_btn = QToolButton(self.widget_3)
        self.signup_existing_btn.setObjectName("signup_existing_btn")
        self.signup_existing_btn.setMinimumSize(QSize(20, 0))
        self.signup_existing_btn.setMaximumSize(QSize(50, 16777215))
        self.signup_existing_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signup_existing_btn.setStyleSheet(
            "/* Default style */\n"
            "QToolButton {\n"
            "    background-color: transparent;\n"
            "    color: rgb(153, 97, 146);\n"
            '    font: 500 11px "Roboto";\n'
            "}\n"
            "\n"
            "/* Hover effect: darker border */\n"
            "QToolButton:hover {\n"
            "    border-color: rgb(198, 99, 137)\n"
            "}\n"
            "\n"
            "/* Pressed effect: even darker border */\n"
            "QToolButton:pressed {\n"
            "    border-color: rgb(144, 72, 101)\n"
            "}\n"
            "\n"
            "/* Disabled state */\n"
            "QToolButton:disabled {\n"
            "    border-color: #CCCCCC;\n"
            "    color: #CCCCCC;\n"
            "}\n"
            ""
        )
        self.signup_existing_btn.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0)
        )

        self.horizontalLayout_9.addWidget(self.signup_existing_btn)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.verticalLayout_16.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(
            20, 149, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_16.addItem(self.verticalSpacer)

        self.horizontalLayout_5.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.page_2)
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setStyleSheet(
            "\n"
            "    background: qlineargradient(\n"
            "        x1: 0, y1: 1, x2: 1, y2: 0,\n"
            "        stop: 0 rgb(253, 122, 124),\n"
            "        stop: 0.5 rgb(250, 184, 183) ,\n"
            "        stop: 1 rgb(244, 212, 212)\n"
            "    );\n"
            ""
        )
        self.verticalLayout_19 = QVBoxLayout(self.widget_4)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalSpacer_7 = QSpacerItem(
            20, 260, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_19.addItem(self.verticalSpacer_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName("label_14")
        self.label_14.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            'font: 600 30px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_12.addWidget(self.label_14)

        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName("label_15")
        self.label_15.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            'font: 500 20px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_12.addWidget(self.label_15)

        self.horizontalLayout_11.addLayout(self.verticalLayout_12)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.verticalLayout_19.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_6 = QSpacerItem(
            20, 259, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_19.addItem(self.verticalSpacer_6)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalSpacer_11 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.logomin_2 = QLabel(self.widget_4)
        self.logomin_2.setObjectName("logomin_2")
        self.logomin_2.setMinimumSize(QSize(40, 30))
        self.logomin_2.setMaximumSize(QSize(40, 30))
        self.logomin_2.setStyleSheet("background-color: transparent")
        self.logomin_2.setPixmap(QPixmap(":/logomin.png"))
        self.logomin_2.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.logomin_2)

        self.verticalLayout_19.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_5.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

        self.load_saved_credentials_delayed()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.logomin_1.setText("")
        self.label_17.setText(
            QCoreApplication.translate("MainWindow", "Hi there.", None)
        )
        self.label_18.setText(
            QCoreApplication.translate(
                "MainWindow", "Let\u2019s get you signed up.", None
            )
        )
        self.label_12.setText(QCoreApplication.translate("MainWindow", "Sign up", None))
        self.username_label.setText(
            QCoreApplication.translate("MainWindow", "Username:", None)
        )
        self.username_line.setText("")
        self.username_line.setPlaceholderText("")
        self.email_label.setText(
            QCoreApplication.translate("MainWindow", "Email Address:", None)
        )
        self.email_line.setText("")
        self.email_line.setPlaceholderText("")
        self.password_label.setText(
            QCoreApplication.translate("MainWindow", "Password:", None)
        )
        self.password_line.setText("")
        self.password_line.setPlaceholderText("")
        self.confirm_label.setText(
            QCoreApplication.translate("MainWindow", "Confirm Password:", None)
        )
        self.confirm_line.setText("")
        self.confirm_line.setPlaceholderText("")
        self.terms_checkbox.setText(
            QCoreApplication.translate(
                "MainWindow", "I agree with terms and continue", None
            )
        )
        self.signup_btn.setText(
            QCoreApplication.translate("MainWindow", "Sign Up", None)
        )
        self.label_19.setText(
            QCoreApplication.translate("MainWindow", "Already have an account?", None)
        )
        self.signin_btn_existing.setText(
            QCoreApplication.translate("MainWindow", "Sign In", None)
        )
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Sign In", None))
        self.signin_email_lbl.setText(
            QCoreApplication.translate("MainWindow", "Email Address:", None)
        )
        self.signin_email_line.setText("")
        self.signin_email_line.setPlaceholderText("")
        self.signin_password_lbl.setText(
            QCoreApplication.translate("MainWindow", "Password:", None)
        )
        self.signin_password_line.setText("")
        self.signin_password_line.setPlaceholderText("")
        self.remember_checkbox.setText(
            QCoreApplication.translate("MainWindow", "Remember me", None)
        )
        self.signin_btn.setText(
            QCoreApplication.translate("MainWindow", "Sign In", None)
        )
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "Dont have an account?", None)
        )
        self.signup_existing_btn.setText(
            QCoreApplication.translate("MainWindow", "Sign up", None)
        )
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", "Hello again.", None)
        )
        self.label_15.setText(
            QCoreApplication.translate(
                "MainWindow", "Let\u2019s get you signed in.", None
            )
        )
        self.logomin_2.setText("")

    def load_saved_credentials(self):
        pass

    def load_saved_credentials_delayed(self):
        settings = QSettings("MyCompany", "MyApp")
        remember_me = settings.value("remember_me", False, type=bool)

        if remember_me:
            saved_email = settings.value("saved_email", "", type=str)
            saved_user_id = settings.value("saved_user_id", "", type=str)

            if saved_email and saved_user_id:
                self.stackedWidget.setCurrentIndex(1)
                self.signin_email_line.setText(saved_email)
                self.remember_checkbox.setChecked(True)

                self.signin_password_line.setFocus()

    def clear_saved_credentials(self):
        """Clear all saved credentials from settings"""
        settings = QSettings("MyCompany", "MyApp")
        settings.remove("remember_me")
        settings.remove("saved_email")
        settings.remove("saved_user_id")
