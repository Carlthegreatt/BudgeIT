from components.auth_manager import AuthManager
import sqlite3

connect = sqlite3.connect("accounts.db")
cursor = connect.cursor()

auth_manager = AuthManager("test", "0908", "0908", "test@test.com")

print(auth_manager.signin("blancaflorcarlferros@gmail.com", "0908"))
