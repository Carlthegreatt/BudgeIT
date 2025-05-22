# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'currentgjpJIn.ui'
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
    QTableView, QToolButton, QVBoxLayout, QWidget)
import icons_rc
import icons_rc
import images_rc
import dsad_rc
import images_rc
import images_rc

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
        self.minlogo.setMaximumSize(QSize(50, 40))
        self.minlogo.setPixmap(QPixmap(u":/images/logo (2).png"))
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
        self.maxlogowidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.maxlogowidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.maxlogo = QLabel(self.maxlogowidget)
        self.maxlogo.setObjectName(u"maxlogo")
        self.maxlogo.setMaximumSize(QSize(110, 40))
        self.maxlogo.setPixmap(QPixmap(u":/images/logomax.png"))
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
        self.tab.setStyleSheet(u"background-color: rgb(245, 245, 245);")
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
"font: 700 20px \"inter\";\n"
"")
        self.expensevalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.expensevalue.setWordWrap(False)

        self.horizontalLayout_9.addWidget(self.expensevalue)

        self.expenselbl = QLabel(self.expensebox)
        self.expenselbl.setObjectName(u"expenselbl")
        self.expenselbl.setMaximumSize(QSize(16777215, 50))
        self.expenselbl.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"font: 600 16px \"Inter\";\n"
"text-align: center;")
        self.expenselbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.expenselbl.setWordWrap(True)

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
"font: 700 20px \"inter\";\n"
"")
        self.incomevalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.incomevalue.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.incomevalue)

        self.incomelbl = QLabel(self.incomebox)
        self.incomelbl.setObjectName(u"incomelbl")
        self.incomelbl.setMaximumSize(QSize(16777215, 50))
        self.incomelbl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.incomelbl.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"font: 600 16px \"Inter\";\n"
