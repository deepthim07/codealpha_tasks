# Insecure Login Application
# This code is intentionally insecure for security review practice.

USERNAME = "admin"
PASSWORD = "admin123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == USERNAME and password == PASSWORD:
    print("Login successful!")
else:
    print("Invalid username or password.")