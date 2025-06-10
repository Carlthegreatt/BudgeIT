import sys
import sqlite3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QMessageBox,
)

DB_NAME = "school.db"
TABLE_SQL = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT
)
"""


# 🔧 Initialize DB
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(TABLE_SQL)
    cursor.execute(
        "INSERT OR IGNORE INTO students (id, name) VALUES (?, ?)", (1, "Default Name")
    )
    conn.commit()
    conn.close()


# ✅ Get name
def get_student_name(student_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM students WHERE id = ?", (student_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "Not found"


# ✅ Update name
def update_student_name(student_id, new_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name = ? WHERE id = ?", (new_name, student_id))
    conn.commit()
    conn.close()


# 🌟 Main GUI
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto-Updating QLabel with SQLite")
        self.setFixedSize(300, 200)

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter new name...")
        self.button = QPushButton("Update Name")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Current name:"))
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.student_id = 1
        self.refresh_label()

        self.button.clicked.connect(self.update_name)

    def refresh_label(self):
        name = get_student_name(self.student_id)
        self.label.setText(name)

    def update_name(self):
        new_name = self.input.text().strip()
        if new_name:
            update_student_name(self.student_id, new_name)
            self.refresh_label()
            self.input.clear()
        else:
            QMessageBox.warning(self, "Empty Input", "Please enter a name.")


if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
