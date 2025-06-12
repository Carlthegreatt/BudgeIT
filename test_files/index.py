import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Data Viewer")

        # Set up the database connection
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("accounts.db")

        if not self.db.open():
            print("Failed to open database")
            sys.exit(-1)

        # Set up the query model
        self.model = QSqlQueryModel()
        self.model.setQuery(
            """
            SELECT transaction_date, amount, description, category
            FROM transactions
        """
        )

        # Optional: Set column names
        self.model.setHeaderData(0, Qt.Horizontal, "User ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Income")
        self.model.setHeaderData(2, Qt.Horizontal, "Expenses")
        self.model.setHeaderData(3, Qt.Horizontal, "Report Date")

        # Create the view and set the model
        self.view = QTableView()
        self.view.setModel(self.model)
        self.setCentralWidget(self.view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 400)
    window.show()
    sys.exit(app.exec())
