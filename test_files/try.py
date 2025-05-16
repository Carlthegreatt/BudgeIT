from PySide6.QtWidgets import QApplication, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
import sys

app = QApplication([])

table = QTableView()
model = QStandardItemModel()
model.setHorizontalHeaderLabels(["ID", "Name", "Age"])

data = [
    [1, "Alice", 25],
    [2, "Bob", 30],
    [3, "Charlie", 22],
]

for row_data in data:
    items = []
    for field in row_data:
        item = QStandardItem(str(field))
        item.setTextAlignment(Qt.AlignCenter)  # CENTER ALIGN HERE
        items.append(item)
    model.appendRow(items)

table.setModel(model)
table.show()
sys.exit(app.exec())
