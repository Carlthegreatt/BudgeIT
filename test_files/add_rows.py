import sqlite3
from random import randint, choice
conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()

def add_new_rows():
    amount_to_add = 3 # for testing purposes only!!!!
    user_id = 1
    cursor.execute("PRAGMA table_info(user_data)")
    columns = [info[1] for info in cursor.fetchall()]
    columns_without_id = columns[1:]  # skip record_id

    col_str = ", ".join(columns_without_id)
    placeholders = ", ".join(["?"] * len(columns_without_id))
    insert_sql = f"INSERT INTO user_data ({col_str}) VALUES ({placeholders})"

    starting_month = 7
    for i in range(amount_to_add):
        test = (
            user_id,
            randint(1000, 2000), randint(1000, 2000), randint(1000, 2000), randint(1000, 2000),
            randint(100, 200), randint(100, 200), randint(100, 200), randint(100, 200),
            randint(100, 200), randint(100, 200), randint(100, 200),
            f"2025-{starting_month}"
        )
        cursor.execute(insert_sql, test)
        conn.commit()
        starting_month += 1
def add_transactions():

    conn = sqlite3.connect("accounts.db")
    cursor = conn.cursor()

    user_id = 5
    categories = ["Food", "Utilities", "Health & Wellness", "Personal & Lifestyle", "Education", "Transportation", "Miscellaneous"]

    months = ["2025-07", "2025-08", "2025-09", "2025-10"]

    transactions = []
    for month in months:
        for i in range(5):
            amount = randint(50, 500)
            category = choice(categories)
            description = f"Sample {category} transaction {i+1} for {month}"
            transactions.append((user_id, month, amount, description, category))

    cursor.executemany("""
        INSERT INTO transactions (user_id, transaction_date, amount, description, category)
        VALUES (?, ?, ?, ?, ?)
    """, transactions)

    conn.commit()
    conn.close()
    
add_transactions()