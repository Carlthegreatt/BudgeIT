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
        self.amountedit = amount_edit
        self.descriptionedit = description_edit
        self.categorycombo = category_combo
        self.model = model

    def add_entry(self):
        amount = self.amountedit.text().strip()
        description = self.descriptionedit.text().strip()
        category = self.categorycombo.currentText()
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

        self.model.appendRow(row)

        # Clear inputs
        self.amountedit.clear()
        self.descriptionedit.clear()
        self.categorycombo.setCurrentIndex(0)
