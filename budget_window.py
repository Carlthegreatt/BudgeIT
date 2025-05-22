import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class BudgetWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(" ")

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setFixedSize(550, 415)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.container = QWidget(self.widget)
        self.container.setObjectName(u"container")
        self.container.setMinimumSize(QSize(0, 50))
        self.container.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 30;")
        self.verticalLayout_3 = QVBoxLayout(self.container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 0)
        self.budgetlbl = QLabel(self.container)
        self.budgetlbl.setObjectName(u"budgetlbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.budgetlbl.sizePolicy().hasHeightForWidth())
        self.budgetlbl.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setBold(True)
        font.setItalic(False)
        self.budgetlbl.setFont(font)
        self.budgetlbl.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 700 40px \"Inter\";\n"
"background-color: transparent\n"
"")
        self.budgetlbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_2.addWidget(self.budgetlbl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.budgettable = QTableView(self.container)
        self.budgettable.setObjectName(u"budgettable")
        self.budgettable.setStyleSheet(u"\n"
"    QTableView {\n"
"        background-color: #ffffff;\n"
"        border: 1px solid #dcdcdc;\n"
"        border-radius: 6px;\n"
"        gridline-color: #e6e6e6;\n"
"        font: 300 12px \"Inter\";\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: #f5f5f5;\n"
"        color: #333333;\n"
"        padding: 8px;\n"
"        border: none;\n"
"        border-bottom: 1px solid #dcdcdc;\n"
"        font-weight: bold;\n"
"    }\n"
"\n"
"    QTableView::item {\n"
"        padding: 6px;\n"
"        border: none;\n"

"        color: #2c2c2c;\n"
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
"")
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ["Categories", "Set Budget", "Remaining Budget"]
        )
        self.budgettable.setModel(self.model)
        self.budgettable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.budgettable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.budgettable.setEditTriggers(QTableView.NoEditTriggers)
        self.budgettable.setSelectionMode(QTableView.NoSelection)
        self.budgettable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.budgettable.setShowGrid(True)
        self.budgettable.setFocusPolicy(Qt.NoFocus)
        self.budgettable.horizontalHeader().setFocusPolicy(Qt.NoFocus)
        self.budgettable.verticalHeader().setVisible(False)
        categories = ["Food", "Utilities", "Health & Wellness", "Personal & Lifestyle", "Education", "Transportation", "Others"]
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
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.budgetlbl.setText(QCoreApplication.translate("Form", u"Your Budget", None))
    # retranslateUi


