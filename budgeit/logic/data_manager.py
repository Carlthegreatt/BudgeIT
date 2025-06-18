from datetime import datetime
from matplotlib import pyplot as plt
from collections import defaultdict
import sqlite3
from .database_manager import get_database_path

conn = sqlite3.connect(get_database_path())
cursor = conn.cursor()


class DataManager:
    def __init__(self, id, report_date):
        self._id = id
        self.report_date = report_date

    def get_data(self) -> tuple:
        cursor.execute(
            "SELECT * FROM user_data WHERE user_id = ? AND report_date = ?",
            (self._id, self.report_date),
        )
        return cursor.fetchall()

    def get_statistics(self) -> dict:
        result = self.get_data()

        for data in result:
            print(data)

        total = {
            "Food": 0,
            "Utilities": 0,
            "Health & Wellness": 0,
            "Personal & Lifestyle": 0,
            "Education": 0,
            "Transportation": 0,
            "Miscellaneous": 0,
        }
        for row in result:
            total["Food"] += row[6]
            total["Utilities"] += row[7]
            total["Health & Wellness"] += row[8]
            total["Personal & Lifestyle"] += row[9]
            total["Education"] += row[10]
            total["Transportation"] += row[11]
            total["Miscellaneous"] += row[12]

        return total

    @staticmethod
    def parse_amount(val):
        if isinstance(val, (int, float)):
            return val
        return float(str(val).replace("₱", "").replace(",", "").strip())

    def get_transactions_data(self):
        data = cursor.execute(
            "SELECT * FROM transactions WHERE user_id = ? AND transaction_date LIKE ?",
            (self._id, f"{self.report_date}%"),
        )
        total = {
            "Food": 0,
            "Utilities": 0,
            "Health & Wellness": 0,
            "Personal & Lifestyle": 0,
            "Education": 0,
            "Transportation": 0,
            "Miscellaneous": 0,
        }
        for row in data:
            category = row[-1]
            if category in total:
                total[category] += DataManager.parse_amount(row[3])
        return total

    def get_activity(self):
        transactions = cursor.execute(
            "SELECT * FROM transactions WHERE user_id = ?", (self._id,)
        )
        count_per_month = {f"{i:02d}": 0 for i in range(1, 13)}
        for transaction in transactions:
            month = transaction[2].split("-")[1]
            count_per_month[month] += 1
        return count_per_month
