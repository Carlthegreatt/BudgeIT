from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTextEdit,
)
from PySide6.QtCore import Qt


class SumWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live Sum of Values")

        # Initialize layout and widgets
        layout = QVBoxLayout()
        self.inputs = []
        self.num_fields = 4  # Number of text fields

        for i in range(self.num_fields):
            text_edit = QTextEdit()
            text_edit.setPlaceholderText(f"Enter value {i+1}")
            text_edit.textChanged.connect(self.update_sum)
            layout.addWidget(text_edit)
            self.inputs.append(text_edit)

        # Label to display the sum
        self.sum_label = QLabel("Sum: ₱0.00")
        self.sum_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.sum_label)

        self.setLayout(layout)

    def update_sum(self):
        total = 0.0
        for text_edit in self.inputs:
            try:
                value = float(text_edit.toPlainText())
                total += value
            except ValueError:
                continue  # Ignore non-numeric input

        self.sum_label.setText(f"Sum: ₱{total:,.2f}")


# Run the application
if __name__ == "__main__":
    app = QApplication([])
    window = SumWidget()
    window.resize(300, 400)
    window.show()
    app.exec()
