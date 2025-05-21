from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import sys
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_ui1leHVVF.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)

class Login_register(QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1000, 600)
        MainWindow.setMaximumSize(QSize(1000, 600))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1000, 600))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1000, 600))
        self.frame.setMaximumSize(QSize(1000, 600))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_18 = QVBoxLayout(self.page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.MAINLAYOUT = QHBoxLayout()
        self.MAINLAYOUT.setObjectName(u"MAINLAYOUT")
        self.sub_window_frame1 = QFrame(self.page)
        self.sub_window_frame1.setObjectName(u"sub_window_frame1")
        self.sub_window_frame1.setStyleSheet(u"background-color: #DC143C;\n"
"border: 0px solid black;\n"
"border-radius: 10px;")
        self.sub_window_frame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.sub_window_frame1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.sub_window_frame1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.sub_window_frame1)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(1000, 600))
        self.label.setStyleSheet(u"font-size: 25px;")
        self.label.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.sub_window_frame1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout_3.addWidget(self.label_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(80, -1, -1, 100)
        self.register_btn = QToolButton(self.sub_window_frame1)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setMaximumSize(QSize(200, 16777215))
        self.register_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.register_btn.setStyleSheet(u"#register_btn{\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"padding: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"#register_btn:pressed{\n"
"background-color: #FFFFFF;\n"
"color: #DC143C;\n"
"}\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.register_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.MAINLAYOUT.addWidget(self.sub_window_frame1)

        self.sub_window_frame_2 = QFrame(self.page)
        self.sub_window_frame_2.setObjectName(u"sub_window_frame_2")
        self.sub_window_frame_2.setStyleSheet(u"#sub_window_frame_2 {\n"
"background-color: #FFFFFF;\n"
"border: 1px solid 	#C21E56;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.sub_window_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.sub_window_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.sub_window_frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 48, -1, -1)
        self.sign_up_layout = QVBoxLayout()
        self.sign_up_layout.setSpacing(12)
        self.sign_up_layout.setObjectName(u"sign_up_layout")
        self.sign_up_layout.setContentsMargins(-1, 13, -1, 19)
        self.sign_up = QLabel(self.sub_window_frame_2)
        self.sign_up.setObjectName(u"sign_up")
        self.sign_up.setStyleSheet(u"font-size: 25px;\n"
"font-weight: bold;\n"
"margin-left: 10px;\n"
"color: #DC143C;\n"
"")
        self.sign_up.setTextFormat(Qt.TextFormat.RichText)

        self.sign_up_layout.addWidget(self.sign_up)

        self.email_layout = QVBoxLayout()
        self.email_layout.setObjectName(u"email_layout")
        self.email_layout.setContentsMargins(160, -1, -1, -1)
        self.lineEdit = QLineEdit(self.sub_window_frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMaximumSize(QSize(240, 16777215))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	padding: 10px;\n"
"	border: 1px solid #DC143C;\n"
"	border-radius: 10px;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"QLineEdit::active {\n"
"    color: #DC143C;  \n"
"    font-style: italic; \n"
"}")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.email_layout.addWidget(self.lineEdit)


        self.sign_up_layout.addLayout(self.email_layout)

        self.password_layout = QVBoxLayout()
        self.password_layout.setObjectName(u"password_layout")
        self.password_layout.setContentsMargins(160, -1, -1, -1)
        self.lineEdit_2 = QLineEdit(self.sub_window_frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(240, 16777215))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	padding: 10px;\n"
"	border: 1px solid #DC143C;\n"
"	border-radius: 10px;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"QLineEdit::active {\n"
"    color: #DC143C;  \n"
"    font-style: italic; \n"
"}")

        self.password_layout.addWidget(self.lineEdit_2)


        self.sign_up_layout.addLayout(self.password_layout)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.forgot_passwprd = QPushButton(self.sub_window_frame_2)
        self.forgot_passwprd.setObjectName(u"forgot_passwprd")
        self.forgot_passwprd.setStyleSheet(u"border: 1px solid transparent;\n"
"color: #DC143C;")

        self.verticalLayout_14.addWidget(self.forgot_passwprd)


        self.sign_up_layout.addLayout(self.verticalLayout_14)


        self.verticalLayout_6.addLayout(self.sign_up_layout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(180, -1, -1, 220)
        self.Login_btn = QToolButton(self.sub_window_frame_2)
        self.Login_btn.setObjectName(u"Login_btn")
        self.Login_btn.setEnabled(True)
        self.Login_btn.setMaximumSize(QSize(200, 50))
        self.Login_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Login_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Login_btn.setStyleSheet(u"#Login_btn{\n"
"background-color: 	#DC143C;\n"
"border: 1px solid transparent;\n"
"border-radius: 10px;\n"
"color: #FFFFFF;\n"
"padding: 10px;\n"
"}\n"
"#Login_btn:pressed{\n"
"background-color: #A10E2A; /* Darker shade when clicked */\n"
"}\n"
"")
        self.Login_btn.setCheckable(False)

        self.verticalLayout_7.addWidget(self.Login_btn)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)


        self.MAINLAYOUT.addWidget(self.sub_window_frame_2)

        self.MAINLAYOUT.setStretch(0, 4)
        self.MAINLAYOUT.setStretch(1, 6)

        self.verticalLayout_18.addLayout(self.MAINLAYOUT)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_27 = QVBoxLayout(self.page_2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.MAINLAYOUT_3 = QHBoxLayout()
        self.MAINLAYOUT_3.setObjectName(u"MAINLAYOUT_3")
        self.sub_window_frame1_3 = QFrame(self.page_2)
        self.sub_window_frame1_3.setObjectName(u"sub_window_frame1_3")
        self.sub_window_frame1_3.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.sub_window_frame1_3.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.sub_window_frame1_3.setStyleSheet(u"background-color: 	#811331;\n"
"border: 0px solid black;\n"
"border-radius: 10px;\n"
"cursor: arrow;")
        self.sub_window_frame1_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.sub_window_frame1_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.sub_window_frame1_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_5 = QLabel(self.sub_window_frame1_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size: 25px;")
        self.label_5.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout_21.addWidget(self.label_5)


        self.verticalLayout_20.addLayout(self.verticalLayout_21)


        self.verticalLayout_19.addLayout(self.verticalLayout_20)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_6 = QLabel(self.sub_window_frame1_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout_22.addWidget(self.label_6)

        self.sub_t = QLabel(self.sub_window_frame1_3)
        self.sub_t.setObjectName(u"sub_t")
        self.sub_t.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout_22.addWidget(self.sub_t)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, -1, 77, 150)
        self.sign_up_btn = QToolButton(self.sub_window_frame1_3)
        self.sign_up_btn.setObjectName(u"sign_up_btn")
        self.sign_up_btn.setMaximumSize(QSize(200, 50))
        self.sign_up_btn.setStyleSheet(u"#sign_up_btn {\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"padding: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"#sign_up_btn:pressed{\n"
"background-color: #FFFFFF;\n"
"color: #811331;\n"
"\n"
"}")

        self.verticalLayout_23.addWidget(self.sign_up_btn)


        self.verticalLayout_22.addLayout(self.verticalLayout_23)


        self.verticalLayout_19.addLayout(self.verticalLayout_22)


        self.MAINLAYOUT_3.addWidget(self.sub_window_frame1_3)

        self.sub_window_frame_4 = QFrame(self.page_2)
        self.sub_window_frame_4.setObjectName(u"sub_window_frame_4")
        self.sub_window_frame_4.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.sub_window_frame_4.setStyleSheet(u"#sub_window_frame_4{\n"
"background-color: #FFFFFF;\n"
"border: 1px solid 	#C21E56;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.sub_window_frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.sub_window_frame_4.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_24 = QVBoxLayout(self.sub_window_frame_4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 48, -1, -1)
        self.sign_up_layout_3 = QVBoxLayout()
        self.sign_up_layout_3.setSpacing(12)
        self.sign_up_layout_3.setObjectName(u"sign_up_layout_3")
        self.sign_up_layout_3.setContentsMargins(-1, 13, -1, 19)
        self.sign_up_3 = QLabel(self.sub_window_frame_4)
        self.sign_up_3.setObjectName(u"sign_up_3")
        self.sign_up_3.setStyleSheet(u"font-size: 25px;\n"
"font-weight: bold;\n"
"margin-left: 10px;\n"
"color: 	#811331;\n"
"")
        self.sign_up_3.setTextFormat(Qt.TextFormat.RichText)

        self.sign_up_layout_3.addWidget(self.sign_up_3)

        self.email_layout_3 = QVBoxLayout()
        self.email_layout_3.setObjectName(u"email_layout_3")
        self.email_layout_3.setContentsMargins(0, -1, 144, -1)
        self.lineEdit_5 = QLineEdit(self.sub_window_frame_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"	padding: 10px;\n"
"	border: 1px solid 	#811331;\n"
"	border-radius: 10px;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"QLineEdit::active {\n"
"    color: 	#811331;  \n"
"    font-style: italic; \n"
"}")
        self.lineEdit_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.email_layout_3.addWidget(self.lineEdit_5)


        self.sign_up_layout_3.addLayout(self.email_layout_3)

        self.password_layout_3 = QVBoxLayout()
        self.password_layout_3.setObjectName(u"password_layout_3")
        self.password_layout_3.setContentsMargins(0, -1, 144, -1)
        self.lineEdit_6 = QLineEdit(self.sub_window_frame_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"	padding: 10px;\n"
"	border: 1px solid 	#811331;\n"
"	border-radius: 10px;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"QLineEdit::active {\n"
"    color: 	#811331;  \n"
"    font-style: italic; \n"
"}")

        self.password_layout_3.addWidget(self.lineEdit_6)


        self.sign_up_layout_3.addLayout(self.password_layout_3)

        self.password_layout_4 = QVBoxLayout()
        self.password_layout_4.setObjectName(u"password_layout_4")
        self.password_layout_4.setContentsMargins(0, -1, 144, -1)
        self.lineEdit_7 = QLineEdit(self.sub_window_frame_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"	padding: 10px;\n"
"	border: 1px solid 	#811331;\n"
"	border-radius: 10px;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"QLineEdit::active {\n"
"    color: 	#811331;  \n"
"    font-style: italic; \n"
"}")

        self.password_layout_4.addWidget(self.lineEdit_7)


        self.sign_up_layout_3.addLayout(self.password_layout_4)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.forgot_passwprd_3 = QPushButton(self.sub_window_frame_4)
        self.forgot_passwprd_3.setObjectName(u"forgot_passwprd_3")
        self.forgot_passwprd_3.setStyleSheet(u"border: 1px solid transparent;\n"
"color: 	#811331;")

        self.verticalLayout_25.addWidget(self.forgot_passwprd_3)


        self.sign_up_layout_3.addLayout(self.verticalLayout_25)


        self.verticalLayout_24.addLayout(self.sign_up_layout_3)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, -1, 175, 100)
        self.Register_btn_2 = QToolButton(self.sub_window_frame_4)
        self.Register_btn_2.setObjectName(u"Register_btn_2")
        self.Register_btn_2.setMaximumSize(QSize(200, 16777215))
        self.Register_btn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Register_btn_2.setStyleSheet(u"#Register_btn_2{\n"
"background-color: #811331;\n"
"border: 1px solid transparent;\n"
"border-radius: 10px;\n"
"color: #FFFFFF;\n"
"padding: 10px;\n"
"}\n"
"\n"
"#Register_btn_2:pressed{\n"
"background-color: #4d0b1d;\n"
"\n"
"}")

        self.verticalLayout_26.addWidget(self.Register_btn_2)


        self.verticalLayout_24.addLayout(self.verticalLayout_26)


        self.MAINLAYOUT_3.addWidget(self.sub_window_frame_4)

        self.MAINLAYOUT_3.setStretch(0, 4)
        self.MAINLAYOUT_3.setStretch(1, 6)

        self.verticalLayout_27.addLayout(self.MAINLAYOUT_3)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<p style = \"text-align:center; font-weight: bold\">Welcome!</p>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<p style = \"text-align: center;\">Manage your wallet,<br> track it with <span style = \"font-weight: bold;\">BudgeIT</span>.</p>", None))
        self.register_btn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.sign_up.setText(QCoreApplication.translate("MainWindow", u"<p style = \"text-align: center;\">Sign up</p>", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.forgot_passwprd.setText(QCoreApplication.translate("MainWindow", u"Forgot password? ", None))
        self.Login_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<p style = \"text-align:center; font-weight: bold\">Welcome!</p>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<p style = \"text-align: center;\">Manage your wallet,<br> track it with <span style = \"font-weight: bold;\">BudgeIT</span>.</p>", None))
        self.sub_t.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">already have an account?</span></p></body></html>", None))
        self.sign_up_btn.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.sign_up_3.setText(QCoreApplication.translate("MainWindow", u"<p style = \"text-align: center;\">REGISTER ACCOUNT</p>", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_6.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm password", None))
        self.lineEdit_7.setEchoMode(QLineEdit.EchoMode.Password)
        self.forgot_passwprd_3.setText(QCoreApplication.translate("MainWindow", u"Forgot password? ", None))
        self.Register_btn_2.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        
        self.sign_up_btn.clicked.connect(self.go_to_login)
        self.register_btn.clicked.connect(self.go_to_register)
        
  
    def go_to_register(self):
        self.stackedWidget.setCurrentIndex(1)  # Switch to register page
    def go_to_login(self):
        self.stackedWidget.setCurrentIndex(0)  # Switch to login page
            
