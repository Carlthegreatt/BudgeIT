from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QLineEdit, QComboBox, QMessageBox
import sqlite3
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from abc import ABC, abstractmethod


class Transaction(ABC):
    """Abstract base transaction class"""

    amount: float
    category: str
    date: str
    description: str

    @abstractmethod
    def add_entry(self) -> str:
        pass


class AddTransactions(Transaction):
    def __init__(
        self,
        user_id: int,
        amount_edit: QLineEdit,
        description_edit: QLineEdit,
        category_combo: QComboBox,
        model: QStandardItemModel,
        parent=None,  # Add parent parameter to access main window methods
    ):
        self.__user_id = user_id
        self.__amountedit = amount_edit
        self.__descriptionedit = description_edit
        self.__categorycombo = category_combo
        self.__model = model
        self.__parent = parent  # Store parent reference

        self.__connect = sqlite3.connect("accounts.db")

    def add_entry(self):
        # Validate inputs
        cursor = self.__connect.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS transactions(
            data_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            transaction_date TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL
        )"""
        )

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
            return False

        try:
            # Remove currency symbol and convert to float
            amount = float(amount.replace("₱", "").replace(",", "").strip())

            # Validate amount is positive
            if amount <= 0:
                QMessageBox.warning(
                    None, "Invalid Amount", "Amount must be greater than zero."
                )
                return False

        except ValueError:
            QMessageBox.warning(
                None, "Invalid Amount", "Please enter a valid number for the amount."
            )
            return False

        # Get current date
        current_date = QDate.currentDate().toString("yyyy-MM-dd")
        report_date = QDate.currentDate().toString("yyyy-MM")

        try:
            # Map categories to their corresponding budget columns
            category_budget_map = {
                "Food": "remaining_food_budget",
                "Utilities": "remaining_utilities_budget",
                "Health & Wellness": "remaining_health_wellness_budget",
                "Personal & Lifestyle": "remaining_personal_lifestyle_budget",
                "Education": "remaining_education_budget",
                "Transportation": "remaining_transportation_budget",
                "Miscellaneous": "remaining_miscellaneous_budget",
            }

            # Get the correct budget column for the selected category
            budget_column = category_budget_map.get(category)
            remaining_budget = cursor.execute(
                f"SELECT {budget_column} FROM remaining_budgets WHERE user_id = ? AND report_date = ?",
                (self.__user_id, report_date),
            ).fetchone()[0]

            if remaining_budget - amount < 0:
                reply = QMessageBox.question(
                    None,
                    "Insufficient Budget",
                    "You do not have enough budget for this category. Would you like to proceed anyway?",
                )
                if reply == QMessageBox.Yes:
                    cursor.execute(
                        f"UPDATE remaining_budgets SET {budget_column} = ? WHERE user_id = ? AND report_date = ?",
                        (0, self.__user_id, report_date),
                    )
                    self.__connect.commit()

                    cursor.execute(
                        "INSERT INTO transactions (user_id, transaction_date, amount, description, category) VALUES (?, ?, ?, ?, ?)",
                        (self.__user_id, current_date, amount, description, category),
                    )
                    self.__connect.commit()

                    cursor.execute(
                        "UPDATE user_data SET monthly_expenses = monthly_expenses + ? WHERE user_id = ? AND report_date = ?",
                        (amount, self.__user_id, report_date),
                    )
                    self.__connect.commit()

                    cursor.execute(
                        """UPDATE remaining_budgets SET remaining_monthly_savings = remaining_monthly_savings - ? WHERE user_id = ? AND report_date = ?""",
                        (amount, self.__user_id, report_date),
                    )
                    self.__connect.commit()

                    # Clear inputs on success
                    self.__amountedit.clear()
                    self.__descriptionedit.clear()
                    self.__categorycombo.setCurrentIndex(0)

                    return True

                else:
                    return False
            else:
                cursor.execute(
                    f"UPDATE remaining_budgets SET {budget_column} = {budget_column} - ? WHERE user_id = ? AND report_date = ?",
                    (amount, self.__user_id, report_date),
                )
                self.__connect.commit()

                cursor.execute(
                    "INSERT INTO transactions (user_id, transaction_date, amount, description, category) VALUES (?, ?, ?, ?, ?)",
                    (self.__user_id, current_date, amount, description, category),
                )
                self.__connect.commit()

                cursor.execute(
                    "UPDATE user_data SET monthly_expenses = monthly_expenses + ? WHERE user_id = ? AND report_date = ?",
                    (amount, self.__user_id, report_date),
                )
                self.__connect.commit()

                # Clear inputs on success
                self.__amountedit.clear()
                self.__descriptionedit.clear()
                self.__categorycombo.setCurrentIndex(0)

                return True

        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to add transaction: {str(e)}")
            return False
        finally:
            cursor.close()
