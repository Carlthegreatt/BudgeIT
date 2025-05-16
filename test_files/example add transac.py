import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
import json
from datetime import datetime


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BudgeIT - Expense Tracker")
        self.setMinimumSize(800, 600)

        # Initialize data
        self.transactions = []
        self.load_transactions()

        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Create header
        header = QLabel("BudgeIT")
        header.setFont(QFont("Arial", 24, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # Create total expense label
        self.total_label = QLabel("Total Expenses: $0.00")
        self.total_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.total_label.setAlignment(Qt.AlignCenter)
        self.total_label.setStyleSheet(
            """
            QLabel {
                color: #2c3e50;
                padding: 10px;
                background-color: #ecf0f1;
                border-radius: 4px;
                margin: 10px 0;
            }
        """
        )
        layout.addWidget(self.total_label)

        # Create input form
        form_layout = QHBoxLayout()

        # Amount input
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Amount")
        self.amount_input.setStyleSheet(
            """
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px;
            }
        """
        )
        form_layout.addWidget(self.amount_input)

        # Description input
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Description")
        self.description_input.setStyleSheet(
            """
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px;
            }
        """
        )
        form_layout.addWidget(self.description_input)

        # Category dropdown
        self.category_input = QComboBox()
        self.category_input.addItems(
            ["Food", "Transport", "Entertainment", "Bills", "Other"]
        )
        self.category_input.setStyleSheet(
            """
            QComboBox {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px;
            }
        """
        )
        form_layout.addWidget(self.category_input)

        # Add button
        add_button = QPushButton("Add Transaction")
        add_button.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        )
        add_button.clicked.connect(self.add_transaction)
        form_layout.addWidget(add_button)

        layout.addLayout(form_layout)

        # Create transactions table
        self.transactions_table = QTableWidget()
        self.transactions_table.setColumnCount(4)
        self.transactions_table.setHorizontalHeaderLabels(
            ["Date", "Amount", "Description", "Category"]
        )
        self.transactions_table.setStyleSheet(
            """
            QTableWidget {
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: #f0f0f0;
                padding: 8px;
                border: none;
                border-bottom: 1px solid #ccc;
            }
        """
        )
        layout.addWidget(self.transactions_table)

        # Update table and total
        self.update_transactions_table()
        self.update_total_expense()

        # Set window style
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: white;
            }
        """
        )

    def add_transaction(self):
        try:
            amount = float(self.amount_input.text())
            description = self.description_input.text()
            category = self.category_input.currentText()

            if not description:
                QMessageBox.warning(self, "Error", "Please enter a description")
                return

            transaction = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "amount": amount,
                "description": description,
                "category": category,
            }

            self.transactions.append(transaction)
            self.save_transactions()
            self.update_transactions_table()
            self.update_total_expense()

            # Clear inputs
            self.amount_input.clear()
            self.description_input.clear()

        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid amount")

    def update_transactions_table(self):
        self.transactions_table.setRowCount(len(self.transactions))
        for i, transaction in enumerate(reversed(self.transactions)):
            self.transactions_table.setItem(i, 0, QTableWidgetItem(transaction["date"]))
            self.transactions_table.setItem(
                i, 1, QTableWidgetItem(f"${transaction['amount']:.2f}")
            )
            self.transactions_table.setItem(
                i, 2, QTableWidgetItem(transaction["description"])
            )
            self.transactions_table.setItem(
                i, 3, QTableWidgetItem(transaction["category"])
            )

        self.transactions_table.resizeColumnsToContents()

    def update_total_expense(self):
        total = sum(transaction["amount"] for transaction in self.transactions)
        self.total_label.setText(f"Total Expenses: ${total:.2f}")

    def save_transactions(self):
        with open("transactions.json", "w") as f:
            json.dump(self.transactions, f)

    def load_transactions(self):
        try:
            with open("transactions.json", "r") as f:
                self.transactions = json.load(f)
        except FileNotFoundError:
            self.transactions = []


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec())
