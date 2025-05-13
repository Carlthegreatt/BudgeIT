from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from components.amounteditor import AmountEditor





class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 600)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(1000, 600))
        font = QFont()
        font.setFamilies(["Calibri"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(
            "\n"
            "QGroupBox#rightsidebar{\n"
            "	\n"
            "	\n"
            "	background-color: rgb(167, 83, 115);\n"
            "border-radius:40\n"
            "}\n"
            "\n"
            "QGroupBox#midbar{\n"
            "border-radius: 40;\n"
            "	\n"
            "	\n"
            "	background-color: rgb(254, 250, 250);\n"
            "border: 1px solid #ccc; \n"
            "}\n"
            "\n"
            "QGroupBox#leftsidebar{\n"
            "\n"
            "	\n"
            "	\n"
            "	background-color: rgb(108, 68, 100);\n"
            'font: 12pt "Roboto";}\n'
            "\n"
            "\n"
            "\n"
            "    \n"
            "QPushButton {\n"
            "color: white;      \n"
            "background: transparent;\n"
            "text-align: left;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "\n"
            ""
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leftsidebar = QGroupBox(self.centralwidget)
        self.leftsidebar.setObjectName("leftsidebar")
        font1 = QFont()
        font1.setFamilies(["Roboto"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.leftsidebar.setFont(font1)
        self.leftsidebar.setStyleSheet(
            "QPushButton {\n"
            "	color: white;      \n"
            "	background: transparent;\n"
            "text-align:left\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(167, 83, 115);\n"
            "	border-color: rgb(167, 83, 115);\n"
            "	border: 2px solid rgb(167, 83, 115);\n"
            "	text-align:left\n"
            "   \n"
            "} \n"
            "QPushButton:checked {\n"
            "background-color: rgb(167, 83, 115);\n"
            "	border-color: rgb(167, 83, 115);\n"
            "	border: 2px solid rgb(167, 83, 115);\n"
            "    \n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "QGroupBox#budgetbox{\n"
            "	background-color: #fefafa;\n"
            "border-radius:15\n"
            "}"
        )
        self.leftsidebar.setFlat(True)
        self.leftsidebar.setCheckable(False)
        self.budgetbox = QGroupBox(self.leftsidebar)
        self.budgetbox.setObjectName("budgetbox")
        self.budgetbox.setGeometry(QRect(10, 40, 141, 131))
        font2 = QFont()
        font2.setPointSize(12)
        self.budgetbox.setFont(font2)
        self.budgetbox.setStyleSheet("text-align: center;")
        self.editbudgetbtn = QPushButton(self.budgetbox)
        self.editbudgetbtn.setObjectName("editbudgetbtn")
        self.editbudgetbtn.setGeometry(QRect(30, 90, 81, 21))
        self.editbudgetbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.editbudgetbtn.setAutoFillBackground(False)
        self.editbudgetbtn.setStyleSheet(
            "\n"
            "\n"
            "\n"
            "QPushButton {\n"
            "background-color: rgb(244, 212, 212);\n"
            "color: rgb(167, 83, 115);\n"
            "border-color: rgb(244, 212, 212);\n"
            "text-align: center;\n"
            'font: 600 7pt "Inter";\n'
            "border-radius: 5;\n"
            "  \n"
            "\n"
            "}\n"
            "QPushButton:hover {\n"
            "\n"
            "	background-color: rgb(231, 201, 201);\n"
            "	border-color: rgb(231, 201, 201);\n"
            "	border: 2px solid rgb(231, 201, 201);\n"
            "   \n"
            "}"
        )
        self.editbudgetbtn.setCheckable(True)
        self.editbudgetbtn.setFlat(True)
        self.amount_editor = AmountEditor(self)  # Create instance of AmountEditor
        self.editbudgetbtn.clicked.connect(
            self.amount_editor.show
        )  # Connect to show method
        self.budgetamount = QLabel(self.budgetbox)
        self.budgetamount.setObjectName("budgetamount")
        self.budgetamount.setGeometry(QRect(10, 30, 121, 31))
        font3 = QFont()
        font3.setFamilies(["Roboto"])
        font3.setPointSize(20)
        font3.setWeight(QFont.Black)
        font3.setItalic(False)
        self.budgetamount.setFont(font3)
        self.budgetamount.setStyleSheet(
            "\n"
            "color: #d46a92;\n"
            'font: 900 20pt "Roboto";\n'
            "\n"
            "    text-align: center;\n"
            "\n"
            "\n"
            ""
        )
        self.budgetamount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currentbudgetlbl = QLabel(self.budgetbox)
        self.currentbudgetlbl.setObjectName("currentbudgetlbl")
        self.currentbudgetlbl.setGeometry(QRect(10, 60, 121, 21))
        self.currentbudgetlbl.setStyleSheet(
            "color: rgb(212, 106, 146);\n"
            'font: 600 10pt "Inter";\n'
            "text-align: center;"
        )
        self.currentbudgetlbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tab1 = QStackedWidget(self.leftsidebar)
        self.tab1.setObjectName("tab1")
        self.tab1.setGeometry(QRect(170, 0, 831, 651))
        self.tab1.setStyleSheet(
            "QStackedWidget {\n" "    background-color: #fefafa;\n" "}\n" ""
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(40)
        shadow.setOffset(120, 120)
        shadow.setColor(QColor(108, 68, 100, 160))  # Semi-transparent black

        self.tab1Page1 = QWidget()
        self.tab1Page1.setObjectName("tab1Page1")

        self.greethello_2 = QLabel(self.tab1Page1)
        self.greethello_2.setObjectName("greethello_2")
        self.greethello_2.setGeometry(QRect(40, 40, 121, 21))
        self.greethello_2.setStyleSheet(
            "color: rgb(212, 106, 146);\n" 'font: 600 15pt "Inter";'
        )
        self.greetuser_2 = QLabel(self.tab1Page1)
        self.greetuser_2.setObjectName("greetuser_2")
        self.greetuser_2.setGeometry(QRect(40, 60, 241, 41))
        self.greetuser_2.setGraphicsEffect(shadow)
        font4 = QFont()
        font4.setFamilies(["Inter"])
        font4.setPointSize(25)
        font4.setBold(True)
        font4.setItalic(False)
        self.greetuser_2.setFont(font4)
        self.greetuser_2.setStyleSheet(
            "color: rgb(108, 68, 100);\n" 'font: 700 25pt "Inter";'
        )
        self.activitybox = QGroupBox(self.tab1Page1)
        self.activitybox.setObjectName("activitybox")
        self.activitybox.setGeometry(QRect(20, 280, 791, 331))
        self.activitybox.setStyleSheet(
            "background-color: rgb(167, 83, 115);\n" "border-radius:20\n" ""
        )

        self.editamounttext = QLineEdit(self.activitybox)
        self.editamounttext.setObjectName("lineEdit")
        self.editamounttext.setGeometry(QRect(270, 10, 81, 31))
        self.editamounttext.setStyleSheet(
            "QLineEdit {\n"
            "	background-color: rgb(254, 250, 250);\n"
            "                padding: 8px;\n"
            "                border: 1px solid #ccc;\n"
            "                border-radius: 7px;\n"
            "                font-size: 10px;\n"
            "            }"
        )
        self.editdesc = QLineEdit(self.activitybox)
        self.editdesc.setObjectName("editdesc")
        self.editdesc.setGeometry(QRect(360, 10, 151, 31))
        self.editdesc.setStyleSheet(
            "QLineEdit {\n"
            "background-color: rgb(254, 250, 250);\n"
            "padding: 8px;\n"
            " border: 1px solid #ccc;\n"
            "border-radius: 7px;\n"
            "  font-size: 10px;\n"
            "\n"
            "            }"
        )
        self.greetuser_6 = QLabel(self.activitybox)
        self.greetuser_6.setObjectName("greetuser_6")
        self.greetuser_6.setGeometry(QRect(20, 0, 231, 51))
        self.greetuser_6.setFont(font4)
        self.greetuser_6.setStyleSheet(
            "color: rgb(254, 250, 250);\n" 'font: 700 23pt "Inter";'
        )
        self.category = QComboBox(self.activitybox)
        self.category.setPlaceholderText('Category')
        self.category.addItem("")
        self.category.addItem("")
        self.category.setObjectName("category")
        self.category.setGeometry(QRect(520, 10, 111, 31))
        self.category.setStyleSheet(
            "QComboBox{\n"
            "	color: rgb(167, 83, 115);\n"
            "				\n"
            "	background-color: rgb(254, 250, 250);\n"
            "                padding: 8px;\n"
            "                border: 1px solid #ccc;\n"
            "                border-radius: 7px;\n"
            "                font-size: 10px;\n"
            "            }"
            "QComboBox QAbstractItemView {\n"
            "background-color: #ffffff;\n"
            "color: #000000; \n"
            "}"
            "QComboBox::drop-down {\n"
            
            "border: none;\n"
            "background: transparent;}\n"
           
        )
        self.category.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.category.setEditable(False)
        self.category.setFrame(True)
        self.recentactbox = QGroupBox(self.activitybox)
        self.recentactbox.setObjectName("recentactbox")
        self.recentactbox.setGeometry(QRect(20, 50, 751, 311))
        self.recentactbox.setStyleSheet(
            "background-color: rgb(244, 212, 212);\n" "border-radius:20\n" ""
        )
        self.incomebox_13 = QGroupBox(self.tab1Page1)
        self.incomebox_13.setObjectName("incomebox_13")
        self.incomebox_13.setGeometry(QRect(409, 119, 351, 139))
        self.incomebox_13.setStyleSheet(
            "background-color: rgb(244, 212, 212);\n" "border-radius:15\n" ""
        )
        self.viewsumlbl = QPushButton(self.incomebox_13)
        self.viewsumlbl.setObjectName("viewsumlbl")
        self.viewsumlbl.setGeometry(QRect(260, 110, 71, 21))
        self.viewsumlbl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.viewsumlbl.setAutoFillBackground(False)
        self.viewsumlbl.setStyleSheet(
            "\n"
            "\n"
            "background-color: rgb(244, 212, 212);\n"
            "color: rgb(167, 83, 115);\n"
            "border-color: rgb(244, 212, 212);\n"
            "text-align: center;\n"
            'font: 600 7pt "Inter";\n'
            "border-radius: 10;\n"
            "  \n"
            ""
        )
        self.viewsumlbl.setCheckable(True)
        self.viewsumlbl.setFlat(True)
        self.expenselbl = QLabel(self.incomebox_13)
        self.expenselbl.setObjectName("expenselbl")
        self.expenselbl.setGeometry(QRect(20, 20, 301, 101))
        font5 = QFont()
        font5.setFamilies(["inter"])
        font5.setPointSize(35)
        font5.setBold(True)
        font5.setItalic(False)
        self.expenselbl.setFont(font5)
        self.expenselbl.setStyleSheet(
            "color: #d46a92;\n" 'font: 700 35pt "inter";\n' ""
        )
        self.expenselbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalexpenseblbl_12 = QLabel(self.incomebox_13)
        self.totalexpenseblbl_12.setObjectName("totalexpenseblbl_12")
        self.totalexpenseblbl_12.setGeometry(QRect(20, 20, 91, 16))
        self.totalexpenseblbl_12.setStyleSheet(
            "color: rgb(108, 68, 100);\n" 'font: 600 10pt "Inter";'
        )
        self.expenselbl.raise_()
        self.viewsumlbl.raise_()
        self.totalexpenseblbl_12.raise_()
        self.incomebox_7 = QGroupBox(self.tab1Page1)
        self.incomebox_7.setObjectName("incomebox_7")
        self.incomebox_7.setGeometry(QRect(60, 120, 341, 139))
        self.incomebox_7.setStyleSheet(
            "background-color: rgb(244, 212, 212);\n" "border-radius:15\n" ""
        )

        self.setincomebtn_7 = QPushButton(self.incomebox_7)
        self.setincomebtn_7.setObjectName("setincomebtn_7")
        self.setincomebtn_7.setGeometry(QRect(260, 110, 71, 21))
        self.setincomebtn_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setincomebtn_7.setAutoFillBackground(False)
        self.setincomebtn_7.setStyleSheet(
            "background-color: rgb(244, 212, 212);\n"
            "color: rgb(167, 83, 115);\n"
            "border-color: rgb(244, 212, 212);\n"
            "text-align: center;\n"
            'font: 600 7pt "Inter";\n'
            "border-radius: 10;\n"
            ""
        )
        self.setincomebtn_7.setCheckable(True)
        self.setincomebtn_7.setFlat(True)
        self.budgetamount_14 = QLabel(self.incomebox_7)
        self.budgetamount_14.setObjectName("budgetamount_14")
        self.budgetamount_14.setGeometry(QRect(20, 20, 301, 101))
        self.budgetamount_14.setFont(font5)
        self.budgetamount_14.setStyleSheet(
            "color: #d46a92;\n" 'font: 700 35pt "inter";\n' ""
        )
        self.budgetamount_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalincomelbl_7 = QLabel(self.incomebox_7)
        self.totalincomelbl_7.setObjectName("totalincomelbl_7")
        self.totalincomelbl_7.setGeometry(QRect(20, 20, 81, 16))
        self.totalincomelbl_7.setStyleSheet(
            "color: rgb(108, 68, 100);\n" 'font: 600 10pt "Inter";'
        )
        self.budgetamount_14.raise_()
        self.setincomebtn_7.raise_()
        self.totalincomelbl_7.raise_()
        self.tab1.addWidget(self.tab1Page1)
        self.tab1Page2 = QWidget()
        self.tab1Page2.setObjectName("tab1Page2")
        self.tab1.addWidget(self.tab1Page2)
        self.tab1Page3 = QWidget()
        self.tab1Page3.setObjectName("tab1Page3")
        self.tab1.addWidget(self.tab1Page3)
        self.homebtn = QPushButton(self.leftsidebar)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.homebtn)

        self.homebtn.setObjectName("homebtn")
        self.homebtn.setGeometry(QRect(0, 190, 171, 41))
        self.homebtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.homebtn.setStyleSheet("")
        self.homebtn.setCheckable(True)
        self.homebtn.setChecked(True)
        self.homebtn.clicked.connect(lambda: self.tab1.setCurrentIndex(0))
        self.homebtn.setStyleSheet("padding-left: 20px;")
        self.analyticsbtn = QPushButton(self.leftsidebar)
        self.buttonGroup_2.addButton(self.analyticsbtn)
        self.analyticsbtn.setObjectName("analyticsbtn")
        self.analyticsbtn.setGeometry(QRect(0, 230, 171, 41))
        self.analyticsbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.analyticsbtn.clicked.connect(lambda: self.tab1.setCurrentIndex(1))
        self.analyticsbtn.setStyleSheet("")
        self.analyticsbtn.setCheckable(True)
        self.analyticsbtn.setChecked(False)
        self.analyticsbtn.setStyleSheet("padding-left: 20px;")
        self.reportbtn = QPushButton(self.leftsidebar)
        self.buttonGroup_2.addButton(self.reportbtn)
        self.reportbtn.setObjectName("reportbtn")
        self.reportbtn.setGeometry(QRect(0, 270, 171, 41))
        self.reportbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reportbtn.setCheckable(True)
        self.reportbtn.setChecked(False)
        self.reportbtn.clicked.connect(lambda: self.tab1.setCurrentIndex(2))
        self.reportbtn.setStyleSheet("padding-left: 20px;")

        self.verticalLayout.addWidget(self.leftsidebar)

        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab1.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.editbudgetbtn.setText(
            QCoreApplication.translate("MainWindow", "Edit Budget", None)
        )
        self.budgetamount.setText(
            QCoreApplication.translate("MainWindow", "2100.00", None)
        )
        self.currentbudgetlbl.setText(
            QCoreApplication.translate("MainWindow", "Current Budget", None)
        )
        self.greethello_2.setText(
            QCoreApplication.translate("MainWindow", "Hello,", None)
        )
        self.greetuser_2.setText(
            QCoreApplication.translate("MainWindow", "Sample.", None)
        )
        self.activitybox.setTitle("")
        self.greetuser_6.setText(
            QCoreApplication.translate("MainWindow", "Recent Activity", None)
        )
        self.viewsumlbl.setText(
            QCoreApplication.translate("MainWindow", "View Summary", None)
        )
        self.expenselbl.setText(
            QCoreApplication.translate("MainWindow", "\u20b1 0300.00", None)
        )
        self.totalexpenseblbl_12.setText(
            QCoreApplication.translate("MainWindow", "Total Expense", None)
        )
        self.incomebox_7.setTitle("")
        self.setincomebtn_7.setText(
            QCoreApplication.translate("MainWindow", "Set Income", None)
        )
        self.budgetamount_14.setText(
            QCoreApplication.translate("MainWindow", "\u20b1 0300.00", None)
        )
        self.totalincomelbl_7.setText(
            QCoreApplication.translate("MainWindow", "Total Income", None)
        )
        self.homebtn.setText(QCoreApplication.translate("MainWindow", "Home", None))
        self.analyticsbtn.setText(
            QCoreApplication.translate("MainWindow", "Analytics", None)
        )
        self.reportbtn.setText(QCoreApplication.translate("MainWindow", "Report", None))
        self.editamounttext.setText("")
        self.editamounttext.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Amount", None)
        )
        self.editdesc.setText("")
        self.editdesc.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Description", None)
        )
        self.category.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Category", None)
        )
        self.category.setItemText(
            0, QCoreApplication.translate("MainWindow", "Food", None)
        )
        self.category.setItemText(
            1, QCoreApplication.translate("MainWindow", "Bills", None)
        )

    # retranslateUi


app = QApplication([])

window = Ui_MainWindow()
window.setupUi(window)
window.show()
app.exec()
