from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from components.icons_rc import *
from components.ui import *


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 679)
        MainWindow.setMinimumSize(QSize(1000, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QGroupBox(self.centralwidget)
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setMinimumSize(QSize(170, 0))
        self.sidebar.setMaximumSize(QSize(500, 16777215))
        self.sidebar.setStyleSheet(
            "QGroupBox {\n"
            "	\n"
            "	\n"
            "	background-color: rgb(43, 27, 40);\n"
            "}\n"
            "QToolButton {\n"
            "	\n"
            "    color: white;\n"
            "    \n"
            "	background-color: rgb(43, 27, 40);\n"
            "    border: none;\n"
            "    padding: 10px 20px;\n"
            "    text-align: left;\n"
            "   \n"
            '    font: 500 13px "Inter";\n'
            "    icon-size: 20px 20px;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "    qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 20px 20px;\n"
            " \n"
            "	color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 20px 20px;\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "    padding-left: 25px;\n"
            "}\n"
            "\n"
            "QToolButton:checked {\n"
            "qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 20px 20px;\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "}\n"
            "\n"
            "QToolButton:disabled {\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb("
            "245, 245, 245);\n"
            "}\n"
            ""
        )
        self.verticalLayout_3 = QVBoxLayout(self.sidebar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 30, 0, 30)
        self.logo = QLabel(self.sidebar)
        self.logo.setObjectName("logo")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies(["Inter"])
        font.setBold(True)
        font.setItalic(False)
        self.logo.setFont(font)
        self.logo.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            "color: rgb(245, 245, 245);\n"
            'font: 700  20px "Inter";\n'
            "background-color: transparent\n"
            "\n"
            ""
        )
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.logo)

        self.verticalLayout_3.addLayout(self.verticalLayout_16)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")

        self.verticalLayout.addLayout(self.verticalLayout_19)

        self.homebtn = QToolButton(self.sidebar)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.homebtn)
        self.homebtn.setObjectName("homebtn")
        sizePolicy.setHeightForWidth(self.homebtn.sizePolicy().hasHeightForWidth())
        self.homebtn.setSizePolicy(sizePolicy)
        self.homebtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.homebtn.setAutoFillBackground(False)
        self.homebtn.clicked.connect(lambda: self.tab.setCurrentIndex(0))
        icon = QIcon()
        icon.addFile(
            ":/icons/dashboardlight.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        icon.addFile(
            ":/icons/dashboarddark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.homebtn.setIcon(icon)
        self.homebtn.setCheckable(True)
        self.homebtn.setChecked(True)
        self.homebtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.homebtn.setAutoRaise(False)
        self.homebtn.setArrowType(Qt.ArrowType.NoArrow)

        self.verticalLayout.addWidget(self.homebtn)

        self.analyticsbtn = QToolButton(self.sidebar)
        self.buttonGroup.addButton(self.analyticsbtn)
        self.analyticsbtn.setObjectName("analyticsbtn")
        sizePolicy.setHeightForWidth(self.analyticsbtn.sizePolicy().hasHeightForWidth())
        self.analyticsbtn.setSizePolicy(sizePolicy)
        self.analyticsbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.analyticsbtn.clicked.connect(lambda: self.tab.setCurrentIndex(1))
        icon1 = QIcon()
        icon1.addFile(
            ":/icons/analyticslight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        icon1.addFile(
            ":/icons/analyticsdark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.analyticsbtn.setIcon(icon1)
        self.analyticsbtn.setCheckable(True)
        self.analyticsbtn.setChecked(False)
        self.analyticsbtn.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.analyticsbtn.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )

        self.verticalLayout.addWidget(self.analyticsbtn)

        self.reportbtn = QToolButton(self.sidebar)
        self.buttonGroup.addButton(self.reportbtn)
        self.reportbtn.setObjectName("reportbtn")
        sizePolicy.setHeightForWidth(self.reportbtn.sizePolicy().hasHeightForWidth())
        self.reportbtn.setSizePolicy(sizePolicy)
        self.reportbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reportbtn.clicked.connect(lambda: self.tab.setCurrentIndex(2))
        icon2 = QIcon()
        icon2.addFile(
            ":/icons/monitoringlight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        icon2.addFile(
            ":/icons/monitoringdark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.reportbtn.setIcon(icon2)
        self.reportbtn.setCheckable(True)
        self.reportbtn.setChecked(False)
        self.reportbtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.reportbtn)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.logoutbtn = QToolButton(self.sidebar)
        self.logoutbtn.setObjectName("logoutbtn")
        sizePolicy.setHeightForWidth(self.logoutbtn.sizePolicy().hasHeightForWidth())
        self.logoutbtn.setSizePolicy(sizePolicy)
        self.logoutbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logoutbtn.setStyleSheet("")
        icon3 = QIcon()

        icon3.addFile(
            ":/icons/logoutlight.svg", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.logoutbtn.setIcon(icon3)
        self.logoutbtn.setCheckable(False)
        self.logoutbtn.setChecked(False)
        self.logoutbtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.logoutbtn)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_6.addWidget(self.sidebar)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tab = QStackedWidget(self.widget)
        self.tab.setObjectName("tab")
        self.page_1 = QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_2 = QVBoxLayout(self.page_1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_1 = QScrollArea(self.page_1)
        self.scrollArea_1.setObjectName("scrollArea_1")
        self.scrollArea_1.setStyleSheet(
            "\n"
            "\n"
            "\n"
            "QScrollArea{\n"
            "	background-color: rgb(254, 254, 254);\n"
            "\n"
            "border: none;}\n"
            "\n"
            "QScrollBar:vertical {\n"
            "    \n"
            "    background-color: rgb(245, 245, 245);\n"
            "    width: 5px;\n"
            "    margin: 0px 0px 0px 0px;\n"
            "	border: none\n"
            "	\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "    background: rgb(80, 51, 74);\n"
            "    min-height: 20px;\n"
            "    border-radius: 10000px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical,\n"
            "QScrollBar::sub-line:vertical {\n"
            "    background: none;\n"
            "    height: 0px;\n"
            "}\n"
            "\n"
            ""
        )
        self.scrollArea_1.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scrollArea_1.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scrollArea_1.setWidgetResizable(True)
        self.scrollArea_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 834, 859))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(20, 15, 20, 15)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 15, -1, -1)
        self.greethello = QLabel(self.scrollAreaWidgetContents_4)
        self.greethello.setObjectName("greethello")
        self.greethello.setMinimumSize(QSize(0, 0))
        self.greethello.setStyleSheet(
            "color: rgb(212, 106, 146);\n"
            "background-color: transparent;\n"
            'font: 600 20px "Inter";'
        )

        self.verticalLayout_13.addWidget(self.greethello)

        self.user = QLabel(self.scrollAreaWidgetContents_4)
        self.user.setObjectName("user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy1)
        self.user.setFont(font)
        self.user.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 40px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.user.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.verticalLayout_13.addWidget(self.user)

        self.verticalLayout_26.addLayout(self.verticalLayout_13)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 15, -1, -1)
        self.totalbudgetbox_2 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.totalbudgetbox_2.setObjectName("totalbudgetbox_2")
        self.totalbudgetbox_2.setMinimumSize(QSize(300, 120))
        self.totalbudgetbox_2.setStyleSheet(
            "background-color: rgb(244, 212, 212);\n"
            "\n"
            "border-radius: 30px;\n"
            "\n"
            ""
        )
        self.verticalLayout_25 = QVBoxLayout(self.totalbudgetbox_2)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(20, 10, -1, -1)
        self.totalbudgetlbl_3 = QLabel(self.totalbudgetbox_2)
        self.totalbudgetlbl_3.setObjectName("totalbudgetlbl_3")
        self.totalbudgetlbl_3.setMinimumSize(QSize(0, 30))
        self.totalbudgetlbl_3.setMaximumSize(QSize(16777215, 25))
        self.totalbudgetlbl_3.setStyleSheet(
            "color: rgb(108, 68, 100);\n" 'font: 600 18px "Inter";'
        )
        self.totalbudgetlbl_3.setTextFormat(Qt.TextFormat.MarkdownText)
        self.totalbudgetlbl_3.setScaledContents(False)
        self.totalbudgetlbl_3.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.totalbudgetlbl_3.setIndent(0)

        self.horizontalLayout_17.addWidget(self.totalbudgetlbl_3)

        self.verticalLayout_25.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 15, -1, -1)
        self.budgetvalue_3 = QLabel(self.totalbudgetbox_2)
        self.budgetvalue_3.setObjectName("budgetvalue_3")
        font1 = QFont()
        font1.setFamilies(["inter"])
        font1.setBold(True)
        font1.setItalic(False)
        self.budgetvalue_3.setFont(font1)
        self.budgetvalue_3.setStyleSheet(
            "color: rgb(167, 83, 115);\n"
            "background-color: transparent;\n"
            'font: 700 45px "inter";\n'
            ""
        )
        self.budgetvalue_3.setFrameShape(QFrame.Shape.NoFrame)
        self.budgetvalue_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.budgetvalue_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.budgetvalue_3)

        self.verticalLayout_25.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(20)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(20, -1, -1, -1)
        self.progressBar = QProgressBar(self.totalbudgetbox_2)
        self.progressBar.setObjectName("progressBar")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setMinimumSize(QSize(0, 0))
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setStyleSheet(
            "QProgressBar {\n"
            "	\n"
            "	\n"
            "	background-color: rgb(245, 245, 245);\n"
            "	\n"
            "	\n"
            "	\n"
            "	\n"
            "	\n"
            "	color: rgb(245, 245, 245);\n"
            ' 	font: 600 7pt "Inter";\n'
            "    \n"
            "    border-radius: 10px;\n"
            "    text-align: left;\n"
            "}\n"
            "\n"
            "QProgressBar::chunk {\n"
            "    background: QLinearGradient(\n"
            "        x1: 0, y1: 0,\n"
            "        x2: 1, y2: 0,\n"
            "	\n"
            "        stop: 0 #6c4464\n"
            "\n"
            "        stop: 1 #a75373\n"
            "    );\n"
            "    border-radius: 9px;\n"
            "}\n"
            ""
        )
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_19.addWidget(self.progressBar)

        self.viewcategorylbl_4 = QToolButton(self.totalbudgetbox_2)
        self.viewcategorylbl_4.setObjectName("viewcategorylbl_4")
        self.viewcategorylbl_4.setMinimumSize(QSize(50, 50))
        self.viewcategorylbl_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.viewcategorylbl_4.setAutoFillBackground(False)
        self.viewcategorylbl_4.setStyleSheet(
            "\n"
            "QToolButton {\n"
            "background-color: rgb(167, 83, 115);\n"
            "color: rgb(167, 83, 115);\n"
            "border-color: rgb(244, 212, 212);\n"
            "text-align: center;\n"
            'font: 600 7pt "Inter";\n'
            "border-radius: 25px;}\n"
            " \n"
            "QToolButton:hover {\n"
            "	background-color: rgb(147, 73, 101);\n"
            "}\n"
            ""
        )
        icon4 = QIcon()
        icon4.addFile(
            ":/icons/walletlight.svg", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.viewcategorylbl_4.setIcon(icon4)
        self.viewcategorylbl_4.setIconSize(QSize(20, 20))
        self.viewcategorylbl_4.setCheckable(False)

        self.horizontalLayout_19.addWidget(self.viewcategorylbl_4)

        self.verticalLayout_25.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_8.addWidget(self.totalbudgetbox_2)

        self.totalbudgetbox_3 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.totalbudgetbox_3.setObjectName("totalbudgetbox_3")
        self.totalbudgetbox_3.setMinimumSize(QSize(300, 120))
        self.totalbudgetbox_3.setStyleSheet(
            "background-color: rgb(244, 212, 212);\n"
            "\n"
            "border-radius:30px;\n"
            "\n"
            ""
        )
        self.verticalLayout_28 = QVBoxLayout(self.totalbudgetbox_3)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 10, -1, -1)
        self.totalbudgetlbl_4 = QLabel(self.totalbudgetbox_3)
        self.totalbudgetlbl_4.setObjectName("totalbudgetlbl_4")
        self.totalbudgetlbl_4.setMinimumSize(QSize(0, 30))
        self.totalbudgetlbl_4.setMaximumSize(QSize(16777215, 25))
        self.totalbudgetlbl_4.setStyleSheet(
            "color: rgb(108, 68, 100);\n" 'font: 600 18px "Inter";'
        )
        self.totalbudgetlbl_4.setTextFormat(Qt.TextFormat.MarkdownText)
        self.totalbudgetlbl_4.setScaledContents(False)
        self.totalbudgetlbl_4.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.totalbudgetlbl_4.setIndent(20)

        self.horizontalLayout_20.addWidget(self.totalbudgetlbl_4)

        self.verticalLayout_28.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 15, -1, -1)
        self.budgetvalue_4 = QLabel(self.totalbudgetbox_3)
        self.budgetvalue_4.setObjectName("budgetvalue_4")
        self.budgetvalue_4.setFont(font1)
        self.budgetvalue_4.setStyleSheet(
            "color: rgb(212, 106, 146);\n"
            "background-color: transparent;\n"
            'font: 700 45px "inter";\n'
            ""
        )
        self.budgetvalue_4.setFrameShape(QFrame.Shape.NoFrame)
        self.budgetvalue_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.budgetvalue_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.budgetvalue_4)

        self.verticalLayout_28.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(20, -1, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_22.addItem(self.horizontalSpacer_3)

        self.viewcategorylbl_5 = QToolButton(self.totalbudgetbox_3)
        self.viewcategorylbl_5.setObjectName("viewcategorylbl_5")
        self.viewcategorylbl_5.setMinimumSize(QSize(50, 50))
        self.viewcategorylbl_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.viewcategorylbl_5.setAutoFillBackground(False)
        self.viewcategorylbl_5.setStyleSheet(
            "QToolButton{\n"
            "\n"
            "background-color: rgb(203, 101, 140);\n"
            "color: rgb(167, 83, 115);\n"
            "border-color: rgb(244, 212, 212);\n"
            "text-align: center;\n"
            'font: 600 7pt "Inter";\n'
            "border-radius: 25px;}\n"
            "\n"
            "QToolButton:hover {\n"
            "    \n"
            "	background-color: rgb(177, 88, 122);\n"
            "}\n"
            "  \n"
            ""
        )
        icon5 = QIcon()
        icon5.addFile(
            ":/icons/savingslight.svg", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.viewcategorylbl_5.setIcon(icon5)
        self.viewcategorylbl_5.setIconSize(QSize(20, 20))
        self.viewcategorylbl_5.setCheckable(False)

        self.horizontalLayout_22.addWidget(self.viewcategorylbl_5)

        self.verticalLayout_28.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_8.addWidget(self.totalbudgetbox_3)

        self.verticalLayout_26.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 10, -1, 10)
        self.savingsbox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.savingsbox.setObjectName("savingsbox")
        self.savingsbox.setMinimumSize(QSize(130, 80))
        font2 = QFont()
        font2.setPointSize(12)
        self.savingsbox.setFont(font2)
        self.savingsbox.setStyleSheet(
            "text-align: center;\n"
            "background-color: rgb(167, 83, 115);\n"
            "border-radius: 20px"
        )
        self.verticalLayout_31 = QVBoxLayout(self.savingsbox)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(40, -1, 30, 0)
        self.incomevalue_3 = QLabel(self.savingsbox)
        self.incomevalue_3.setObjectName("incomevalue_3")
        sizePolicy.setHeightForWidth(
            self.incomevalue_3.sizePolicy().hasHeightForWidth()
        )
        self.incomevalue_3.setSizePolicy(sizePolicy)
        self.incomevalue_3.setMaximumSize(QSize(16777215, 50))
        self.incomevalue_3.setFont(font1)
        self.incomevalue_3.setStyleSheet(
            "color: rgb(250, 250, 250);\n" 'font: 700 30px "inter";\n' ""
        )
        self.incomevalue_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.incomevalue_3.setWordWrap(True)

        self.horizontalLayout_13.addWidget(self.incomevalue_3)

        self.savingslbl = QLabel(self.savingsbox)
        self.savingslbl.setObjectName("savingslbl")
        self.savingslbl.setMaximumSize(QSize(16777215, 20))
        self.savingslbl.setStyleSheet(
            "color: rgb(250, 250, 250);\n"
            'font: 600 14px "Inter";\n'
            "text-align: center;"
        )
        self.savingslbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.savingslbl)

        self.verticalLayout_31.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_9.addWidget(self.savingsbox)

        self.incomebox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.incomebox.setObjectName("incomebox")
        self.incomebox.setMinimumSize(QSize(130, 80))
        self.incomebox.setFont(font2)
        self.incomebox.setStyleSheet(
            "text-align: center;\n"
            "background-color: rgb(167, 83, 115);\n"
            "border-radius: 20px"
        )
        self.verticalLayout_33 = QVBoxLayout(self.incomebox)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, -1, -1, 12)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(21)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(40, -1, 30, 0)
        self.incomevalue_2 = QLabel(self.incomebox)
        self.incomevalue_2.setObjectName("incomevalue_2")
        sizePolicy.setHeightForWidth(
            self.incomevalue_2.sizePolicy().hasHeightForWidth()
        )
        self.incomevalue_2.setSizePolicy(sizePolicy)
        self.incomevalue_2.setMaximumSize(QSize(16777215, 50))
        self.incomevalue_2.setFont(font1)
        self.incomevalue_2.setStyleSheet(
            "color: rgb(250, 250, 250);\n" 'font: 700 30px "inter";\n' ""
        )
        self.incomevalue_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.incomevalue_2.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.incomevalue_2)

        self.incomlbl = QLabel(self.incomebox)
        self.incomlbl.setObjectName("incomlbl")
        self.incomlbl.setMaximumSize(QSize(16777215, 20))
        self.incomlbl.setStyleSheet(
            "color: rgb(250, 250, 250);\n"
            'font: 600 14px "Inter";\n'
            "text-align: center;"
        )
        self.incomlbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.incomlbl)

        self.verticalLayout_33.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9.addWidget(self.incomebox)

        self.verticalLayout_26.addLayout(self.horizontalLayout_9)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 10, 0, 20)
        self.activitybox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.activitybox.setObjectName("activitybox")
        self.activitybox.setMinimumSize(QSize(0, 381))
        self.activitybox.setStyleSheet(
            "background-color: rgb(108, 68, 100);\n" "border-radius:20\n" ""
        )
        self.verticalLayout_10 = QVBoxLayout(self.activitybox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, 15, 20, -1)
        self.activitylbl = QLabel(self.activitybox)
        self.activitylbl.setObjectName("activitylbl")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.activitylbl.sizePolicy().hasHeightForWidth())
        self.activitylbl.setSizePolicy(sizePolicy3)
        self.activitylbl.setFont(font)
        self.activitylbl.setStyleSheet(
            "color: rgb(254, 250, 250);\n" 'font: 700 30px "Inter";'
        )

        self.horizontalLayout_7.addWidget(self.activitylbl)

        self.amountedit = QLineEdit(self.activitybox)
        self.amountedit.setObjectName("amountedit")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.amountedit.sizePolicy().hasHeightForWidth())
        self.amountedit.setSizePolicy(sizePolicy4)
        self.amountedit.setStyleSheet(
            "QLineEdit {\n"
            "	background-color: rgb(254, 250, 250);\n"
            "                padding: 8px;\n"
            "                border: 1px solid #ccc;\n"
            "                border-radius: 7px;\n"
            "                font-size: 10px;\n"
            "            }"
        )

        self.horizontalLayout_7.addWidget(self.amountedit)

        self.descriptionedit = QLineEdit(self.activitybox)
        self.descriptionedit.setObjectName("descriptionedit")
        sizePolicy4.setHeightForWidth(
            self.descriptionedit.sizePolicy().hasHeightForWidth()
        )
        self.descriptionedit.setSizePolicy(sizePolicy4)
        self.descriptionedit.setStyleSheet(
            "QLineEdit {\n"
            "	\n"
            "	\n"
            "					background-color: rgb(254, 250, 250);\n"
            "                padding: 8px;\n"
            "                border: 1px solid #ccc;\n"
            "                border-radius: 7px;\n"
            "                font-size: 10px;\n"
            "\n"
            "            }"
        )

        self.horizontalLayout_7.addWidget(self.descriptionedit)

        self.categorycombo = QComboBox(self.activitybox)
        self.categorycombo.setPlaceholderText("Category")
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.setObjectName("categorycombo")
        sizePolicy4.setHeightForWidth(
            self.categorycombo.sizePolicy().hasHeightForWidth()
        )
        self.categorycombo.setSizePolicy(sizePolicy4)
        self.categorycombo.setStyleSheet(
            "QComboBox{\n"
            "	color: rgb(167, 83, 115);\n"
            "	alternate-background-color: rgb(240, 240, 240);\n"
            "				\n"
            "	background-color: rgb(254, 250, 250);\n"
            "                padding: 8px;\n"
            "                border: 1px solid #ccc;\n"
            "                border-radius: 7px;\n"
            "                font-size: 10px;\n"
            "\n"
            "\n"
            "            }\n"
            "\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "background-color: #ffffff;\n"
            "color: #000000; \n"
            "}"
            "QComboBox::drop-down {\n"
            "    border: none;\n"
            "    background: transparent;\n"
            "}"
        )
        self.categorycombo.setEditable(False)
        self.categorycombo.setFrame(True)

        self.horizontalLayout_7.addWidget(self.categorycombo)

        self.addtransbtn = QPushButton(self.activitybox)
        self.addtransbtn.setObjectName("addtransbtn")
        sizePolicy4.setHeightForWidth(self.addtransbtn.sizePolicy().hasHeightForWidth())
        self.addtransbtn.setSizePolicy(sizePolicy4)
        self.addtransbtn.setMinimumSize(QSize(90, 34))
        self.addtransbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addtransbtn.setAutoFillBackground(False)
        self.addtransbtn.setStyleSheet(
            "\n"
            "\n"
            "\n"
            "QPushButton {\n"
            "	\n"
            "	\n"
            "	\n"
            "	color: rgb(245, 245, 245);\n"
            "	background-color: rgb(167, 83, 115);\n"
            "	\n"
            "border-color: rgb(244, 212, 212);\n"
            "text-align: center;\n"
            " font-size: 10px;\n"
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
        self.addtransbtn.setCheckable(True)
        self.addtransbtn.setFlat(True)
        self.addtransbtn.clicked.connect(self.add_entry)

        self.horizontalLayout_7.addWidget(self.addtransbtn)

        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(15, 15, 15, 15)
        self.tablebox = QGroupBox(self.activitybox)
        self.tablebox.setObjectName("tablebox")
        sizePolicy.setHeightForWidth(self.tablebox.sizePolicy().hasHeightForWidth())
        self.tablebox.setSizePolicy(sizePolicy)
        self.tablebox.setMaximumSize(QSize(16777215, 291))
        self.tablebox.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius:15\n" ""
        )

        self.verticalLayout_14 = QVBoxLayout(self.tablebox)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.activities = QTableView(self.tablebox)
        self.activities.setObjectName("activities")
        sizePolicy.setHeightForWidth(self.activities.sizePolicy().hasHeightForWidth())
        self.activities.setSizePolicy(sizePolicy)
        self.activities.horizontalHeader().setCascadingSectionResizes(True)
        self.activities.horizontalHeader().setDefaultSectionSize(120)
        self.activities = QTableView()
        self.model = QStandardItemModel()

        self.model.setHorizontalHeaderLabels(
            ["Date", "Amount", "Description", "Category"]
        )

        self.activities.setModel(self.model)
        self.activities.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.activities.verticalHeader().setVisible(False)
        self.activities.setAlternatingRowColors(True)
        self.activities.setShowGrid(False)

        self.activities.setStyleSheet(
            "QTableView {\n"
            "    background-color: #ffffff;\n"
            "    alternate-background-color: #f2f2f2;\n"
            "    gridline-color: #d9d9d9;\n"
            "    selection-background-color: #cce6ff;\n"
            "    selection-color: #003366;\n"
            '    font: 12pt "Segoe UI";\n'
            "    border-radius: 15px;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    background-color: transparent;\n"
            "    padding: 5px;\n"
            "    border: 1px solid #ccc;\n"
            "}\n"
            "QTableView::item {\n"
            "    padding: 5px;\n"
            "}\n"
        )

        self.verticalLayout_14.addWidget(self.activities)

        self.verticalLayout_15.addWidget(self.tablebox)

        self.verticalLayout_10.addLayout(self.verticalLayout_15)

        self.verticalLayout_9.addWidget(self.activitybox)

        self.verticalLayout_26.addLayout(self.verticalLayout_9)

        self.scrollArea_1.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_2.addWidget(self.scrollArea_1)

        self.tab.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.page_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 15, 10, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(120)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, 10)
        self.incomebox_33 = QGroupBox(self.page_2)
        self.incomebox_33.setObjectName("incomebox_33")
        self.incomebox_33.setMinimumSize(QSize(720, 70))
        self.incomebox_33.setMaximumSize(QSize(700, 70))
        self.incomebox_33.setStyleSheet(
            "background-color: rgb(167, 83, 115);\n" "border-radius:20\n" ""
        )
        self.verticalLayout_17 = QVBoxLayout(self.incomebox_33)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(15, -1, 20, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_12 = QComboBox(self.incomebox_33)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.setStyleSheet(
            "QComboBox{\n"
            "	color: rgb(167, 83, 115);\n"
            "	alternate-background-color: rgb(240, 240, 240);\n"
            "				\n"
            "	background-color: rgb(254, 250, 250);\n"
            "                padding: 8px;\n"
            "                border: 1px solid #ccc;\n"
            "                border-radius: 7px;\n"
            "                font-size: 10px;\n"
            "\n"
            "\n"
            "            }\n"
            "\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    border: none;\n"
            "    background: transparent;\n"
            "}"
        )
        self.comboBox_12.setEditable(False)
        self.comboBox_12.setFrame(True)

        self.horizontalLayout.addWidget(self.comboBox_12)

        self.comboBox_13 = QComboBox(self.incomebox_33)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.setStyleSheet(
            "QComboBox{\n"
            "	color: rgb(167, 83, 115);\n"
            "	alternate-background-color: rgb(240, 240, 240);\n"
            "				\n"
            "	background-color: rgb(254, 250, 250);\n"
            "                padding: 8px;\n"
            "                border: 1px solid #ccc;\n"
            "                border-radius: 7px;\n"
            "                font-size: 10px;\n"
            "\n"
            "\n"
            "            }\n"
            "\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    border: none;\n"
            "    background: transparent;\n"
            "}"
        )
        self.comboBox_13.setEditable(False)
        self.comboBox_13.setFrame(True)

        self.horizontalLayout.addWidget(self.comboBox_13)

        self.editbudgetbtn_10 = QPushButton(self.incomebox_33)
        self.editbudgetbtn_10.setObjectName("editbudgetbtn_10")
        sizePolicy.setHeightForWidth(
            self.editbudgetbtn_10.sizePolicy().hasHeightForWidth()
        )
        self.editbudgetbtn_10.setSizePolicy(sizePolicy)
        self.editbudgetbtn_10.setMaximumSize(QSize(70, 34))
        self.editbudgetbtn_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.editbudgetbtn_10.setAutoFillBackground(False)
        self.editbudgetbtn_10.setStyleSheet(
            "\n"
            "\n"
            "\n"
            "QPushButton {\n"
            "	background-color: rgb(108, 68, 100);\n"
            "	color: rgb(254, 250, 250);\n"
            "border-color: rgb(244, 212, 212);\n"
            "text-align: center;\n"
            " font-size: 10px;\n"
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
        self.editbudgetbtn_10.setCheckable(True)
        self.editbudgetbtn_10.setFlat(True)

        self.horizontalLayout.addWidget(self.editbudgetbtn_10)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(30, -1, 10, -1)
        self.greetuser_15 = QLabel(self.incomebox_33)
        self.greetuser_15.setObjectName("greetuser_15")
        sizePolicy1.setHeightForWidth(
            self.greetuser_15.sizePolicy().hasHeightForWidth()
        )
        self.greetuser_15.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies(["Inter"])
        font3.setWeight(QFont.DemiBold)
        font3.setItalic(False)
        self.greetuser_15.setFont(font3)
        self.greetuser_15.setStyleSheet(
            "\n"
            "color: rgb(254, 250, 250);\n"
            'font: 600 30px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.greetuser_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.greetuser_15)

        self.horizontalLayout.addLayout(self.verticalLayout_18)

        self.verticalLayout_17.addLayout(self.horizontalLayout)

        self.horizontalLayout_5.addWidget(self.incomebox_33)

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.scrollArea_3 = QScrollArea(self.page_2)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollArea_3.setStyleSheet(
            "background-color: transparent;\n" "border-radius: 10;\n" "border: none;"
        )
        self.scrollArea_3.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 166, 540))
        self.scrollAreaWidgetContents_2.setStyleSheet("border-radius:15")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(0, 500))
        self.groupBox_7.setStyleSheet(
            "background-color: rgb(254, 250, 250);\n" "border-radius: 25"
        )
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.incomebox_37 = QGroupBox(self.groupBox_7)
        self.incomebox_37.setObjectName("incomebox_37")
        self.incomebox_37.setMinimumSize(QSize(0, 200))
        self.incomebox_37.setMaximumSize(QSize(16777215, 500))
        self.incomebox_37.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border-color: rgb(229, 229, 229);\n"
            "border-radius:20;\n"
            "border: 1px solid\n"
            ""
        )
        self.verticalLayout_22 = QVBoxLayout(self.incomebox_37)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(15, -1, 20, -1)
        self.tableWidget = QTableWidget(self.incomebox_37)
        if self.tableWidget.columnCount() < 4:
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if self.tableWidget.rowCount() < 5:
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        self.tableWidget.setObjectName("tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_22.addWidget(self.tableWidget)

        self.verticalLayout_23.addWidget(self.incomebox_37)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.incomebox_35 = QGroupBox(self.groupBox_7)
        self.incomebox_35.setObjectName("incomebox_35")
        self.incomebox_35.setMinimumSize(QSize(0, 200))
        self.incomebox_35.setStyleSheet(
            "background-color: rgb(167, 83, 115);\n" "border-radius:20\n" ""
        )
        self.verticalLayout_20 = QVBoxLayout(self.incomebox_35)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(15, -1, 20, -1)

        self.horizontalLayout_10.addWidget(self.incomebox_35)

        self.incomebox_36 = QGroupBox(self.groupBox_7)
        self.incomebox_36.setObjectName("incomebox_36")
        self.incomebox_36.setMinimumSize(QSize(0, 200))
        self.incomebox_36.setStyleSheet(
            "background-color: rgb(167, 83, 115);\n" "border-radius:20\n" ""
        )
        self.verticalLayout_21 = QVBoxLayout(self.incomebox_36)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(15, -1, 20, -1)

        self.horizontalLayout_10.addWidget(self.incomebox_36)

        self.verticalLayout_23.addLayout(self.horizontalLayout_10)

        self.verticalLayout_6.addWidget(self.groupBox_7)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.scrollArea_3)

        self.verticalLayout_5.addLayout(self.verticalLayout_8)

        self.tab.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.page_3.setStyleSheet("")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.greetuser_12 = QLabel(self.page_3)
        self.greetuser_12.setObjectName("greetuser_12")
        sizePolicy1.setHeightForWidth(
            self.greetuser_12.sizePolicy().hasHeightForWidth()
        )
        self.greetuser_12.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamilies(["Inter"])
        font4.setPointSize(30)
        font4.setBold(True)
        font4.setItalic(False)
        self.greetuser_12.setFont(font4)
        self.greetuser_12.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 30pt "Inter";\n'
            "background-color: transparent\n"
            ""
        )

        self.verticalLayout_12.addWidget(self.greetuser_12)

        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet(
            "\n"
            "QScrollArea{\n"
            "border: none;}\n"
            "\n"
            "QScrollBar:vertical {\n"
            "    \n"
            "    background-color: rgb(245, 245, 245);\n"
            "    width: 5px;\n"
            "    margin: 0px 0px 0px 0px;\n"
            "	border: none\n"
            "	\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "    background: rgb(80, 51, 74);\n"
            "    min-height: 20px;\n"
            "    border-radius: 10000px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical,\n"
            "QScrollBar::sub-line:vertical {\n"
            "    background: none;\n"
            "    height: 0px;\n"
            "}\n"
            ""
        )
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 669, 826))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(25, -1, 20, -1)
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(300, 247))
        self.groupBox_2.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 15"
        )

        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(300, 247))
        self.groupBox_3.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 15"
        )

        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(25, -1, 20, -1)
        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(300, 247))
        self.groupBox_4.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 15"
        )

        self.horizontalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName("groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMinimumSize(QSize(300, 247))
        self.groupBox_6.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 15"
        )

        self.horizontalLayout_3.addWidget(self.groupBox_6)

        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(25, -1, 20, 50)
        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(300, 247))
        self.groupBox_5.setMaximumSize(QSize(800, 247))
        self.groupBox_5.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 15"
        )

        self.horizontalLayout_4.addWidget(self.groupBox_5)

        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.tab.addWidget(self.page_3)

        self.verticalLayout_4.addWidget(self.tab)

        self.horizontalLayout_6.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    def add_entry(self):
        amount = self.amountedit.text().strip()
        description = self.descriptionedit.text().strip()
        category = self.categorycombo.currentText()
        current_datetime = QDate.currentDate().toString("yyyy-MM-dd")

        if not amount.isdigit():
            print("Invalid input")
            return

        # Add to table
        row = [
            QStandardItem(current_datetime),
            QStandardItem(amount),
            QStandardItem(description),
            QStandardItem(category),
        ]
        # Append row directly since row already contains QStandardItems
        for item in row:
            item.setTextAlignment(Qt.AlignCenter)
        self.model.appendRow(row)

        # Clear inputs
        self.amountedit.clear()
        self.descriptionedit.clear()
        self.categorycombo.setCurrentIndex(0)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.sidebar.setTitle("")
        self.logo.setText(QCoreApplication.translate("MainWindow", "BudgeIT", None))
        self.homebtn.setText(
            QCoreApplication.translate("MainWindow", "   Dashboard", None)
        )
        self.analyticsbtn.setText(
            QCoreApplication.translate("MainWindow", "   Analytics", None)
        )
        self.reportbtn.setText(
            QCoreApplication.translate("MainWindow", "   Reports", None)
        )
        self.logoutbtn.setText(
            QCoreApplication.translate("MainWindow", "   Logout", None)
        )
        self.greethello.setText(
            QCoreApplication.translate("MainWindow", "Hello,", None)
        )
        self.user.setText(QCoreApplication.translate("MainWindow", "Oscar Pol", None))
        self.totalbudgetbox_2.setTitle("")
        self.totalbudgetlbl_3.setText(
            QCoreApplication.translate("MainWindow", "Current budget", None)
        )
        self.budgetvalue_3.setText(
            QCoreApplication.translate("MainWindow", "\u20b1 54300.00", None)
        )
        self.viewcategorylbl_4.setText(
            QCoreApplication.translate("MainWindow", "View Category", None)
        )
        self.totalbudgetbox_3.setTitle("")
        self.totalbudgetlbl_4.setText(
            QCoreApplication.translate("MainWindow", "Savings", None)
        )
        self.budgetvalue_4.setText(
            QCoreApplication.translate("MainWindow", "\u20b1 34500.00", None)
        )
        self.viewcategorylbl_5.setText(
            QCoreApplication.translate("MainWindow", "View Category", None)
        )
        self.savingsbox.setTitle("")
        self.incomevalue_3.setText(
            QCoreApplication.translate("MainWindow", "\u20b1 54420.00", None)
        )
        self.savingslbl.setText(
            QCoreApplication.translate("MainWindow", "Total expense", None)
        )
        self.incomebox.setTitle("")
        self.incomevalue_2.setText(
            QCoreApplication.translate("MainWindow", "\u20b1 54420.00", None)
        )
        self.incomlbl.setText(
            QCoreApplication.translate("MainWindow", "Total income", None)
        )
        self.activitybox.setTitle("")
        self.activitylbl.setText(
            QCoreApplication.translate("MainWindow", "Recent Activity", None)
        )
        self.amountedit.setText("")
        self.amountedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Amount", None)
        )
        self.descriptionedit.setText("")
        self.descriptionedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Description", None)
        )
        self.categorycombo.setItemText(
            0, QCoreApplication.translate("MainWindow", "Food", None)
        )
        self.categorycombo.setItemText(
            1, QCoreApplication.translate("MainWindow", "Utilities", None)
        )
        self.categorycombo.setItemText(
            2, QCoreApplication.translate("MainWindow", "Health & Wellness", None)
        )
        self.categorycombo.setItemText(
            3, QCoreApplication.translate("MainWindow", "Personal & Lifestyle", None)
        )
        self.categorycombo.setItemText(
            4, QCoreApplication.translate("MainWindow", "Education", None)
        )
        self.categorycombo.setItemText(
            5, QCoreApplication.translate("MainWindow", "Transportation", None)
        )
        self.categorycombo.setItemText(
            6, QCoreApplication.translate("MainWindow", "Others", None)
        )

        self.categorycombo.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Category", None)
        )
        self.addtransbtn.setText(
            QCoreApplication.translate("MainWindow", "Add Transaction", None)
        )
        self.tablebox.setTitle("")
        self.incomebox_33.setTitle("")
        self.comboBox_12.setItemText(
            0, QCoreApplication.translate("MainWindow", "January", None)
        )
        self.comboBox_12.setItemText(
            1, QCoreApplication.translate("MainWindow", "February", None)
        )

        self.comboBox_12.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Month", None)
        )
        self.comboBox_13.setItemText(
            0, QCoreApplication.translate("MainWindow", "Food", None)
        )
        self.comboBox_13.setItemText(
            1, QCoreApplication.translate("MainWindow", "Utilities", None)
        )
        self.comboBox_13.setItemText(
            2, QCoreApplication.translate("MainWindow", "Health & Wellness", None)
        )
        self.comboBox_13.setItemText(
            3, QCoreApplication.translate("MainWindow", "Personal & Lifestyle", None)
        )
        self.comboBox_13.setItemText(
            4, QCoreApplication.translate("MainWindow", "Education", None)
        )
        self.comboBox_13.setItemText(
            5, QCoreApplication.translate("MainWindow", "Transportation", None)
        )
        self.comboBox_13.setItemText(
            6, QCoreApplication.translate("MainWindow", "Others", None)
        )

        self.comboBox_13.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Year", None)
        )
        self.editbudgetbtn_10.setText(
            QCoreApplication.translate("MainWindow", "View", None)
        )
        self.greetuser_15.setText(
            QCoreApplication.translate("MainWindow", "Periodic Report", None)
        )
        self.groupBox_7.setTitle("")
        self.incomebox_37.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "New Column", None)
        )
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "New Column", None)
        )
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", "New Column", None)
        )
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", "New Column", None)
        )
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", "New Row", None)
        )
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", "New Row", None)
        )
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("MainWindow", "New Row", None)
        )
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", "New Row", None)
        )
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate("MainWindow", "New Row", None)
        )
        self.incomebox_35.setTitle("")
        self.incomebox_36.setTitle("")
        self.greetuser_12.setText(
            QCoreApplication.translate("MainWindow", "Analytics", None)
        )
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle("")
        self.groupBox_4.setTitle("")
        self.groupBox_6.setTitle("")
        self.groupBox_5.setTitle("")

    # retranslateUi


app = QApplication([])
window = Ui_MainWindow()
window.setupUi(window)
window.show()
app.exec()
