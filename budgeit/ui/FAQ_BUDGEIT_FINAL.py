import os

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
                               QWidget, QVBoxLayout, QPushButton, QScrollArea,
                               QHBoxLayout, QSpacerItem, QStyle)

# Global icon for the collapsible buttons
_piggy_question_icon = None

# Define the light pink border color based on the piggy icon
_PIGGY_PINK_BORDER_COLOR = "#F99BA9"
# Define the light gray background color for answers
_LIGHT_GRAY_ANSWER_BACKGROUND = "#F8F8F8" # Using a very light gray

class CollapsibleButton(QWidget):
    def __init__(self, title="", parent=None):
        super().__init__(parent)
        self.toggle_button = QPushButton(title)
        self.toggle_button.setStyleSheet(f"""
            QPushButton {{
                text-align: left;
                background-color: white;
                color: #333333;
                padding: 12px 15px;
                border: 1px solid {_PIGGY_PINK_BORDER_COLOR};
                border-radius: 8px;
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton::hover {{
                background-color: #F0F0F0;
            }}
            QPushButton::pressed {{
                background-color: #E0E0E0;
            }}
        """)
        self.toggle_button.setIconSize(QSize(32, 32))

        self.content_label = QLabel()
        self.content_label.setStyleSheet(f"""
            QLabel {{
                background-color: {_LIGHT_GRAY_ANSWER_BACKGROUND}; /* Changed background color to light gray */
                color: #555555;
                padding: 15px;
                border: 1px solid {_PIGGY_PINK_BORDER_COLOR};
                border-top: none;
                border-bottom-left-radius: 8px;
                border-bottom-right-radius: 8px;
                font-size: 13px;
                line-height: 1.5;
            }}
        """)
        self.content_label.setWordWrap(True)
        self.content_label.hide()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.toggle_button)
        self.layout.addWidget(self.content_label)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.toggle_button.clicked.connect(self.toggle_content)

    def set_content(self, text):
        self.content_label.setText(text)

    def toggle_content(self):
        if self.content_label.isHidden():
            self.content_label.show()
            self.toggle_button.setIcon(_piggy_question_icon)
        else:
            self.content_label.hide()
            self.toggle_button.setIcon(_piggy_question_icon)