"text-align: center;")
        self.incomelbl.setTextFormat(Qt.TextFormat.AutoText)
        self.incomelbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.incomelbl.setWordWrap(True)

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
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 777, 786))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(60, -1, 60, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.categorycombo_3 = QComboBox(self.scrollAreaWidgetContents)
        self.categorycombo_3.addItem("")
        self.categorycombo_3.addItem("")
        self.categorycombo_3.addItem("")
        self.categorycombo_3.addItem("")
        self.categorycombo_3.addItem("")
        self.categorycombo_3.addItem("")
        self.categorycombo_3.addItem("")
        self.categorycombo_3.addItem("")
        self.categorycombo_3.addItem("")
        self.categorycombo_3.addItem("")
        self.categorycombo_3.addItem("")
        self.categorycombo_3.addItem("")
        self.categorycombo_3.setObjectName(u"categorycombo_3")
        sizePolicy5.setHeightForWidth(self.categorycombo_3.sizePolicy().hasHeightForWidth())
        self.categorycombo_3.setSizePolicy(sizePolicy5)
        self.categorycombo_3.setStyleSheet(u"QComboBox{\n"
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
"    min-height: 20px;\n"
"    border-radius: 10000px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"}")
        self.categorycombo_3.setEditable(False)
        self.categorycombo_3.setFrame(True)

        self.horizontalLayout_4.addWidget(self.categorycombo_3)

        self.categorycombo_4 = QComboBox(self.scrollAreaWidgetContents)
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.addItem("")
        self.categorycombo_4.setObjectName(u"categorycombo_4")
        sizePolicy5.setHeightForWidth(self.categorycombo_4.sizePolicy().hasHeightForWidth())
        self.categorycombo_4.setSizePolicy(sizePolicy5)
        self.categorycombo_4.setStyleSheet(u"QComboBox{\n"
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
"    min-height: 20px;\n"
"    border-radius: 10000px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"}")
        self.categorycombo_4.setEditable(False)
        self.categorycombo_4.setFrame(True)

        self.horizontalLayout_4.addWidget(self.categorycombo_4)

        self.categorycombo_5 = QComboBox(self.scrollAreaWidgetContents)
        self.categorycombo_5.addItem("")
        self.categorycombo_5.addItem("")
        self.categorycombo_5.setObjectName(u"categorycombo_5")
        sizePolicy5.setHeightForWidth(self.categorycombo_5.sizePolicy().hasHeightForWidth())
        self.categorycombo_5.setSizePolicy(sizePolicy5)
        self.categorycombo_5.setStyleSheet(u"QComboBox{\n"
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
"    min-height: 20px;\n"
"    border-radius: 10000px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"}")
        self.categorycombo_5.setEditable(False)
        self.categorycombo_5.setFrame(True)

        self.horizontalLayout_4.addWidget(self.categorycombo_5)

        self.addtransbtn_3 = QPushButton(self.scrollAreaWidgetContents)
        self.addtransbtn_3.setObjectName(u"addtransbtn_3")
        sizePolicy5.setHeightForWidth(self.addtransbtn_3.sizePolicy().hasHeightForWidth())
        self.addtransbtn_3.setSizePolicy(sizePolicy5)
        self.addtransbtn_3.setMinimumSize(QSize(90, 34))
        self.addtransbtn_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addtransbtn_3.setAutoFillBackground(False)
        self.addtransbtn_3.setStyleSheet(u"\n"
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
        self.addtransbtn_3.setCheckable(True)
        self.addtransbtn_3.setFlat(True)

        self.horizontalLayout_4.addWidget(self.addtransbtn_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 700))
        self.widget.setMaximumSize(QSize(16777215, 900))
        self.widget.setStyleSheet(u"background-color: rgb(254, 254, 254);\n"
"border-radius: 30\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 200))
        self.widget_3.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")

        self.horizontalLayout_10.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")

        self.horizontalLayout_10.addWidget(self.widget_5)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)


        self.verticalLayout_11.addWidget(self.widget_3)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(30, -1, -1, -1)
        self.user_2 = QLabel(self.widget)
        self.user_2.setObjectName(u"user_2")
        sizePolicy1.setHeightForWidth(self.user_2.sizePolicy().hasHeightForWidth())
        self.user_2.setSizePolicy(sizePolicy1)
        self.user_2.setFont(font2)
        self.user_2.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 700 40px \"Inter\";\n"
"background-color: transparent\n"
"")
        self.user_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_7.addWidget(self.user_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, -1, 20, -1)
        self.totalbudgetbox_2 = QGroupBox(self.widget)
        self.totalbudgetbox_2.setObjectName(u"totalbudgetbox_2")
        self.totalbudgetbox_2.setMinimumSize(QSize(300, 120))
        self.totalbudgetbox_2.setStyleSheet(u"background-color: rgb(244, 212, 212);\n"
"\n"
"border-radius: 30px;\n"
"\n"
"")
        self.verticalLayout_27 = QVBoxLayout(self.totalbudgetbox_2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.activities_2 = QTableView(self.totalbudgetbox_2)
        self.activities_2.setObjectName(u"activities_2")
        sizePolicy.setHeightForWidth(self.activities_2.sizePolicy().hasHeightForWidth())
        self.activities_2.setSizePolicy(sizePolicy)
        self.activities_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20")
        self.activities_2.horizontalHeader().setCascadingSectionResizes(True)
        self.activities_2.horizontalHeader().setDefaultSectionSize(120)

        self.verticalLayout_27.addWidget(self.activities_2)


        self.verticalLayout_8.addWidget(self.totalbudgetbox_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.verticalLayout_11.addLayout(self.verticalLayout_9)


        self.verticalLayout_6.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = QWidget(self.page_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(254, 254, 254);\n"
"border-radius: 30\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.user_3 = QLabel(self.widget_2)
        self.user_3.setObjectName(u"user_3")
        sizePolicy1.setHeightForWidth(self.user_3.sizePolicy().hasHeightForWidth())
        self.user_3.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"Inter"])
        font5.setWeight(QFont.DemiBold)
        font5.setItalic(False)
        self.user_3.setFont(font5)
        self.user_3.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 600 20px \"Inter\";\n"
"background-color: transparent\n"
"")
        self.user_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_5.addWidget(self.user_3)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 756, 707))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, -1, 10, 0)
        self.overallbudgetbox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.overallbudgetbox.setObjectName(u"overallbudgetbox")
        self.overallbudgetbox.setMinimumSize(QSize(300, 80))
        self.overallbudgetbox.setMaximumSize(QSize(16777215, 80))
        self.overallbudgetbox.setFont(font4)
        self.overallbudgetbox.setStyleSheet(u"text-align: center;\n"
"background-color: rgb(167, 83, 115);\n"
"border-radius: 20px")
        self.verticalLayout_32 = QVBoxLayout(self.overallbudgetbox)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(20)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(40, -1, 30, 0)
        self.overallbudgetvalue = QLabel(self.overallbudgetbox)
        self.overallbudgetvalue.setObjectName(u"overallbudgetvalue")
        sizePolicy.setHeightForWidth(self.overallbudgetvalue.sizePolicy().hasHeightForWidth())
        self.overallbudgetvalue.setSizePolicy(sizePolicy)
        self.overallbudgetvalue.setMaximumSize(QSize(16777215, 50))
        self.overallbudgetvalue.setFont(font3)
        self.overallbudgetvalue.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"font: 700 15px \"inter\";\n"
