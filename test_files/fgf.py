# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'currentXqkzlm.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
import icons_rc
import icons_rc
import components.images_rc as images_rc
import dsad_rc
import components.images_rc as images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1023, 664)
        MainWindow.setMinimumSize(QSize(0, 664))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.sidebarlayout = QVBoxLayout()
        self.sidebarlayout.setObjectName(u"sidebarlayout")
        self.sidebarlayout.setContentsMargins(0, -1, 0, -1)
        self.sidebarwidget = QWidget(self.centralwidget)
        self.sidebarwidget.setObjectName(u"sidebarwidget")
        self.sidebarwidget.setMinimumSize(QSize(0, 0))
        self.sidebarwidget.setMaximumSize(QSize(500, 16777215))
        font = QFont()
        font.setKerning(False)
        self.sidebarwidget.setFont(font)
        self.sidebarwidget.setStyleSheet(u"QGroupBox {\n"
"\n"
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
"    font: 500 13px \"Inter\";\n"
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
"    color: rgb(75, 47, 69);\n"
"	background-color: rgb(245, 245, 245);\n"
"    padding-left: 25px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    color: rgb(75, 47, 69);\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    color: rgb(75, 47, 69);\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"")
        self.horizontalLayout_31 = QHBoxLayout(self.sidebarwidget)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.minsidebar = QWidget(self.sidebarwidget)
        self.minsidebar.setObjectName(u"minsidebar")
        self.minsidebar.setMinimumSize(QSize(70, 0))
        self.minsidebar.setMaximumSize(QSize(70, 16777215))
        self.minsidebar.setStyleSheet(u"QWidget {\n"
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
"    font: 500 13px \"Inter\";\n"
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
"	background-color: rgb(245, 245"
                        ", 245);\n"
"}\n"
"")
        self.verticalLayout_51 = QVBoxLayout(self.minsidebar)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.line = QFrame(self.minsidebar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_52.addWidget(self.line)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 15, 0, 15)
        self.minlogowidget = QWidget(self.minsidebar)
        self.minlogowidget.setObjectName(u"minlogowidget")
        self.horizontalLayout = QHBoxLayout(self.minlogowidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minlogo = QLabel(self.minlogowidget)
        self.minlogo.setObjectName(u"minlogo")
        self.minlogo.setMaximumSize(QSize(50, 50))
        self.minlogo.setPixmap(QPixmap(u":/newPrefix/logo (2).png"))
        self.minlogo.setScaledContents(True)
        self.minlogo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.minlogo)


        self.verticalLayout_54.addWidget(self.minlogowidget)


        self.verticalLayout_52.addLayout(self.verticalLayout_54)

        self.homebtn_min = QToolButton(self.minsidebar)
        self.homebtn_min.setObjectName(u"homebtn_min")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homebtn_min.sizePolicy().hasHeightForWidth())
        self.homebtn_min.setSizePolicy(sizePolicy)
        self.homebtn_min.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.homebtn_min.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons/dashboardlight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/dashboardlight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon.addFile(u":/dashboarddark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.homebtn_min.setIcon(icon)
        self.homebtn_min.setIconSize(QSize(20, 20))
        self.homebtn_min.setCheckable(True)
        self.homebtn_min.setChecked(True)
        self.homebtn_min.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.homebtn_min.setAutoRaise(False)
        self.homebtn_min.setArrowType(Qt.ArrowType.NoArrow)

        self.verticalLayout_52.addWidget(self.homebtn_min)

        self.analyticsbtn_min = QToolButton(self.minsidebar)
        self.analyticsbtn_min.setObjectName(u"analyticsbtn_min")
        sizePolicy.setHeightForWidth(self.analyticsbtn_min.sizePolicy().hasHeightForWidth())
        self.analyticsbtn_min.setSizePolicy(sizePolicy)
        self.analyticsbtn_min.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/analyticslight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/analyticslight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon1.addFile(u":/analyticsdark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.analyticsbtn_min.setIcon(icon1)
        self.analyticsbtn_min.setCheckable(True)
        self.analyticsbtn_min.setChecked(False)
        self.analyticsbtn_min.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.analyticsbtn_min.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.verticalLayout_52.addWidget(self.analyticsbtn_min)

        self.reportbtn_min = QToolButton(self.minsidebar)
        self.reportbtn_min.setObjectName(u"reportbtn_min")
        sizePolicy.setHeightForWidth(self.reportbtn_min.sizePolicy().hasHeightForWidth())
        self.reportbtn_min.setSizePolicy(sizePolicy)
        self.reportbtn_min.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/monitoringlight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/monitoringlight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon2.addFile(u":/monitoringdark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.reportbtn_min.setIcon(icon2)
        self.reportbtn_min.setCheckable(True)
        self.reportbtn_min.setChecked(False)
        self.reportbtn_min.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.verticalLayout_52.addWidget(self.reportbtn_min)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_7)


        self.verticalLayout_51.addLayout(self.verticalLayout_52)


        self.horizontalLayout_31.addWidget(self.minsidebar)

        self.maxsidebar = QWidget(self.sidebarwidget)
        self.maxsidebar.setObjectName(u"maxsidebar")
        self.maxsidebar.setMinimumSize(QSize(170, 0))
        self.maxsidebar.setMaximumSize(QSize(500, 16777215))
        self.maxsidebar.setStyleSheet(u"QWidget {\n"
"\n"
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
"    font: 500 13px \"Inter\";\n"
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
"	background-color: rgb(245, 245,"
                        " 245);\n"
"}\n"
"")
        self.verticalLayout_29 = QVBoxLayout(self.maxsidebar)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 15, 0, 15)
        self.maxlogowidget = QWidget(self.maxsidebar)
        self.maxlogowidget.setObjectName(u"maxlogowidget")
        self.horizontalLayout_2 = QHBoxLayout(self.maxlogowidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.maxlogo = QLabel(self.maxlogowidget)
        self.maxlogo.setObjectName(u"maxlogo")
        self.maxlogo.setMaximumSize(QSize(120, 50))
        self.maxlogo.setPixmap(QPixmap(u":/newPrefix/logomax.png"))
        self.maxlogo.setScaledContents(True)
        self.maxlogo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.maxlogo)


        self.verticalLayout_50.addWidget(self.maxlogowidget)


        self.verticalLayout_30.addLayout(self.verticalLayout_50)

        self.homebtn = QToolButton(self.maxsidebar)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.homebtn)
        self.homebtn.setObjectName(u"homebtn")
        sizePolicy.setHeightForWidth(self.homebtn.sizePolicy().hasHeightForWidth())
        self.homebtn.setSizePolicy(sizePolicy)
        self.homebtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.homebtn.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/dashboardlight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/dashboarddark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon3.addFile(u":/dashboarddark.svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.homebtn.setIcon(icon3)
        self.homebtn.setCheckable(True)
        self.homebtn.setChecked(True)
        self.homebtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.homebtn.setAutoRaise(False)
        self.homebtn.setArrowType(Qt.ArrowType.NoArrow)

        self.verticalLayout_30.addWidget(self.homebtn)

        self.analyticsbtn = QToolButton(self.maxsidebar)
        self.buttonGroup.addButton(self.analyticsbtn)
        self.analyticsbtn.setObjectName(u"analyticsbtn")
        sizePolicy.setHeightForWidth(self.analyticsbtn.sizePolicy().hasHeightForWidth())
        self.analyticsbtn.setSizePolicy(sizePolicy)
        self.analyticsbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/analyticslight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/analyticsdark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.analyticsbtn.setIcon(icon4)
        self.analyticsbtn.setCheckable(True)
        self.analyticsbtn.setChecked(False)
        self.analyticsbtn.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.analyticsbtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_30.addWidget(self.analyticsbtn)

        self.reportbtn = QToolButton(self.maxsidebar)
        self.buttonGroup.addButton(self.reportbtn)
        self.reportbtn.setObjectName(u"reportbtn")
        sizePolicy.setHeightForWidth(self.reportbtn.sizePolicy().hasHeightForWidth())
        self.reportbtn.setSizePolicy(sizePolicy)
        self.reportbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/monitoringlight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/monitoringlight.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon5.addFile(u":/monitoringdark.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.reportbtn.setIcon(icon5)
        self.reportbtn.setCheckable(True)
        self.reportbtn.setChecked(False)
        self.reportbtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_30.addWidget(self.reportbtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_2)

        self.logoutbtn = QToolButton(self.maxsidebar)
        self.logoutbtn.setObjectName(u"logoutbtn")
        sizePolicy.setHeightForWidth(self.logoutbtn.sizePolicy().hasHeightForWidth())
        self.logoutbtn.setSizePolicy(sizePolicy)
        self.logoutbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logoutbtn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/logout_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/logoutlight.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.logoutbtn.setIcon(icon6)
        self.logoutbtn.setCheckable(False)
        self.logoutbtn.setChecked(False)
        self.logoutbtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_30.addWidget(self.logoutbtn)


        self.verticalLayout_29.addLayout(self.verticalLayout_30)


        self.horizontalLayout_31.addWidget(self.maxsidebar)


        self.sidebarlayout.addWidget(self.sidebarwidget)


        self.horizontalLayout_6.addLayout(self.sidebarlayout)

        self.tabframe = QFrame(self.centralwidget)
        self.tabframe.setObjectName(u"tabframe")
        self.tabframe.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.verticalLayout_2 = QVBoxLayout(self.tabframe)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dashboardwidget = QWidget(self.tabframe)
        self.dashboardwidget.setObjectName(u"dashboardwidget")
        self.dashboardwidget.setMinimumSize(QSize(0, 40))
        self.dashboardwidget.setMaximumSize(QSize(16777215, 40))
        self.dashboardwidget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(191, 191, 191);}")
        self.horizontalLayout_24 = QHBoxLayout(self.dashboardwidget)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.menubtn = QToolButton(self.dashboardwidget)
        self.menubtn.setObjectName(u"menubtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menubtn.sizePolicy().hasHeightForWidth())
        self.menubtn.setSizePolicy(sizePolicy1)
        self.menubtn.setMinimumSize(QSize(25, 25))
        self.menubtn.setMaximumSize(QSize(20, 20))
        self.menubtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.menubtn.setAutoFillBackground(False)
        self.menubtn.setStyleSheet(u"QToolButton {\n"
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
"")
        icon7 = QIcon()
        icon7.addFile(u":/menudark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menubtn.setIcon(icon7)
        self.menubtn.setIconSize(QSize(15, 15))
        self.menubtn.setCheckable(True)
        self.menubtn.setChecked(False)
        self.menubtn.setAutoExclusive(False)
        self.menubtn.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.menubtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        self.menubtn.setAutoRaise(True)

        self.horizontalLayout_16.addWidget(self.menubtn)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 6, -1, -1)
        self.menulabel = QLabel(self.dashboardwidget)
        self.menulabel.setObjectName(u"menulabel")
        sizePolicy1.setHeightForWidth(self.menulabel.sizePolicy().hasHeightForWidth())
        self.menulabel.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setWeight(QFont.Medium)
        font1.setItalic(False)
        self.menulabel.setFont(font1)
        self.menulabel.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 500 20px \"Inter\";\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.menulabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_17.addWidget(self.menulabel)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_17)

        self.horizontalSpacer = QSpacerItem(554, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer)

        self.notificationsbtn = QToolButton(self.dashboardwidget)
        self.notificationsbtn.setObjectName(u"notificationsbtn")
        self.notificationsbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.notificationsbtn.setStyleSheet(u"border: none;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/notificationdark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationsbtn.setIcon(icon8)
        self.notificationsbtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.notificationsbtn)

        self.profilebtn = QToolButton(self.dashboardwidget)
        self.profilebtn.setObjectName(u"profilebtn")
        self.profilebtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.profilebtn.setStyleSheet(u"border: none;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/profiledark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profilebtn.setIcon(icon9)
        self.profilebtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.profilebtn)

        self.morebtn = QToolButton(self.dashboardwidget)
        self.morebtn.setObjectName(u"morebtn")
        self.morebtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.morebtn.setStyleSheet(u"border: none;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/morepurple.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.morebtn.setIcon(icon10)
        self.morebtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.morebtn)


        self.verticalLayout.addWidget(self.dashboardwidget)

        self.tab = QStackedWidget(self.tabframe)
        self.tab.setObjectName(u"tab")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_3 = QVBoxLayout(self.page_1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page1_scrollarea = QScrollArea(self.page_1)
        self.page1_scrollarea.setObjectName(u"page1_scrollarea")
        self.page1_scrollarea.setStyleSheet(u"\n"
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
"")
        self.page1_scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.page1_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.page1_scrollarea.setWidgetResizable(True)
        self.page1_scrollarea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_1 = QWidget()
        self.scrollAreaWidgetContents_1.setObjectName(u"scrollAreaWidgetContents_1")
        self.scrollAreaWidgetContents_1.setGeometry(QRect(0, 0, 779, 821))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_1)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(20, 15, 20, 15)
        self.greetlayout = QVBoxLayout()
        self.greetlayout.setSpacing(0)
        self.greetlayout.setObjectName(u"greetlayout")
        self.greetlayout.setContentsMargins(20, 0, -1, -1)
        self.greethello = QLabel(self.scrollAreaWidgetContents_1)
        self.greethello.setObjectName(u"greethello")
        self.greethello.setMinimumSize(QSize(0, 0))
        self.greethello.setStyleSheet(u"color: rgb(212, 106, 146);\n"
"background-color: transparent;\n"
"font: 600 20px \"Inter\";")

        self.greetlayout.addWidget(self.greethello)

        self.user = QLabel(self.scrollAreaWidgetContents_1)
        self.user.setObjectName(u"user")
        sizePolicy1.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setBold(True)
        font2.setItalic(False)
        self.user.setFont(font2)
        self.user.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 700 40px \"Inter\";\n"
"background-color: transparent\n"
"")
        self.user.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.greetlayout.addWidget(self.user)


        self.verticalLayout_26.addLayout(self.greetlayout)

        self.budgetsavingslayout = QHBoxLayout()
        self.budgetsavingslayout.setSpacing(10)
        self.budgetsavingslayout.setObjectName(u"budgetsavingslayout")
        self.budgetsavingslayout.setContentsMargins(-1, 0, -1, -1)
        self.totalbudgetbox = QGroupBox(self.scrollAreaWidgetContents_1)
        self.totalbudgetbox.setObjectName(u"totalbudgetbox")
        self.totalbudgetbox.setMinimumSize(QSize(300, 120))
        self.totalbudgetbox.setStyleSheet(u"background-color: rgb(244, 212, 212);\n"
"\n"
"border-radius: 30px;\n"
"\n"
"")
        self.verticalLayout_25 = QVBoxLayout(self.totalbudgetbox)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.layout_1 = QHBoxLayout()
        self.layout_1.setSpacing(0)
        self.layout_1.setObjectName(u"layout_1")
        self.layout_1.setContentsMargins(20, 10, -1, -1)
        self.totalbudgetlbl = QLabel(self.totalbudgetbox)
        self.totalbudgetlbl.setObjectName(u"totalbudgetlbl")
        self.totalbudgetlbl.setMinimumSize(QSize(0, 30))
        self.totalbudgetlbl.setMaximumSize(QSize(16777215, 25))
        self.totalbudgetlbl.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 700 18px \"Inter\";")
        self.totalbudgetlbl.setTextFormat(Qt.TextFormat.MarkdownText)
        self.totalbudgetlbl.setScaledContents(False)
        self.totalbudgetlbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.totalbudgetlbl.setIndent(0)

        self.layout_1.addWidget(self.totalbudgetlbl)


        self.verticalLayout_25.addLayout(self.layout_1)

        self.layout_2 = QHBoxLayout()
        self.layout_2.setObjectName(u"layout_2")
        self.layout_2.setContentsMargins(-1, 15, -1, -1)
        self.budgetvalue = QLabel(self.totalbudgetbox)
        self.budgetvalue.setObjectName(u"budgetvalue")
        font3 = QFont()
        font3.setFamilies([u"inter"])
        font3.setBold(True)
        font3.setItalic(False)
        self.budgetvalue.setFont(font3)
        self.budgetvalue.setStyleSheet(u"color: rgb(167, 83, 115);\n"
"background:transparent;\n"
"font: 700 45px \"inter\";\n"
"")
        self.budgetvalue.setFrameShape(QFrame.Shape.NoFrame)
        self.budgetvalue.setFrameShadow(QFrame.Shadow.Sunken)
        self.budgetvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_2.addWidget(self.budgetvalue)


        self.verticalLayout_25.addLayout(self.layout_2)

        self.layout_3 = QHBoxLayout()
        self.layout_3.setSpacing(20)
        self.layout_3.setObjectName(u"layout_3")
        self.layout_3.setContentsMargins(20, -1, -1, -1)
        self.progressBar = QProgressBar(self.totalbudgetbox)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setMinimumSize(QSize(0, 0))
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	\n"
"	background-color: rgb(245, 245, 245);\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	color: rgb(245, 245, 245);\n"
" 	font: 600 7pt \"Inter\";\n"
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
"")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.layout_3.addWidget(self.progressBar)

        self.viewcategorybtn = QToolButton(self.totalbudgetbox)
        self.viewcategorybtn.setObjectName(u"viewcategorybtn")
        self.viewcategorybtn.setMinimumSize(QSize(50, 50))
        self.viewcategorybtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.viewcategorybtn.setAutoFillBackground(False)
        self.viewcategorybtn.setStyleSheet(u"\n"
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
"font: 600 7pt \"Inter\";\n"
"border-radius: 25px;}\n"
" \n"
"QToolButton:hover {\n"
"	background-color: rgb(147, 73, 101);\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/walletlight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.viewcategorybtn.setIcon(icon11)
        self.viewcategorybtn.setIconSize(QSize(20, 20))
        self.viewcategorybtn.setCheckable(False)

        self.layout_3.addWidget(self.viewcategorybtn)


        self.verticalLayout_25.addLayout(self.layout_3)


        self.budgetsavingslayout.addWidget(self.totalbudgetbox)

        self.savingsbox_3 = QGroupBox(self.scrollAreaWidgetContents_1)
        self.savingsbox_3.setObjectName(u"savingsbox_3")
        self.savingsbox_3.setMinimumSize(QSize(300, 120))
        self.savingsbox_3.setStyleSheet(u"background-color: rgb(244, 212, 212);\n"
"border-radius:30px;\n"
"\n"
"")
        self.verticalLayout_28 = QVBoxLayout(self.savingsbox_3)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.layout_5 = QHBoxLayout()
        self.layout_5.setSpacing(0)
        self.layout_5.setObjectName(u"layout_5")
        self.layout_5.setContentsMargins(-1, 10, -1, -1)
        self.savingslbl = QLabel(self.savingsbox_3)
        self.savingslbl.setObjectName(u"savingslbl")
        self.savingslbl.setMinimumSize(QSize(0, 30))
        self.savingslbl.setMaximumSize(QSize(16777215, 25))
        self.savingslbl.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 600 18px \"Inter\";")
        self.savingslbl.setTextFormat(Qt.TextFormat.MarkdownText)
        self.savingslbl.setScaledContents(False)
        self.savingslbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.savingslbl.setIndent(20)

        self.layout_5.addWidget(self.savingslbl)


        self.verticalLayout_28.addLayout(self.layout_5)

        self.layout_6 = QHBoxLayout()
        self.layout_6.setObjectName(u"layout_6")
        self.layout_6.setContentsMargins(-1, 15, -1, -1)
        self.savingsvalue = QLabel(self.savingsbox_3)
        self.savingsvalue.setObjectName(u"savingsvalue")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.savingsvalue.sizePolicy().hasHeightForWidth())
        self.savingsvalue.setSizePolicy(sizePolicy3)
        self.savingsvalue.setFont(font3)
        self.savingsvalue.setStyleSheet(u"color: rgb(212, 106, 146);\n"
"background-color: transparent;\n"
"font: 700 45px \"inter\";\n"
"")
        self.savingsvalue.setFrameShape(QFrame.Shape.NoFrame)
        self.savingsvalue.setFrameShadow(QFrame.Shadow.Sunken)
        self.savingsvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.savingsvalue.setWordWrap(True)

        self.layout_6.addWidget(self.savingsvalue)


        self.verticalLayout_28.addLayout(self.layout_6)

        self.hlayout7 = QHBoxLayout()
        self.hlayout7.setObjectName(u"hlayout7")
        self.hlayout7.setContentsMargins(20, -1, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hlayout7.addItem(self.horizontalSpacer_2)

        self.savingsbtn = QToolButton(self.savingsbox_3)
        self.savingsbtn.setObjectName(u"savingsbtn")
        self.savingsbtn.setMinimumSize(QSize(50, 50))
        self.savingsbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.savingsbtn.setAutoFillBackground(False)
        self.savingsbtn.setStyleSheet(u"QToolButton{\n"
"\n"
"background: qradialgradient(\n"
"            cx: 0.5, cy: 0.5, radius: 0.6,\n"
"            fx: 0.5, fy: 0.5,\n"
"		stop: 0 #a75373\n"
"        stop: 1 #d46a92\n"
"    );\n"
"color: rgb(167, 83, 115);\n"
"border-color: rgb(244, 212, 212);\n"
"text-align: center;\n"
"font: 600 7pt \"Inter\";\n"
"border-radius: 25px;}\n"
"\n"
"QToolButton:hover {\n"
"    \n"
"	background-color: rgb(177, 88, 122);\n"
"}\n"
"  \n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/savingslight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.savingsbtn.setIcon(icon12)
        self.savingsbtn.setIconSize(QSize(20, 20))
        self.savingsbtn.setCheckable(False)

        self.hlayout7.addWidget(self.savingsbtn)


        self.verticalLayout_28.addLayout(self.hlayout7)


        self.budgetsavingslayout.addWidget(self.savingsbox_3)


        self.verticalLayout_26.addLayout(self.budgetsavingslayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 10, 0, 10)
        self.expensebox = QGroupBox(self.scrollAreaWidgetContents_1)
        self.expensebox.setObjectName(u"expensebox")
        self.expensebox.setMinimumSize(QSize(300, 80))
        font4 = QFont()
        font4.setPointSize(12)
        self.expensebox.setFont(font4)
        self.expensebox.setStyleSheet(u"text-align: center;\n"
"background-color: rgb(167, 83, 115);\n"
"border-radius: 20px")
        self.verticalLayout_31 = QVBoxLayout(self.expensebox)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(40, -1, 30, 0)
        self.expensevalue = QLabel(self.expensebox)
        self.expensevalue.setObjectName(u"expensevalue")
        sizePolicy.setHeightForWidth(self.expensevalue.sizePolicy().hasHeightForWidth())
        self.expensevalue.setSizePolicy(sizePolicy)
        self.expensevalue.setMaximumSize(QSize(16777215, 50))
        self.expensevalue.setFont(font3)
        self.expensevalue.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"font: 700 30px \"inter\";\n"
"")
        self.expensevalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.expensevalue.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.expensevalue)

        self.expenselbl = QLabel(self.expensebox)
        self.expenselbl.setObjectName(u"expenselbl")
        self.expenselbl.setMaximumSize(QSize(16777215, 20))
        self.expenselbl.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"font: 600 16px \"Inter\";\n"
