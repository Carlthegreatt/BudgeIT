from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QLineEdit, QComboBox, QMessageBox
import sqlite3
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Dict, Any
from .database_manager import get_database_path
from budgeit.utils.warning_email_automation import EmailSender


@dataclass
class TransactionData:
    user_id: int
    amount: float
    description: str
    category: str
    date: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "amount": self.amount,
            "description": self.description,
            "category": self.category,
            "date": self.date,
        }


@dataclass
class BudgetData:
    remaining_category_budget: float
    remaining_monthly_savings: float
    remaining_monthly_budget: float


class DatabaseInterface(ABC):
    @abstractmethod
    def get_remaining_budget(
        self, user_id: int, report_date: str, category: str
    ) -> Optional[BudgetData]:
        pass

    @abstractmethod
    def update_category_budget(
        self, user_id: int, report_date: str, category: str, amount: float
    ) -> bool:
        pass

    @abstractmethod
    def insert_transaction(self, transaction: TransactionData) -> bool:
        pass

    @abstractmethod
    def update_monthly_expenses(
        self, user_id: int, report_date: str, amount: float
    ) -> bool:
        pass

    @abstractmethod
    def update_monthly_savings(
        self, user_id: int, report_date: str, amount: float
    ) -> bool:
        pass

    @abstractmethod
    def update_monthly_budget(
        self, user_id: int, report_date: str, amount: float
    ) -> bool:
        pass

    @abstractmethod
    def reset_all_budgets(self, user_id: int, report_date: str) -> bool:
        pass


class TransactionDatabase(DatabaseInterface):
    def __init__(self, db_path: str = None):
        self.__db_path = db_path or get_database_path()
        self.__category_budget_map = {
            "Food": "remaining_food_budget",
            "Utilities": "remaining_utilities_budget",
            "Health & Wellness": "remaining_health_wellness_budget",
            "Personal & Lifestyle": "remaining_personal_lifestyle_budget",
            "Education": "remaining_education_budget",
            "Transportation": "remaining_transportation_budget",
            "Miscellaneous": "remaining_miscellaneous_budget",
        }

    # get the username and email of the us
    def get_user_email_and_name(self, user_id: int) -> tuple[str, str] | None:
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT email, username FROM users WHERE user_id = ?", (user_id,)
                )
                result = cursor.fetchone()
                if result:
                    return result
                return None
        except Exception as e:
            print(f"Error fetching user email: {e}")
            return None

    def __get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.__db_path)

    def __create_table_if_not_exists(self, cursor: sqlite3.Cursor) -> None:
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

    def get_remaining_budget(
        self, user_id: int, report_date: str, category: str
    ) -> Optional[BudgetData]:
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()
                budget_column = self.__category_budget_map.get(category)
                if not budget_column:
                    return None

                result = cursor.execute(
                    f"SELECT {budget_column}, remaining_monthly_savings, remaining_monthly_budget FROM remaining_budgets WHERE user_id = ? AND report_date = ?",
                    (user_id, report_date),
                ).fetchone()

                if result:
                    return BudgetData(
                        remaining_category_budget=result[0],
                        remaining_monthly_savings=result[1],
                        remaining_monthly_budget=result[2],
                    )
                return None
        except Exception as e:
            print(f"Error getting budget: {e}")
            return None

    def update_category_budget(
        self, user_id: int, report_date: str, category: str, amount: float
    ) -> bool:
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()
                budget_column = self.__category_budget_map.get(category)
                if not budget_column:
                    return False

                cursor.execute(
                    f"UPDATE remaining_budgets SET {budget_column} = {budget_column} - ? WHERE user_id = ? AND report_date = ?",
                    (amount, user_id, report_date),
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"Error updating category budget: {e}")
            return False

    def insert_transaction(self, transaction: TransactionData) -> bool:
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()
                self.__create_table_if_not_exists(cursor)

                cursor.execute(
                    "INSERT INTO transactions (user_id, transaction_date, amount, description, category) VALUES (?, ?, ?, ?, ?)",
                    (
                        transaction.user_id,
                        transaction.date,
                        transaction.amount,
                        transaction.description,
                        transaction.category,
                    ),
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"Error inserting transaction: {e}")
            return False

    def update_monthly_expenses(
        self, user_id: int, report_date: str, amount: float
    ) -> bool:
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE user_data SET monthly_expenses = monthly_expenses + ? WHERE user_id = ? AND report_date = ?",
                    (amount, user_id, report_date),
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"Error updating monthly expenses: {e}")
            return False

    def update_monthly_savings(
        self, user_id: int, report_date: str, amount: float
    ) -> bool:
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE remaining_budgets SET remaining_monthly_savings = remaining_monthly_savings - ? WHERE user_id = ? AND report_date = ?",
                    (amount, user_id, report_date),
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"Error updating monthly savings: {e}")
            return False

    def update_monthly_budget(
        self, user_id: int, report_date: str, amount: float
    ) -> bool:
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE remaining_budgets SET remaining_monthly_budget = remaining_monthly_budget - ? WHERE user_id = ? AND report_date = ?",
                    (amount, user_id, report_date),
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"Error updating monthly budget: {e}")
            return False

    def reset_all_budgets(self, user_id: int, report_date: str) -> bool:
        try:
            with self.__get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """UPDATE remaining_budgets SET 
                       remaining_monthly_budget = 0, 
                       remaining_food_budget = 0, 
                       remaining_utilities_budget = 0, 
                       remaining_health_wellness_budget = 0, 
                       remaining_personal_lifestyle_budget = 0, 
                       remaining_education_budget = 0, 
                       remaining_transportation_budget = 0, 
                       remaining_miscellaneous_budget = 0 
                       WHERE user_id = ? AND report_date = ?""",
                    (user_id, report_date),
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"Error resetting budgets: {e}")
            return False


