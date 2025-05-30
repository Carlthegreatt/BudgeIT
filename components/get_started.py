from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from components.login import *

# import images_rc  // Comment muna if di pa available ang images_rc
import sys


class get_started(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 592)
        MainWindow.setMaximumSize(QSize(1000, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GetStartedFrame = QFrame(self.centralwidget)
        self.GetStartedFrame.setObjectName("GetStartedFrame")
        self.GetStartedFrame.setMaximumSize(QSize(16777215, 16777211))
        self.GetStartedFrame.setStyleSheet(
            "#GetStartedFrame {\n"
            "background: qlineargradient(\n"
            "    spread:pad,\n"
            "    x1:0, y1:0,\n"
            "    x2:1, y2:0,\n"
            "    stop:0 #3A1C71,     /* Light Orange */\n"
            "    stop:0.5 #D76D77,   /* Pink */\n"
            "    stop:1   #FFAF7B    /* Lighter Velvet */\n"
            ");\n"
            "\n"
            "}"
        )
        self.GetStartedFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.GetStartedFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.GetStartedFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_frames = QFrame(self.GetStartedFrame)
        self.header_frames.setObjectName("header_frames")
        self.header_frames.setStyleSheet(
            "#header_frames {\n"
            "background-color: rgba(0,0,0,0.5);\n"
            "border: 1px solid Transparent;\n"
            "border-radius: 30px\n"
            "}"
        )
        self.header_frames.setFrameShape(QFrame.Shape.StyledPanel)
        self.header_frames.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.header_frames)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.h1_gs = QLabel(self.header_frames)
        self.h1_gs.setObjectName("h1_gs")
        self.h1_gs.setStyleSheet("QLabel {\n" 'font: 900 25px "Inter";\n' "\n" "\n" "}")
        self.h1_gs.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout_3.addWidget(self.h1_gs)

        self.h2_gs = QLabel(self.header_frames)
        self.h2_gs.setObjectName("h2_gs")
        self.h2_gs.setStyleSheet("QLabel {\n" 'font: 900 25px "Inter";\n' "}")

        self.verticalLayout_3.addWidget(self.h2_gs)

        self.h2_gs_2 = QLabel(self.header_frames)
        self.h2_gs_2.setObjectName("h2_gs_2")
        self.h2_gs_2.setStyleSheet("QLabel {\n" 'font: 900 30px "Inter";\n' "}")

        self.verticalLayout_3.addWidget(self.h2_gs_2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout.addWidget(self.header_frames)

        self.get_started_frame = QFrame(self.GetStartedFrame)
        self.get_started_frame.setObjectName("get_started_frame")
        self.get_started_frame.setStyleSheet(
            "#get_started_frame {\n" "background-color : rgba(0,0,0,0)\n" "}"
        )
        self.get_started_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.get_started_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.get_started_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(117, -1, -1, -1)
        self.get_started_btn = QToolButton(self.get_started_frame)
        self.get_started_btn.setObjectName("get_started_btn")
        self.get_started_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.get_started_btn.setStyleSheet(
            "#get_started_btn {\n"
            "border: 1px solid #000000;\n"
            "border-radius: 20px;\n"
            "background-color: rgba(0,0,0,0.8);\n"
            "color: #FFAF7B;\n"
            "font-weight: bold;\n"
            "font-size: 20px;\n"
            "padding: 20px;\n"
            "transition: background-color 2s ease-in-out;\n"
            "\n"
            "}\n"
            "\n"
            "#get_started_btn:pressed{\n"
            "background-color: rgba(0,0,0,1);\n"
            "}"
        )
        self.get_started_btn.clicked.connect(lambda: self.open_login())

        self.verticalLayout_2.addWidget(self.get_started_btn)

        self.horizontalLayout.addWidget(self.get_started_frame)

        self.verticalLayout.addWidget(self.GetStartedFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.h1_gs.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Manage your wallet,</p></body></html>',
                None,
            )
        )
        self.h2_gs.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<p style = "text-align: center;"><b>Track</> it with</p>',
                None,
            )
        )
        self.h2_gs_2.setText(
            QCoreApplication.translate(
                "MainWindow", '<p style = "text-align: center;">BudgeIT</p>', None
            )
        )
        self.get_started_btn.setText(
            QCoreApplication.translate("MainWindow", "Get Started", None)
        )

    # retranslateUi

    # ...existing code...

    def open_login(self):
        # Open the login/register window and close the current main window
        self.login_window = QMainWindow()
        self.login = Login_register()
        self.login.setupUi(self.login_window)
        self.login_window.show()
        # Find the parent MainWindow and close it
        parent = self.centralwidget.parent()
        if parent is not None:
            parent.close()


# ...existing code...
# filepath: c:\Users\DELL\Desktop\BudgeIT GetStarted\main.py
# ...existing code...

# ...existing code...


if __name__ == "__main__":
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = get_started()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec())
