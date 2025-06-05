from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class SignOutWindow(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(" ")
        # Initialize opacity to 0 for fade-in effect
        self.setWindowOpacity(0.0)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(427, 250)
        Dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        Dialog.setStyleSheet(
            """
            QDialog {
                background-color: transparent;
                border-radius: 20px;
            }
            
            QWidget#container {
                background-color: white;
                border-radius: 20px;
                border: 2px solid rgb(108, 68, 100);
            }
            """
        )
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(427, 250))
        Dialog.setMaximumSize(QSize(427, 250))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 30px;"
        )
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 30, 20, 40)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSpacer_1 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_1)

        self.logomax = QLabel(self.widget)
        self.logomax.setObjectName("logomax")
        sizePolicy.setHeightForWidth(self.logomax.sizePolicy().hasHeightForWidth())
        self.logomax.setSizePolicy(sizePolicy)
        self.logomax.setMinimumSize(QSize(181, 71))
        self.logomax.setMaximumSize(QSize(149, 71))
        font = QFont()
        font.setFamilies(["Inter"])
        font.setBold(True)
        font.setItalic(False)
        self.logomax.setFont(font)
        self.logomax.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 30px "Inter";\n'
            "background-color: transparent\n"
            ""
        )

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_1 = QVBoxLayout()
        self.verticalLayout_1.setSpacing(0)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.signoutlbl = QLabel(self.widget)
        self.signoutlbl.setObjectName("signoutlbl")
        sizePolicy.setHeightForWidth(self.signoutlbl.sizePolicy().hasHeightForWidth())
        self.signoutlbl.setSizePolicy(sizePolicy)
        self.signoutlbl.setFont(font)
        self.signoutlbl.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 25px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.signoutlbl.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_7.addWidget(self.signoutlbl)

        self.horizontalSpacer_12 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.verticalLayout_1.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_11 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.confirmationlbl = QLabel(self.widget)
        self.confirmationlbl.setObjectName("confirmationlbl")
        sizePolicy.setHeightForWidth(
            self.confirmationlbl.sizePolicy().hasHeightForWidth()
        )
        self.confirmationlbl.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies(["Inter"])
        font1.setWeight(QFont.Medium)
        font1.setItalic(False)
        self.confirmationlbl.setFont(font1)
        self.confirmationlbl.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 500 15px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.confirmationlbl.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_8.addWidget(self.confirmationlbl)

        self.horizontalSpacer_13 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)

        self.verticalLayout_1.addLayout(self.horizontalLayout_8)

        self.verticalLayout.addLayout(self.verticalLayout_1)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setSpacing(5)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.horizontalLayout_1.setContentsMargins(-1, 0, -1, -1)
        self.signoutbtn = QToolButton(self.widget)
        self.signoutbtn.setObjectName("signoutbtn")
        self.signoutbtn.setMinimumSize(QSize(130, 34))
        self.signoutbtn.setMaximumSize(QSize(130, 16777215))
        self.signoutbtn.setStyleSheet(
            "\n"
            "\n"
            "\n"
            "QToolButton {\n"
            "	\n"
            "	\n"
            "	\n"
            "	color: rgb(245, 245, 245);\n"
            "	background-color: rgb(167, 83, 115);\n"
            "	border: 1px solid #ccc;\n"
            "    border-radius: 5px;\n"
            "	border-color: rgb(144, 72, 99);\n"
            "text-align: center;\n"
            ' font: 300 10px "Inter";\n'
            "\n"
            "\n"
            "  \n"
            "\n"
            "}\n"
            "QToolButton:hover {\n"
            "\n"
            "	\n"
            "	background-color: rgb(138, 69, 95);\n"
            "	\n"
            "   \n"
            "}"
        )

        self.horizontalLayout_1.addWidget(self.signoutbtn)

        self.cancelbtn = QToolButton(self.widget)
        self.cancelbtn.setObjectName("cancelbtn")
        self.cancelbtn.clicked.connect(Dialog.close)
        self.cancelbtn.setMinimumSize(QSize(130, 34))
        self.cancelbtn.setMaximumSize(QSize(130, 34))
        self.cancelbtn.setStyleSheet(
            "\n"
            "\n"
            "\n"
            "QToolButton {\n"
            "	\n"
            "	\n"
            "	\n"
            "	color: rgb(245, 245, 245);\n"
            "	background-color: rgb(167, 83, 115);\n"
            "	border: 1px solid #ccc;\n"
            "    border-radius: 5px;\n"
            "	border-color: rgb(144, 72, 99);\n"
            "text-align: center;\n"
            ' font: 300 10px "Inter";\n'
            "\n"
            "\n"
            "  \n"
            "\n"
            "}\n"
            "QToolButton:hover {\n"
            "\n"
            "	\n"
            "	background-color: rgb(138, 69, 95);\n"
            "	\n"
            "   \n"
            "}"
        )

        self.horizontalLayout_1.addWidget(self.cancelbtn)

        self.horizontalLayout.addLayout(self.horizontalLayout_1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.logomax.setText("")
        self.signoutlbl.setText(QCoreApplication.translate("Dialog", "Sign Out", None))
        self.confirmationlbl.setText(
            QCoreApplication.translate(
                "Dialog", "Are you sure you want to sign out?", None
            )
        )
        self.signoutbtn.setText(QCoreApplication.translate("Dialog", "Sign out", None))
        self.cancelbtn.setText(QCoreApplication.translate("Dialog", "Cancel", None))

    # retranslateUi

    def showEvent(self, event):
        # Create fade-in animation
        self.fade_anim = QPropertyAnimation(self, b"windowOpacity")
        self.fade_anim.setStartValue(0.0)
        self.fade_anim.setEndValue(1.0)
        self.fade_anim.setDuration(250)
        self.fade_anim.setEasingCurve(QEasingCurve.Type.InOutQuad)

        # Create scale animation for the widget
        self.scale_anim = QPropertyAnimation(self.widget, b"geometry")
        start_rect = self.widget.geometry()
        start_rect.setHeight(start_rect.height() * 0.8)
        start_rect.setWidth(start_rect.width() * 0.8)
        start_rect.moveCenter(self.widget.geometry().center())

        self.scale_anim.setStartValue(start_rect)
        self.scale_anim.setEndValue(self.widget.geometry())
        self.scale_anim.setDuration(100)
        self.scale_anim.setEasingCurve(QEasingCurve.Type.InOutQuad)

        # Start both animations
        self.fade_anim.start()
        self.scale_anim.start()

        super().showEvent(event)
