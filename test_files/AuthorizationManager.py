import mysql.connector

connect = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Janmarco.100",
  database="Users"
)
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS test(
               user_id INT AUTO_INCREMENT PRIMARY KEY,
               username text,
               password text,
               email text)""")

connect.commit()

'''
class User():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
'''


    

class AuthManager:

    def __init__(self, connect, cursor):
        self.cursor = cursor
        self.connect = connect
    
    # This function will register a user by inserting their username and password into the database
    def register(self, username, password, confirmPassword, email):
        if password != confirmPassword:
            print("Passwords do not match.")
            return
            #add a code to handle the case where passwords do not match
        else:
            self.cursor.execute("INSERT INTO test (username, password, email) VALUES (%s,%s,%s)", (username, password, email))
            self.connect.commit()
        
    # This function will log in a user by checking if the username and password match an entry in the database
    # If they match, it will create a User object and return it
    def login(self, email, password):
        self.cursor.execute("SELECT * FROM test WHERE email = %s AND password = %s", (email, password))
        data = cursor.fetchone()
        print(data)




#Test code
while True:
    authorizationManager = AuthManager(connect, cursor)
    select = int(input('enter 1 for register, 2 for login'))
    if select == 1:
        username = input('enter username')
        password = input('enter password')
        confirmPassword = input('confirm password')
        email = input('enter email')
        authorizationManager.register(username, password, confirmPassword, email)

    elif select == 2:
        email = input('enter email')
        password = input('enter password')
        authorizationManager.login(email, password)



