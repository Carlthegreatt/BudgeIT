import mysql.connector

connect = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Janmarco.100",
  database="Users"
)

cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS test(
               username text,
               password text)""")

connect.commit()


class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    

class AuthManager:

    def __init__(self, connect, cursor):
        self.cursor = cursor
        self.connect = connect
    
    # This function will register a user by inserting their username and password into the database
    def register(self, username, password):
        cursor.execute("INSERT INTO test (username, password) VALUES (?,?)", (username, password))
        connect.commit()
        
    # This function will log in a user by checking if the username and password match an entry in the database
    # If they match, it will create a User object and return it
    def login(self, username, password):
        cursor.execute("SELECT * FROM test WHERE username = ? AND password = ?", (username, password))
        data = cursor.fetchone()
        user = User(data[0], data[1])
        currentuser = user.username




#Test code
while True:
    authorizationManager = AuthManager(connect, cursor)
    select = int(input('enter 1 for reguster, 2 for login'))
    if select == 1:
        username = input('enter username')
        password = input('enter password')
        authorizationManager.register(username, password)

    elif select == 2:
        username = input('enter username')
        password = input('enter password')
        authorizationManager.login(username, password)



