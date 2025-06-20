from datetime import datetime
from matplotlib import pyplot as plt
from collections import defaultdict
import sqlite3
from typing import Dict, List, Tuple, Union
from .database_manager import get_database_path


class DataManager:

    def __init__(self, user_id: int, report_date: str):
        self._user_id = user_id
        self._report_date = report_date
        self._conn = sqlite3.connect(get_database_path())
        self._cursor = self._conn.cursor()
        self._categories = {
            "Food": 0,
            "Utilities": 0,
            "Health & Wellness": 0,
            "Personal & Lifestyle": 0,
            "Education": 0,
            "Transportation": 0,
            "Miscellaneous": 0,
        }

    @property
    def user_id(self) -> int:
        """Get the user ID."""
        return self._user_id

    @property
    def report_date(self) -> str:
        """Get the report date."""
        return self._report_date

    @report_date.setter
    def report_date(self, value: str) -> None:
        """Set the report date."""
        self._report_date = value

    def _get_data(self) -> List[Tuple]:
        """
        Retrieve user data from the database.

        Returns:
            List[Tuple]: Raw data from the database
        """
        self._cursor.execute(
            "SELECT * FROM user_data WHERE user_id = ? AND report_date = ?",
            (self._user_id, self._report_date),
        )
        return self._cursor.fetchall()

    def get_statistics(self) -> Dict[str, float]:
        """
        Calculate statistics for each spending category.

        Returns:
            Dict[str, float]: Total spending by category
        """
        result = self._get_data()
        totals = self._categories.copy()

        for row in result:
            totals["Food"] += row[6]
            totals["Utilities"] += row[7]
            totals["Health & Wellness"] += row[8]
            totals["Personal & Lifestyle"] += row[9]
            totals["Education"] += row[10]
            totals["Transportation"] += row[11]
            totals["Miscellaneous"] += row[12]

        return totals

    @staticmethod
    def _parse_amount(val: Union[int, float, str]) -> float:
        """
        Parse a monetary amount from various formats.

        Args:
            val: The value to parse

        Returns:
            float: The parsed amount
        """
        if isinstance(val, (int, float)):
            return float(val)
        return float(str(val).replace("₱", "").replace(",", "").strip())

    def get_transactions_data(self) -> Dict[str, float]:
        """
        Get total spending by category for transactions in the report period.

        Returns:
            Dict[str, float]: Total spending by category
        """
        data = self._cursor.execute(
            "SELECT * FROM transactions WHERE user_id = ? AND transaction_date LIKE ?",
            (self._user_id, f"{self._report_date}%"),
        )
        totals = self._categories.copy()

        for row in data:
            category = row[-1]
            if category in totals:
                totals[category] += self._parse_amount(row[3])
        return totals

    def get_activity(self) -> Dict[str, int]:
        """
        Get transaction count by month.

        Returns:
            Dict[str, int]: Number of transactions per month
        """
        transactions = self._cursor.execute(
            "SELECT * FROM transactions WHERE user_id = ?", (self._user_id,)
        )
        count_per_month = {f"{i:02d}": 0 for i in range(1, 13)}
        for transaction in transactions:
            month = transaction[2].split("-")[1]
            count_per_month[month] += 1
        return count_per_month

    def __del__(self):
        """Cleanup database connections when object is destroyed."""
        self._cursor.close()
        self._conn.close()
