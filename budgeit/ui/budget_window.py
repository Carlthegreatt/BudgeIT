import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..logic.auth_manager import get_db_connection
from datetime import datetime


class BudgetWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle(" ")
        self.load_budget_data()
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

    def load_budget_data(self):
        """Load budget data from database and update table"""
        if not hasattr(self.parent, "user_id"):
            return

        with get_db_connection() as connect:
            current_month = datetime.today().strftime("%Y-%m")
            cursor = connect.cursor()
            cursor.execute(
                "SELECT * FROM user_data WHERE user_id = ? AND report_date = ?",
                (self.parent.user_id, current_month),
            )
            user_data = cursor.fetchone()

            cursor.execute(
                "SELECT * FROM remaining_budgets WHERE user_id = ? AND report_date = ?",
                (self.parent.user_id, current_month),
            )
            remaining_data = cursor.fetchone()

            if user_data:
                # Update table with budget data
                categories = [
                    "Food",
                    "Utilities",
                    "Health & Wellness",
                    "Personal & Lifestyle",
                    "Education",
                    "Transportation",
                    "Others",
                ]

                budget_values = [
                    user_data[6],  # food_budget
                    user_data[7],  # utilities_budget
                    user_data[8],  # health_wellness_budget
                    user_data[9],  # personal_lifestyle_budget
                    user_data[10],  # education_budget
                    user_data[11],  # transportation_budget
                    user_data[12],  # miscellaneous_budget
                ]

                remaining_values = [
                    remaining_data[5],  # remaining_food_budget
                    remaining_data[6],  # remaining_utilities_budget
                    remaining_data[7],  # remaining_health_wellness_budget
                    remaining_data[8],  # remaining_personal_lifestyle_budget
                    remaining_data[9],  # remaining_education_budget
                    remaining_data[10],  # remaining_transportation_budget
                    remaining_data[11],  # remaining_miscellaneous_budget
                ]

                for i, (category, budget, remaining) in enumerate(
                    zip(categories, budget_values, remaining_values)
                ):
                    category_item = QStandardItem(category)
                    budget_item = QStandardItem(f"₱{float(budget):,.2f}")
                    remaining_item = QStandardItem(f"₱{float(remaining):,.2f}")

                    # Center align all items
                    category_item.setTextAlignment(Qt.AlignCenter)
                    budget_item.setTextAlignment(Qt.AlignCenter)
                    remaining_item.setTextAlignment(Qt.AlignCenter)

                    self.model.setItem(i, 0, category_item)
                    self.model.setItem(i, 1, budget_item)
                    self.model.setItem(i, 2, remaining_item)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.setFixedSize(600, 415)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.container = QWidget(self.widget)
        self.container.setObjectName("container")
        self.container.setMinimumSize(QSize(0, 50))
        self.container.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 30;"
        )
        self.verticalLayout_3 = QVBoxLayout(self.container)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 0)
        self.budgetlbl = QLabel(self.container)
        self.budgetlbl.setObjectName("budgetlbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.budgetlbl.sizePolicy().hasHeightForWidth())
        self.budgetlbl.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies(["Roboto"])
        font.setBold(True)
        font.setItalic(False)
        self.budgetlbl.setFont(font)
        self.budgetlbl.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 40px "Roboto";\n'
            "background-color: transparent\n"
            ""
        )
        self.budgetlbl.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_2.addWidget(self.budgetlbl)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.budgettable = QTableView(self.container)
        self.budgettable.setObjectName("budgettable")
        self.budgettable.setStyleSheet(
            "\n"
            "    QTableView {\n"
            "        background-color: #ffffff;\n"
            "        border: 1px solid #dcdcdc;\n"
            "        border-radius: 6px;\n"
            "        gridline-color: #e6e6e6;\n"
            '        font: 400 12px "Roboto";\n'
            "    }\n"
            "\n"
            "    QHeaderView::section {\n"
            "        background-color: #f5f5f5;\n"
            "        color: #593852;\n"
            "        padding: 8px;\n"
            "        border: none;\n"
            "        border-bottom: 1px solid #dcdcdc;\n"
            "        font: 600 14px 'Roboto';\n"
            "    }\n"
            "\n"
            "    QTableView::item {\n"
            "        padding: 6px;\n"
            "        border: none;\n"
            "        color: #939393;\n"
            "    }\n"
            "\n"
            "    QTableView::item:selected {\n"
            "        background-color: #0078d7;\n"
            "        color: #ffffff;\n"
            "    }\n"
            "\n"
            "    QScrollBar:vertical {\n"
            "        background: #f0f0f0;\n"
            "        width: 12px;\n"
            "        margin: 2px 0 2px 0;\n"
            "        border-radius: 6px;\n"
            "    }\n"
            "\n"
            "    QScrollBar::handle:vertical {\n"
            "        background: #c0c0c0;\n"
            "        min-height: 20px;\n"
            "        border-radius: 6px;\n"
            "    }\n"
            ""
            "\n"
            "    QScrollBar::handle:vertical:hover {\n"
            "        background: #a0a0a0;\n"
            "    }\n"
            "\n"
            "    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
            "        height: 0px;\n"
            "    }\n"
            "\n"
            "    QScrollBar:horizontal {\n"
            "        background: #f0f0f0;\n"
            "        height: 12px;\n"
            "        margin: 0 2px 0 2px;\n"
            "        border-radius: 6px;\n"
            "    }\n"
            "\n"
            "    QScrollBar::handle:horizontal {\n"
            "        background: #c0c0c0;\n"
            "        min-width: 20px;\n"
            "        border-radius: 6px;\n"
            "    }\n"
            "\n"
            "    QScrollBar::handle:horizontal:hover {\n"
            "        background: #a0a0a0;\n"
            "    }\n"
            "\n"
            "    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
            "    width: 0px;\n"
            "    }\n"
            "\n"
            ""
        )
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ["Categories", "Budget Amount", "Remaining Budget"]
        )
        self.budgettable.setModel(self.model)
        self.budgettable.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.budgettable.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.budgettable.setEditTriggers(QTableView.NoEditTriggers)
        self.budgettable.setSelectionMode(QTableView.NoSelection)
        self.budgettable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.budgettable.setShowGrid(True)
        self.budgettable.setFocusPolicy(Qt.NoFocus)
        self.budgettable.horizontalHeader().setFocusPolicy(Qt.NoFocus)
        self.budgettable.verticalHeader().setVisible(False)
        categories = [
            "Food",
            "Utilities",
            "Health & Wellness",
            "Personal & Lifestyle",
            "Education",
            "Transportation",
            "Others",
        ]
        for category in categories:
            row = [
                QStandardItem(category),
                QStandardItem(""),
                QStandardItem(""),
            ]
            for item in row:
                item.setTextAlignment(Qt.AlignCenter)
            self.model.appendRow(row)

        self.budgettable.setCornerButtonEnabled(False)

        self.horizontalLayout.addWidget(self.budgettable)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addWidget(self.container)

        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.budgetlbl.setText(
            QCoreApplication.translate("Form", "Budget Overview", None)
        )

    # retranslateUi
