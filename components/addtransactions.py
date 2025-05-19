from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QLineEdit, QComboBox


class AddTransactions:
    def __init__(
        self,
        amount_edit: QLineEdit,
        description_edit: QLineEdit,
        category_combo: QComboBox,
        model: QStandardItemModel,
    ):
        self.__amountedit = amount_edit
        self.__descriptionedit = description_edit
        self.__categorycombo = category_combo
        self.__model = model

    def add_entry(self):
        amount = self.__amountedit.text().strip()
        description = self.__descriptionedit.text().strip()
        category = self.__categorycombo.currentText()
        current_date = QDate.currentDate().toString("yyyy-MM-dd")

        try:
            # Remove currency symbol and convert to float
            amount = float(amount.replace("₱", "").replace(",", "").strip())
        except ValueError:
            print("Invalid input: Amount must be a valid number.")
            return

        # Create table row
        row = [
            QStandardItem(current_date),
            QStandardItem(
                f"₱ {amount:,.2f}"
            ),  # Format amount with currency symbol and commas
            QStandardItem(description),
            QStandardItem(category),
        ]
        for item in row:
            item.setTextAlignment(Qt.AlignCenter)

        self.__model.appendRow(row)

        # Clear inputs
        self.__amountedit.clear()
        self.__descriptionedit.clear()
        self.__categorycombo.setCurrentIndex(0)
