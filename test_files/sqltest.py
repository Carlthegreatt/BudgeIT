import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",  # or your host, e.g., '127.0.0.1'
    user="root",  # your MySQL username
    password="09082005",  # your MySQL password
    database="airbnb",  # your database name
)

# Create a cursor
cursor = conn.cursor()

# Execute a query
input_username = input("Enter your username: ")
input_email = input("Enter your email: ")
input_password = input("Enter your password: ")


# Replace 'users' with your table name

sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
cursor.execute(sql, (input_username, input_email, input_password))
conn.commit()


# Fetch all rows
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

# Close the connection
cursor.close()
conn.close()
