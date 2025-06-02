import mysql.connector


def login():
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host="localhost",  # or your host, e.g., '127.0.0.1'
            user="root",  # your MySQL username
            password="09082005",  # your MySQL password
            database="account",  # your database name
        )

        # Create a cursor
        cursor = conn.cursor(buffered=True)

        input_email = input("Enter your email: ")
        input_password = input("Enter your password: ")

        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(sql, (input_email, input_password))
        result = cursor.fetchone()
        if result:
            print("Login successful")
            print("User data:", result)  # Print the user details from first query

            # Get user_id from the result tuple
            user_id = result[0]  # Assuming user_id is the first column

            sql = "SELECT * FROM user_data WHERE user_id = %s"
            cursor.execute(sql, (user_id,))  # Add missing parameter
            user_data = cursor.fetchall()
            print("Additional user data:", user_data)
        else:
            print("Login failed")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conn" in locals():
            conn.close()


def update_user_data(
    user_id,
    monthly_income,
    monthly_budget,
    food_budget,
    transport_budget,
    personal_and_lifestyle_budget,
):
    try:
        conn = mysql.connector.connect(
            host="localhost", user="root", password="09082005", database="account"
        )
        cursor = conn.cursor(buffered=True)

        sql = "UPDATE user_data SET monthly_income = %s, monthly_budget = %s, food_budget = %s, transport_budget = %s, personal_and_lifestyle_budget = %s WHERE user_id = %s"
        cursor.execute(
            sql,
            (
                monthly_income,
                monthly_budget,
                food_budget,
                transport_budget,
                personal_and_lifestyle_budget,
                user_id,
            ),
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conn" in locals():
            conn.close()


update_user_data(6, 432, 1043, 4343566, 54543, 540)
