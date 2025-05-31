# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'features UI testMOEPKt.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Features_ui(object):
    def setupUi(self, features_ui):
        if not features_ui.objectName():
            features_ui.setObjectName(u"features_ui")
        features_ui.resize(827, 548)
        features_ui.setMinimumSize(QSize(0, 0))
        features_ui.setMaximumSize(QSize(827, 548))
        self.verticalLayout_5 = QVBoxLayout(features_ui)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea = QScrollArea(features_ui)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"\n"
"background-color: #FFFFFF;\n"
"padding: 5px;\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 785, 729))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.header_container = QWidget(self.scrollAreaWidgetContents)
        self.header_container.setObjectName(u"header_container")
        self.horizontalLayout = QHBoxLayout(self.header_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_header_container = QWidget(self.header_container)
        self.text_header_container.setObjectName(u"text_header_container")
        self.text_header_container.setStyleSheet(u"#text_header_container {\n"
"border-bottom: 1px solid rgb(108,68,100);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.text_header_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.text_header_container)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 32px inter;\n"
"color: rgb(108,68,100);\n"
"")

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addWidget(self.text_header_container)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.coming_soon_container = QWidget(self.header_container)
        self.coming_soon_container.setObjectName(u"coming_soon_container")
        self.coming_soon_container.setStyleSheet(u"#coming_soon_container{\n"
"border-bottom: 1px solid  rgb(108,68,100);\n"
"\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.coming_soon_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.coming_soon_container)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 32px inter;\n"
"color: rgb(108,68,100);\n"
"")

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.coming_soon_container)


        self.verticalLayout_27.addWidget(self.header_container)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(352, 33))
        self.label_13.setStyleSheet(u"font: 700 16px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_13.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_13)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(209, 55))
        self.label_14.setStyleSheet(u"font: 450 12px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_14.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_14)


        self.horizontalLayout_5.addLayout(self.verticalLayout_11)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_23 = QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 700 16px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_23.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_23)

        self.label_24 = QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(209, 55))
        self.label_24.setStyleSheet(u"font: 450 12px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_24.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_24)


        self.horizontalLayout_5.addLayout(self.verticalLayout_16)


        self.verticalLayout_27.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_25 = QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 33))
        self.label_25.setStyleSheet(u"font: 700 16px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_25.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_25)

        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(209, 55))
        self.label_26.setStyleSheet(u"font: 450 12px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_26.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_26)


        self.horizontalLayout_8.addLayout(self.verticalLayout_17)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_27 = QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 700 16px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_27.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_27)

        self.label_28 = QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(209, 55))
        self.label_28.setStyleSheet(u"font: 450 12px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_28.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_28)


        self.horizontalLayout_8.addLayout(self.verticalLayout_18)


        self.verticalLayout_27.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_33 = QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 33))
        self.label_33.setStyleSheet(u"font: 700 16px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_33.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_33)

        self.label_34 = QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(209, 55))
        self.label_34.setStyleSheet(u"font: 450 12px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_34.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_34)


        self.horizontalLayout_10.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_35 = QLabel(self.scrollAreaWidgetContents)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 700 16px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_35.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.label_35)

        self.label_36 = QLabel(self.scrollAreaWidgetContents)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(209, 55))
        self.label_36.setStyleSheet(u"font: 450 12px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_36.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.label_36)


        self.horizontalLayout_10.addLayout(self.verticalLayout_22)


        self.verticalLayout_27.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_41 = QLabel(self.scrollAreaWidgetContents)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 33))
        self.label_41.setStyleSheet(u"font: 700 16px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_41.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.label_41)

        self.label_42 = QLabel(self.scrollAreaWidgetContents)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(209, 55))
        self.label_42.setStyleSheet(u"font: 450 12px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_42.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.label_42)


        self.horizontalLayout_12.addLayout(self.verticalLayout_25)

        self.horizontalSpacer_5 = QSpacerItem(400, 34, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.verticalLayout_27.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_37 = QLabel(self.scrollAreaWidgetContents)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 33))
        self.label_37.setStyleSheet(u"font: 700 16px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_37.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label_37)

        self.label_38 = QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(209, 55))
        self.label_38.setStyleSheet(u"font: 450 12px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_38.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label_38)


        self.horizontalLayout_11.addLayout(self.verticalLayout_23)

        self.horizontalSpacer_6 = QSpacerItem(400, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_27.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_29 = QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 33))
        self.label_29.setStyleSheet(u"font: 700 16px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_29.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_29)

        self.label_30 = QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(209, 55))
        self.label_30.setStyleSheet(u"font: 450 12px inter;\n"
"color: rgb(108,68,100);\n"
"")
        self.label_30.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_30)


        self.horizontalLayout_9.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_7 = QSpacerItem(400, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.verticalLayout_27.addLayout(self.horizontalLayout_9)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(700, 50))
        self.widget.setMaximumSize(QSize(1000, 50))
        self.widget.setStyleSheet(u"QWidget {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 #FEA1A3\n"
"        stop: 1 #F6D3CE\n"
"    );\n"
"}\n"
"")

        self.verticalLayout_27.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.retranslateUi(features_ui)

        QMetaObject.connectSlotsByName(features_ui)
    # setupUi

    def retranslateUi(self, features_ui):
        features_ui.setWindowTitle(QCoreApplication.translate("features_ui", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("features_ui", u"features", None))
        self.label_2.setText(QCoreApplication.translate("features_ui", u"Coming soon", None))
        self.label_13.setText(QCoreApplication.translate("features_ui", u"Smart Budget Creation", None))
        self.label_14.setText(QCoreApplication.translate("features_ui", u"Create monthly or weekly budgets tailored to your income and spending habits.", None))
        self.label_23.setText(QCoreApplication.translate("features_ui", u"AI Spending insights", None))
        self.label_24.setText(QCoreApplication.translate("features_ui", u"Get personalized suggestions based on your spending habits \u2014 know where you're overspending and where you can save.", None))
        self.label_25.setText(QCoreApplication.translate("features_ui", u"Expense Tracking in Real-Time", None))
        self.label_26.setText(QCoreApplication.translate("features_ui", u"Log expenses as they happen, or sync with your bank to auto-track.", None))
        self.label_27.setText(QCoreApplication.translate("features_ui", u"BudgeBot - AI chat assistance", None))
        self.label_28.setText(QCoreApplication.translate("features_ui", u"Ask BudgeBot anything about your finances.", None))
        self.label_33.setText(QCoreApplication.translate("features_ui", u"Categorized Spending Breakdown", None))
        self.label_34.setText(QCoreApplication.translate("features_ui", u"Automatically sort your spending into categories like Food, Transport, Utilities, etc", None))
        self.label_35.setText(QCoreApplication.translate("features_ui", u"Shared budgets", None))
        self.label_36.setText(QCoreApplication.translate("features_ui", u"Budget together with your friends and family for a more fun and organized spending habits", None))
        self.label_41.setText(QCoreApplication.translate("features_ui", u"Bill Reminders & Alerts", None))
        self.label_42.setText(QCoreApplication.translate("features_ui", u"Get notified when a bill is due or when you're close to overspending", None))
        self.label_37.setText(QCoreApplication.translate("features_ui", u"Visual Reports & Insights", None))
        self.label_38.setText(QCoreApplication.translate("features_ui", u"View charts and summaries of your financial activity \u2014 understand where your money goes.", None))
        self.label_29.setText(QCoreApplication.translate("features_ui", u"Smart Budget Creation", None))
        self.label_30.setText(QCoreApplication.translate("features_ui", u"Create monthly or weekly budgets tailored to your income and spending habits.", None))
    # retranslateUi

    