"text-align: center;")
        self.expenselbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.expenselbl)


        self.verticalLayout_31.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_8.addWidget(self.expensebox)

        self.incomebox = QGroupBox(self.scrollAreaWidgetContents_1)
        self.incomebox.setObjectName(u"incomebox")
        self.incomebox.setMinimumSize(QSize(300, 80))
        self.incomebox.setFont(font4)
        self.incomebox.setStyleSheet(u"text-align: center;\n"
"background-color: rgb(167, 83, 115);\n"
"border-radius: 20px")
        self.verticalLayout_55 = QVBoxLayout(self.incomebox)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(40, -1, 30, 0)
        self.incomevalue = QLabel(self.incomebox)
        self.incomevalue.setObjectName(u"incomevalue")
        sizePolicy.setHeightForWidth(self.incomevalue.sizePolicy().hasHeightForWidth())
        self.incomevalue.setSizePolicy(sizePolicy)
        self.incomevalue.setMaximumSize(QSize(16777215, 50))
        self.incomevalue.setFont(font3)
        self.incomevalue.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"font: 700 30px \"inter\";\n"
"")
        self.incomevalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.incomevalue.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.incomevalue)

        self.incomelbl = QLabel(self.incomebox)
        self.incomelbl.setObjectName(u"incomelbl")
        self.incomelbl.setMaximumSize(QSize(16777215, 20))
        self.incomelbl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.incomelbl.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"font: 600 16px \"Inter\";\n"
