from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class AmountEditor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Amount Editor")
        self.setGeometry(100, 100, 300, 200)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create label to display amount
        self.amount_label = QLabel("Amount: 0")
        self.amount_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.amount_label)

        # Create button to edit amount
        self.edit_button = QPushButton("Edit Amount")
        self.edit_button.clicked.connect(self.edit_amount)
        layout.addWidget(self.edit_button)

        # Initialize amount
        self.amount = 0
        self.parent = parent

    def edit_amount(self):
        # Create input dialog
        amount, ok = QInputDialog.getInt(
            self,
            "Edit Amount",
            "Enter new amount:",
            self.amount,  # Default value
            0,  # Minimum value
            1000000,  # Maximum value
            1,  # Step value
        )

        # Update amount if user clicked OK
        if ok:
            self.amount = amount
            if self.parent and hasattr(self.parent, "budgetamount"):
                self.parent.budgetamount.setText(f"{self.amount}")
                self.destroy()