class TransactionValidator:
    @staticmethod
    def validate_input(
        amount_text: str, description: str
    ) -> tuple[bool, str, Optional[float]]:
        if not amount_text.strip() or not description.strip():
            return False, "Please fill in both amount and description fields.", None

        try:
            amount = float(amount_text.replace("₱", "").replace(",", "").strip())
            if amount <= 0:
                return False, "Amount must be greater than zero.", None
            return True, "", amount
        except ValueError:
            return False, "Please enter a valid number for the amount.", None


class BudgetManager:
    def __init__(self, database: DatabaseInterface):
        self.__database = database

    def process_transaction_budget_impact(
        self, user_id: int, amount: float, category: str, report_date: str
    ) -> tuple[bool, str]:
        budget_data = self.__database.get_remaining_budget(
            user_id, report_date, category
        )
        if not budget_data:
            return False, "Unable to retrieve budget information."

        if budget_data.remaining_category_budget - amount < 0:
            reply = QMessageBox.question(
                None,
                "Insufficient Budget",
                "You do not have enough budget for this category. Would you like to proceed anyway?",
            )
            if reply != QMessageBox.Yes:
                return False, "Transaction cancelled by user."

            return self.__handle_insufficient_budget(
                user_id, amount, category, report_date, budget_data
            )
        else:
            return self.__handle_sufficient_budget(
                user_id, amount, category, report_date, budget_data
            )

    def __handle_insufficient_budget(
        self,
        user_id: int,
        amount: float,
        category: str,
        report_date: str,
        budget_data: BudgetData,
    ) -> tuple[bool, str]:
        if not self.__database.update_category_budget(
            user_id, report_date, category, budget_data.remaining_category_budget
        ):
            return False, "Failed to update category budget."

        if budget_data.remaining_monthly_savings - amount < 0:
            confirmation = QMessageBox.question(
                None,
                "Insufficient Budget",
                "You have exceeded your monthly savings. Would you like to proceed?",
            )
            if confirmation != QMessageBox.Yes:
                return False, "Transaction cancelled by user."

            if not self.__database.update_monthly_savings(
                user_id, report_date, budget_data.remaining_monthly_savings
            ):
                return False, "Failed to update monthly savings."
        else:
            if not self.__database.update_monthly_savings(user_id, report_date, amount):
                return False, "Failed to update monthly savings."

        if budget_data.remaining_monthly_budget - amount < 0:
            QMessageBox.warning(
                None,
                "Insufficient Budget",
                "You have exceeded your monthly budget. Please adjust your spending and mind your next transactions.",
            )
            if not self.__database.reset_all_budgets(user_id, report_date):
                return False, "Failed to reset budgets."

            # Send warning email if budget is zero
            user_info = self.__database.get_user_email_and_name(user_id)
            if user_info:
                user_email, user_name = user_info
                email_sender = EmailSender(user_email, user_name)
                email_sender.send_email()
        else:
            if not self.__database.update_monthly_budget(user_id, report_date, amount):
                return False, "Failed to update monthly budget."

        return (
            True,
            "Transaction processed successfully despite insufficient category budget.",
        )

    def __handle_sufficient_budget(
        self,
        user_id: int,
        amount: float,
        category: str,
        report_date: str,
        budget_data: BudgetData,
    ) -> tuple[bool, str]:
        if not self.__database.update_category_budget(
            user_id, report_date, category, amount
        ):
            return False, "Failed to update category budget."

        if not self.__database.update_monthly_savings(user_id, report_date, amount):
            return False, "Failed to update monthly savings."

        if not self.__database.update_monthly_budget(user_id, report_date, amount):
            return False, "Failed to update monthly budget."

        return True, "Transaction processed successfully."


