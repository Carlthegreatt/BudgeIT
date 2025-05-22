from datetime import datetime
from matplotlib import pyplot as plt
from collections import defaultdict

sample_transactions = [
    {"Date": "2025-05-01", "Category": "Food", "Amount": 500},
    {"Date": "2025-05-01", "Category": "Transportation", "Amount": 200},
    {"Date": "2025-05-02", "Category": "Entertainment", "Amount": 1200},
    {"Date": "2025-05-02", "Category": "Utilities", "Amount": 800},
    {"Date": "2025-05-03", "Category": "Food", "Amount": 650},
    {"Date": "2025-05-03", "Category": "Transportation", "Amount": 150},
    {"Date": "2025-05-04", "Category": "Food", "Amount": 400},
    {"Date": "2025-05-04", "Category": "Savings", "Amount": 2000},
    {"Date": "2025-05-05", "Category": "Taxes", "Amount": 1000},
    {"Date": "2025-05-06", "Category": "Shopping", "Amount": 1800},
    {"Date": "2025-05-07", "Category": "Shopping", "Amount": 900},
    {"Date": "2025-05-08", "Category": "Entertainment", "Amount": 700},
    {"Date": "2025-05-09", "Category": "Utilities", "Amount": 750},
    {"Date": "2025-05-10", "Category": "Transportation", "Amount": 100},
    {"Date": "2025-05-10", "Category": "Food", "Amount": 300},
]


class DataManager:
    def __init__(self, transactions: list):
        self._transactions = transactions

    def get_report(self, period: str) -> dict:
        filtered = []  # For transaction within that period
        # Assumes that period is month

        for transaction in self._transactions:
            transaction_date = datetime.strptime(transaction["Date"], "%Y-%m-%d")
            transaction_period = transaction_date.strftime("%B %Y")

            if transaction_period == period:
                filtered.append(transaction)

        report_trx = defaultdict(
            float
        )  # This will be the dictionary the budget manager will use
        total = 0.0

        for transaction in filtered:
            report_trx[transaction["Category"]] += transaction["Amount"]
            total += transaction["Amount"]

        return {"Period": period, "Total_spent": total, "Category": dict(report_trx)}

    def get_statistics(self, total_income) -> dict:
        total_transactions = total_expense = 0
        trx_cnt = (
            []
        )  # stores all the transaction amount to see which one is the largest, smallest
        trx_cat_ptg = trx_cat_total = defaultdict(
            float
        )  # Keeps tracks of the user's total expenses per category

        for transaction in self._transactions:
            total_transactions += 1
            total_expense += transaction["Amount"]
            trx_cnt.append((transaction["Category"], transaction["Amount"]))
            trx_cat_total[transaction["Category"]] += transaction["Amount"]

        for category, amount in trx_cat_total.items():
            trx_cat_ptg[category] = (f"{(amount/total_income) * 100}", amount)

        return {
            "Total Expenses": total_expense,
            "Total Income": total_income,
            "Average transaction": f"{total_expense/total_transactions:.2f}",
            "Largest Transaction": max(trx_cnt, key=lambda item: item[1]),
            "Smallest Transaction": min(trx_cnt, key=lambda item: item[1]),
            "Category Percentage and amount": dict(trx_cat_ptg),
        }

    def generate_graph(self, total_income):
        # Gen a Bar chart for most categry spent
        # Gen a Pie chart for most Category spent in percentage relative to the budget of the user
        # Gen a Scatter plot of the user's spending habit based on the transaction so far
        stats = self.get_statistics(total_income)
        category_data = stats["Category Percentage and amount"]

        categories = list(category_data.keys())
        amounts = [data[1] for data in category_data.values()]  # Extract amounts
        percentages = [
            float(data[0]) for data in category_data.values()
        ]  # Extract percentages

        # Bar Chart -------------------
        plt.figure(figsize=(10, 5))
        plt.bar(categories, amounts, color="skyblue")
        plt.title("Spending per Category")
        plt.xlabel("Category")
        plt.ylabel("Amount Spent")
        plt.tight_layout()
        plt.show()

        # Pie Chart ----------------
        plt.figure(figsize=(8, 8))
        plt.pie(percentages, labels=categories, autopct="%1.1f%%", startangle=140)
        plt.title("Spending as % of Total Income")
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
