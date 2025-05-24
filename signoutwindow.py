# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signoutwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QToolButton,
    QVBoxLayout,
    QWidget,
)
import assets.images.images_rc  # Import the compiled resources


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(427, 250)
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
        self.verticalLayout_2.setContentsMargins(30, 20, 30, 40)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.budgetlbl_6 = QLabel(Dialog)
        self.budgetlbl_6.setObjectName("budgetlbl_6")
        sizePolicy.setHeightForWidth(self.budgetlbl_6.sizePolicy().hasHeightForWidth())
        self.budgetlbl_6.setSizePolicy(sizePolicy)
        self.budgetlbl_6.setMinimumSize(QSize(181, 71))
        self.budgetlbl_6.setMaximumSize(QSize(149, 71))
        font = QFont()
        font.setFamilies(["Inter"])
        font.setBold(True)
        font.setItalic(False)
        self.budgetlbl_6.setFont(font)
        self.budgetlbl_6.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 30px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.budgetlbl_6.setPixmap(QPixmap(":/logomax.png"))
        self.budgetlbl_6.setScaledContents(True)
        self.budgetlbl_6.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_4.addWidget(self.budgetlbl_6)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.budgetlbl_7 = QLabel(Dialog)
        self.budgetlbl_7.setObjectName("budgetlbl_7")
        sizePolicy.setHeightForWidth(self.budgetlbl_7.sizePolicy().hasHeightForWidth())
        self.budgetlbl_7.setSizePolicy(sizePolicy)
        self.budgetlbl_7.setFont(font)
        self.budgetlbl_7.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 25px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.budgetlbl_7.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_7.addWidget(self.budgetlbl_7)

        self.horizontalSpacer_12 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_13 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)

        self.budgetlbl_8 = QLabel(Dialog)
        self.budgetlbl_8.setObjectName("budgetlbl_8")
        sizePolicy.setHeightForWidth(self.budgetlbl_8.sizePolicy().hasHeightForWidth())
        self.budgetlbl_8.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies(["Inter"])
        font1.setWeight(QFont.Medium)
        font1.setItalic(False)
        self.budgetlbl_8.setFont(font1)
        self.budgetlbl_8.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 500 15px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.budgetlbl_8.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_8.addWidget(self.budgetlbl_8)

        self.horizontalSpacer_14 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_14)

        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.toolButton = QToolButton(Dialog)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setMinimumSize(QSize(130, 34))
        self.toolButton.setMaximumSize(QSize(130, 16777215))
        self.toolButton.setStyleSheet(
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

        self.horizontalLayout_9.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(Dialog)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(130, 34))
        self.toolButton_2.setMaximumSize(QSize(130, 34))
        self.toolButton_2.setStyleSheet(
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

        self.horizontalLayout_9.addWidget(self.toolButton_2)

        self.horizontalLayout.addLayout(self.horizontalLayout_9)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.budgetlbl_6.setText("")
        self.budgetlbl_7.setText(QCoreApplication.translate("Dialog", "Sign Out", None))
        self.budgetlbl_8.setText(
            QCoreApplication.translate(
                "Dialog", "Are you sure you want to sign out?", None
            )
        )
        self.toolButton.setText(QCoreApplication.translate("Dialog", "Sign out", None))
        self.toolButton_2.setText(QCoreApplication.translate("Dialog", "Cancel", None))

    # retranslateUi


if __name__ == "__main__":
    app = QApplication([])
    dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.setWindowTitle("Sign Out")
    dialog.show()
    app.exec()