"text-align: center;")
        self.incomelbl.setTextFormat(Qt.TextFormat.AutoText)
        self.incomelbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.incomelbl)


        self.verticalLayout_55.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_8.addWidget(self.incomebox)


        self.verticalLayout_26.addLayout(self.horizontalLayout_8)

        self.activitylayout = QVBoxLayout()
        self.activitylayout.setObjectName(u"activitylayout")
        self.activitylayout.setContentsMargins(0, 10, 0, 10)
        self.activitybox = QGroupBox(self.scrollAreaWidgetContents_1)
        self.activitybox.setObjectName(u"activitybox")
        self.activitybox.setMinimumSize(QSize(0, 381))
        self.activitybox.setStyleSheet(u"background-color: rgb(108, 68, 100);\n"
"border-radius:20\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.activitybox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, 15, 20, -1)
        self.activitylbl = QLabel(self.activitybox)
        self.activitylbl.setObjectName(u"activitylbl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.activitylbl.sizePolicy().hasHeightForWidth())
        self.activitylbl.setSizePolicy(sizePolicy4)
        self.activitylbl.setFont(font2)
        self.activitylbl.setStyleSheet(u"color: rgb(254, 250, 250);\n"
"font: 700 30px \"Inter\";")

        self.horizontalLayout_13.addWidget(self.activitylbl)

        self.amountedit = QLineEdit(self.activitybox)
        self.amountedit.setObjectName(u"amountedit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.amountedit.sizePolicy().hasHeightForWidth())
        self.amountedit.setSizePolicy(sizePolicy5)
        self.amountedit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(254, 250, 250);\n"
"                padding: 8px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 7px;\n"
"                font-size: 10px;\n"
"            }")

        self.horizontalLayout_13.addWidget(self.amountedit)

        self.descriptionedit = QLineEdit(self.activitybox)
        self.descriptionedit.setObjectName(u"descriptionedit")
        sizePolicy5.setHeightForWidth(self.descriptionedit.sizePolicy().hasHeightForWidth())
        self.descriptionedit.setSizePolicy(sizePolicy5)
        self.descriptionedit.setStyleSheet(u"QLineEdit {\n"
"	\n"
"	\n"
"					background-color: rgb(254, 250, 250);\n"
"                padding: 8px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 7px;\n"
"                font-size: 10px;\n"
"\n"
"            }")

        self.horizontalLayout_13.addWidget(self.descriptionedit)

        self.categorycombo = QComboBox(self.activitybox)
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.addItem("")
        self.categorycombo.setObjectName(u"categorycombo")
        sizePolicy5.setHeightForWidth(self.categorycombo.sizePolicy().hasHeightForWidth())
        self.categorycombo.setSizePolicy(sizePolicy5)
        self.categorycombo.setStyleSheet(u"QComboBox{\n"
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
"            }")
        self.categorycombo.setEditable(False)
        self.categorycombo.setFrame(True)

        self.horizontalLayout_13.addWidget(self.categorycombo)

        self.addtransbtn = QPushButton(self.activitybox)
        self.addtransbtn.setObjectName(u"addtransbtn")
        sizePolicy5.setHeightForWidth(self.addtransbtn.sizePolicy().hasHeightForWidth())
        self.addtransbtn.setSizePolicy(sizePolicy5)
        self.addtransbtn.setMinimumSize(QSize(90, 34))
        self.addtransbtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addtransbtn.setAutoFillBackground(False)
        self.addtransbtn.setStyleSheet(u"\n"
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
"}")
        self.addtransbtn.setCheckable(True)
        self.addtransbtn.setFlat(True)

        self.horizontalLayout_13.addWidget(self.addtransbtn)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.tablelayout = QVBoxLayout()
        self.tablelayout.setObjectName(u"tablelayout")
        self.tablelayout.setContentsMargins(15, 15, 15, 16)
        self.tablebox = QGroupBox(self.activitybox)
        self.tablebox.setObjectName(u"tablebox")
        sizePolicy.setHeightForWidth(self.tablebox.sizePolicy().hasHeightForWidth())
        self.tablebox.setSizePolicy(sizePolicy)
        self.tablebox.setMaximumSize(QSize(16777215, 291))
        self.tablebox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:20\n"
"")
        self.verticalLayout_14 = QVBoxLayout(self.tablebox)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.activities = QTableView(self.tablebox)
        self.activities.setObjectName(u"activities")
        sizePolicy.setHeightForWidth(self.activities.sizePolicy().hasHeightForWidth())
        self.activities.setSizePolicy(sizePolicy)
        self.activities.horizontalHeader().setCascadingSectionResizes(True)
        self.activities.horizontalHeader().setDefaultSectionSize(120)

        self.verticalLayout_14.addWidget(self.activities)


        self.tablelayout.addWidget(self.tablebox)


        self.verticalLayout_10.addLayout(self.tablelayout)


        self.activitylayout.addWidget(self.activitybox)


        self.verticalLayout_26.addLayout(self.activitylayout)

        self.page1_scrollarea.setWidget(self.scrollAreaWidgetContents_1)

        self.verticalLayout_3.addWidget(self.page1_scrollarea)

        self.tab.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 15, 10, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(120)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, 10)
        self.incomebox_34 = QGroupBox(self.page_3)
        self.incomebox_34.setObjectName(u"incomebox_34")
        self.incomebox_34.setMinimumSize(QSize(720, 70))
        self.incomebox_34.setMaximumSize(QSize(700, 70))
        self.incomebox_34.setStyleSheet(u"background-color: rgb(167, 83, 115);\n"
"border-radius:20\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.incomebox_34)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(15, -1, 20, -1)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.comboBox_14 = QComboBox(self.incomebox_34)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setStyleSheet(u"QComboBox{\n"
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
"}")
        self.comboBox_14.setEditable(False)
        self.comboBox_14.setFrame(True)

        self.horizontalLayout_10.addWidget(self.comboBox_14)

        self.comboBox_15 = QComboBox(self.incomebox_34)
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.setObjectName(u"comboBox_15")
        self.comboBox_15.setStyleSheet(u"QComboBox{\n"
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
"}")
        self.comboBox_15.setEditable(False)
        self.comboBox_15.setFrame(True)

        self.horizontalLayout_10.addWidget(self.comboBox_15)

        self.editbudgetbtn_11 = QPushButton(self.incomebox_34)
        self.editbudgetbtn_11.setObjectName(u"editbudgetbtn_11")
        sizePolicy.setHeightForWidth(self.editbudgetbtn_11.sizePolicy().hasHeightForWidth())
        self.editbudgetbtn_11.setSizePolicy(sizePolicy)
        self.editbudgetbtn_11.setMaximumSize(QSize(70, 34))
        self.editbudgetbtn_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.editbudgetbtn_11.setAutoFillBackground(False)
        self.editbudgetbtn_11.setStyleSheet(u"\n"
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
"}")
        self.editbudgetbtn_11.setCheckable(True)
        self.editbudgetbtn_11.setFlat(True)

        self.horizontalLayout_10.addWidget(self.editbudgetbtn_11)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(30, -1, 10, -1)
        self.greetuser_16 = QLabel(self.incomebox_34)
        self.greetuser_16.setObjectName(u"greetuser_16")
        sizePolicy1.setHeightForWidth(self.greetuser_16.sizePolicy().hasHeightForWidth())
        self.greetuser_16.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"Inter"])
        font5.setWeight(QFont.DemiBold)
        font5.setItalic(False)
        self.greetuser_16.setFont(font5)
        self.greetuser_16.setStyleSheet(u"\n"
"color: rgb(254, 250, 250);\n"
"font: 600 30px \"Inter\";\n"
"background-color: transparent\n"
"")
        self.greetuser_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.greetuser_16)


        self.horizontalLayout_10.addLayout(self.verticalLayout_24)


        self.verticalLayout_19.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_7.addWidget(self.incomebox_34)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.scrollArea_4 = QScrollArea(self.page_3)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 10;\n"