"")
        self.overallbudgetvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overallbudgetvalue.setWordWrap(False)

        self.horizontalLayout_18.addWidget(self.overallbudgetvalue)

        self.overallbudgetlbl = QLabel(self.overallbudgetbox)
        self.overallbudgetlbl.setObjectName(u"overallbudgetlbl")
        self.overallbudgetlbl.setMaximumSize(QSize(16777215, 50))
        self.overallbudgetlbl.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"font: 600 16px \"Inter\";\n"
"text-align: center;")
        self.overallbudgetlbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overallbudgetlbl.setWordWrap(True)

        self.horizontalLayout_18.addWidget(self.overallbudgetlbl)


        self.verticalLayout_32.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_14.addWidget(self.overallbudgetbox)

        self.expensebox_3 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.expensebox_3.setObjectName(u"expensebox_3")
        self.expensebox_3.setMinimumSize(QSize(300, 80))
        self.expensebox_3.setMaximumSize(QSize(16777215, 80))
        self.expensebox_3.setFont(font4)
        self.expensebox_3.setStyleSheet(u"text-align: center;\n"
"background-color: rgb(167, 83, 115);\n"
"border-radius: 20px")
        self.verticalLayout_33 = QVBoxLayout(self.expensebox_3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(40, -1, 30, 0)
        self.totalexpensevalue = QLabel(self.expensebox_3)
        self.totalexpensevalue.setObjectName(u"totalexpensevalue")
        sizePolicy.setHeightForWidth(self.totalexpensevalue.sizePolicy().hasHeightForWidth())
        self.totalexpensevalue.setSizePolicy(sizePolicy)
        self.totalexpensevalue.setMaximumSize(QSize(16777215, 50))
        self.totalexpensevalue.setFont(font3)
        self.totalexpensevalue.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"font: 700 15px \"inter\";\n"
"")
        self.totalexpensevalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalexpensevalue.setWordWrap(False)

        self.horizontalLayout_22.addWidget(self.totalexpensevalue)

        self.totalexpenselbl = QLabel(self.expensebox_3)
        self.totalexpenselbl.setObjectName(u"totalexpenselbl")
        self.totalexpenselbl.setMaximumSize(QSize(16777215, 50))
        self.totalexpenselbl.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"font: 600 16px \"Inter\";\n"
