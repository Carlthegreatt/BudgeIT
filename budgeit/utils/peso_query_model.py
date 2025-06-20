from PySide6.QtSql import QSqlQueryModel
from PySide6.QtCore import Qt


class PesoQueryModel(QSqlQueryModel):
    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            col = index.column()
            value = super().data(index, role)

            # Format amount column (index 1) with peso sign
            if col == 1:  # Amount column
                try:
                    amount = float(value)
                    return f"₱{amount:,.2f}"
                except (ValueError, TypeError):
                    return value
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        return super().data(index, role)