class UIManager:
    def __init__(
        self,
        amount_edit: QLineEdit,
        description_edit: QLineEdit,
        category_combo: QComboBox,
    ):
        self.__amount_edit = amount_edit
        self.__description_edit = description_edit
        self.__category_combo = category_combo

    def get_input_data(self) -> tuple[str, str, str]:
        return (
            self.__amount_edit.text().strip(),
            self.__description_edit.text().strip(),
            self.__category_combo.currentText(),
        )

    def clear_inputs(self) -> None:
        self.__amount_edit.clear()
        self.__description_edit.clear()
        self.__category_combo.setCurrentIndex(0)

    @staticmethod
    def show_error(title: str, message: str) -> None:
        QMessageBox.warning(None, title, message)

    @staticmethod
    def show_critical_error(title: str, message: str) -> None:
        QMessageBox.critical(None, title, message)


class TransactionService:
    def __init__(self, database: DatabaseInterface, budget_manager: BudgetManager):
        self.__database = database
        self.__budget_manager = budget_manager
        self.__validator = TransactionValidator()

    def add_transaction(
        self, user_id: int, amount_text: str, description: str, category: str
    ) -> bool:
        is_valid, error_message, amount = self.__validator.validate_input(
            amount_text, description
        )
        if not is_valid:
            UIManager.show_error("Invalid Input", error_message)
            return False

        current_date = QDate.currentDate().toString("yyyy-MM-dd")
        report_date = QDate.currentDate().toString("yyyy-MM")

        budget_success, budget_message = (
            self.__budget_manager.process_transaction_budget_impact(
                user_id, amount, category, report_date
            )
        )
        if not budget_success:
            if "cancelled" not in budget_message.lower():
                UIManager.show_error("Budget Error", budget_message)
            return False

        transaction = TransactionData(
            user_id=user_id,
            amount=amount,
            description=description,
            category=category,
            date=current_date,
        )

        if not self.__database.insert_transaction(transaction):
            UIManager.show_critical_error(
                "Error", "Failed to add transaction to database."
            )
            return False

        if not self.__database.update_monthly_expenses(user_id, report_date, amount):
            UIManager.show_critical_error("Error", "Failed to update monthly expenses.")
            return False

        return True


class Transaction(ABC):
    @abstractmethod
    def add_entry(self) -> bool:
        pass


class AddTransactions(Transaction):
    def __init__(
        self,
        user_id: int,
        amount_edit: QLineEdit,
        description_edit: QLineEdit,
        category_combo: QComboBox,
        model: QStandardItemModel,
        parent=None,
        database: DatabaseInterface = None,
    ):
        self.__user_id = user_id
        self.__model = model
        self.__parent = parent

        self.__database = database or TransactionDatabase()
        self.__budget_manager = BudgetManager(self.__database)
        self.__transaction_service = TransactionService(
            self.__database, self.__budget_manager
        )
        self.__ui_manager = UIManager(amount_edit, description_edit, category_combo)

    def add_entry(self) -> bool:
        try:
            amount_text, description, category = self.__ui_manager.get_input_data()

            success = self.__transaction_service.add_transaction(
                self.__user_id, amount_text, description, category
            )

            if success:
                self.__ui_manager.clear_inputs()

            return success

        except Exception as e:
            UIManager.show_critical_error(
                "Error", f"An unexpected error occurred: {str(e)}"
            )
            return False
