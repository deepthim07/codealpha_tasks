import hashlib
import getpass

# Stored username
stored_username = "admin"

# Store a hashed password instead of the actual password
stored_password_hash = hashlib.sha256("Admin@123".encode()).hexdigest()

max_attempts = 3

for attempt in range(max_attempts):
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ")

    if not username or not password:
        print("Username and password cannot be empty.")
        continue

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    if username == stored_username and password_hash == stored_password_hash:
        print("Login successful")
        break
    else:
        remaining = max_attempts - attempt - 1
        if remaining > 0:
            print(f"Invalid credentials. Attempts remaining: {remaining}")
        else:
            print("Login blocked. Maximum attempts reached.")