import sqlite3
import getpass

# SQLite database file (will be created if doesn't exist)
DATABASE = "account.db"


# Connect to the database
def connect():
    return sqlite3.connect(DATABASE)


# Initialize database (create tables)
def init_db():
    db = connect()
    cursor = db.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """
    )
    db.commit()
    cursor.close()
    db.close()


# Sign up function
def sign_up():
    username = input("Choose a username: ")
    password = getpass.getpass("Choose a password: ")

    db = connect()
    cursor = db.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password),
        )
        db.commit()
        print("✅ Signup successful!")
    except sqlite3.IntegrityError:
        print("❌ Username already exists!")
    except sqlite3.Error as err:
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
        "SELECT * FROM users WHERE username = ? AND password = ?",
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
    print("Welcome to the Local Database Login System")
    init_db()  # Initialize database on startup

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
