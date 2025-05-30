import mysql.connector


try:
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",  # or your host, e.g., '127.0.0.1'
        user="root",  # your MySQL username
        password="09082005",  # your MySQL password
        database="account",  # your database name
    )

    # Create a cursor
    cursor = conn.cursor()

    # Execute a query
    input_username = input("Enter your username: ")
    input_email = input("Enter your email: ")
    input_password = input("Enter your password: ")
    default_monthly_income = 0
    default_monthly_budget = 0
    default_food_budget = 0
    default_transport_budget = 0
    default_personal_and_lifestyle_budget = 0

    # Insert into users table
    sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(sql, (input_username, input_email, input_password))

    # Get the last inserted user_id
    user_id = cursor.lastrowid

    # Insert into user_data table
    data = "INSERT INTO user_data (user_id, monthly_income, monthly_budget, food_budget, transport_budget, personal_and_lifestyle_budget) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(
        data,
        (
            user_id,  # Use the user_id from the previous insert
            default_monthly_income,
            default_monthly_budget,
            default_food_budget,
            default_transport_budget,
            default_personal_and_lifestyle_budget,
        ),
    )
    conn.commit()

    # Fetch all rows
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the connection
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()
