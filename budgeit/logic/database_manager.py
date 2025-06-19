from datetime import datetime
import sqlite3
import os
from contextlib import contextmanager


def get_database_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    budgeit_dir = os.path.dirname(current_dir)
    return os.path.join(budgeit_dir, "accounts.db")


@contextmanager
def get_db_connection(db_name=None):
    if db_name is None:
        db_name = get_database_path()
    conn = sqlite3.connect(db_name)
    try:
        yield conn
    finally:
        conn.close()


def check_monthly_reset(user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS meta (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """
        )
        conn.commit()

        cursor.execute("SELECT value FROM meta WHERE key='last_reset'")
        row = cursor.fetchone()

        today = datetime.today()
        current_month = today.strftime("%Y-%m")

        if row is None:
            cursor.execute(
                "INSERT INTO meta (key, value) VALUES (?, ?)",
                ("last_reset", current_month),
            )
            conn.commit()

        else:
            last_reset_month = row[0][:7]

            if last_reset_month != current_month:
                cursor.execute(
                    "UPDATE meta SET value=? WHERE key='last_reset'",
                    (current_month,),
                )
                conn.commit()
                return True
            else:
                return False