"text-align: center;")
        self.totalexpenselbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalexpenselbl.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.totalexpenselbl)


        self.verticalLayout_33.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_14.addWidget(self.expensebox_3)


        self.verticalLayout_16.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(10, -1, 10, 10)
        self.accumulatedsavingsbox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.accumulatedsavingsbox.setObjectName(u"accumulatedsavingsbox")
        self.accumulatedsavingsbox.setMinimumSize(QSize(300, 80))
        self.accumulatedsavingsbox.setMaximumSize(QSize(16777215, 80))
        self.accumulatedsavingsbox.setFont(font4)
        self.accumulatedsavingsbox.setStyleSheet(u"text-align: center;\n"
"background-color: #f4d4d4;\n"
"border-radius: 20px")
        self.verticalLayout_34 = QVBoxLayout(self.accumulatedsavingsbox)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(40, -1, 30, 0)
        self.accumulatedsavingvalue = QLabel(self.accumulatedsavingsbox)
        self.accumulatedsavingvalue.setObjectName(u"accumulatedsavingvalue")
        sizePolicy.setHeightForWidth(self.accumulatedsavingvalue.sizePolicy().hasHeightForWidth())
        self.accumulatedsavingvalue.setSizePolicy(sizePolicy)
        self.accumulatedsavingvalue.setMaximumSize(QSize(16777215, 50))
        self.accumulatedsavingvalue.setFont(font3)
        self.accumulatedsavingvalue.setStyleSheet(u"color: rgb(167, 83, 115);\n"
"font: 700 15px \"inter\";\n"
"")
        self.accumulatedsavingvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.accumulatedsavingvalue.setWordWrap(False)

        self.horizontalLayout_23.addWidget(self.accumulatedsavingvalue)

        self.accumulatedsavingslbl = QLabel(self.accumulatedsavingsbox)
        self.accumulatedsavingslbl.setObjectName(u"accumulatedsavingslbl")
        self.accumulatedsavingslbl.setMaximumSize(QSize(16777215, 50))
        self.accumulatedsavingslbl.setStyleSheet(u"color: rgb(167, 83, 115);\n"
"font: 600 16px \"Inter\";\n"
"text-align: center;")
        self.accumulatedsavingslbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.accumulatedsavingslbl.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.accumulatedsavingslbl)


        self.verticalLayout_34.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_21.addWidget(self.accumulatedsavingsbox)

        self.totalincomebox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.totalincomebox.setObjectName(u"totalincomebox")
        self.totalincomebox.setMinimumSize(QSize(300, 80))
        self.totalincomebox.setMaximumSize(QSize(16777215, 80))
        self.totalincomebox.setFont(font4)
        self.totalincomebox.setStyleSheet(u"text-align: center;\n"
"background-color: #f4d4d4;\n"
"border-radius: 20px")
        self.verticalLayout_35 = QVBoxLayout(self.totalincomebox)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(40, -1, 30, 0)
        self.totalincomevalue = QLabel(self.totalincomebox)
        self.totalincomevalue.setObjectName(u"totalincomevalue")
        sizePolicy.setHeightForWidth(self.totalincomevalue.sizePolicy().hasHeightForWidth())
        self.totalincomevalue.setSizePolicy(sizePolicy)
        self.totalincomevalue.setMaximumSize(QSize(16777215, 50))
        self.totalincomevalue.setFont(font3)
        self.totalincomevalue.setStyleSheet(u"color: rgb(166, 83, 115);\n"
"font: 700 15px \"inter\";\n"
"")
        self.totalincomevalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalincomevalue.setWordWrap(False)

        self.horizontalLayout_25.addWidget(self.totalincomevalue)

        self.totalincomelbl = QLabel(self.totalincomebox)
        self.totalincomelbl.setObjectName(u"totalincomelbl")
        self.totalincomelbl.setMaximumSize(QSize(16777215, 50))
        self.totalincomelbl.setStyleSheet(u"color: rgb(167, 83, 115);\n"
"font: 600 16px \"Inter\";\n"
"text-align: center;")
        self.totalincomelbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalincomelbl.setWordWrap(True)

        self.horizontalLayout_25.addWidget(self.totalincomelbl)


        self.verticalLayout_35.addLayout(self.horizontalLayout_25)


        self.horizontalLayout_21.addWidget(self.totalincomebox)


        self.verticalLayout_16.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, -1, 10, -1)
        self.transactionsummarybox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.transactionsummarybox.setObjectName(u"transactionsummarybox")
        sizePolicy.setHeightForWidth(self.transactionsummarybox.sizePolicy().hasHeightForWidth())
        self.transactionsummarybox.setSizePolicy(sizePolicy)
        self.transactionsummarybox.setMinimumSize(QSize(300, 247))
        self.transactionsummarybox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15")
        self.verticalLayout_12 = QVBoxLayout(self.transactionsummarybox)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(10, 10, -1, -1)
        self.transactionsummary = QLabel(self.transactionsummarybox)
        self.transactionsummary.setObjectName(u"transactionsummary")
        sizePolicy1.setHeightForWidth(self.transactionsummary.sizePolicy().hasHeightForWidth())
        self.transactionsummary.setSizePolicy(sizePolicy1)
        self.transactionsummary.setFont(font1)
        self.transactionsummary.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 500 15px \"Inter\";\n"
