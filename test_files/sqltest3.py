import mysql.connector


try:
    # Connect to the database
    conn = mysql.connector.connect(
        host="110.54.161.221",  # or your host, e.g., '127.0.0.1'
        user="root",  # your MySQL username
        password="09082005",  # your MySQL password
        database="account",  # your database name
    )

    con = conn.cursor(buffered=True)

    sql = "SELECT * FROM users"
    con.execute(sql)
    result = con.fetchall()
    print(result)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if "conn" in locals():
        conn.close()
