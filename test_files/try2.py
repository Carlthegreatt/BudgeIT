from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table View Example")
        self.setGeometry(100, 100, 500, 300)

        # Create Table View widget
        self.table_view = QTableView()
        self.setCentralWidget(self.table_view)

        # Create and set the model
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Name", "Age", "Grade"])
        self.populate_table()
        self.table_view.setModel(self.model)

        # Optional: stretch columns
        self.table_view.horizontalHeader().setStretchLastSection(True)

    def populate_table(self):
        data = [["Alice", 17, "A"], ["Bob", 16, "B"], ["Charlie", 18, "C"]]

        for row_data in data:
            row_items = [QStandardItem(str(item)) for item in row_data]
            self.model.appendRow(row_items)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