"background-color: transparent\n"
"")
        self.transactionsummary.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_30.addWidget(self.transactionsummary)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_4)


        self.verticalLayout_12.addLayout(self.horizontalLayout_30)

        self.transactionsummarywidget = QWidget(self.transactionsummarybox)
        self.transactionsummarywidget.setObjectName(u"transactionsummarywidget")

        self.verticalLayout_12.addWidget(self.transactionsummarywidget)


        self.horizontalLayout_19.addWidget(self.transactionsummarybox)

        self.budgetsummarybox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.budgetsummarybox.setObjectName(u"budgetsummarybox")
        self.budgetsummarybox.setMinimumSize(QSize(300, 247))
        self.budgetsummarybox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15")
        self.verticalLayout_13 = QVBoxLayout(self.budgetsummarybox)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(10, 10, -1, -1)
        self.budgetsummarylbl = QLabel(self.budgetsummarybox)
        self.budgetsummarylbl.setObjectName(u"budgetsummarylbl")
        sizePolicy1.setHeightForWidth(self.budgetsummarylbl.sizePolicy().hasHeightForWidth())
        self.budgetsummarylbl.setSizePolicy(sizePolicy1)
        self.budgetsummarylbl.setFont(font1)
        self.budgetsummarylbl.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 500 15px \"Inter\";\n"
"background-color: transparent\n"
"")
        self.budgetsummarylbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_27.addWidget(self.budgetsummarylbl)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_5)


        self.verticalLayout_13.addLayout(self.horizontalLayout_27)

        self.budgetsummarywidget = QWidget(self.budgetsummarybox)
        self.budgetsummarywidget.setObjectName(u"budgetsummarywidget")

        self.verticalLayout_13.addWidget(self.budgetsummarywidget)


        self.horizontalLayout_19.addWidget(self.budgetsummarybox)


        self.verticalLayout_16.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, -1, 10, -1)
        self.youractivitybox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.youractivitybox.setObjectName(u"youractivitybox")
        self.youractivitybox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15")
        self.verticalLayout_18 = QVBoxLayout(self.youractivitybox)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(10, 10, -1, -1)
        self.youractivitylbl = QLabel(self.youractivitybox)
        self.youractivitylbl.setObjectName(u"youractivitylbl")
        sizePolicy1.setHeightForWidth(self.youractivitylbl.sizePolicy().hasHeightForWidth())
        self.youractivitylbl.setSizePolicy(sizePolicy1)
        self.youractivitylbl.setFont(font1)
        self.youractivitylbl.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 500 15px \"Inter\";\n"
"background-color: transparent\n"
"")
        self.youractivitylbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_29.addWidget(self.youractivitylbl)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_6)


        self.verticalLayout_18.addLayout(self.horizontalLayout_29)

        self.youractivitywidget = QWidget(self.youractivitybox)
        self.youractivitywidget.setObjectName(u"youractivitywidget")

        self.verticalLayout_18.addWidget(self.youractivitywidget)


        self.horizontalLayout_20.addWidget(self.youractivitybox)

        self.totaltransactionbox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.totaltransactionbox.setObjectName(u"totaltransactionbox")
        sizePolicy.setHeightForWidth(self.totaltransactionbox.sizePolicy().hasHeightForWidth())
        self.totaltransactionbox.setSizePolicy(sizePolicy)
        self.totaltransactionbox.setMinimumSize(QSize(300, 247))
        self.totaltransactionbox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15")
        self.verticalLayout_17 = QVBoxLayout(self.totaltransactionbox)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(10, 10, -1, -1)
        self.totaltransactionlbl = QLabel(self.totaltransactionbox)
        self.totaltransactionlbl.setObjectName(u"totaltransactionlbl")
        sizePolicy1.setHeightForWidth(self.totaltransactionlbl.sizePolicy().hasHeightForWidth())
        self.totaltransactionlbl.setSizePolicy(sizePolicy1)
        self.totaltransactionlbl.setFont(font1)
        self.totaltransactionlbl.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 500 15px \"Inter\";\n"
