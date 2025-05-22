from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QLineEdit, QComboBox, QMessageBox


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
        # Validate inputs
        amount = self.__amountedit.text().strip()
        description = self.__descriptionedit.text().strip()
        category = self.__categorycombo.currentText()

        # Validate empty fields
        if not amount or not description:
            QMessageBox.warning(
                None,
                "Invalid Input",
                "Please fill in both amount and description fields.",
            )
            return

        try:
            # Remove currency symbol and convert to float
            amount = float(amount.replace("₱", "").replace(",", "").strip())

            # Validate amount is positive
            if amount <= 0:
                QMessageBox.warning(
                    None, "Invalid Amount", "Amount must be greater than zero."
                )
                return

        except ValueError:
            QMessageBox.warning(
                None, "Invalid Amount", "Please enter a valid number for the amount."
            )
            return

        # Get current date
        current_date = QDate.currentDate().toString("yyyy-MM-dd")

        try:
            # Create table row
            row = [
                QStandardItem(current_date),
                QStandardItem(f"₱ {amount:,.2f}"),
                QStandardItem(description),
                QStandardItem(category),
            ]

            # Set alignment
            for item in row:
                item.setTextAlignment(Qt.AlignCenter)

            # Add row to model
            self.__model.appendRow(row)

            # Clear inputs on success
            self.__amountedit.clear()
            self.__descriptionedit.clear()
            self.__categorycombo.setCurrentIndex(0)

        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to add transaction: {str(e)}")
