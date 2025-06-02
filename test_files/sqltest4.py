import mysql.connector
import getpass

# Your shared MySQL database credentials
HOST = "112.198.70.130"
USER = "user1"
PASSWORD = "userpassword"
DATABASE = "account"


# Connect to the database
def connect():
    return mysql.connector.connect(
        host=HOST, user=USER, password=PASSWORD, database=DATABASE
    )


# Sign up function
def sign_up():
    username = input("Choose a username: ")
    password = getpass.getpass("Choose a password: ")

    db = connect()
    cursor = db.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password),
        )
        db.commit()
        print("✅ Signup successful!")
    except mysql.connector.Error as err:
        print("❌ Error:", err)
    finally:
        cursor.close()
        db.close()


# Login function
def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    db = connect()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = %s AND password = %s",
        (username, password),
    )
    result = cursor.fetchone()

    if result:
        print("✅ Login successful! Welcome,", username)
    else:
        print("❌ Login failed. Check your credentials.")

    cursor.close()
    db.close()


# Main menu
def main():
    print("Welcome to the Shared Database Login System")
    while True:
        print("\n1. Sign Up\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
