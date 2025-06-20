from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Features_ui(object):
    def setupUi(self, features_ui):
        if not features_ui.objectName():
            features_ui.setObjectName("features_ui")
        features_ui.resize(827, 548)
        features_ui.setMinimumSize(QSize(0, 0))
        features_ui.setMaximumSize(QSize(827, 548))
        self.verticalLayout_5 = QVBoxLayout(features_ui)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QScrollArea(features_ui)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet(
            "\n" "background-color: #FFFFFF;\n" "padding: 5px;\n" ""
        )
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 785, 729))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.header_container = QWidget(self.scrollAreaWidgetContents)
        self.header_container.setObjectName("header_container")
        self.horizontalLayout = QHBoxLayout(self.header_container)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text_header_container = QWidget(self.header_container)
        self.text_header_container.setObjectName("text_header_container")
        self.text_header_container.setStyleSheet(
            "#text_header_container {\n"
            "border-bottom: 1px solid rgb(108,68,100);\n"
            "}"
        )
        self.verticalLayout = QVBoxLayout(self.text_header_container)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.text_header_container)
        self.label.setObjectName("label")
        self.label.setStyleSheet(
            "font: 700 32px inter;\n" "color: rgb(108,68,100);\n" ""
        )

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout.addWidget(self.text_header_container)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.coming_soon_container = QWidget(self.header_container)
        self.coming_soon_container.setObjectName("coming_soon_container")
        self.coming_soon_container.setStyleSheet(
            "#coming_soon_container{\n"
            "border-bottom: 1px solid  rgb(108,68,100);\n"
            "\n"
            "}\n"
            ""
        )
        self.verticalLayout_2 = QVBoxLayout(self.coming_soon_container)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QLabel(self.coming_soon_container)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(
            "font: 700 32px inter;\n" "color: rgb(108,68,100);\n" ""
        )

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout.addWidget(self.coming_soon_container)

        self.verticalLayout_27.addWidget(self.header_container)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.label_13.setMaximumSize(QSize(352, 33))
        self.label_13.setStyleSheet(
            "font: 700 16px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_13.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_13)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.label_14.setMinimumSize(QSize(209, 55))
        self.label_14.setStyleSheet(
            "font: 450 12px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_14.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_14)

        self.horizontalLayout_5.addLayout(self.verticalLayout_11)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_16.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.label_23 = QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName("label_23")
        self.label_23.setStyleSheet(
            "font: 700 16px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_23.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_23)

        self.label_24 = QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName("label_24")
        self.label_24.setMinimumSize(QSize(209, 55))
        self.label_24.setStyleSheet(
            "font: 450 12px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_24.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_24)

        self.horizontalLayout_5.addLayout(self.verticalLayout_16)

        self.verticalLayout_27.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_25 = QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName("label_25")
        self.label_25.setMaximumSize(QSize(16777215, 33))
        self.label_25.setStyleSheet(
            "font: 700 16px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_25.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_25)

        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName("label_26")
        self.label_26.setMinimumSize(QSize(209, 55))
        self.label_26.setStyleSheet(
            "font: 450 12px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_26.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_26)

        self.horizontalLayout_8.addLayout(self.verticalLayout_17)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_18.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.label_27 = QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName("label_27")
        self.label_27.setStyleSheet(
            "font: 700 16px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_27.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_27)

        self.label_28 = QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName("label_28")
        self.label_28.setMinimumSize(QSize(209, 55))
        self.label_28.setStyleSheet(
            "font: 450 12px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_28.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_28)

        self.horizontalLayout_8.addLayout(self.verticalLayout_18)

        self.verticalLayout_27.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_33 = QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName("label_33")
        self.label_33.setMaximumSize(QSize(16777215, 33))
        self.label_33.setStyleSheet(
            "font: 700 16px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_33.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_33)

        self.label_34 = QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName("label_34")
        self.label_34.setMinimumSize(QSize(209, 55))
        self.label_34.setStyleSheet(
            "font: 450 12px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_34.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_34)

        self.horizontalLayout_10.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_22.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.label_35 = QLabel(self.scrollAreaWidgetContents)
        self.label_35.setObjectName("label_35")
        self.label_35.setStyleSheet(
            "font: 700 16px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_35.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.label_35)

        self.label_36 = QLabel(self.scrollAreaWidgetContents)
        self.label_36.setObjectName("label_36")
        self.label_36.setMinimumSize(QSize(209, 55))
        self.label_36.setStyleSheet(
            "font: 450 12px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_36.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.label_36)

        self.horizontalLayout_10.addLayout(self.verticalLayout_22)

        self.verticalLayout_27.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_41 = QLabel(self.scrollAreaWidgetContents)
        self.label_41.setObjectName("label_41")
        self.label_41.setMaximumSize(QSize(16777215, 33))
        self.label_41.setStyleSheet(
            "font: 700 16px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_41.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.label_41)

        self.label_42 = QLabel(self.scrollAreaWidgetContents)
        self.label_42.setObjectName("label_42")
        self.label_42.setMinimumSize(QSize(209, 55))
        self.label_42.setStyleSheet(
            "font: 450 12px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_42.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.label_42)

        self.horizontalLayout_12.addLayout(self.verticalLayout_25)

        self.horizontalSpacer_5 = QSpacerItem(
            400, 34, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.verticalLayout_27.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_37 = QLabel(self.scrollAreaWidgetContents)
        self.label_37.setObjectName("label_37")
        self.label_37.setMaximumSize(QSize(16777215, 33))
        self.label_37.setStyleSheet(
            "font: 700 16px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_37.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label_37)

        self.label_38 = QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName("label_38")
        self.label_38.setMinimumSize(QSize(209, 55))
        self.label_38.setStyleSheet(
            "font: 450 12px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_38.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label_38)

        self.horizontalLayout_11.addLayout(self.verticalLayout_23)

        self.horizontalSpacer_6 = QSpacerItem(
            400, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.verticalLayout_27.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_29 = QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName("label_29")
        self.label_29.setMaximumSize(QSize(16777215, 33))
        self.label_29.setStyleSheet(
            "font: 700 16px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_29.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_29)

        self.label_30 = QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName("label_30")
        self.label_30.setMinimumSize(QSize(209, 55))
        self.label_30.setStyleSheet(
            "font: 450 12px inter;\n" "color: rgb(108,68,100);\n" ""
        )
        self.label_30.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_30)

        self.horizontalLayout_9.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_7 = QSpacerItem(
            400, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.verticalLayout_27.addLayout(self.horizontalLayout_9)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.widget.setMinimumSize(QSize(700, 50))
        self.widget.setMaximumSize(QSize(1000, 50))
        self.widget.setStyleSheet(
            "QWidget {\n"
            "    background-color: qlineargradient(\n"
            "        x1: 0, y1: 0, x2: 1, y2: 1,\n"
            "        stop: 0 #FEA1A3\n"
            "        stop: 1 #F6D3CE\n"
            "    );\n"
            "}\n"
            ""
        )

        self.verticalLayout_27.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)

        self.retranslateUi(features_ui)

        QMetaObject.connectSlotsByName(features_ui)
        self.retranslateUi(features_ui)
        QMetaObject.connectSlotsByName(features_ui)

        self.retranslateUi(features_ui)
        QMetaObject.connectSlotsByName(features_ui)

        # Start the animation after the UI is set up
        QTimer.singleShot(100, lambda: self.animate_in(features_ui))

    def animate_in(self, features_ui):
        widgets = [
            self.header_container,
            self.coming_soon_container,
            self.label_13,
            self.label_14,
            self.label_23,
            self.label_24,
            self.label_25,
            self.label_26,
            self.label_27,
            self.label_28,
            self.label_33,
            self.label_34,
            self.label_35,
            self.label_36,
            self.label_41,
            self.label_42,
            self.label_37,
            self.label_38,
            self.label_29,
            self.label_30,
        ]
        self._anims = []
        for i, widget in enumerate(widgets):
            # Fade-in effect
            opacity_effect = QGraphicsOpacityEffect(widget)
            widget.setGraphicsEffect(opacity_effect)
            opacity_effect.setOpacity(0)

            fade_anim = QPropertyAnimation(opacity_effect, b"opacity", features_ui)
            fade_anim.setStartValue(0)
            fade_anim.setEndValue(1)
            fade_anim.setDuration(400)
            fade_anim.setEasingCurve(QEasingCurve.OutCubic)

            # Float-up effect
            orig_pos = widget.pos()
            start_pos = orig_pos + QPoint(0, 40)
            widget.move(start_pos)
            move_anim = QPropertyAnimation(widget, b"pos", features_ui)
            move_anim.setStartValue(start_pos)
            move_anim.setEndValue(orig_pos)
            move_anim.setDuration(400)
            move_anim.setEasingCurve(QEasingCurve.OutCubic)

            # Start both animations staggered
            QTimer.singleShot(i * 40, fade_anim.start)
            QTimer.singleShot(i * 40, move_anim.start)

            self._anims.append(fade_anim)
            self._anims.append(move_anim)
        # setupUi

    def retranslateUi(self, features_ui):
        features_ui.setWindowTitle(
            QCoreApplication.translate("features_ui", "Features", None)
        )
        self.label.setText(QCoreApplication.translate("features_ui", "Features", None))
        self.label_2.setText(
            QCoreApplication.translate("features_ui", "Coming soon", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("features_ui", "Smart Budget Creation", None)
        )
        self.label_14.setText(
            QCoreApplication.translate(
                "features_ui",
                "Create monthly or weekly budgets tailored to your income and spending habits.",
                None,
            )
        )
        self.label_23.setText(
            QCoreApplication.translate("features_ui", "AI Spending insights", None)
        )
        self.label_24.setText(
            QCoreApplication.translate(
                "features_ui",
                "Get personalized suggestions based on your spending habits \u2014 know where you're overspending and where you can save.",
                None,
            )
        )
        self.label_25.setText(
            QCoreApplication.translate(
                "features_ui", "Expense Tracking in Real-Time", None
            )
        )
        self.label_26.setText(
            QCoreApplication.translate(
                "features_ui",
                "Log expenses as they happen, or sync with your bank to auto-track.",
                None,
            )
        )
        self.label_27.setText(
            QCoreApplication.translate(
                "features_ui", "BudgeBot - AI chat assistance", None
            )
        )
        self.label_28.setText(
            QCoreApplication.translate(
                "features_ui", "Ask BudgeBot anything about your finances.", None
            )
        )
        self.label_33.setText(
            QCoreApplication.translate(
                "features_ui", "Categorized Spending Breakdown", None
            )
        )
        self.label_34.setText(
            QCoreApplication.translate(
                "features_ui",
                "Automatically sort your spending into categories like Food, Transport, Utilities, etc",
                None,
            )
        )
        self.label_35.setText(
            QCoreApplication.translate("features_ui", "Shared budgets", None)
        )
        self.label_36.setText(
            QCoreApplication.translate(
                "features_ui",
                "Budget together with your friends and family for a more fun and organized spending habits",
                None,
            )
        )
        self.label_41.setText(
            QCoreApplication.translate("features_ui", "Bill Reminders & Alerts", None)
        )
        self.label_42.setText(
            QCoreApplication.translate(
                "features_ui",
                "Get notified when a bill is due or when you're close to overspending",
                None,
            )
        )
        self.label_37.setText(
            QCoreApplication.translate("features_ui", "Visual Reports & Insights", None)
        )
        self.label_38.setText(
            QCoreApplication.translate(
                "features_ui",
                "View charts and summaries of your financial activity \u2014 understand where your money goes.",
                None,
            )
        )
        self.label_29.setText(
            QCoreApplication.translate("features_ui", "Smart Budget Creation", None)
        )
        self.label_30.setText(
            QCoreApplication.translate(
                "features_ui",
                "Create monthly or weekly budgets tailored to your income and spending habits.",
                None,
            )
        )

    # retranslateUi
