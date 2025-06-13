import os
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import assets.icons.icons_rc
import assets.images.images_rc
from addtransactions import AddTransactions
from components.budget_window import BudgetWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from components.datamanager import DataManager
from signoutwindow import SignOutWindow
from account_setup import AccountSetup
import sqlite3
from database_manager import *
from update_month_setup import UpdateMonthSetup
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from components.pesoquerymodel import PesoQueryModel


class BudgetApp(QMainWindow):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.connect = sqlite3.connect("accounts.db")
        self.cursor = self.connect.cursor()
        print("from budgetapp: user data", self.user_id)
        self.setupUi(self)
        self.setWindowTitle(" ")
        self.cursor.execute(
            "SELECT * FROM users WHERE user_id = ? AND account_setup = 0",
            (self.user_id,),
        )
        self.user_data = self.cursor.fetchone()

        self.account_setup = AccountSetup(
            self.user_id, datetime.today().strftime("%Y-%m")
        )
        self.account_setup.setup_completed.connect(self.refresh_data)
        if self.user_data:
            print("Account setup required")
            QTimer.singleShot(600, self.account_setup.show)

        else:
            print("Account already set up")
            self.refresh_data()

            if check_monthly_reset(self.user_id) == True:
                self.update_month_setup = UpdateMonthSetup(
                    self.user_id, datetime.today().strftime("%Y-%m")
                )
                self.update_month_setup.show()
        print("Now in main")

    def setupUi(self, MainWindow):
        print("from budgetapp setupUi: current user id", self.user_id)
        self.cursor.execute(
            "SELECT * FROM user_data WHERE user_id = ?", (self.user_id,)
        )
        self.user_data = self.cursor.fetchone()
        print(self.user_data)
        font_path = os.path.join(
            os.path.dirname(__file__), "assets", "fonts", "Inter.ttf"
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

        title_icon = QIcon()
        title_icon.addFile(":/logomin.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.setWindowIcon(title_icon)
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 640)
        MainWindow.setMinimumSize(QSize(1000, 640))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.sidebarlayout = QVBoxLayout()
        self.sidebarlayout.setObjectName("sidebarlayout")
        self.sidebarlayout.setContentsMargins(0, -1, 0, -1)
        self.sidebarwidget = QWidget(self.centralwidget)
        self.sidebarwidget.setObjectName("sidebarwidget")
        self.sidebarwidget.setMinimumSize(QSize(0, 0))
        self.sidebarwidget.setMaximumSize(QSize(500, 16777215))
        self.sidebarwidget.setStyleSheet(
            "QGroupBox {\n"
            "\n"
            "	background-color: rgb(43, 27, 40);\n"
            "}\n"
            "QToolButton {\n"
            "	\n"
            "    color: white;\n"
            "    \n"
            "	background-color: rgb(43, 27, 40);\n"
            "    border: none;\n"
            "    padding: 10px 18px;\n"
            "    text-align: left;\n"
            "   \n"
            '    font: 500 12px "Inter";\n'
            "    icon-size: 18px 18px;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "    qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 18px 18px;\n"
            " \n"
            "	color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 18px 18px;\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "    padding-left: 25px;\n"
            "}\n"
            "\n"
            "QToolButton:checked {\n"
            "qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 18px 18px;\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "}\n"
            "\n"
            "QToolButton:disabled {\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 24"
            "5, 245);\n"
            "}\n"
            ""
        )
        self.horizontalLayout_31 = QHBoxLayout(self.sidebarwidget)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.minsidebar = QWidget(self.sidebarwidget)
        self.minsidebar.setObjectName("minsidebar")
        self.minsidebar.setMinimumSize(QSize(70, 0))
        self.minsidebar.setMaximumSize(QSize(70, 16777215))
        self.minsidebar.setStyleSheet(
            "QWidget {\n"
            "\n"
            "	background-color: rgb(43, 27, 40);\n"
            "}\n"
            "QToolButton {\n"
            "	\n"
            "    color: white;\n"
            "    \n"
            "	background-color: rgb(43, 27, 40);\n"
            "    border: none;\n"
            "    padding: 10px 18px;\n"
            "    text-align: left;\n"
            "   \n"
            '    font: 500 12px "Inter";\n'
            "    icon-size: 18px 18px;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "    qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 18px 18px;\n"
            " \n"
            "	color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 18px 18px;\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "    padding-left: 25px;\n"
            "}\n"
            "\n"
            "QToolButton:checked {\n"
            "qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 18px 18px;\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "}\n"
            "\n"
            "QToolButton:disabled {\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 24"
            "5, 245);\n"
            "}\n"
            ""
        )
        self.verticalLayout_51 = QVBoxLayout(self.minsidebar)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.line = QFrame(self.minsidebar)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_52.addWidget(self.line)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName("verticalLayout_53")

        self.verticalLayout_52.addLayout(self.verticalLayout_53)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 15, 0, 15)
        self.minlogowidget = QWidget(self.minsidebar)
        self.minlogowidget.setObjectName("minlogowidget")
        self.horizontalLayout = QHBoxLayout(self.minlogowidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minlogo = QLabel(self.minlogowidget)
        self.minlogo.setObjectName("minlogo")
        self.minlogo.setMaximumSize(QSize(50, 40))
        self.minlogo.setPixmap(QPixmap(":/logomin.png"))
        self.minlogo.setScaledContents(True)
        self.minlogo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.minlogo)

        self.verticalLayout_54.addWidget(self.minlogowidget)

        self.verticalLayout_52.addLayout(self.verticalLayout_54)

        self.homebtn_min = QToolButton(self.minsidebar)
        self.homebtn_min.setObjectName("homebtn_min")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homebtn_min.sizePolicy().hasHeightForWidth())
        self.homebtn_min.setSizePolicy(sizePolicy)
        self.homebtn_min.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.homebtn_min.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(
            ":/icons/dashboardlight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        icon.addFile(
            ":/icons/dashboarddark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.homebtn_min.setIcon(icon)
        self.homebtn_min.setCheckable(True)
        self.homebtn_min.setChecked(True)
        self.homebtn_min.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.homebtn_min.setAutoRaise(False)
        self.homebtn_min.setArrowType(Qt.ArrowType.NoArrow)
        self.homebtn_min.clicked.connect(lambda: self.tab.setCurrentIndex(0))

        self.verticalLayout_52.addWidget(self.homebtn_min)

        self.analyticsbtn_min = QToolButton(self.minsidebar)
        self.analyticsbtn_min.setObjectName("analyticsbtn_min")
        sizePolicy.setHeightForWidth(
            self.analyticsbtn_min.sizePolicy().hasHeightForWidth()
        )
        self.analyticsbtn_min.setSizePolicy(sizePolicy)
        self.analyticsbtn_min.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(
            ":/icons/analyticslight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        icon1.addFile(
            ":/icons/analyticsdark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.analyticsbtn_min.setIcon(icon1)
        self.analyticsbtn_min.setCheckable(True)
        self.analyticsbtn_min.setChecked(False)
        self.analyticsbtn_min.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.analyticsbtn_min.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.analyticsbtn_min.clicked.connect(lambda: self.tab.setCurrentIndex(1))

        self.verticalLayout_52.addWidget(self.analyticsbtn_min)

        self.reportbtn_min = QToolButton(self.minsidebar)
        self.reportbtn_min.setObjectName("reportbtn_min")
        sizePolicy.setHeightForWidth(
            self.reportbtn_min.sizePolicy().hasHeightForWidth()
        )
        self.reportbtn_min.setSizePolicy(sizePolicy)
        self.reportbtn_min.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(
            ":/icons/monitoringlight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        icon2.addFile(
            ":/icons/monitoringdark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.reportbtn_min.setIcon(icon2)
        self.reportbtn_min.setCheckable(True)
        self.reportbtn_min.setChecked(False)
        self.reportbtn_min.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.reportbtn_min.clicked.connect(lambda: self.tab.setCurrentIndex(2))

        self.verticalLayout_52.addWidget(self.reportbtn_min)

        self.verticalSpacer_7 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_52.addItem(self.verticalSpacer_7)

        self.verticalLayout_51.addLayout(self.verticalLayout_52)

        self.horizontalLayout_31.addWidget(self.minsidebar)

        self.maxsidebar = QWidget(self.sidebarwidget)
        self.maxsidebar.setObjectName("maxsidebar")
        self.maxsidebar.setMinimumSize(QSize(170, 0))
        self.maxsidebar.setMaximumSize(QSize(500, 16777215))
        self.maxsidebar.setStyleSheet(
            "QWidget {\n"
            "\n"
            "	background-color: rgb(43, 27, 40);\n"
            "}\n"
            "QToolButton {\n"
            "	\n"
            "    color: white;\n"
            "    \n"
            "	background-color: rgb(43, 27, 40);\n"
            "    border: none;\n"
            "    padding: 10px 18px;\n"
            "    text-align: left;\n"
            "   \n"
            '    font: 500 12px "Inter";\n'
            "    icon-size: 18px 18px;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "    qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 18px 18px;\n"
            " \n"
            "	color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 18px 18px;\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "    padding-left: 25px;\n"
            "}\n"
            "\n"
            "QToolButton:checked {\n"
            "qproperty-icon: url(:/icons/home.svg);\n"
            "    qproperty-iconSize: 18px 18px;\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 245, 245);\n"
            "}\n"
            "\n"
            "QToolButton:disabled {\n"
            "    color: rgb(75, 47, 69);\n"
            "	background-color: rgb(245, 24"
            "5, 245);\n"
            "}\n"
            ""
        )
        self.verticalLayout_29 = QVBoxLayout(self.maxsidebar)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 15, 0, 15)
        self.maxlogowidget = QWidget(self.maxsidebar)
        self.maxlogowidget.setObjectName("maxlogowidget")
        self.horizontalLayout_2 = QHBoxLayout(self.maxlogowidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.maxlogo = QLabel(self.maxlogowidget)
        self.maxlogo.setObjectName("maxlogo")
        self.maxlogo.setMaximumSize(QSize(110, 40))
        self.maxlogo.setPixmap(QPixmap(":/logomax.png"))
        self.maxlogo.setScaledContents(True)
        self.maxlogo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.maxlogo)

        self.verticalLayout_50.addWidget(self.maxlogowidget)

        self.verticalLayout_30.addLayout(self.verticalLayout_50)

        self.homebtn = QToolButton(self.maxsidebar)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.homebtn)
        self.homebtn.setObjectName("homebtn")
        sizePolicy.setHeightForWidth(self.homebtn.sizePolicy().hasHeightForWidth())
        self.homebtn.setSizePolicy(sizePolicy)
        self.homebtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.homebtn.setAutoFillBackground(False)
        self.homebtn.setIcon(icon)
        self.homebtn.setCheckable(True)
        self.homebtn.setChecked(True)
        self.homebtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.homebtn.setAutoRaise(False)
        self.homebtn.setArrowType(Qt.ArrowType.NoArrow)
        self.homebtn.clicked.connect(lambda: self.tab.setCurrentIndex(0))

        self.verticalLayout_30.addWidget(self.homebtn)

        self.analyticsbtn = QToolButton(self.maxsidebar)
        self.buttonGroup.addButton(self.analyticsbtn)
        self.analyticsbtn.setObjectName("analyticsbtn")
        sizePolicy.setHeightForWidth(self.analyticsbtn.sizePolicy().hasHeightForWidth())
        self.analyticsbtn.setSizePolicy(sizePolicy)
        self.analyticsbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.analyticsbtn.setIcon(icon1)
        self.analyticsbtn.setCheckable(True)
        self.analyticsbtn.setChecked(False)
        self.analyticsbtn.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.analyticsbtn.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )
        self.analyticsbtn.clicked.connect(lambda: self.tab.setCurrentIndex(1))

        self.verticalLayout_30.addWidget(self.analyticsbtn)

        self.reportbtn = QToolButton(self.maxsidebar)
        self.buttonGroup.addButton(self.reportbtn)
        self.reportbtn.setObjectName("reportbtn")
        sizePolicy.setHeightForWidth(self.reportbtn.sizePolicy().hasHeightForWidth())
        self.reportbtn.setSizePolicy(sizePolicy)
        self.reportbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reportbtn.setIcon(icon2)
        self.reportbtn.setCheckable(True)
        self.reportbtn.setChecked(False)
        self.reportbtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.reportbtn.clicked.connect(lambda: self.tab.setCurrentIndex(2))

        self.verticalLayout_30.addWidget(self.reportbtn)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_30.addItem(self.verticalSpacer_2)

        self.logoutbtn = QToolButton(self.maxsidebar)
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
        self.logoutbtn.clicked.connect(lambda: self.signoutwindow())

        self.verticalLayout_30.addWidget(self.logoutbtn)

        self.verticalLayout_29.addLayout(self.verticalLayout_30)

        self.horizontalLayout_31.addWidget(self.maxsidebar)

        self.sidebarlayout.addWidget(self.sidebarwidget)

        self.horizontalLayout_6.addLayout(self.sidebarlayout)

        self.tabframe = QFrame(self.centralwidget)
        self.tabframe.setObjectName("tabframe")
        self.tabframe.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.verticalLayout_2 = QVBoxLayout(self.tabframe)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dashboardwidget = QWidget(self.tabframe)
        self.dashboardwidget.setObjectName("dashboardwidget")
        self.dashboardwidget.setMinimumSize(QSize(0, 40))
        self.dashboardwidget.setMaximumSize(QSize(16777215, 40))
        self.dashboardwidget.setStyleSheet(
            "QWidget{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px solid;\n"
            "	border-color: rgb(255, 255, 255);\n"
            "border-bottom-color: rgb(191, 191, 191)};"
        )
        self.horizontalLayout_24 = QHBoxLayout(self.dashboardwidget)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.menubtn = QToolButton(self.dashboardwidget)
        self.menubtn.setObjectName("menubtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menubtn.sizePolicy().hasHeightForWidth())
        self.menubtn.setSizePolicy(sizePolicy1)
        self.menubtn.setMinimumSize(QSize(25, 25))
        self.menubtn.setMaximumSize(QSize(20, 20))
        self.menubtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.menubtn.setAutoFillBackground(False)
        self.menubtn.clicked.connect(self.toggle_sidebar)
        self.menubtn.setStyleSheet(
            "QToolButton {\n"
            "	\n"
            "	\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid;\n"
            "	background-color: rgb(255, 255, 255);\n"
            "	border-color: rgb(213, 213, 213);\n"
            "   \n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "   \n"
            "	\n"
            "	background-color: rgb(245, 245, 245);\n"
            "}\n"
            "\n"
            "\n"
            ""
        )
        icon4 = QIcon()
        icon4.addFile(
            ":/icons/menudark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.menubtn.setIcon(icon4)
        self.menubtn.setIconSize(QSize(15, 15))
        self.menubtn.setCheckable(True)
        self.menubtn.setChecked(False)
        self.menubtn.setAutoExclusive(False)
        self.menubtn.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.menubtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        self.menubtn.setAutoRaise(False)

        self.horizontalLayout_16.addWidget(self.menubtn)

        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_24.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 6, -1, -1)
        self.menulabel = QLabel(self.dashboardwidget)
        self.menulabel.setObjectName("menulabel")
        sizePolicy1.setHeightForWidth(self.menulabel.sizePolicy().hasHeightForWidth())
        self.menulabel.setSizePolicy(sizePolicy1)
        Inter = QFont()
        Inter.setFamilies(["Inter"])
        Inter.setWeight(QFont.Medium)
        Inter.setItalic(False)
        self.menulabel.setFont(Inter)
        self.menulabel.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 500 14px "Inter";\n'
            "background-color: transparent;\n"
            "border: none;\n"
            ""
        )
        self.menulabel.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_17.addWidget(self.menulabel)

        self.horizontalLayout_24.addLayout(self.horizontalLayout_17)

        self.horizontalSpacer = QSpacerItem(
            554, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_24.addItem(self.horizontalSpacer)

        self.notificationsbtn = QToolButton(self.dashboardwidget)
        self.notificationsbtn.setObjectName("notificationsbtn")
        self.notificationsbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.notificationsbtn.setStyleSheet("border: none;")
        icon5 = QIcon()
        icon5.addFile(
            ":/icons/notificationdark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.notificationsbtn.setIcon(icon5)
        self.notificationsbtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.notificationsbtn)

        self.profilebtn = QToolButton(self.dashboardwidget)
        self.profilebtn.setObjectName("profilebtn")
        self.profilebtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.profilebtn.setStyleSheet("border: none;")
        icon6 = QIcon()
        icon6.addFile(
            ":/icons/profiledark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.profilebtn.setIcon(icon6)
        self.profilebtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.profilebtn)

        self.morebtn = QToolButton(self.dashboardwidget)
        self.morebtn.setObjectName("morebtn")
        self.morebtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.morebtn.setStyleSheet("border: none;")
        icon7 = QIcon()
        icon7.addFile(
            ":/icons/morepurple.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.morebtn.setIcon(icon7)
        self.morebtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.morebtn)
        self.verticalLayout.addWidget(self.dashboardwidget)

        # start of page 1
        self.tab = QStackedWidget(self.tabframe)
        self.tab.setObjectName("tab")
        self.page_1 = QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_3 = QVBoxLayout(self.page_1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page1_scrollarea = QScrollArea(self.page_1)
        self.page1_scrollarea.setObjectName("page1_scrollarea")
        self.page1_scrollarea.setStyleSheet(
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
            "    min-height: 18px;\n"
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
        self.page1_scrollarea.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.page1_scrollarea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.page1_scrollarea.setWidgetResizable(True)
        self.page1_scrollarea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_1 = QWidget()
        self.scrollAreaWidgetContents_1.setObjectName("scrollAreaWidgetContents_1")
        self.scrollAreaWidgetContents_1.setGeometry(QRect(0, 0, 760, 821))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_1)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(20, 15, 20, 15)
        self.greetlayout = QVBoxLayout()
        self.greetlayout.setSpacing(0)
        self.greetlayout.setObjectName("greetlayout")
        self.greetlayout.setContentsMargins(20, 0, -1, -1)
        self.greethello = QLabel(self.scrollAreaWidgetContents_1)
        self.greethello.setObjectName("greethello")
        self.greethello.setMinimumSize(QSize(0, 0))
        self.greethello.setStyleSheet(
            "color: rgb(212, 106, 146);\n"
            "background-color: transparent;\n"
            'font: 600 18px "Inter";'
        )

        self.greetlayout.addWidget(self.greethello)

        self.user = QLabel(self.scrollAreaWidgetContents_1)
        self.user.setObjectName("user")
        sizePolicy1.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy1)
        self.user.setFont(Inter)
        self.user.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 32px "Inter";\n'
            "background-color: transparent\n"
            ""
        )

        self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (self.user_id,))
        self.user_details = self.cursor.fetchone()
        self.user.setText(str(self.user_details[1]))

        self.user.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.greetlayout.addWidget(self.user)

        self.verticalLayout_26.addLayout(self.greetlayout)

        self.budgetsavingslayout = QHBoxLayout()
        self.budgetsavingslayout.setSpacing(10)
        self.budgetsavingslayout.setObjectName("budgetsavingslayout")
        self.budgetsavingslayout.setContentsMargins(-1, 0, -1, -1)
        self.totalbudgetbox = QGroupBox(self.scrollAreaWidgetContents_1)
        self.totalbudgetbox.setObjectName("totalbudgetbox")
        self.totalbudgetbox.setMinimumSize(QSize(300, 120))
        self.totalbudgetbox.setStyleSheet(
            "background-color: rgb(244, 212, 212);\n"
            "\n"
            "border-radius: 18px;\n"
            "\n"
            ""
        )
        self.verticalLayout_25 = QVBoxLayout(self.totalbudgetbox)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.layout_1 = QHBoxLayout()
        self.layout_1.setSpacing(0)
        self.layout_1.setObjectName("layout_1")
        self.layout_1.setContentsMargins(20, 10, -1, -1)
        self.totalbudgetlbl = QLabel(self.totalbudgetbox)
        self.totalbudgetlbl.setObjectName("totalbudgetlbl")
        self.totalbudgetlbl.setMinimumSize(QSize(0, 30))
        self.totalbudgetlbl.setMaximumSize(QSize(16777215, 25))
        self.totalbudgetlbl.setStyleSheet(
            "color: rgb(108, 68, 100);\n" 'font: 600 14px "Inter";'
        )
        self.totalbudgetlbl.setTextFormat(Qt.TextFormat.MarkdownText)
        self.totalbudgetlbl.setScaledContents(False)
        self.totalbudgetlbl.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.totalbudgetlbl.setIndent(0)

        self.layout_1.addWidget(self.totalbudgetlbl)

        self.verticalLayout_25.addLayout(self.layout_1)

        self.layout_2 = QHBoxLayout()
        self.layout_2.setObjectName("layout_2")
        self.layout_2.setContentsMargins(-1, 15, -1, -1)
        self.budgetvalue = QLabel(self.totalbudgetbox)
        self.budgetvalue.setObjectName("budgetvalue")
        font2 = QFont()
        font2.setFamilies(["Inter"])
        font2.setBold(True)
        font2.setItalic(False)
        self.budgetvalue.setFont(font2)
        self.budgetvalue.setStyleSheet(
            "color: rgb(167, 83, 115);\n"
            "background:transparent;\n"
            'font: 700 32px "Inter";\n'
            ""
        )

        self.budgetvalue.setFrameShape(QFrame.Shape.NoFrame)
        self.budgetvalue.setFrameShadow(QFrame.Shadow.Sunken)
        self.budgetvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.budgetvalue.setText(f"₱{self.user_data[4]:,.2f}")

        self.layout_2.addWidget(self.budgetvalue)

        self.verticalLayout_25.addLayout(self.layout_2)

        self.layout_3 = QHBoxLayout()
        self.layout_3.setSpacing(20)
        self.layout_3.setObjectName("layout_3")
        self.layout_3.setContentsMargins(20, -1, -1, -1)
        self.progressBar = QProgressBar(self.totalbudgetbox)
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
        self.progressBar.setValue(70)
        self.progressBar.setTextVisible(False)

        self.layout_3.addWidget(self.progressBar)

        self.viewcategorybtn = QToolButton(self.totalbudgetbox)
        self.viewcategorybtn.setObjectName("viewcategorybtn")
        self.viewcategorybtn.setMinimumSize(QSize(50, 50))
        self.viewcategorybtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.viewcategorybtn.setAutoFillBackground(False)
        self.viewcategorybtn.clicked.connect(lambda: self.budget_window())
        self.viewcategorybtn.setStyleSheet(
            "\n"
            "QToolButton {\n"
            "background: qradialgradient(\n"
            "            cx: 0.5, cy: 0.5, radius: 0.6,\n"
            "            fx: 0.5, fy: 0.5,\n"
            "		stop: 0 #6c4464\n"
            "        stop: 1 #a75373\n"
            "    );\n"
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
        icon8 = QIcon()

        icon8.addFile(
            ":/icons/walletlight.svg", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.viewcategorybtn.setIcon(icon8)
        self.viewcategorybtn.setIconSize(QSize(20, 20))
        self.viewcategorybtn.setCheckable(False)

        self.layout_3.addWidget(self.viewcategorybtn)

        self.verticalLayout_25.addLayout(self.layout_3)

        self.budgetsavingslayout.addWidget(self.totalbudgetbox)

        self.savingsbox_3 = QGroupBox(self.scrollAreaWidgetContents_1)
        self.savingsbox_3.setObjectName("savingsbox_3")
        self.savingsbox_3.setMinimumSize(QSize(300, 120))
        self.savingsbox_3.setStyleSheet(
            "background-color: rgb(244, 212, 212);\n" "border-radius:18px;\n" "\n" ""
        )
        self.verticalLayout_28 = QVBoxLayout(self.savingsbox_3)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.layout_5 = QHBoxLayout()
        self.layout_5.setSpacing(0)
        self.layout_5.setObjectName("layout_5")
        self.layout_5.setContentsMargins(-1, 10, -1, -1)
        self.savingslbl = QLabel(self.savingsbox_3)
        self.savingslbl.setObjectName("savingslbl")
        self.savingslbl.setMinimumSize(QSize(0, 30))
        self.savingslbl.setMaximumSize(QSize(16777215, 25))
        self.savingslbl.setStyleSheet(
            "color: rgb(108, 68, 100);\n" 'font: 600 14px "Inter";'
        )
        self.savingslbl.setTextFormat(Qt.TextFormat.MarkdownText)
        self.savingslbl.setScaledContents(False)
        self.savingslbl.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.savingslbl.setIndent(20)

        self.layout_5.addWidget(self.savingslbl)

        self.verticalLayout_28.addLayout(self.layout_5)

        self.layout_6 = QHBoxLayout()
        self.layout_6.setObjectName("layout_6")
        self.layout_6.setContentsMargins(-1, 15, -1, -1)
        self.savingsvalue = QLabel(self.savingsbox_3)
        self.savingsvalue.setObjectName("savingsvalue")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.savingsvalue.sizePolicy().hasHeightForWidth()
        )
        self.savingsvalue.setSizePolicy(sizePolicy3)
        self.savingsvalue.setFont(font2)
        self.savingsvalue.setStyleSheet(
            "color: rgb(212, 106, 146);\n"
            "background-color: transparent;\n"
            'font: 700 32px "Inter";\n'
            ""
        )

        self.savingsvalue.setFrameShape(QFrame.Shape.NoFrame)
        self.savingsvalue.setFrameShadow(QFrame.Shadow.Sunken)
        self.savingsvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.savingsvalue.setWordWrap(True)
        self.savingsvalue.setText(f"₱{self.user_data[2]:,.2f}")

        self.layout_6.addWidget(self.savingsvalue)

        self.verticalLayout_28.addLayout(self.layout_6)

        self.hlayout7 = QHBoxLayout()
        self.hlayout7.setObjectName("hlayout7")
        self.hlayout7.setContentsMargins(20, -1, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.hlayout7.addItem(self.horizontalSpacer_2)
        self.savingsbtn = QToolButton(self.savingsbox_3)
        self.savingsbtn.setObjectName("savingsbtn")
        self.savingsbtn.setMinimumSize(QSize(50, 50))
        self.savingsbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.savingsbtn.setAutoFillBackground(False)

        self.savingsbtn.setStyleSheet(
            "QToolButton{\n"
            "\n"
            "background: qradialgradient(\n"
            "cx: 0.5, cy: 0.5, radius: 0.6,\n"
            "fx: 0.5, fy: 0.5,\n"
            "		stop: 0 #a75373\n"
            "        stop: 1 #d46a92\n"
            "    );\n"
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
        icon9 = QIcon()
        icon9.addFile(
            ":/icons/savingslight.svg", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.savingsbtn.setIcon(icon9)
        self.savingsbtn.setIconSize(QSize(20, 20))
        self.savingsbtn.setCheckable(False)

        self.hlayout7.addWidget(self.savingsbtn)

        self.verticalLayout_28.addLayout(self.hlayout7)

        self.budgetsavingslayout.addWidget(self.savingsbox_3)

        self.verticalLayout_26.addLayout(self.budgetsavingslayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 10, 0, 10)
        self.expensebox = QGroupBox(self.scrollAreaWidgetContents_1)
        self.expensebox.setObjectName("expensebox")
        self.expensebox.setMinimumSize(QSize(300, 80))
        font3 = QFont()
        font3.setPointSize(12)
        self.expensebox.setFont(font3)
        self.expensebox.setStyleSheet(
            "text-align: center;\n"
            "background-color: rgb(167, 83, 115);\n"
            "border-radius: 18px"
        )
        self.verticalLayout_31 = QVBoxLayout(self.expensebox)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(40, -1, 30, 0)
        self.expensevalue = QLabel(self.expensebox)
        self.expensevalue.setObjectName("expensevalue")
        sizePolicy.setHeightForWidth(self.expensevalue.sizePolicy().hasHeightForWidth())
        self.expensevalue.setSizePolicy(sizePolicy)
        self.expensevalue.setMaximumSize(QSize(16777215, 50))
        self.expensevalue.setFont(font2)
        self.expensevalue.setStyleSheet(
            "color: rgb(250, 250, 250);\n" 'font: 700 18px "Inter";\n' ""
        )
        self.expensevalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.expensevalue.setWordWrap(False)
        self.expensevalue.setText(f"₱{self.user_data[3]:,.2f}")

        self.horizontalLayout_9.addWidget(self.expensevalue)

        self.expenselbl = QLabel(self.expensebox)
        self.expenselbl.setObjectName("expenselbl")
        self.expenselbl.setMaximumSize(QSize(16777215, 50))
        self.expenselbl.setWordWrap(True)
        self.expenselbl.setStyleSheet(
            "color: rgb(250, 250, 250);\n"
            'font: 600 14px "Inter";\n'
            "text-align: center;"
        )
        self.expenselbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.expenselbl)

        self.verticalLayout_31.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8.addWidget(self.expensebox)

        self.incomebox = QGroupBox(self.scrollAreaWidgetContents_1)
        self.incomebox.setObjectName("incomebox")
        self.incomebox.setMinimumSize(QSize(300, 80))
        self.incomebox.setFont(font3)
        self.incomebox.setStyleSheet(
            "text-align: center;\n"
            "background-color: rgb(167, 83, 115);\n"
            "border-radius: 18px"
        )
        self.verticalLayout_55 = QVBoxLayout(self.incomebox)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(40, -1, 30, 0)
        self.incomevalue = QLabel(self.incomebox)
        self.incomevalue.setObjectName("incomevalue")
        sizePolicy.setHeightForWidth(self.incomevalue.sizePolicy().hasHeightForWidth())
        self.incomevalue.setSizePolicy(sizePolicy)
        self.incomevalue.setMaximumSize(QSize(16777215, 50))
        self.incomevalue.setFont(font2)
        self.incomevalue.setStyleSheet(
            "color: rgb(250, 250, 250);\n" 'font: 700 18px "Inter";\n' ""
        )

        self.incomevalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.incomevalue.setWordWrap(False)
        self.incomevalue.setText(f"₱{self.user_data[4]:,.2f}")

        self.horizontalLayout_12.addWidget(self.incomevalue)

        self.incomelbl = QLabel(self.incomebox)
        self.incomelbl.setObjectName("incomelbl")
        self.incomelbl.setMaximumSize(QSize(16777215, 50))
        self.incomelbl.setWordWrap(True)
        self.incomelbl.setStyleSheet(
            "color: rgb(250, 250, 250);\n"
            'font: 600 14px "Inter";\n'
            "text-align: center;"
        )
        self.incomelbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.incomelbl)

        self.verticalLayout_55.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_8.addWidget(self.incomebox)

        self.verticalLayout_26.addLayout(self.horizontalLayout_8)

        self.activitylayout = QVBoxLayout()
        self.activitylayout.setObjectName("activitylayout")
        self.activitylayout.setContentsMargins(0, 10, 0, 10)
        self.activitybox = QGroupBox(self.scrollAreaWidgetContents_1)
        self.activitybox.setObjectName("activitybox")
        self.activitybox.setMinimumSize(QSize(0, 381))
        self.activitybox.setStyleSheet(
            "background-color: rgb(108, 68, 100);\n" "border-radius:20\n" ""
        )

        self.verticalLayout_10 = QVBoxLayout(self.activitybox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, 15, 20, -1)
        self.activitylbl = QLabel(self.activitybox)
        self.activitylbl.setObjectName("activitylbl")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.activitylbl.sizePolicy().hasHeightForWidth())
        self.activitylbl.setSizePolicy(sizePolicy4)
        self.activitylbl.setFont(Inter)
        self.activitylbl.setStyleSheet(
            "color: rgb(254, 250, 250);\n" 'font: 700 32px "Inter";'
        )

        self.horizontalLayout_13.addWidget(self.activitylbl)

        self.amountedit = QLineEdit(self.activitybox)
        self.amountedit.setObjectName("amountedit")
        sizePolicy5 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.amountedit.sizePolicy().hasHeightForWidth())
        self.amountedit.setSizePolicy(sizePolicy5)
        self.amountedit.setStyleSheet(
            "QLineEdit {\n"
            "	background-color: rgb(254, 250, 250);\n"
            "                padding: 8px;\n"
            "                border: 1px solid #ccc;\n"
            "                border-radius: 7px;\n"
            "                font-size: 10px;\n"
            "color: rgb(167, 83, 115);\n"
            "font-weight: bold\n"
            "            }"
        )

        self.horizontalLayout_13.addWidget(self.amountedit)

        self.descriptionedit = QLineEdit(self.activitybox)
        self.descriptionedit.setObjectName("descriptionedit")
        sizePolicy5.setHeightForWidth(
            self.descriptionedit.sizePolicy().hasHeightForWidth()
        )
        self.descriptionedit.setSizePolicy(sizePolicy5)
        self.descriptionedit.setStyleSheet(
            "QLineEdit {\n"
            "	\n"
            "	\n"
            "					background-color: rgb(254, 250, 250);\n"
            "                padding: 8px;\n"
            "                border: 1px solid #ccc;\n"
            "                border-radius: 7px;\n"
            "                font-size: 10px;\n"
            "				color: rgb(167, 83, 115);\n"
            "font-weight:bold;\n"
            "\n"
            "            }\n"
            ""
        )

        self.horizontalLayout_13.addWidget(self.descriptionedit)

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
        sizePolicy5.setHeightForWidth(
            self.categorycombo.sizePolicy().hasHeightForWidth()
        )
        self.categorycombo.setSizePolicy(sizePolicy5)
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
            "QComboBox::drop-down {\n"
            "    border: none;\n"
            "    background: transparent;\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "            background-color: #ffffff;\n"
            "            color: #000000; \n"
            "            }"
        )
        self.categorycombo.setEditable(False)
        self.categorycombo.setFrame(True)

        self.horizontalLayout_13.addWidget(self.categorycombo)

        self.addtransbtn = QPushButton(self.activitybox)
        self.addtransbtn.setObjectName("addtransbtn")
        sizePolicy5.setHeightForWidth(self.addtransbtn.sizePolicy().hasHeightForWidth())
        self.addtransbtn.setSizePolicy(sizePolicy5)
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
            "	border: 1px solid #ccc;\n"
            "    border-radius: 7px;\n"
            "	border-color: rgb(144, 72, 99);\n"
            "text-align: center;\n"
            " font-size: 10px;\n"
            "\n"
            "\n"
            "  \n"
            "\n"
            "}\n"
            "QPushButton:hover {\n"
            "\n"
            "	\n"
            "	background-color: rgb(138, 69, 95);\n"
            "	\n"
            "   \n"
            "}"
        )
        self.addtransbtn.setCheckable(True)
        self.addtransbtn.setFlat(True)
        self.addtransbtn.clicked.connect(lambda: self.handle_add_transaction())

        self.horizontalLayout_13.addWidget(self.addtransbtn)

        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.tablelayout = QVBoxLayout()
        self.tablelayout.setObjectName("tablelayout")
        self.tablelayout.setContentsMargins(15, 15, 15, 15)
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

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("accounts.db")

        if not self.db.open():
            print("Failed to open database")
            sys.exit(-1)

        self.activities_model = PesoQueryModel()
        self.activities_model.setQuery(
            """
            SELECT transaction_date, amount, description, category
            FROM transactions
            ORDER BY data_id DESC
        """
        )

        self.activities_model.setHeaderData(0, Qt.Horizontal, "Date")
        self.activities_model.setHeaderData(1, Qt.Horizontal, "Amount")
        self.activities_model.setHeaderData(2, Qt.Horizontal, "Description")
        self.activities_model.setHeaderData(3, Qt.Horizontal, "Category")

        self.activities.setModel(self.activities_model)
        self.activities.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.activities.verticalHeader().setVisible(False)
        self.activities.verticalHeader().setDefaultSectionSize(40)
        self.activities.setAlternatingRowColors(True)
        self.activities.setShowGrid(False)
        self.activities.setSelectionMode(QTableView.NoSelection)
        self.activities.setEditTriggers(QTableView.NoEditTriggers)
        self.activities.setFocusPolicy(Qt.NoFocus)
        self.activities.horizontalHeader().setFocusPolicy(Qt.NoFocus)
        self.activities.setStyleSheet(
            """QTableView {
    background-color: white;
    alternate-background-color: #f0f8ff; /* light blue */
    gridline-color: #dcdcdc;
    font: 300 12px "Inter";
    border: none;
}


QTableView::item:hover {
    background-color: #e0f7fa;  /* light cyan */
}



QTableView::item {
    padding: 8px;
    color: rgb(105, 104, 104);
    font: 900 12px "Inter";
}

QHeaderView::section {
    font: 500 12px "Inter";
    background-color: white;
    color: rgb(92, 91, 91);
    padding: 5px;
    border: 1px solid rgb(230, 230, 230);
    border-top: none;
    border-left: none;
    border-right: none;
}

"""
        )
        self.verticalLayout_14.addWidget(self.activities)
        self.tablelayout.addWidget(self.tablebox)
        self.verticalLayout_10.addLayout(self.tablelayout)
        self.activitylayout.addWidget(self.activitybox)
        self.verticalLayout_26.addLayout(self.activitylayout)
        self.page1_scrollarea.setWidget(self.scrollAreaWidgetContents_1)
        self.verticalLayout_3.addWidget(self.page1_scrollarea)
        self.tab.addWidget(self.page_1)

        # start of page 2
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.page_2.setStyleSheet("")
        self.verticalLayout_15 = QVBoxLayout(self.page_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.scrollArea_2 = QScrollArea(self.page_2)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setStyleSheet(
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
            "    min-height: 18px;\n"
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
        self.scrollArea_2.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn
        )
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 756, 707))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, -1, 10, 0)
        self.overallbudgetbox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.overallbudgetbox.setObjectName("overallbudgetbox")
        self.overallbudgetbox.setMinimumSize(QSize(300, 80))
        self.overallbudgetbox.setMaximumSize(QSize(16777215, 80))
        self.overallbudgetbox.setFont(Inter)
        self.overallbudgetbox.setStyleSheet(
            "text-align: center;\n"
            "background-color: rgb(167, 83, 115);\n"
            "border-radius: 18px"
        )
        self.verticalLayout_32 = QVBoxLayout(self.overallbudgetbox)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(20)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(40, -1, 30, 0)
        self.overallbudgetvalue = QLabel(self.overallbudgetbox)
        self.overallbudgetvalue.setObjectName("overallbudgetvalue")
        sizePolicy.setHeightForWidth(
            self.overallbudgetvalue.sizePolicy().hasHeightForWidth()
        )
        self.overallbudgetvalue.setSizePolicy(sizePolicy)
        self.overallbudgetvalue.setMaximumSize(QSize(16777215, 50))
        self.overallbudgetvalue.setFont(font3)
        self.overallbudgetvalue.setStyleSheet(
            "color: rgb(250, 250, 250);\n" 'font: 700 15px "Inter";\n' ""
        )
        self.overallbudgetvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overallbudgetvalue.setWordWrap(False)

        self.horizontalLayout_18.addWidget(self.overallbudgetvalue)

        self.overallbudgetlbl = QLabel(self.overallbudgetbox)
        self.overallbudgetlbl.setObjectName("overallbudgetlbl")
        self.overallbudgetlbl.setMaximumSize(QSize(16777215, 50))
        self.overallbudgetlbl.setStyleSheet(
            "color: rgb(250, 250, 250);\n"
            'font: 600 14px "Inter";\n'
            "text-align: center;"
        )
        self.overallbudgetlbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overallbudgetlbl.setWordWrap(True)

        self.horizontalLayout_18.addWidget(self.overallbudgetlbl)

        self.verticalLayout_32.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_14.addWidget(self.overallbudgetbox)

        self.expensebox_3 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.expensebox_3.setObjectName("expensebox_3")
        self.expensebox_3.setMinimumSize(QSize(300, 80))
        self.expensebox_3.setMaximumSize(QSize(16777215, 80))
        self.expensebox_3.setFont(Inter)
        self.expensebox_3.setStyleSheet(
            "text-align: center;\n"
            "background-color: rgb(167, 83, 115);\n"
            "border-radius: 18px"
        )
        self.verticalLayout_33 = QVBoxLayout(self.expensebox_3)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(20)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(40, -1, 30, 0)
        self.totalexpensevalue = QLabel(self.expensebox_3)
        self.totalexpensevalue.setObjectName("totalexpensevalue")
        sizePolicy.setHeightForWidth(
            self.totalexpensevalue.sizePolicy().hasHeightForWidth()
        )
        self.totalexpensevalue.setSizePolicy(sizePolicy)
        self.totalexpensevalue.setMaximumSize(QSize(16777215, 50))
        self.totalexpensevalue.setFont(font3)
        self.totalexpensevalue.setStyleSheet(
            "color: rgb(250, 250, 250);\n" 'font: 700 15px "Inter";\n' ""
        )
        self.totalexpensevalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalexpensevalue.setWordWrap(False)
        self.totalexpensevalue.setText(f"₱{self.user_data[6]:,.2f}")

        self.horizontalLayout_22.addWidget(self.totalexpensevalue)

        self.totalexpenselbl = QLabel(self.expensebox_3)
        self.totalexpenselbl.setObjectName("totalexpenselbl")
        self.totalexpenselbl.setMaximumSize(QSize(16777215, 50))
        self.totalexpenselbl.setStyleSheet(
            "color: rgb(250, 250, 250);\n"
            'font: 600 14px "Inter";\n'
            "text-align: center;"
        )
        self.totalexpenselbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalexpenselbl.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.totalexpenselbl)

        self.verticalLayout_33.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_14.addWidget(self.expensebox_3)

        self.verticalLayout_16.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(10, -1, 10, 10)
        self.accumulatedsavingsbox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.accumulatedsavingsbox.setObjectName("accumulatedsavingsbox")
        self.accumulatedsavingsbox.setMinimumSize(QSize(300, 80))
        self.accumulatedsavingsbox.setMaximumSize(QSize(16777215, 80))
        self.accumulatedsavingsbox.setFont(Inter)
        self.accumulatedsavingsbox.setStyleSheet(
            "text-align: center;\n" "background-color: #f4d4d4;\n" "border-radius: 18px"
        )
        self.verticalLayout_34 = QVBoxLayout(self.accumulatedsavingsbox)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(40, -1, 30, 0)
        self.accumulatedsavingvalue = QLabel(self.accumulatedsavingsbox)
        self.accumulatedsavingvalue.setObjectName("accumulatedsavingvalue")
        sizePolicy.setHeightForWidth(
            self.accumulatedsavingvalue.sizePolicy().hasHeightForWidth()
        )
        self.accumulatedsavingvalue.setSizePolicy(sizePolicy)
        self.accumulatedsavingvalue.setMaximumSize(QSize(16777215, 50))
        self.accumulatedsavingvalue.setFont(font3)
        self.accumulatedsavingvalue.setStyleSheet(
            "color: rgb(167, 83, 115);\n" 'font: 700 15px "Inter";\n' ""
        )
        self.accumulatedsavingvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.accumulatedsavingvalue.setWordWrap(False)

        self.horizontalLayout_23.addWidget(self.accumulatedsavingvalue)

        self.accumulatedsavingslbl = QLabel(self.accumulatedsavingsbox)
        self.accumulatedsavingslbl.setObjectName("accumulatedsavingslbl")
        self.accumulatedsavingslbl.setMaximumSize(QSize(16777215, 50))
        self.accumulatedsavingslbl.setStyleSheet(
            "color: rgb(167, 83, 115);\n"
            'font: 600 14px "Inter";\n'
            "text-align: center;"
        )
        self.accumulatedsavingslbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.accumulatedsavingslbl.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.accumulatedsavingslbl)

        self.verticalLayout_34.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_21.addWidget(self.accumulatedsavingsbox)

        self.totalincomebox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.totalincomebox.setObjectName("totalincomebox")
        self.totalincomebox.setMinimumSize(QSize(300, 80))
        self.totalincomebox.setMaximumSize(QSize(16777215, 80))
        self.totalincomebox.setFont(Inter)
        self.totalincomebox.setStyleSheet(
            "text-align: center;\n" "background-color: #f4d4d4;\n" "border-radius: 18px"
        )
        self.verticalLayout_35 = QVBoxLayout(self.totalincomebox)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(40, -1, 30, 0)
        self.totalincomevalue = QLabel(self.totalincomebox)
        self.totalincomevalue.setObjectName("totalincomevalue")
        sizePolicy.setHeightForWidth(
            self.totalincomevalue.sizePolicy().hasHeightForWidth()
        )
        self.totalincomevalue.setSizePolicy(sizePolicy)
        self.totalincomevalue.setMaximumSize(QSize(16777215, 50))
        self.totalincomevalue.setFont(font3)
        self.totalincomevalue.setStyleSheet(
            "color: rgb(166, 83, 115);\n" 'font: 700 15px "Inter";\n' ""
        )
        self.totalincomevalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalincomevalue.setWordWrap(False)

        self.horizontalLayout_25.addWidget(self.totalincomevalue)

        self.totalincomelbl = QLabel(self.totalincomebox)
        self.totalincomelbl.setObjectName("totalincomelbl")
        self.totalincomelbl.setMaximumSize(QSize(16777215, 50))
        self.totalincomelbl.setStyleSheet(
            "color: rgb(167, 83, 115);\n"
            'font: 600 14px "Inter";\n'
            "text-align: center;"
        )
        self.totalincomelbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalincomelbl.setWordWrap(True)

        self.horizontalLayout_25.addWidget(self.totalincomelbl)

        self.verticalLayout_35.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_21.addWidget(self.totalincomebox)

        self.verticalLayout_16.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, -1, 10, -1)
        self.transactionsummarybox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.transactionsummarybox.setObjectName("transactionsummarybox")
        sizePolicy.setHeightForWidth(
            self.transactionsummarybox.sizePolicy().hasHeightForWidth()
        )
        self.transactionsummarybox.setSizePolicy(sizePolicy)
        self.transactionsummarybox.setMinimumSize(QSize(300, 300))
        self.transactionsummarybox.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 15"
        )
        self.verticalLayout_12 = QVBoxLayout(self.transactionsummarybox)
        self.verticalLayout_12.setObjectName("verticalLayout_12")

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(10, 10, -1, -1)
        self.transactionsummary = QLabel(self.transactionsummarybox)
        self.transactionsummary.setObjectName("transactionsummary")
        sizePolicy1.setHeightForWidth(
            self.transactionsummary.sizePolicy().hasHeightForWidth()
        )
        self.transactionsummary.setSizePolicy(sizePolicy1)
        self.transactionsummary.setFont(Inter)
        self.transactionsummary.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 500 15px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.transactionsummary.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_30.addWidget(self.transactionsummary)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_30.addItem(self.horizontalSpacer_4)

        self.verticalLayout_12.addLayout(self.horizontalLayout_30)

        self.transactionsummarywidget = QWidget(self.transactionsummarybox)
        self.transactionsummarywidget.setObjectName("transactionsummarywidget")
        self.transactionsummarywidget.setMinimumSize(
            QSize(0, 250)
        )  # Set minimum height
        self.transactionsummarywidget.setStyleSheet(
            """
            QWidget {
                background-color: rgb(255, 255, 255);
                border: none;
            }
        """
        )
        self.horizontalLayout_transactionsummary = QHBoxLayout(
            self.transactionsummarywidget
        )
        self.horizontalLayout_transactionsummary.setObjectName(
            "horizontalLayout_transactionsummary"
        )
        self.horizontalLayout_transactionsummary.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.transactionsummarywidget)

        self.horizontalLayout_19.addWidget(self.transactionsummarybox)

        self.budgetsummarybox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.budgetsummarybox.setObjectName("budgetsummarybox")
        self.budgetsummarybox.setMinimumSize(QSize(300, 247))
        self.budgetsummarybox.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 15"
        )
        self.verticalLayout_13 = QVBoxLayout(self.budgetsummarybox)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(10, 10, -1, -1)
        self.budgetsummarylbl = QLabel(self.budgetsummarybox)
        self.budgetsummarylbl.setObjectName("budgetsummarylbl")
        sizePolicy1.setHeightForWidth(
            self.budgetsummarylbl.sizePolicy().hasHeightForWidth()
        )
        self.budgetsummarylbl.setSizePolicy(sizePolicy1)
        self.budgetsummarylbl.setFont(Inter)
        self.budgetsummarylbl.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 500 15px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.budgetsummarylbl.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_27.addWidget(self.budgetsummarylbl)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_27.addItem(self.horizontalSpacer_5)

        self.verticalLayout_13.addLayout(self.horizontalLayout_27)

        self.budgetsummarywidget = QWidget(self.budgetsummarybox)
        self.budgetsummarywidget.setObjectName("budgetsummarywidget")
        self.horizontalLayout_budgetsummary = QHBoxLayout(self.budgetsummarywidget)
        self.horizontalLayout_budgetsummary.setObjectName(
            "horizontalLayout_budgetsummary"
        )
        self.horizontalLayout_budgetsummary.setContentsMargins(0, 0, 0, 0)


        self.verticalLayout_13.addWidget(self.budgetsummarywidget)

        self.horizontalLayout_19.addWidget(self.budgetsummarybox)

        self.verticalLayout_16.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, -1, 10, -1)
        self.youractivitybox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.youractivitybox.setObjectName("youractivitybox")
        self.youractivitybox.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 15"
        )
        self.verticalLayout_18 = QVBoxLayout(self.youractivitybox)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(10, 10, -1, -1)
        self.youractivitylbl = QLabel(self.youractivitybox)
        self.youractivitylbl.setObjectName("youractivitylbl")
        sizePolicy1.setHeightForWidth(
            self.youractivitylbl.sizePolicy().hasHeightForWidth()
        )
        self.youractivitylbl.setSizePolicy(sizePolicy1)
        self.youractivitylbl.setFont(Inter)
        self.youractivitylbl.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 500 15px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.youractivitylbl.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_29.addWidget(self.youractivitylbl)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_29.addItem(self.horizontalSpacer_6)

        self.verticalLayout_18.addLayout(self.horizontalLayout_29)

        self.youractivitywidget = QWidget(self.youractivitybox)
        self.youractivitywidget.setObjectName("youractivitywidget")

        self.verticalLayout_18.addWidget(self.youractivitywidget)

        self.horizontalLayout_20.addWidget(self.youractivitybox)

        self.totaltransactionbox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.totaltransactionbox.setObjectName("totaltransactionbox")
        sizePolicy.setHeightForWidth(
            self.totaltransactionbox.sizePolicy().hasHeightForWidth()
        )
        self.totaltransactionbox.setSizePolicy(sizePolicy)
        self.totaltransactionbox.setMinimumSize(QSize(300, 300))
        self.totaltransactionbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 15"
        )
        self.verticalLayout_17 = QVBoxLayout(self.totaltransactionbox)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(10, 10, -1, -1)
        self.totaltransactionlbl = QLabel(self.totaltransactionbox)
        self.totaltransactionlbl.setObjectName("totaltransactionlbl")
        sizePolicy1.setHeightForWidth(
            self.totaltransactionlbl.sizePolicy().hasHeightForWidth()
        )
        self.totaltransactionlbl.setSizePolicy(sizePolicy1)
        self.totaltransactionlbl.setFont(Inter)
        self.totaltransactionlbl.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 500 15px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.totaltransactionlbl.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_28.addWidget(self.totaltransactionlbl)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_28.addItem(self.horizontalSpacer_7)

        self.verticalLayout_17.addLayout(self.horizontalLayout_28)

        self.totaltransactionwidget = QWidget(self.totaltransactionbox)
        self.totaltransactionwidget.setObjectName("totaltransactionwidget")
        self.horizontalLayout_26 = QHBoxLayout(self.totaltransactionwidget)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.totaltransactionvalue = QLabel(self.totaltransactionwidget)
        self.totaltransactionvalue.setObjectName("totaltransactionvalue")
        sizePolicy1.setHeightForWidth(
            self.totaltransactionvalue.sizePolicy().hasHeightForWidth()
        )
        self.totaltransactionvalue.setSizePolicy(sizePolicy1)
        self.totaltransactionvalue.setFont(font2)
        self.totaltransactionvalue.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 700 32px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.totaltransactionvalue.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_26.addWidget(self.totaltransactionvalue)

        self.verticalLayout_17.addWidget(self.totaltransactionwidget)

        self.horizontalLayout_20.addWidget(self.totaltransactionbox)

        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_15.addWidget(self.scrollArea_2)

        self.tab.addWidget(self.page_2)

        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.page_3)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(60, 0))
        self.scrollArea_3.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.scrollArea_3.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 760, 787))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(40, -1, 40, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.monthcombo = QComboBox(self.scrollAreaWidgetContents_3)
        self.monthcombo.setPlaceholderText("Month")
        self.monthcombo.addItem("")
        self.monthcombo.addItem("")
        self.monthcombo.addItem("")
        self.monthcombo.addItem("")
        self.monthcombo.addItem("")
        self.monthcombo.addItem("")
        self.monthcombo.addItem("")
        self.monthcombo.addItem("")
        self.monthcombo.addItem("")
        self.monthcombo.addItem("")
        self.monthcombo.addItem("")
        self.monthcombo.addItem("")
        self.monthcombo.setObjectName("monthcombo")
        sizePolicy5.setHeightForWidth(self.monthcombo.sizePolicy().hasHeightForWidth())
        self.monthcombo.setSizePolicy(sizePolicy5)
        self.monthcombo.setMinimumSize(QSize(100, 0))
        self.monthcombo.setStyleSheet(
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
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "            background-color: #ffffff;\n"
            "            color: #000000; \n"
            "\n"
            "            }\n"
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
            "    min-height: 18px;\n"
            "    border-radius: 10000px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical,\n"
            "QScrollBar::sub-line:vertical {\n"
            "    background: none;\n"
            "    height: 0px;\n"
            "}"
        )
        self.monthcombo.setEditable(False)
        self.monthcombo.setFrame(True)
        self.horizontalLayout_4.addWidget(self.monthcombo)

        self.daycombo = QComboBox(self.scrollAreaWidgetContents_3)
        self.daycombo.setPlaceholderText("Day")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.addItem("")
        self.daycombo.setObjectName("daycombo")
        sizePolicy5.setHeightForWidth(self.daycombo.sizePolicy().hasHeightForWidth())
        self.daycombo.setSizePolicy(sizePolicy5)
        self.daycombo.setMinimumSize(QSize(60, 0))
        self.daycombo.setStyleSheet(
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
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "            background-color: #ffffff;\n"
            "            color: #000000; \n"
            "            }\n"
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
            "    min-height: 18px;\n"
            "    border-radius: 10000px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical,\n"
            "QScrollBar::sub-line:vertical {\n"
            "    background: none;\n"
            "    height: 0px;\n"
            "}"
        )
        self.daycombo.setEditable(False)
        self.daycombo.setFrame(True)
        self.horizontalLayout_4.addWidget(self.daycombo)

        self.yearcombo = QComboBox(self.scrollAreaWidgetContents_3)
        self.yearcombo.setPlaceholderText("Year")
        self.yearcombo.addItem("")
        self.yearcombo.addItem("")
        self.yearcombo.setObjectName("yearcombo")
        sizePolicy5.setHeightForWidth(self.yearcombo.sizePolicy().hasHeightForWidth())
        self.yearcombo.setSizePolicy(sizePolicy5)
        self.yearcombo.setMinimumSize(QSize(60, 0))
        self.yearcombo.setStyleSheet(
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
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "            background-color: #ffffff;\n"
            "            color: #000000; \n"
            "            }\n"
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
            "    min-height: 18px;\n"
            "    border-radius: 10000px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical,\n"
            "QScrollBar::sub-line:vertical {\n"
            "    background: none;\n"
            "    height: 0px;\n"
            "}"
        )
        self.yearcombo.setEditable(False)
        self.yearcombo.setFrame(True)

        self.horizontalLayout_4.addWidget(self.yearcombo)

        self.viewbtn = QPushButton(self.scrollAreaWidgetContents_3)
        self.viewbtn.setObjectName("viewbtn")
        sizePolicy5.setHeightForWidth(self.viewbtn.sizePolicy().hasHeightForWidth())
        self.viewbtn.setSizePolicy(sizePolicy5)
        self.viewbtn.setMinimumSize(QSize(20, 34))
        self.viewbtn.setMaximumSize(QSize(90, 34))
        self.viewbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.viewbtn.setAutoFillBackground(False)
        self.viewbtn.setStyleSheet(
            "\n"
            "\n"
            "\n"
            "QPushButton {\n"
            "	\n"
            "	\n"
            "	\n"
            "	color: rgb(245, 245, 245);\n"
            "	background-color: rgb(167, 83, 115);\n"
            "	border: 1px solid #ccc;\n"
            "    border-radius: 7px;\n"
            "	border-color: rgb(144, 72, 99);\n"
            "text-align: center;\n"
            " font-size: 10px;\n"
            "\n"
            "\n"
            "  \n"
            "\n"
            "}\n"
            "QPushButton:hover {\n"
            "\n"
            "	\n"
            "	background-color: rgb(138, 69, 95);\n"
            "	\n"
            "   \n"
            "}"
        )
        self.viewbtn.setCheckable(True)
        self.viewbtn.setFlat(True)

        self.horizontalLayout_4.addWidget(self.viewbtn)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.monthlyreport_lbl = QLabel(self.scrollAreaWidgetContents_3)
        self.monthlyreport_lbl.setObjectName("monthlyreport_lbl")
        sizePolicy1.setHeightForWidth(
            self.monthlyreport_lbl.sizePolicy().hasHeightForWidth()
        )
        self.monthlyreport_lbl.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies(["Inter"])
        font5.setWeight(QFont.DemiBold)
        font5.setItalic(False)
        self.monthlyreport_lbl.setFont(font5)
        self.monthlyreport_lbl.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 600 18px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.monthlyreport_lbl.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_3.addWidget(self.monthlyreport_lbl)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_4 = QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_6 = QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QWidget(self.page_4)
        self.widget.setObjectName("widget")
        self.widget.setMinimumSize(QSize(0, 700))
        self.widget.setMaximumSize(QSize(16777215, 900))
        self.widget.setStyleSheet(
            "background-color: rgb(254, 254, 254);\n" "border-radius: 30\n" ""
        )
        self.verticalLayout_11 = QVBoxLayout(self.widget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(20, 10, 20, -1)
        self.budgetreport = QGroupBox(self.widget)
        self.budgetreport.setObjectName("budgetreport")
        self.budgetreport.setMaximumSize(QSize(16777215, 80))
        self.budgetreport.setFont(Inter)
        self.budgetreport.setStyleSheet(
            "text-align: center;\n" "background-color: #f4d4d4;\n" "border-radius: 15px"
        )
        self.verticalLayout_38 = QVBoxLayout(self.budgetreport)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(5)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(20, -1, 20, 0)
        self.budgetreport_value = QLabel(self.budgetreport)
        self.budgetreport_value.setObjectName("budgetreport_value")
        sizePolicy.setHeightForWidth(
            self.budgetreport_value.sizePolicy().hasHeightForWidth()
        )
        self.budgetreport_value.setSizePolicy(sizePolicy)
        self.budgetreport_value.setMaximumSize(QSize(16777215, 50))
        self.budgetreport_value.setFont(font3)
        self.budgetreport_value.setStyleSheet(
            "color: rgb(167, 83, 115);\n" 'font: 700 12px "Inter";\n' ""
        )
        self.budgetreport_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.budgetreport_value.setWordWrap(False)

        self.horizontalLayout_36.addWidget(self.budgetreport_value)

        self.budgetlbl = QLabel(self.budgetreport)
        self.budgetlbl.setObjectName("budgetlbl")
        self.budgetlbl.setMaximumSize(QSize(16777215, 50))
        self.budgetlbl.setStyleSheet(
            "color: rgb(167, 83, 115);\n"
            'font: 600 12px "Inter";\n'
            "text-align: center;"
        )
        self.budgetlbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.budgetlbl.setWordWrap(True)

        self.horizontalLayout_36.addWidget(self.budgetlbl)

        self.verticalLayout_38.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_35.addWidget(self.budgetreport)

        self.savingsreport = QGroupBox(self.widget)
        self.savingsreport.setObjectName("savingsreport")
        self.savingsreport.setMaximumSize(QSize(16777215, 80))
        self.savingsreport.setFont(Inter)
        self.savingsreport.setStyleSheet(
            "text-align: center;\n" "background-color: #f4d4d4;\n" "border-radius: 15px"
        )
        self.verticalLayout_39 = QVBoxLayout(self.savingsreport)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(5)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(20, -1, 20, 0)
        self.savingsreport_value = QLabel(self.savingsreport)
        self.savingsreport_value.setObjectName("savingsreport_value")
        sizePolicy.setHeightForWidth(
            self.savingsreport_value.sizePolicy().hasHeightForWidth()
        )
        self.savingsreport_value.setSizePolicy(sizePolicy)
        self.savingsreport_value.setMaximumSize(QSize(16777215, 50))
        self.savingsreport_value.setFont(font3)
        self.savingsreport_value.setStyleSheet(
            "color: rgb(167, 83, 115);\n" 'font: 700 12px "Inter";\n' ""
        )
        self.savingsreport_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.savingsreport_value.setWordWrap(False)

        self.horizontalLayout_37.addWidget(self.savingsreport_value)

        self.savingslbl_2 = QLabel(self.savingsreport)
        self.savingslbl_2.setObjectName("savingslbl_2")
        self.savingslbl_2.setMaximumSize(QSize(16777215, 50))
        self.savingslbl_2.setStyleSheet(
            "color: rgb(167, 83, 115);\n"
            'font: 600 12px "Inter";\n'
            "text-align: center;"
        )
        self.savingslbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.savingslbl_2.setWordWrap(True)

        self.horizontalLayout_37.addWidget(self.savingslbl_2)

        self.verticalLayout_39.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_35.addWidget(self.savingsreport)

        self.expensereport = QGroupBox(self.widget)
        self.expensereport.setObjectName("expensereport")
        self.expensereport.setMaximumSize(QSize(16777215, 80))
        self.expensereport.setFont(Inter)
        self.expensereport.setStyleSheet(
            "text-align: center;\n" "background-color: #f4d4d4;\n" "border-radius: 15px"
        )
        self.verticalLayout_40 = QVBoxLayout(self.expensereport)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(20, -1, 20, 0)
        self.expensereport_value = QLabel(self.expensereport)
        self.expensereport_value.setObjectName("expensereport_value")
        sizePolicy.setHeightForWidth(
            self.expensereport_value.sizePolicy().hasHeightForWidth()
        )
        self.expensereport_value.setSizePolicy(sizePolicy)
        self.expensereport_value.setMaximumSize(QSize(16777215, 50))
        self.expensereport_value.setFont(font3)
        self.expensereport_value.setStyleSheet(
            "color: rgb(167, 83, 115);\n" 'font: 700 12px "Inter";\n' ""
        )
        self.expensereport_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.expensereport_value.setWordWrap(False)

        self.horizontalLayout_38.addWidget(self.expensereport_value)

        self.expenselbl_2 = QLabel(self.expensereport)
        self.expenselbl_2.setObjectName("expenselbl_2")
        self.expenselbl_2.setMaximumSize(QSize(16777215, 50))
        self.expenselbl_2.setStyleSheet(
            "color: rgb(167, 83, 115);\n"
            'font: 600 12px "Inter";\n'
            "text-align: center;"
        )
        self.expenselbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.expenselbl_2.setWordWrap(True)

        self.horizontalLayout_38.addWidget(self.expenselbl_2)

        self.verticalLayout_40.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_35.addWidget(self.expensereport)

        self.verticalLayout_11.addLayout(self.horizontalLayout_35)

        self.graphwidget = QWidget(self.widget)
        self.graphwidget.setObjectName("graphwidget")
        self.graphwidget.setMinimumSize(QSize(0, 200))
        self.graphwidget.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_11 = QHBoxLayout(self.graphwidget)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.transactionsummarybox_2 = QGroupBox(self.graphwidget)
        self.transactionsummarybox_2.setObjectName("transactionsummarybox_2")
        sizePolicy.setHeightForWidth(
            self.transactionsummarybox_2.sizePolicy().hasHeightForWidth()
        )
        self.transactionsummarybox_2.setSizePolicy(sizePolicy)
        self.transactionsummarybox_2.setMinimumSize(QSize(300, 247))
        self.transactionsummarybox_2.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 15"
        )
        self.verticalLayout_22 = QVBoxLayout(self.transactionsummarybox_2)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(10, 0, -1, -1)
        self.transactionsummary_2 = QLabel(self.transactionsummarybox_2)
        self.transactionsummary_2.setObjectName("transactionsummary_2")
        sizePolicy1.setHeightForWidth(
            self.transactionsummary_2.sizePolicy().hasHeightForWidth()
        )
        self.transactionsummary_2.setSizePolicy(sizePolicy1)
        self.transactionsummary_2.setFont(Inter)
        self.transactionsummary_2.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 500 15px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.transactionsummary_2.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_32.addWidget(self.transactionsummary_2)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_32.addItem(self.horizontalSpacer_8)

        self.verticalLayout_22.addLayout(self.horizontalLayout_32)

        self.transactionreport_widget = QWidget(self.transactionsummarybox_2)
        self.transactionreport_widget.setObjectName("transactionreport_widget")
        self.verticalLayout_23 = QVBoxLayout(self.transactionreport_widget)
        self.verticalLayout_23.setObjectName("verticalLayout_23")

        self.verticalLayout_22.addWidget(self.transactionreport_widget)

        self.horizontalLayout_10.addWidget(self.transactionsummarybox_2)

        self.transactionsummarybox_3 = QGroupBox(self.graphwidget)
        self.transactionsummarybox_3.setObjectName("transactionsummarybox_3")
        sizePolicy.setHeightForWidth(
            self.transactionsummarybox_3.sizePolicy().hasHeightForWidth()
        )
        self.transactionsummarybox_3.setSizePolicy(sizePolicy)
        self.transactionsummarybox_3.setMinimumSize(QSize(300, 247))
        self.transactionsummarybox_3.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 15"
        )
        self.verticalLayout_36 = QVBoxLayout(self.transactionsummarybox_3)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(10, 0, -1, -1)
        self.budgetsummary = QLabel(self.transactionsummarybox_3)
        self.budgetsummary.setObjectName("budgetsummary")
        sizePolicy1.setHeightForWidth(
            self.budgetsummary.sizePolicy().hasHeightForWidth()
        )
        self.budgetsummary.setSizePolicy(sizePolicy1)
        self.budgetsummary.setFont(Inter)
        self.budgetsummary.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 500 15px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.budgetsummary.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_34.addWidget(self.budgetsummary)

        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_34.addItem(self.horizontalSpacer_10)

        self.verticalLayout_36.addLayout(self.horizontalLayout_34)

        self.budgetreport_widget = QWidget(self.transactionsummarybox_3)
        self.budgetreport_widget.setObjectName("budgetreport_widget")
        self.verticalLayout_37 = QVBoxLayout(self.budgetreport_widget)
        self.verticalLayout_37.setObjectName("verticalLayout_37")

        self.verticalLayout_36.addWidget(self.budgetreport_widget)

        self.horizontalLayout_10.addWidget(self.transactionsummarybox_3)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)

        self.verticalLayout_11.addWidget(self.graphwidget)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, -1, -1, -1)
        self.translbl_2 = QLabel(self.widget)
        self.translbl_2.setObjectName("translbl_2")
        sizePolicy1.setHeightForWidth(self.translbl_2.sizePolicy().hasHeightForWidth())
        self.translbl_2.setSizePolicy(sizePolicy1)
        self.translbl_2.setFont(font5)
        self.translbl_2.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 600 18px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.translbl_2.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_7.addWidget(self.translbl_2)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, -1, 20, -1)
        self.transwidgetbox = QWidget(self.widget)
        self.transwidgetbox.setObjectName("transwidgetbox")
        self.transwidgetbox.setStyleSheet("background-color: rgb(167, 83, 115);")
        self.verticalLayout_20 = QVBoxLayout(self.transwidgetbox)
        self.verticalLayout_20.setSpacing(15)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(15, 15, 15, 15)
        self.transtableviewwidget = QWidget(self.transwidgetbox)
        self.transtableviewwidget.setObjectName("transtableviewwidget")
        self.transtableviewwidget.setStyleSheet(
            "background-color:rgb(255, 255, 255);\n" "border-radius: 25"
        )
        self.verticalLayout_21 = QVBoxLayout(self.transtableviewwidget)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.transactions = QTableView()

        self.transactions.setModel(self.activities_model)
        self.transactions.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.transactions.verticalHeader().setVisible(False)
        self.transactions.verticalHeader().setDefaultSectionSize(40)
        self.transactions.setAlternatingRowColors(True)
        self.transactions.setShowGrid(False)
        self.transactions.setSelectionMode(QTableView.NoSelection)
        self.transactions.setEditTriggers(QTableView.NoEditTriggers)
        self.transactions.setFocusPolicy(Qt.NoFocus)
        self.transactions.horizontalHeader().setFocusPolicy(Qt.NoFocus)
        self.transactions.setStyleSheet(
            """QTableView {
    background-color: white;
    alternate-background-color: #f0f8ff; /* light blue */
    gridline-color: #dcdcdc;
    font: 300 12px "Inter";
    border: none;
}


QTableView::item:hover {
    background-color: #e0f7fa;  /* light cyan */
}



QTableView::item {
    padding: 8px;
    color: rgb(105, 104, 104);
    font: 900 12px "Inter";
}

QHeaderView::section {
    font: 500 12px "Inter";
    background-color: white;
    color: rgb(92, 91, 91);
    padding: 5px;
    border: 1px solid rgb(230, 230, 230);
    border-top: none;
    border-left: none;
    border-right: none;
}

"""
        )

        self.verticalLayout_21.addWidget(self.transactions)

        self.verticalLayout_20.addWidget(self.transtableviewwidget)

        self.verticalLayout_8.addWidget(self.transwidgetbox)

        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.verticalLayout_11.addLayout(self.verticalLayout_9)

        self.verticalLayout_6.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page_4)
        self.no_available_report_page = QWidget()
        self.no_available_report_page.setObjectName("no_available_report_page")
        self.verticalLayout_7 = QVBoxLayout(self.no_available_report_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.noavailablereportwidget = QWidget(self.no_available_report_page)
        self.noavailablereportwidget.setObjectName("noavailablereportwidget")
        self.noavailablereportwidget.setStyleSheet(
            "background-color: rgb(254, 254, 254);\n" "border-radius: 30\n" ""
        )
        self.horizontalLayout_5 = QHBoxLayout(self.noavailablereportwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.noavailablereportlbl = QLabel(self.noavailablereportwidget)
        self.noavailablereportlbl.setObjectName("noavailablereportlbl")
        sizePolicy1.setHeightForWidth(
            self.noavailablereportlbl.sizePolicy().hasHeightForWidth()
        )
        self.noavailablereportlbl.setSizePolicy(sizePolicy1)
        self.noavailablereportlbl.setFont(font5)
        self.noavailablereportlbl.setStyleSheet(
            "color: rgb(108, 68, 100);\n"
            'font: 600 18px "Inter";\n'
            "background-color: transparent\n"
            ""
        )
        self.noavailablereportlbl.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout_5.addWidget(self.noavailablereportlbl)

        self.verticalLayout_7.addWidget(self.noavailablereportwidget)

        self.stackedWidget.addWidget(self.no_available_report_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollArea_3)

        self.tab.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.tab)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_6.addWidget(self.tabframe)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.homebtn.toggled.connect(self.homebtn_min.setChecked)
        self.analyticsbtn.toggled.connect(self.analyticsbtn_min.setChecked)
        self.reportbtn.toggled.connect(self.reportbtn_min.setChecked)
        self.homebtn_min.toggled.connect(self.homebtn.setChecked)
        self.analyticsbtn_min.toggled.connect(self.analyticsbtn.setChecked)
        self.reportbtn_min.toggled.connect(self.reportbtn.setChecked)
        self.menubtn.toggled.connect(self.maxsidebar.setVisible)
        self.menubtn.toggled.connect(self.minsidebar.setHidden)

        self.tab.setCurrentIndex(0)

        # Add connection for tab changes
        self.tab.currentChanged.connect(self.update_menu_label)

        QMetaObject.connectSlotsByName(MainWindow)
        self.maxsidebar.hide()
        self.minsidebar.show()
        self.sidebar_expanded = True

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.minlogo.setText("")
        self.homebtn_min.setText(
            QCoreApplication.translate("MainWindow", "   Dashboard", None)
        )
        self.analyticsbtn_min.setText(
            QCoreApplication.translate("MainWindow", "   Analytics", None)
        )
        self.reportbtn_min.setText(
            QCoreApplication.translate("MainWindow", "   Reports", None)
        )
        self.maxlogo.setText("")
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
        self.menubtn.setText(
            QCoreApplication.translate("MainWindow", "PushButton", None)
        )
        self.menulabel.setText(
            QCoreApplication.translate("MainWindow", "Dashboard", None)
        )
        self.notificationsbtn.setText(
            QCoreApplication.translate("MainWindow", "...", None)
        )
        self.profilebtn.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.morebtn.setText(QCoreApplication.translate("MainWindow", "...", None))
        # if QT_CONFIG(accessibility)
        self.tab.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.greethello.setText(
            QCoreApplication.translate("MainWindow", "Hello,", None)
        )

        self.totalbudgetbox.setTitle("")
        self.totalbudgetlbl.setText(
            QCoreApplication.translate("MainWindow", "Current Budget", None)
        )

        self.viewcategorybtn.setText(
            QCoreApplication.translate("MainWindow", "View Category", None)
        )
        self.savingsbox_3.setTitle("")
        self.savingslbl.setText(
            QCoreApplication.translate("MainWindow", "Savings", None)
        )
        self.savingsbtn.setText(
            QCoreApplication.translate("MainWindow", "View Category", None)
        )
        self.expensebox.setTitle("")

        self.expenselbl.setText(
            QCoreApplication.translate("MainWindow", "Amount Spent", None)
        )
        self.incomebox.setTitle("")
        self.incomelbl.setText(
            QCoreApplication.translate("MainWindow", "Monthly Income", None)
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
        self.monthcombo.setItemText(
            0, QCoreApplication.translate("MainWindow", "January", None)
        )
        self.monthcombo.setItemText(
            1, QCoreApplication.translate("MainWindow", "February", None)
        )
        self.monthcombo.setItemText(
            2, QCoreApplication.translate("MainWindow", "March", None)
        )
        self.monthcombo.setItemText(
            3, QCoreApplication.translate("MainWindow", "April", None)
        )
        self.monthcombo.setItemText(
            4, QCoreApplication.translate("MainWindow", "May", None)
        )
        self.monthcombo.setItemText(
            5, QCoreApplication.translate("MainWindow", "June", None)
        )
        self.monthcombo.setItemText(
            6, QCoreApplication.translate("MainWindow", "July", None)
        )
        self.monthcombo.setItemText(
            7, QCoreApplication.translate("MainWindow", "August", None)
        )
        self.monthcombo.setItemText(
            8, QCoreApplication.translate("MainWindow", "September", None)
        )
        self.monthcombo.setItemText(
            9, QCoreApplication.translate("MainWindow", "October", None)
        )
        self.monthcombo.setItemText(
            10, QCoreApplication.translate("MainWindow", "November", None)
        )
        self.monthcombo.setItemText(
            11, QCoreApplication.translate("MainWindow", "December", None)
        )

        self.monthcombo.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Month", None)
        )
        self.daycombo.setItemText(
            0, QCoreApplication.translate("MainWindow", "01", None)
        )
        self.daycombo.setItemText(
            1, QCoreApplication.translate("MainWindow", "02", None)
        )
        self.daycombo.setItemText(
            2, QCoreApplication.translate("MainWindow", "03", None)
        )
        self.daycombo.setItemText(
            3, QCoreApplication.translate("MainWindow", "04", None)
        )
        self.daycombo.setItemText(
            4, QCoreApplication.translate("MainWindow", "05", None)
        )
        self.daycombo.setItemText(
            5, QCoreApplication.translate("MainWindow", "06", None)
        )
        self.daycombo.setItemText(
            6, QCoreApplication.translate("MainWindow", "07", None)
        )
        self.daycombo.setItemText(
            7, QCoreApplication.translate("MainWindow", "08", None)
        )
        self.daycombo.setItemText(
            8, QCoreApplication.translate("MainWindow", "09", None)
        )
        self.daycombo.setItemText(
            9, QCoreApplication.translate("MainWindow", "10", None)
        )
        self.daycombo.setItemText(
            10, QCoreApplication.translate("MainWindow", "11", None)
        )
        self.daycombo.setItemText(
            11, QCoreApplication.translate("MainWindow", "12", None)
        )
        self.daycombo.setItemText(
            12, QCoreApplication.translate("MainWindow", "13", None)
        )
        self.daycombo.setItemText(
            13, QCoreApplication.translate("MainWindow", "14", None)
        )
        self.daycombo.setItemText(
            14, QCoreApplication.translate("MainWindow", "15", None)
        )
        self.daycombo.setItemText(
            15, QCoreApplication.translate("MainWindow", "16", None)
        )
        self.daycombo.setItemText(
            16, QCoreApplication.translate("MainWindow", "17", None)
        )
        self.daycombo.setItemText(
            17, QCoreApplication.translate("MainWindow", "18", None)
        )
        self.daycombo.setItemText(
            18, QCoreApplication.translate("MainWindow", "19", None)
        )
        self.daycombo.setItemText(
            19, QCoreApplication.translate("MainWindow", "20", None)
        )
        self.daycombo.setItemText(
            20, QCoreApplication.translate("MainWindow", "21", None)
        )
        self.daycombo.setItemText(
            21, QCoreApplication.translate("MainWindow", "22", None)
        )
        self.daycombo.setItemText(
            22, QCoreApplication.translate("MainWindow", "23", None)
        )
        self.daycombo.setItemText(
            23, QCoreApplication.translate("MainWindow", "24", None)
        )
        self.daycombo.setItemText(
            24, QCoreApplication.translate("MainWindow", "25", None)
        )
        self.daycombo.setItemText(
            25, QCoreApplication.translate("MainWindow", "26", None)
        )
        self.daycombo.setItemText(
            26, QCoreApplication.translate("MainWindow", "27", None)
        )
        self.daycombo.setItemText(
            27, QCoreApplication.translate("MainWindow", "28", None)
        )
        self.daycombo.setItemText(
            28, QCoreApplication.translate("MainWindow", "29", None)
        )
        self.daycombo.setItemText(
            29, QCoreApplication.translate("MainWindow", "30", None)
        )
        self.daycombo.setItemText(
            30, QCoreApplication.translate("MainWindow", "31", None)
        )

        self.daycombo.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Day", None)
        )
        self.yearcombo.setItemText(
            0, QCoreApplication.translate("MainWindow", "2024", None)
        )
        self.yearcombo.setItemText(
            1, QCoreApplication.translate("MainWindow", "2025", None)
        )

        self.yearcombo.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Year", None)
        )
        self.viewbtn.setText(QCoreApplication.translate("MainWindow", "View", None))
        self.monthlyreport_lbl.setText(
            QCoreApplication.translate("MainWindow", "Filter Report", None)
        )
        self.budgetreport.setTitle("")
        self.budgetreport_value.setText(
            QCoreApplication.translate("MainWindow", "\u20b1 3254.00", None)
        )
        self.budgetlbl.setText(QCoreApplication.translate("MainWindow", "Budget", None))
        self.savingsreport.setTitle("")
        self.savingsreport_value.setText(
            QCoreApplication.translate("MainWindow", "\u20b1 554.00", None)
        )
        self.savingslbl_2.setText(
            QCoreApplication.translate("MainWindow", "Savings", None)
        )
        self.expensereport.setTitle("")
        self.expensereport_value.setText(
            QCoreApplication.translate("MainWindow", "\u20b1 854.00", None)
        )
        self.expenselbl_2.setText(
            QCoreApplication.translate("MainWindow", "Amount Spent", None)
        )
        self.transactionsummarybox_2.setTitle("")
        self.transactionsummary_2.setText(
            QCoreApplication.translate("MainWindow", "Transactions Summary", None)
        )
        self.transactionsummarybox_3.setTitle("")
        self.budgetsummary.setText(
            QCoreApplication.translate("MainWindow", "Budget Summary", None)
        )
        self.translbl_2.setText(
            QCoreApplication.translate("MainWindow", "Transactions", None)
        )
        self.noavailablereportlbl.setText(
            QCoreApplication.translate("MainWindow", "No Available Report", None)
        )
        self.overallbudgetbox.setTitle("")
        self.overallbudgetvalue.setText(
            QCoreApplication.translate("MainWindow", "\u20b1 54320.00", None)
        )
        self.overallbudgetlbl.setText(
            QCoreApplication.translate("MainWindow", "Overall Budget", None)
        )
        self.expensebox_3.setTitle("")

        self.totalexpenselbl.setText(
            QCoreApplication.translate("MainWindow", "Amount Spent", None)
        )
        self.accumulatedsavingsbox.setTitle("")
        self.accumulatedsavingvalue.setText(
            QCoreApplication.translate("MainWindow", "\u20b1 554.00", None)
        )
        self.accumulatedsavingslbl.setText(
            QCoreApplication.translate("MainWindow", "Accumulated Savings", None)
        )
        self.totalincomebox.setTitle("")
        self.totalincomelbl.setText(
            QCoreApplication.translate("MainWindow", "Total Income", None)
        )
        self.transactionsummarybox.setTitle("")
        self.transactionsummary.setText(
            QCoreApplication.translate("MainWindow", "Transactions Summary", None)
        )
        self.budgetsummarybox.setTitle("")
        self.budgetsummarylbl.setText(
            QCoreApplication.translate("MainWindow", "Budget Summary", None)
        )
        self.youractivitybox.setTitle("")
        self.youractivitylbl.setText(
            QCoreApplication.translate("MainWindow", "Your Activity", None)
        )
        self.totaltransactionbox.setTitle("")
        self.totaltransactionlbl.setText(
            QCoreApplication.translate("MainWindow", "Total Transactions", None)
        )
        self.totaltransactionvalue.setText(
            QCoreApplication.translate("MainWindow", "204", None)
        )

    # retranslateUi

    # helper functions
    def update_menu_label(self, index):
        if index == 0:
            self.menulabel.setText("Dashboard")
        elif index == 1:
            self.menulabel.setText("Analytics")
        elif index == 2:
            self.menulabel.setText("Reports")

    def toggle_sidebar(self):
        if self.sidebar_expanded:
            self.maxsidebar.hide()
            self.minsidebar.show()
        else:
            self.minsidebar.hide()
            self.maxsidebar.show()
        self.sidebar_expanded = not self.sidebar_expanded

    def budget_window(self):
        dialog = BudgetWindow(self)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.show()
        dialog.exec()

    def signoutwindow(self):
        dialog = SignOutWindow(self)
        dialog.signOutRequested.connect(self.show_sign_in)
        dialog.show()

    def show_sign_in(self):
        from user_sign import SignEntry

        self.signin = SignEntry()
        self.signin.show()

    def add_graph_to_widget(self, widget: QWidget):
        # Create DataManager instance with sample data
        data_manager = DataManager(self.user_id)

        # Clear any existing plots and create new figure
        plt.close("all")
        fig = plt.figure(figsize=(4, 3), dpi=100)
        ax = fig.add_subplot(111)

        # Get statistics from DataManager
        stats = data_manager.get_transactions_data()  # get returned dictionary from stats

        # Extract data for plotting
        categories = list(stats.keys())
        amounts = list(stats.values())

        print(f"Cat in graph: {categories}")
        print(f"amounts in graph: {amounts}") # for cross checking
        
        # Create bar chart with styling
        bars = ax.bar(categories, amounts, color="#a75373")

        # Customize the appearance
        ax.set_xlabel("Category", fontsize=7, labelpad=8)
        ax.set_ylabel("Amount Spent", fontsize=7, labelpad=8)

        # Rotate and align the tick labels so they look better
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", fontsize=7)
        plt.setp(ax.get_yticklabels(), fontsize=7)

        # Add some padding between the axis and the labels
        ax.tick_params(axis="x", which="major", pad=5)

        # Adjust layout to prevent label cutoff
        fig.tight_layout()

        # Convert to Qt canvas
        canvas = FigureCanvas(fig)
        canvas.setMinimumSize(300, 200)

        # Get the existing layout
        layout = widget.layout()

        # Clear any existing widgets in the layout
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            # Add the canvas to the existing layout
            layout.addWidget(canvas)
        # Force the widget to update
        widget.update()
        canvas.draw()

    def add_graph_to_budget_summary(self, widget: QWidget):
        # Use the current user's ID
        data_manager = DataManager(self.user_id)

        # Clear any existing plots and create new figure
        plt.close("all")
        fig = plt.figure(figsize=(3, 3), dpi=100)
        ax = fig.add_subplot(111)

        # Get statistics from DataManager
        stats = data_manager.get_statistics()

        # Extract data for plotting
        categories = list(stats.keys())
        percentages = list(stats.values())
        
        print(f"Cat in pie: {categories}")
        print(f"amounts in pie: {percentages}") # for cross checking

        # Create pie chart with styling
        wedges, texts, autotexts = ax.pie(
            percentages,
            labels=categories,
            autopct="%1.1f%%",
            startangle=140,
            colors=["#a75373", "#6c4464", "#d46a92", "#904863", "#f4d4d4"],
        )

        # Style the labels and percentages
        plt.setp(texts, size=7)
        plt.setp(autotexts, size=7)

        # Adjust layout to prevent label cutoff
        fig.tight_layout()

        # Convert to Qt canvas
        canvas = FigureCanvas(fig)
        canvas.setMinimumSize(300, 200)

        # Get the existing layout
        layout = widget.layout()

        # Clear any existing widgets in the layout
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            # Add the canvas to the existing layout
            layout.addWidget(canvas)

        # Force the widget to update
        widget.update()
        canvas.draw()
    def refresh_data(self):
        """Refresh all user data and UI elements after account setup"""
        try:
            current_month = datetime.today().strftime("%Y-%m")
            print("Starting data refresh...")
            # Fetch latest user data
            self.cursor.execute(
                "SELECT * FROM user_data WHERE user_id = ? AND report_date = ?",
                (self.user_id, current_month),
            )
            self.user_data = self.cursor.fetchone()

            if self.user_data:
                print(f"User data fetched: {self.user_data}")

                # Update income and budget values
                monthly_income = float(self.user_data[4])
                monthly_budget = float(self.user_data[5])
                monthly_expenses = float(self.user_data[3])

                # Update UI elements with proper formatting
                self.savingsvalue.setText(f"₱{self.user_data[2]:,.2f}")
                self.incomevalue.setText(f"₱{monthly_income:,.2f}")
                self.budgetvalue.setText(f"₱{monthly_budget:,.2f}")

                # Update category budgets
                food_budget = float(self.user_data[6])
                utilities_budget = float(self.user_data[7])
                health_budget = float(self.user_data[8])
                personal_budget = float(self.user_data[9])
                education_budget = float(self.user_data[10])
                transportation_budget = float(self.user_data[11])
                misc_budget = float(self.user_data[12])

                # Update expense and savings values
                self.cursor.execute(
                    "SELECT SUM(monthly_expenses), SUM(monthly_savings), SUM(monthly_income), SUM(monthly_budget) FROM user_data WHERE user_id = ?",
                    (self.user_id,),
                )

                result = self.cursor.fetchone()
                if result is None:
                    # Set default values if no data is found
                    self.total_expenses = 0
                    self.total_savings = 0
                    self.total_income = 0
                    self.total_budget = 0
                else:
                    self.total_expenses = result[0] or 0
                    self.total_savings = result[1] or 0
                    self.total_income = result[2] or 0
                    self.total_budget = result[3] or 0

                self.totalexpensevalue.setText(f"₱{float(self.total_expenses):,.2f}")
                self.accumulatedsavingvalue.setText(
                    f"₱{float(self.total_savings):,.2f}"
                )
                self.totalincomevalue.setText(f"₱{float(self.total_income):,.2f}")
                self.overallbudgetvalue.setText(f"₱{float(self.total_budget):,.2f}")
                self.expensevalue.setText(f"₱{float(monthly_expenses):,.2f}")

                # Refresh graphs with new data
                # self.add_graph_to_widget(self.graph_widget)
                # self.add_graph_to_budget_summary(self.summary_widget)
                self.add_graph_to_widget(self.transactionsummarywidget)
                self.add_graph_to_budget_summary(self.budgetsummarywidget)

                print("Data refresh completed successfully")
            else:
                print("No user data found during refresh")

        except Exception as e:
            print(f"Error during data refresh: {e}")
            QMessageBox.warning(
                self, "Refresh Error", "Failed to refresh data. Please try again."
            )

    def refresh_model(self):
        """Refresh the activities model with latest transactions"""
        query = QSqlQuery()
        query.prepare(
            "SELECT transaction_date, amount, description, category FROM transactions WHERE user_id = ? ORDER BY data_id DESC"
        )
        query.addBindValue(self.user_id)
        query.exec_()
        self.activities_model.setQuery(query)

    def handle_add_transaction(self):
        """Handle adding a new transaction and refreshing the view"""
        add_trans = AddTransactions(
            self.user_id,
            self.amountedit,
            self.descriptionedit,
            self.categorycombo,
            self.activities_model,
            self,
        )
        if add_trans.add_entry():
            self.refresh_model()
            self.refresh_data()
