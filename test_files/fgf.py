from datetime import datetime
from dateutil.relativedelta import relativedelta
import sqlite3

user_id = 2
start_date = datetime(2024, 7, 1)  # 12 months starting July 2024

yearly_data = []

for i in range(12):
    date = start_date + relativedelta(months=i)
    report_date = date.strftime("%Y-%m")

    monthly_income = 20000 + (i % 3) * 500  # slight variation
    monthly_expenses = 12000 + (i % 4) * 300
    monthly_savings = monthly_income - monthly_expenses
    monthly_budget = monthly_income - 1000  # assume fixed goal

    # simple proportional breakdown of the budget
    food_budget = 0.25 * monthly_budget
    utilities_budget = 0.10 * monthly_budget
    health_budget = 0.05 * monthly_budget
    lifestyle_budget = 0.08 * monthly_budget
    education_budget = 0.15 * monthly_budget
    transport_budget = 0.12 * monthly_budget
    misc_budget = monthly_budget - (
        food_budget
        + utilities_budget
        + health_budget
        + lifestyle_budget
        + education_budget
        + transport_budget
    )

    yearly_data.append(
        (
            user_id,
            round(monthly_savings, 2),
            round(monthly_expenses, 2),
            round(monthly_income, 2),
            round(monthly_budget, 2),
            round(food_budget, 2),
            round(utilities_budget, 2),
            round(health_budget, 2),
            round(lifestyle_budget, 2),
            round(education_budget, 2),
            round(transport_budget, 2),
            round(misc_budget, 2),
            report_date,
        )
    )


insert_query = """
    INSERT INTO user_data (
        user_id,
        monthly_savings,
        monthly_expenses,
        monthly_income,
        monthly_budget,
        food_budget,
        utilities_budget,
        health_wellness_budget,
        personal_lifestyle_budget,
        education_budget,
        transportation_budget,
        miscellaneous_budget,
        report_date
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""
dummy_user = "INSERT INTO users (username, password, email, account_setup) VALUES ('dei', '123456', 'dei@gmail.com', 1)"

connection = sqlite3.connect("accounts.db")
cursor = connection.cursor()

cursor.execute(dummy_user)
cursor.executemany(insert_query, yearly_data)
connection.commit()
