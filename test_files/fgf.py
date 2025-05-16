import os

print("Files in current directory:", os.listdir())
print("Exists:", os.path.exists("icons.qrc"))


print("Current directory:", os.getcwd())
print("Files and folders:", os.listdir())
print("icons folder:", os.listdir("assets/icons"))  # This should show your .svg files
