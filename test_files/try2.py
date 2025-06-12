from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live User Data Viewer")

        # Connect to SQLite
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("your_database.db")
        if not self.db.open():
            print("Failed to open database")
            sys.exit(-1)

        # Set up table model
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable("user_data")
        self.model.select()  # Load data

        # Set up table view
        self.view = QTableView()
        self.view.setModel(self.model)
        self.setCentralWidget(self.view)

    def refresh_table(self):
        """Call this method to reload the table (after an insert)."""
        self.model.select()


# App startup
app = QApplication(sys.argv)
window = MainWindow()
window.resize(800, 400)
window.show()

# Optionally simulate a data insert and refresh
import sqlite3

conn = sqlite3.connect("your_database.db")
cur = conn.cursor()
cur.execute(
    """
    INSERT INTO user_data (
        user_id, monthly_savings, monthly_expenses,
        monthly_income, monthly_budget,
        food_budget, utilities_budget, health_wellness_budget,
        personal_lifestyle_budget, education_budget,
        transportation_budget, miscellaneous_budget, report_date
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""",
    (
        1,
        5000,
        10000,
        15000,
        14000,
        3000,
        2000,
        1000,
        1000,
        2000,
        1000,
        1000,
        "2025-06-12",
    ),
)
conn.commit()
conn.close()

# Refresh the table to show new data
window.refresh_table()

sys.exit(app.exec())
