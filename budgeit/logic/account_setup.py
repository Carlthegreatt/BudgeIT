from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sqlite3
from .auth_manager import get_db_connection
import os


class AccountSetup(QDialog):
    setup_completed = Signal()

    def __init__(self, user_id, current_month, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.current_month = current_month
        self.setupUi(self)
        self.setWindowTitle(" ")
        self.inputs = [
            self.foodedit,
            self.utilitiesedit,
            self.healthwellnessedit,
            self.personallifestyeedit,
            self.educationedit,
            self.transportationedit,
            self.miscellaneousedit,
        ]
        print("from account setup: user id", self.user_id)

    def show(self):
        """Show the dialog and set it as modal"""
        self.setWindowModality(Qt.ApplicationModal)
        super().show()

    def setupUi(self, Dialog):
        font_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "assets", "fonts", "Roboto.ttf"
        )
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            if font_families:
                app_font = QFont(font_families[0])
                QApplication.setFont(app_font)

        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(500, 510)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(500, 510))
        Dialog.setMaximumSize(QSize(500, 510))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.verticalLayout_8 = QVBoxLayout(Dialog)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 10, -1, -1)

        self.setuplbl = QLabel(Dialog)
        self.setuplbl.setObjectName("setuplbl")
        self.setuplbl.setStyleSheet(
            'color: rgb(108, 68, 100);font: 700 40px "Inter";background-color: transparent'
        )
        self.verticalLayout_7.addWidget(self.setuplbl)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.requirementlbl = QLabel(Dialog)
        self.requirementlbl.setObjectName("requirementlbl")
        self.requirementlbl.setStyleSheet(
            'color:rgb(167, 83, 115);font:500 14px "Inter";background-color: transparent'
        )
        self.horizontalLayout_4.addWidget(self.requirementlbl)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )
        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.setlbl = QLabel(Dialog)
        self.setlbl.setObjectName("setlbl")
        self.setlbl.setStyleSheet(
            'color:rgb(166, 166, 166);font:500 12px "Inter";background-color: transparent'
        )
        self.verticalLayout_3.addWidget(self.setlbl)

        self.allowanceincomeedit = QLineEdit(Dialog)
        self.allowanceincomeedit.setObjectName("allowanceincomeedit")
        sizePolicy.setHeightForWidth(
            self.allowanceincomeedit.sizePolicy().hasHeightForWidth()
        )
        self.allowanceincomeedit.setSizePolicy(sizePolicy)
        self.allowanceincomeedit.setMinimumSize(QSize(180, 35))
        self.allowanceincomeedit.setStyleSheet(
            'QLineEdit {background-color: transparent;border: 1px solid #dcdcdc;border-radius: 10px;padding-left: 14px;font: 500 12px "Inter";color: rgb(108, 68, 103)}QLineEdit:focus {border: 1px solid rgb(255, 157, 160);background-color: #ffffff;outline: none;}QLineEdit[echoMode="1"] {letter-spacing: 2px;}QLineEdit::placeholder {color: rgb(223, 223, 223);}'
        )
        self.allowanceincomeedit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.allowanceincomeedit.setDragEnabled(True)
        self.allowanceincomeedit.setReadOnly(False)
        self.allowanceincomeedit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.allowanceincomeedit.setClearButtonEnabled(True)
        self.verticalLayout_3.addWidget(self.allowanceincomeedit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.monthbudgetlbl = QLabel(Dialog)
        self.monthbudgetlbl.setObjectName("monthbudgetlbl")
        self.monthbudgetlbl.setStyleSheet(
            'color:rgb(166, 166, 166);font:500 12px "Inter";background-color: transparent'
        )
        self.verticalLayout_4.addWidget(self.monthbudgetlbl)

        self.budgetvalue = QLabel(Dialog)
        self.budgetvalue.setObjectName("budgetvalue")
        self.budgetvalue.setMinimumSize(QSize(180, 35))
        self.budgetvalue.setMaximumSize(QSize(180, 16777215))
        self.budgetvalue.setStyleSheet(
            'color: white;font: 600 16px "Inter";background-color: rgb(167, 83, 115);border-radius: 10px'
        )
        self.budgetvalue.setText(f"₱{0.00:,.2f}")
        self.budgetvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_4.addWidget(self.budgetvalue)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.budgetpercategorylbl = QLabel(Dialog)
        self.budgetpercategorylbl.setObjectName("budgetpercategorylbl")
        self.budgetpercategorylbl.setStyleSheet(
            'color:rgb(166, 166, 166);font:500 12px "Inter";background-color: transparent'
        )
        self.verticalLayout_5.addWidget(self.budgetpercategorylbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 20)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")

        self.foodedit = QLineEdit(Dialog)
        self.foodedit.setObjectName("foodedit")
        sizePolicy.setHeightForWidth(self.foodedit.sizePolicy().hasHeightForWidth())
        self.foodedit.setSizePolicy(sizePolicy)
        self.foodedit.setMinimumSize(QSize(180, 35))
        self.foodedit.setStyleSheet(
            'QLineEdit {background-color: transparent;border: 1px solid #dcdcdc;border-radius: 10px;padding-left: 14px;font: 500 12px "Inter";color: rgb(108, 68, 103)}QLineEdit:focus {border: 1px solid rgb(255, 157, 160);background-color: #ffffff;outline: none;}QLineEdit[echoMode="1"] {letter-spacing: 2px;}'
        )
        self.foodedit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.foodedit.setDragEnabled(True)
        self.foodedit.setReadOnly(False)
        self.foodedit.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.foodedit)

        self.utilitiesedit = QLineEdit(Dialog)
        self.utilitiesedit.setObjectName("utilitiesedit")
        sizePolicy.setHeightForWidth(
            self.utilitiesedit.sizePolicy().hasHeightForWidth()
        )
        self.utilitiesedit.setSizePolicy(sizePolicy)
        self.utilitiesedit.setMinimumSize(QSize(180, 35))
        self.utilitiesedit.setStyleSheet(
            'QLineEdit {background-color: transparent;border: 1px solid #dcdcdc;border-radius: 10px;padding-left: 14px;font: 500 12px "Inter";color: rgb(108, 68, 103)}QLineEdit:focus {border: 1px solid rgb(255, 157, 160);background-color: #ffffff;outline: none;}QLineEdit[echoMode="1"] {letter-spacing: 2px;}QLineEdit::placeholder {color: rgb(223, 223, 223);}'
        )
        self.utilitiesedit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.utilitiesedit.setDragEnabled(True)
        self.utilitiesedit.setReadOnly(False)
        self.utilitiesedit.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.utilitiesedit)

        self.healthwellnessedit = QLineEdit(Dialog)
        self.healthwellnessedit.setObjectName("healthwellnessedit")
        sizePolicy.setHeightForWidth(
            self.healthwellnessedit.sizePolicy().hasHeightForWidth()
        )
        self.healthwellnessedit.setSizePolicy(sizePolicy)
        self.healthwellnessedit.setMinimumSize(QSize(180, 35))
        self.healthwellnessedit.setStyleSheet(
            'QLineEdit {background-color: transparent;border: 1px solid #dcdcdc;border-radius: 10px;padding-left: 14px;font: 500 12px "Inter";color: rgb(108, 68, 103)}QLineEdit:focus {border: 1px solid rgb(255, 157, 160);background-color: #ffffff;outline: none;}QLineEdit[echoMode="1"] {letter-spacing: 2px;}QLineEdit::placeholder {color: rgb(223, 223, 223);}'
        )
        self.healthwellnessedit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.healthwellnessedit.setDragEnabled(True)
        self.healthwellnessedit.setReadOnly(False)
        self.healthwellnessedit.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.healthwellnessedit)

        self.personallifestyeedit = QLineEdit(Dialog)
        self.personallifestyeedit.setObjectName("personallifestyeedit")
        sizePolicy.setHeightForWidth(
            self.personallifestyeedit.sizePolicy().hasHeightForWidth()
        )
        self.personallifestyeedit.setSizePolicy(sizePolicy)
        self.personallifestyeedit.setMinimumSize(QSize(180, 35))
        self.personallifestyeedit.setStyleSheet(
            'QLineEdit {background-color: transparent;border: 1px solid #dcdcdc;border-radius: 10px;padding-left: 14px;font: 500 12px "Inter";color: rgb(108, 68, 103)}QLineEdit:focus {border: 1px solid rgb(255, 157, 160);background-color: #ffffff;outline: none;}QLineEdit[echoMode="1"] {letter-spacing: 2px;}QLineEdit::placeholder {color: rgb(223, 223, 223);}'
        )
        self.personallifestyeedit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.personallifestyeedit.setDragEnabled(True)
        self.personallifestyeedit.setReadOnly(False)
        self.personallifestyeedit.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.personallifestyeedit)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.educationedit = QLineEdit(Dialog)
        self.educationedit.setObjectName("educationedit")
        sizePolicy.setHeightForWidth(
            self.educationedit.sizePolicy().hasHeightForWidth()
        )
        self.educationedit.setSizePolicy(sizePolicy)
        self.educationedit.setMinimumSize(QSize(180, 35))
        self.educationedit.setStyleSheet(
            'QLineEdit {background-color: transparent;border: 1px solid #dcdcdc;border-radius: 10px;padding-left: 14px;font: 500 12px "Inter";color: rgb(108, 68, 103)}QLineEdit:focus {border: 1px solid rgb(255, 157, 160);background-color: #ffffff;outline: none;}QLineEdit[echoMode="1"] {letter-spacing: 2px;}QLineEdit::placeholder {color: rgb(223, 223, 223);}'
        )
        self.educationedit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.educationedit.setDragEnabled(True)
        self.educationedit.setReadOnly(False)
        self.educationedit.setClearButtonEnabled(True)
        self.verticalLayout_2.addWidget(self.educationedit)

        self.transportationedit = QLineEdit(Dialog)
        self.transportationedit.setObjectName("transportationedit")
        sizePolicy.setHeightForWidth(
            self.transportationedit.sizePolicy().hasHeightForWidth()
        )
        self.transportationedit.setSizePolicy(sizePolicy)
        self.transportationedit.setMinimumSize(QSize(180, 35))
        self.transportationedit.setStyleSheet(
            'QLineEdit {background-color: transparent;border: 1px solid #dcdcdc;border-radius: 10px;padding-left: 14px;font: 500 12px "Inter";color: rgb(108, 68, 103)}QLineEdit:focus {border: 1px solid rgb(255, 157, 160);background-color: #ffffff;outline: none;}QLineEdit[echoMode="1"] {letter-spacing: 2px;}QLineEdit::placeholder {color: rgb(223, 223, 223);}'
        )
        self.transportationedit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.transportationedit.setDragEnabled(True)
        self.transportationedit.setReadOnly(False)
        self.transportationedit.setClearButtonEnabled(True)
        self.verticalLayout_2.addWidget(self.transportationedit)

        self.miscellaneousedit = QLineEdit(Dialog)
        self.miscellaneousedit.setObjectName("miscellaneousedit")
        sizePolicy.setHeightForWidth(
            self.miscellaneousedit.sizePolicy().hasHeightForWidth()
        )
        self.miscellaneousedit.setSizePolicy(sizePolicy)
        self.miscellaneousedit.setMinimumSize(QSize(180, 35))
        self.miscellaneousedit.setStyleSheet(
            'QLineEdit {background-color: transparent;border: 1px solid #dcdcdc;border-radius: 10px;padding-left: 14px;font: 500 12px "Inter";color: rgb(108, 68, 103)}QLineEdit:focus {border: 1px solid rgb(255, 157, 160);background-color: #ffffff;outline: none;}QLineEdit[echoMode="1"] {letter-spacing: 2px;}QLineEdit::placeholder {color: rgb(223, 223, 223);}'
        )
        self.miscellaneousedit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.miscellaneousedit.setDragEnabled(True)
        self.miscellaneousedit.setReadOnly(False)
        self.miscellaneousedit.setClearButtonEnabled(True)
        self.verticalLayout_2.addWidget(self.miscellaneousedit)

        self.submitbtn = QToolButton(Dialog)
        self.submitbtn.setObjectName("submitbtn")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.submitbtn.sizePolicy().hasHeightForWidth())
        self.submitbtn.setSizePolicy(sizePolicy1)
        self.submitbtn.setMinimumSize(QSize(0, 35))
        self.submitbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.submitbtn.setStyleSheet(
            'QToolButton {background: qlineargradient(x1: 0, y1: 1, x2: 1, y2: 0,stop: 0 rgb(255, 130, 136),stop: 1 rgb(244, 212, 212));color: white;border: none;border-radius: 10px;font: 500 12px "Inter";}QToolButton:hover {background-color: rgb(230, 146, 149)}QToolButton:pressed {background-color: rgb(144, 72, 101)}QToolButton:disabled {background-color: #A6A6A6;color: #666666;QToolButton#signUpButton {background-color: #28A745;}QToolButton#signUpButton:hover {background-color: #1E7E34;}QToolButton#signUpButton:pressed {background-color: #155D27;}}'
        )
        self.submitbtn.clicked.connect(self.submit_account_setup)
        self.verticalLayout_2.addWidget(self.submitbtn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(
            20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )
        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

        self.allowanceincomeedit.textChanged.connect(self.update_sum)
        self.foodedit.textChanged.connect(self.update_sum)
        self.utilitiesedit.textChanged.connect(self.update_sum)
        self.healthwellnessedit.textChanged.connect(self.update_sum)
        self.personallifestyeedit.textChanged.connect(self.update_sum)
        self.educationedit.textChanged.connect(self.update_sum)
        self.transportationedit.textChanged.connect(self.update_sum)
        self.miscellaneousedit.textChanged.connect(self.update_sum)

    def submit_account_setup(self):
        try:
            with get_db_connection() as connect:
                income = float(self.allowanceincomeedit.text())
                budget = float(
                    self.budgetvalue.text().replace("₱", "").replace(",", "").strip()
                )

                print(f"Debug - Income: {income}, Budget: {budget}")

                if income < budget:
                    print(f"Debug - Income ({income}) is less than budget ({budget})")
                    QMessageBox.warning(
                        self,
                        "Validation Error",
                        "Your allowance/income is less than your budget. Please adjust your budget.",
                    )
                    return
                else:
                    cursor = connect.cursor()
                    cursor.execute(
                        "SELECT * FROM user_data WHERE user_id = ?", (self.user_id,)
                    )
                    self.user_data = cursor.fetchone()

                    values = [
                        self.allowanceincomeedit.text(),
                        self.budgetvalue.text()
                        .replace("₱", "")
                        .replace(",", "")
                        .strip(),
                        self.foodedit.text().strip(),
                        self.utilitiesedit.text().strip(),
                        self.healthwellnessedit.text().strip(),
                        self.personallifestyeedit.text().strip(),
                        self.educationedit.text().strip(),
                        self.transportationedit.text().strip(),
                        self.miscellaneousedit.text().strip(),
                        float(self.allowanceincomeedit.text())
                        - float(self.user_data[6]),
                    ]

                    if not all(values):
                        QMessageBox.warning(
                            self, "Validation Error", "Please fill in all fields."
                        )
                        return

                    try:
                        [float(v) for v in values]
                    except ValueError:
                        QMessageBox.warning(
                            self,
                            "Validation Error",
                            "All fields must contain valid numbers.",
                        )
                        return

                    if self.user_data:
                        cursor.execute(
                            """
                            UPDATE user_data SET
                                monthly_income = ?,
                                monthly_budget = ?,
                                food_budget = ?,
                                utilities_budget = ?,
                                health_wellness_budget = ?,
                                personal_lifestyle_budget = ?,
                                education_budget = ?,
                                transportation_budget = ?,
                                miscellaneous_budget = ?,
                                monthly_savings = ?,  
                                report_date = ?
                            WHERE user_id = ?
                            """,
                            (
                                *values,
                                self.current_month,
                                self.user_id,
                            ),
                        )

                        cursor.execute(
                            "UPDATE remaining_budgets SET remaining_income = ?, remaining_monthly_savings = ?, remaining_monthly_budget = ?, remaining_food_budget = ?, remaining_utilities_budget = ?, remaining_health_wellness_budget = ?, remaining_personal_lifestyle_budget = ?, remaining_education_budget = ?, remaining_transportation_budget = ?, remaining_miscellaneous_budget = ?, report_date = ? WHERE user_id = ?",
                            (
                                self.allowanceincomeedit.text(),
                                self.allowanceincomeedit.text(),
                                self.budgetvalue.text()
                                .replace("₱", "")
                                .replace(",", "")
                                .strip(),
                                self.foodedit.text(),
                                self.utilitiesedit.text(),
                                self.healthwellnessedit.text(),
                                self.personallifestyeedit.text(),
                                self.educationedit.text(),
                                self.transportationedit.text(),
                                self.miscellaneousedit.text(),
                                self.current_month,
                                self.user_id,
                            ),
                        )
                    else:
                        cursor.execute(
                            """
                            INSERT INTO user_data (
                                user_id,
                                monthly_income,
                                food_budget,
                                utilities_budget,
                                health_wellness_budget,
                                personal_lifestyle_budget,
                                education_budget,
                                transportation_budget,
                                miscellaneous_budget,
                                monthly_savings,
                                monthly_budget,
                                report_date
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (
                                self.user_id,
                                *values,
                                self.current_month,
                            ),
                        )

                        cursor.execute(
                            "INSERT INTO remaining_budgets (user_id, remaining_income, remaining_monthly_savings, remaining_monthly_budget, remaining_food_budget, remaining_utilities_budget, remaining_health_wellness_budget, remaining_personal_lifestyle_budget, remaining_education_budget, remaining_transportation_budget, remaining_miscellaneous_budget, report_date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                            (
                                self.user_id,
                                self.allowanceincomeedit.text(),
                                self.allowanceincomeedit.text(),
                                self.budgetvalue.text()
                                .replace("₱", "")
                                .replace(",", "")
                                .strip(),
                                self.foodedit.text(),
                                self.utilitiesedit.text(),
                                self.healthwellnessedit.text(),
                                self.personallifestyeedit.text(),
                                self.educationedit.text(),
                                self.transportationedit.text(),
                                self.miscellaneousedit.text(),
                                self.current_month,
                            ),
                        )

                    connect.commit()
                    print("Account setup successful - user_data updated")

                    cursor.execute(
                        "UPDATE users SET account_setup = ? WHERE user_id = ?",
                        (True, self.user_id),
                    )
                    connect.commit()
                    print("Account setup successful - users table updated")

                    self.setup_completed.emit()
                    print("Setup completed signal emitted")
                    self.accept()

        except Exception as e:
            print(f"Error in account setup: {e}")
            QMessageBox.warning(
                self,
                "Setup Error",
                "There was an error saving your account setup. Please try again.",
            )

    def update_sum(self):
        total = 0.0
        for text_edit in self.inputs:
            try:
                value = float(text_edit.text())
                total += value
            except ValueError:
                continue
        self.budgetvalue.setText(f"₱{total:,.2f}")

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.setuplbl.setText(
            QCoreApplication.translate("Dialog", "Set up your account", None)
        )
        self.requirementlbl.setText(
            QCoreApplication.translate("Dialog", "Please fill in all fields.", None)
        )
        self.setlbl.setText(
            QCoreApplication.translate("Dialog", "Set Monthly Income/Allowance", None)
        )
        self.allowanceincomeedit.setText("")
        self.allowanceincomeedit.setPlaceholderText(
            QCoreApplication.translate("Dialog", "e.g. 32900", None)
        )
        self.monthbudgetlbl.setText(
            QCoreApplication.translate("Dialog", "This month's budget", None)
        )
        self.budgetpercategorylbl.setText(
            QCoreApplication.translate("Dialog", "Add budget per category", None)
        )
        self.foodedit.setText("")
        self.foodedit.setPlaceholderText(
            QCoreApplication.translate("Dialog", "Food", None)
        )
        self.utilitiesedit.setText("")
        self.utilitiesedit.setPlaceholderText(
            QCoreApplication.translate("Dialog", "Utilities", None)
        )
        self.healthwellnessedit.setText("")
        self.healthwellnessedit.setPlaceholderText(
            QCoreApplication.translate("Dialog", "Health & Wellness", None)
        )
        self.personallifestyeedit.setText("")
        self.personallifestyeedit.setPlaceholderText(
            QCoreApplication.translate("Dialog", "Personal & Lifestyle", None)
        )
        self.educationedit.setText("")
        self.educationedit.setPlaceholderText(
            QCoreApplication.translate("Dialog", "Education", None)
        )
        self.transportationedit.setText("")
        self.transportationedit.setPlaceholderText(
            QCoreApplication.translate("Dialog", "Transportation", None)
        )
        self.miscellaneousedit.setText("")
        self.miscellaneousedit.setPlaceholderText(
            QCoreApplication.translate("Dialog", "Miscellaneous", None)
        )
        self.submitbtn.setText(QCoreApplication.translate("Dialog", "Submit", None))
