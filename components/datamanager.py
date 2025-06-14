from datetime import datetime
from matplotlib import pyplot as plt
from collections import defaultdict
import sqlite3

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()


class DataManager:
    def __init__(self, id):
        self._id = id

    def get_data(self) -> tuple:

        cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (self._id,))
        return cursor.fetchall()  # Gets user data in tuples

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

    def get_transactions_data(self):
        data = cursor.execute(f"SELECT * FROM transactions WHERE user_id = {self._id}")
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
            total[f"{row[-1]}"] += row[3]
        return total

    def generate_graph(self):
        # Gen a Bar chart for most categry spent
        # Gen a Pie chart for most Category spent in percentage relative to the budget of the user
        # Gen a Scatter plot of the user's spending habit based on the transaction so far
        categories = list(self.get_statistics().keys())
        amounts = list(self.get_statistics().values())

        # Pie chart -------------------
        plt.figure(figsize=(8, 8))
        plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
        plt.title("Spending per Category")
        plt.tight_layout()
        plt.show()

        # Bar Chart -------------------
        plt.figure(figsize=(10, 5))
        plt.bar(categories, amounts, color="skyblue")
        plt.title("Spending per Category")
        plt.xlabel("Category")
        plt.ylabel("Amount Spent")
        plt.tight_layout()
        plt.show()
        # Scatterrrr -------------
        plt.figure(figsize=(8, 5))
        x_vals = list(range(len(self._transactions)))
        y_vals = [t["Amount"] for t in self._transactions]
        plt.scatter(x_vals, y_vals, color="purple")
        plt.title("Spending Pattern")
        plt.xlabel("Transaction Index")
        plt.ylabel("Amount")
        plt.tight_layout()
        plt.show()


test = DataManager(1)
for key, val in test.get_statistics().items():
    print(f"{key}:{val}")

for key, val in test.get_transactions_data().items():
    print(f"{key}:{val}")