"background-color: transparent\n"
"")
        self.totaltransactionlbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_28.addWidget(self.totaltransactionlbl)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_7)


        self.verticalLayout_17.addLayout(self.horizontalLayout_28)

        self.totaltransactionwidget = QWidget(self.totaltransactionbox)
        self.totaltransactionwidget.setObjectName(u"totaltransactionwidget")
        self.horizontalLayout_26 = QHBoxLayout(self.totaltransactionwidget)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.totaltransactionvalue = QLabel(self.totaltransactionwidget)
        self.totaltransactionvalue.setObjectName(u"totaltransactionvalue")
        sizePolicy1.setHeightForWidth(self.totaltransactionvalue.sizePolicy().hasHeightForWidth())
        self.totaltransactionvalue.setSizePolicy(sizePolicy1)
        self.totaltransactionvalue.setFont(font2)
        self.totaltransactionvalue.setStyleSheet(u"color: rgb(108, 68, 100);\n"
"font: 700 45px \"Inter\";\n"
"background-color: transparent\n"
"")
        self.totaltransactionvalue.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_26.addWidget(self.totaltransactionvalue)


        self.verticalLayout_17.addWidget(self.totaltransactionwidget)


        self.horizontalLayout_20.addWidget(self.totaltransactionbox)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_15.addWidget(self.scrollArea_2)

        self.tab.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.tab)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_6.addWidget(self.tabframe)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(0)


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
#if QT_CONFIG(accessibility)
        self.tab.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
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
        self.expensevalue.setText(QCoreApplication.translate("MainWindow", u"\u20b1 44340.00", None))
        self.expenselbl.setText(QCoreApplication.translate("MainWindow", u"Expense", None))
        self.incomebox.setTitle("")
        self.incomevalue.setText(QCoreApplication.translate("MainWindow", u"\u20b1 44300.00", None))
        self.incomelbl.setText(QCoreApplication.translate("MainWindow", u"Monthly Income", None))
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
        self.categorycombo_3.setItemText(0, QCoreApplication.translate("MainWindow", u"January", None))
        self.categorycombo_3.setItemText(1, QCoreApplication.translate("MainWindow", u"February", None))
        self.categorycombo_3.setItemText(2, QCoreApplication.translate("MainWindow", u"March", None))
        self.categorycombo_3.setItemText(3, QCoreApplication.translate("MainWindow", u"April", None))
        self.categorycombo_3.setItemText(4, QCoreApplication.translate("MainWindow", u"May", None))
        self.categorycombo_3.setItemText(5, QCoreApplication.translate("MainWindow", u"June", None))
        self.categorycombo_3.setItemText(6, QCoreApplication.translate("MainWindow", u"July", None))
        self.categorycombo_3.setItemText(7, QCoreApplication.translate("MainWindow", u"August", None))
        self.categorycombo_3.setItemText(8, QCoreApplication.translate("MainWindow", u"September", None))
        self.categorycombo_3.setItemText(9, QCoreApplication.translate("MainWindow", u"October", None))
        self.categorycombo_3.setItemText(10, QCoreApplication.translate("MainWindow", u"November", None))
        self.categorycombo_3.setItemText(11, QCoreApplication.translate("MainWindow", u"December", None))

        self.categorycombo_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Month", None))
        self.categorycombo_4.setItemText(0, QCoreApplication.translate("MainWindow", u"01", None))
        self.categorycombo_4.setItemText(1, QCoreApplication.translate("MainWindow", u"02", None))
        self.categorycombo_4.setItemText(2, QCoreApplication.translate("MainWindow", u"03", None))
        self.categorycombo_4.setItemText(3, QCoreApplication.translate("MainWindow", u"04", None))
        self.categorycombo_4.setItemText(4, QCoreApplication.translate("MainWindow", u"05", None))
        self.categorycombo_4.setItemText(5, QCoreApplication.translate("MainWindow", u"06", None))
        self.categorycombo_4.setItemText(6, QCoreApplication.translate("MainWindow", u"07", None))
        self.categorycombo_4.setItemText(7, QCoreApplication.translate("MainWindow", u"08", None))
        self.categorycombo_4.setItemText(8, QCoreApplication.translate("MainWindow", u"09", None))
        self.categorycombo_4.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.categorycombo_4.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.categorycombo_4.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.categorycombo_4.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.categorycombo_4.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.categorycombo_4.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.categorycombo_4.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.categorycombo_4.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.categorycombo_4.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.categorycombo_4.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.categorycombo_4.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.categorycombo_4.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.categorycombo_4.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.categorycombo_4.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.categorycombo_4.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.categorycombo_4.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.categorycombo_4.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.categorycombo_4.setItemText(26, QCoreApplication.translate("MainWindow", u"27", None))
        self.categorycombo_4.setItemText(27, QCoreApplication.translate("MainWindow", u"28", None))
        self.categorycombo_4.setItemText(28, QCoreApplication.translate("MainWindow", u"29", None))
        self.categorycombo_4.setItemText(29, QCoreApplication.translate("MainWindow", u"30", None))
        self.categorycombo_4.setItemText(30, QCoreApplication.translate("MainWindow", u"31", None))

        self.categorycombo_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.categorycombo_5.setItemText(0, QCoreApplication.translate("MainWindow", u"2024", None))
        self.categorycombo_5.setItemText(1, QCoreApplication.translate("MainWindow", u"2025", None))

        self.categorycombo_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.addtransbtn_3.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.user_2.setText(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.totalbudgetbox_2.setTitle("")
        self.user_3.setText(QCoreApplication.translate("MainWindow", u"No Available Report", None))
        self.overallbudgetbox.setTitle("")
        self.overallbudgetvalue.setText(QCoreApplication.translate("MainWindow", u"\u20b1 54320.00", None))
        self.overallbudgetlbl.setText(QCoreApplication.translate("MainWindow", u"Overall Budget", None))
        self.expensebox_3.setTitle("")
        self.totalexpensevalue.setText(QCoreApplication.translate("MainWindow", u"\u20b1 450.00", None))
        self.totalexpenselbl.setText(QCoreApplication.translate("MainWindow", u"Total Expense", None))
        self.accumulatedsavingsbox.setTitle("")
        self.accumulatedsavingvalue.setText(QCoreApplication.translate("MainWindow", u"\u20b1 554.00", None))
        self.accumulatedsavingslbl.setText(QCoreApplication.translate("MainWindow", u"Accumulated Savings", None))
        self.totalincomebox.setTitle("")
        self.totalincomevalue.setText(QCoreApplication.translate("MainWindow", u"\u20b1 44350.00", None))
        self.totalincomelbl.setText(QCoreApplication.translate("MainWindow", u"Total Income", None))
        self.transactionsummarybox.setTitle("")
        self.transactionsummary.setText(QCoreApplication.translate("MainWindow", u"Transactions Summary", None))
        self.budgetsummarybox.setTitle("")
        self.budgetsummarylbl.setText(QCoreApplication.translate("MainWindow", u"Budget Summary", None))
        self.youractivitybox.setTitle("")
        self.youractivitylbl.setText(QCoreApplication.translate("MainWindow", u"Your Activity", None))
        self.totaltransactionbox.setTitle("")
        self.totaltransactionlbl.setText(QCoreApplication.translate("MainWindow", u"Total Transactons", None))
        self.totaltransactionvalue.setText(QCoreApplication.translate("MainWindow", u"204", None))
    # retranslateUi

