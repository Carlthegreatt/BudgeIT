import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..logic.auth_manager import get_db_connection
from datetime import datetime


class SavingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle(" ")
        self.load_savings_data()
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

    def load_savings_data(self):
        if not hasattr(self.parent, "user_id"):
            return

        with get_db_connection() as connect:
            current_month = datetime.today().strftime("%Y-%m")
            cursor = connect.cursor()
            cursor.execute(
                """SELECT SUM(monthly_savings) FROM user_data WHERE user_id = ?""",
                (self.parent.user_id,),
            )

            result = cursor.fetchone()
            if result is None:
                total_savings = 0
            else:
                total_savings = result[0]

            self.savingswindowvalue.setText(f"₱{float(total_savings):,.2f}")

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(486, 111)
        Dialog.setMinimumSize(QSize(0, 111))
        Dialog.setMaximumSize(QSize(16777215, 111))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.totalsavingslbl = QLabel(Dialog)
        self.totalsavingslbl.setObjectName("totalsavingslbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.totalsavingslbl.sizePolicy().hasHeightForWidth()
        )
        self.totalsavingslbl.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies(["Inter"])
        font.setBold(True)
        font.setItalic(False)
        self.totalsavingslbl.setFont(font)
        self.totalsavingslbl.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 32px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.totalsavingslbl.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout.addWidget(self.totalsavingslbl)

        self.savingswindowvalue = QLabel(Dialog)
        self.savingswindowvalue.setObjectName("savingswindowvalue")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.savingswindowvalue.sizePolicy().hasHeightForWidth()
        )
        self.savingswindowvalue.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies(["inter"])
        font1.setBold(True)
        font1.setItalic(False)
        self.savingswindowvalue.setFont(font1)
        self.savingswindowvalue.setStyleSheet(
            "color: rgb(212, 106, 146);\n"
            "background-color: transparent;\n"
            'font: 700 32px "inter";\n'
            ""
        )
        self.savingswindowvalue.setFrameShape(QFrame.Shape.NoFrame)
        self.savingswindowvalue.setFrameShadow(QFrame.Shadow.Sunken)
        self.savingswindowvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.savingswindowvalue.setWordWrap(False)

        self.horizontalLayout.addWidget(self.savingswindowvalue)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.totalsavingslbl.setText(
            QCoreApplication.translate("Dialog", "Total Savings:", None)
        )

    # retranslateUi