class Ui_Dialog(QObject):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(719, 650)

        # Main layout for the dialog
        self.main_layout = QVBoxLayout(Dialog)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Background label
        self.background_label = QLabel(Dialog)
        bg_image_path = os.path.join(os.path.dirname(__file__), "download (28).jpg")
        pixmap_bg = QPixmap(bg_image_path)
        if pixmap_bg.isNull():
            print(f"WARNING: Background image '{bg_image_path}' not found or could not be loaded. Check file path and existence.")
            self.background_label.setStyleSheet("background-color: #F0F0F0;")
            self.background_label.setPixmap(QPixmap())
        else:
            self.background_label.setPixmap(pixmap_bg)

        self.background_label.setScaledContents(True)
        self.background_label.setAlignment(Qt.AlignCenter)
        self.background_label.setGeometry(Dialog.rect())
        Dialog.setObjectName("Dialog")
        Dialog.installEventFilter(self)

        # Header section (now only contains the title container)
        self.header_widget = QWidget()
        self.header_widget.setStyleSheet("background-color: transparent;")
        self.header_layout = QVBoxLayout(self.header_widget)
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        # Container for main titles and sub-text
        self.title_container = QWidget(self.header_widget)
        self.title_layout = QVBoxLayout(self.title_container)
        self.title_layout.setContentsMargins(20, 10, 20, 10)
        self.title_layout.setSpacing(5)
        self.title_container.setStyleSheet("background-color: #982761;")

        self.label_3 = QLabel(self.title_container)
        font_faq = QFont()
        font_faq.setFamilies([u"Segoe UI"])
        font_faq.setPointSize(36)
        font_faq.setBold(True)
        self.label_3.setFont(font_faq)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setStyleSheet("color: white;")

        self.label_2 = QLabel(self.title_container)
        font_sub_title = QFont()
        font_sub_title.setFamilies([u"Segoe UI"])
        font_sub_title.setPointSize(10)
        font_sub_title.setBold(False)
        self.label_2.setFont(font_sub_title)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setStyleSheet("color: white;")
        self.label_5 = QLabel(self.title_container)
        self.label_5.setFont(font_sub_title)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setStyleSheet("color: white;")

        self.title_layout.addWidget(self.label_3)
        self.title_layout.addWidget(self.label_2)
        self.title_layout.addWidget(self.label_5)

        self.header_layout.addWidget(self.title_container)

        self.main_layout.addWidget(self.header_widget)

        # Scroll Area for FAQ content
        self.scroll_area = QScrollArea(Dialog)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        self.faq_content_widget = QWidget()
        self.faq_content_widget.setStyleSheet("background-color: white;")
        self.faq_layout = QVBoxLayout(self.faq_content_widget)
        self.faq_layout.setContentsMargins(20, 20, 20, 20)
        self.faq_layout.setSpacing(15)

        # --- FAQ Questions and Answers ---
        faqs = [
            {"question": "What kind of reports does BudgeIT present?", "answer": "BudgeIT goes beyond basic tracking, offering insightful weekly, monthly, and yearly financial summaries. These reports provide a clear overview of your budgets, expenses, and savings across various categories, along with a percentage breakdown, showing precisely how much of your budget is being utilized in each area."},
            {"question": "Can I transfer my data to a new device?", "answer": "Absolutely! You can easily transfer your BudgeIT data to a new device. Simply log in using your BudgeIT account, and all your financial information will automatically sync and be securely transferred."},
            {"question": "Are all of the features of BudgeIT free to use?", "answer": "Yes, that's right! All of BudgeIT's features are completely free to use. There are no hidden costs, premium subscriptions, or in-app purchases required to access any of its functionalities."},
            {"question": "Is my financial data safe and secure?", "answer": "Absolutely! We take your financial data security very seriously. Rest assured, your data is never sold or shared with any third parties."},
            {"question": "How can I contact Customer support?", "answer": "You can contact our team through the app by pressing the About us page and contacting a team member through their provided email."},
        ]

        for faq in faqs:
            collapsible_btn = CollapsibleButton(faq["question"])
            collapsible_btn.set_content(faq["answer"])
            self.faq_layout.addWidget(collapsible_btn)
            collapsible_btn.toggle_button.setIcon(_piggy_question_icon)

        self.faq_layout.addStretch()

        self.scroll_area.setWidget(self.faq_content_widget)
        self.main_layout.addWidget(self.scroll_area)

        self.background_label.lower()

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def eventFilter(self, obj, event):
        if obj.objectName() == "Dialog" and event.type() == QEvent.Resize:
            if hasattr(self, 'background_label') and self.background_label:
                self.background_label.setGeometry(obj.rect())
        return super().eventFilter(obj, event)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"FAQ - BudgeIT", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"FAQs", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Got some questions?", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Here are the most commonly asked questions about BudgeIT!", None))

        self.label_3.setStyleSheet("color: white; font-size: 36pt; font-weight: bold;")
        self.label_2.setStyleSheet("color: white; font-size: 10pt;")
        self.label_5.setStyleSheet("color: white; font-size: 10pt;")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    # --- Load the piggy question mark icon with robust path handling and error checking ---
    script_dir = os.path.dirname(__file__)
    icon_filename = "f5488489-312c-49fd-bd05-896c54844847-removebg-preview.png"
    icon_path = os.path.join(script_dir, icon_filename)

    _piggy_question_icon = QIcon(icon_path)

    if _piggy_question_icon.isNull():
        print(f"ERROR: Could not load icon '{icon_filename}' from path: '{icon_path}'")
        print("Please ensure the image file is in the same directory as your Python script.")
        print("Falling back to a standard Qt question mark icon for visibility.")
        _piggy_question_icon = QApplication.style().standardIcon(QStyle.SP_MessageBoxQuestion)
    else:
        print(f"SUCCESS: Icon '{icon_filename}' loaded from: '{icon_path}'")

    Dialog = QDialog()
    Dialog.setObjectName("Dialog")

    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
    