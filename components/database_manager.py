from datetime import datetime
import sqlite3
from contextlib import contextmanager


@contextmanager
def get_db_connection(db_name="accounts.db"):
    conn = sqlite3.connect(db_name)
    try:
        yield conn
    finally:
        conn.close()


def check_monthly_reset(user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Create meta table if it doesn't exist
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS meta (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """
        )
        conn.commit()

        # Get last reset date
        cursor.execute("SELECT value FROM meta WHERE key='last_reset'")
        row = cursor.fetchone()

        today = datetime.today()
        current_month = today.strftime("%Y-%m")

        if row is None:
            # First time setup
            cursor.execute(
                "INSERT INTO meta (key, value) VALUES (?, ?)",
                ("last_reset", current_month),
            )
            conn.commit()

        else:
            last_reset_month = row[0][:7]  # Only YYYY-MM

            if last_reset_month != current_month:
                cursor.execute(
                    "UPDATE meta SET value=? WHERE key='last_reset'",
                    (current_month,),
                )
                conn.commit()
                return True
            else:
                return False