"border: none;")
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 166, 540))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"border-radius:15")
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 20, 20, 20)
        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(0, 500))
        self.groupBox_8.setStyleSheet(u"background-color: rgb(254, 250, 250);\n"
"border-radius: 25")
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.incomebox_38 = QGroupBox(self.groupBox_8)
        self.incomebox_38.setObjectName(u"incomebox_38")
        self.incomebox_38.setMinimumSize(QSize(0, 200))
        self.incomebox_38.setMaximumSize(QSize(16777215, 500))
        self.incomebox_38.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(229, 229, 229);\n"
"border-radius:20;\n"
"border: 1px solid\n"
"")
        self.verticalLayout_33 = QVBoxLayout(self.incomebox_38)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(15, -1, 20, -1)
        self.tableWidget_2 = QTableWidget(self.incomebox_38)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget_2.rowCount() < 5):
            self.tableWidget_2.setRowCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem8)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_33.addWidget(self.tableWidget_2)


        self.verticalLayout_27.addWidget(self.incomebox_38)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.incomebox_39 = QGroupBox(self.groupBox_8)
        self.incomebox_39.setObjectName(u"incomebox_39")
        self.incomebox_39.setMinimumSize(QSize(0, 200))
        self.incomebox_39.setStyleSheet(u"background-color: rgb(167, 83, 115);\n"
"border-radius:20\n"
"")
        self.verticalLayout_56 = QVBoxLayout(self.incomebox_39)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(15, -1, 20, -1)

        self.horizontalLayout_18.addWidget(self.incomebox_39)

        self.incomebox_40 = QGroupBox(self.groupBox_8)
        self.incomebox_40.setObjectName(u"incomebox_40")
        self.incomebox_40.setMinimumSize(QSize(0, 200))
        self.incomebox_40.setStyleSheet(u"background-color: rgb(167, 83, 115);\n"
"border-radius:20\n"
"")
        self.verticalLayout_57 = QVBoxLayout(self.incomebox_40)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(15, -1, 20, -1)

        self.horizontalLayout_18.addWidget(self.incomebox_40)


        self.verticalLayout_27.addLayout(self.horizontalLayout_18)


        self.verticalLayout_13.addWidget(self.groupBox_8)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_11.addWidget(self.scrollArea_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_11)

        self.tab.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.page_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea_2 = QScrollArea(self.page_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"\n"
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
"")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 669, 826))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(25, -1, 20, -1)
        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setMinimumSize(QSize(300, 247))
        self.groupBox_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15")

        self.horizontalLayout_19.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(300, 247))
        self.groupBox_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15")

        self.horizontalLayout_19.addWidget(self.groupBox_10)


        self.verticalLayout_16.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(25, -1, 20, -1)
        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(300, 247))
        self.groupBox_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15")

        self.horizontalLayout_20.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy)
        self.groupBox_12.setMinimumSize(QSize(300, 247))
        self.groupBox_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15")

        self.horizontalLayout_20.addWidget(self.groupBox_12)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(25, -1, 20, 50)
        self.groupBox_13 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(300, 247))
        self.groupBox_13.setMaximumSize(QSize(800, 247))
        self.groupBox_13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15")

        self.horizontalLayout_21.addWidget(self.groupBox_13)


        self.verticalLayout_16.addLayout(self.horizontalLayout_21)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_15.addWidget(self.scrollArea_2)

        self.tab.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.tab)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_6.addWidget(self.tabframe)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minlogo.setText("")
        self.homebtn_min.setText(QCoreApplication.translate("MainWindow", u"   Dashboard", None))
        self.analyticsbtn_min.setText(QCoreApplication.translate("MainWindow", u"   Analytics", None))
        self.reportbtn_min.setText(QCoreApplication.translate("MainWindow", u"   Reports", None))
        self.maxlogo.setText("")
        self.homebtn.setText(QCoreApplication.translate("MainWindow", u"   Dashboard", None))
        self.analyticsbtn.setText(QCoreApplication.translate("MainWindow", u"   Analytics", None))
        self.reportbtn.setText(QCoreApplication.translate("MainWindow", u"   Reports", None))
        self.logoutbtn.setText(QCoreApplication.translate("MainWindow", u"   Logout", None))
        self.menubtn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menulabel.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.notificationsbtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.profilebtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.morebtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.greethello.setText(QCoreApplication.translate("MainWindow", u"Hello,", None))
        self.user.setText(QCoreApplication.translate("MainWindow", u"Oscar Pol", None))
        self.totalbudgetbox.setTitle("")
        self.totalbudgetlbl.setText(QCoreApplication.translate("MainWindow", u"Current Budget", None))
        self.budgetvalue.setText(QCoreApplication.translate("MainWindow", u"\u20b1 54300.00", None))
        self.viewcategorybtn.setText(QCoreApplication.translate("MainWindow", u"View Category", None))
        self.savingsbox_3.setTitle("")
        self.savingslbl.setText(QCoreApplication.translate("MainWindow", u"Savings", None))
        self.savingsvalue.setText(QCoreApplication.translate("MainWindow", u"\u20b1 34500.00", None))
        self.savingsbtn.setText(QCoreApplication.translate("MainWindow", u"View Category", None))
        self.expensebox.setTitle("")
        self.expensevalue.setText(QCoreApplication.translate("MainWindow", u"\u20b1 00.00", None))
        self.expenselbl.setText(QCoreApplication.translate("MainWindow", u"Total Expense", None))
        self.incomebox.setTitle("")
        self.incomevalue.setText(QCoreApplication.translate("MainWindow", u"\u20b1 00.00", None))
        self.incomelbl.setText(QCoreApplication.translate("MainWindow", u"Total Income", None))
        self.activitybox.setTitle("")
        self.activitylbl.setText(QCoreApplication.translate("MainWindow", u"Recent Activity", None))
        self.amountedit.setText("")
        self.amountedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.descriptionedit.setText("")
        self.descriptionedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.categorycombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Food", None))
        self.categorycombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Utilities", None))
        self.categorycombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Health & Wellness", None))
        self.categorycombo.setItemText(3, QCoreApplication.translate("MainWindow", u"Personal & Lifestyle", None))
        self.categorycombo.setItemText(4, QCoreApplication.translate("MainWindow", u"Education", None))
        self.categorycombo.setItemText(5, QCoreApplication.translate("MainWindow", u"Transportation", None))
        self.categorycombo.setItemText(6, QCoreApplication.translate("MainWindow", u"Others", None))

        self.categorycombo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.addtransbtn.setText(QCoreApplication.translate("MainWindow", u"Add Transaction", None))
        self.tablebox.setTitle("")
        self.incomebox_34.setTitle("")
        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"January", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"February", None))

        self.comboBox_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Month", None))
        self.comboBox_15.setItemText(0, QCoreApplication.translate("MainWindow", u"Food", None))
        self.comboBox_15.setItemText(1, QCoreApplication.translate("MainWindow", u"Utilities", None))
        self.comboBox_15.setItemText(2, QCoreApplication.translate("MainWindow", u"Health & Wellness", None))
        self.comboBox_15.setItemText(3, QCoreApplication.translate("MainWindow", u"Personal & Lifestyle", None))
        self.comboBox_15.setItemText(4, QCoreApplication.translate("MainWindow", u"Education", None))
        self.comboBox_15.setItemText(5, QCoreApplication.translate("MainWindow", u"Transportation", None))
        self.comboBox_15.setItemText(6, QCoreApplication.translate("MainWindow", u"Others", None))

        self.comboBox_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.editbudgetbtn_11.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.greetuser_16.setText(QCoreApplication.translate("MainWindow", u"Periodic Report", None))
        self.groupBox_8.setTitle("")
        self.incomebox_38.setTitle("")
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem4 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.incomebox_39.setTitle("")
        self.incomebox_40.setTitle("")
        self.groupBox_9.setTitle("")
        self.groupBox_10.setTitle("")
        self.groupBox_11.setTitle("")
        self.groupBox_12.setTitle("")
        self.groupBox_13.setTitle("")
    # retranslateUi

