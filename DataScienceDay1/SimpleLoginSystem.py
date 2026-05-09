import csv
import os

# --- Simple Login System ---
# A basic system to handle user registration and login.

FILENAME = "users.csv"
# Dictionary format: { username: password }
users = {}

def load_users():
    """Loads existing users from the CSV file."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    users[row['username']] = row['password']
            print("User database loaded.")
        except Exception as e:
            print(f"Error loading users: {e}")

def save_users():
    """Saves the current user dictionary to the CSV file."""
    try:
        with open(FILENAME, mode='w', newline='') as file:
            fieldnames = ["username", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for username, password in users.items():
                writer.writerow({"username": username, "password": password})
        print("User database saved.")
    except Exception as e:
        print(f"Error saving users: {e}")

def register():
    """Handles new user registration."""
    print("\n--- Register ---")
    username = input("Enter a new username: ").strip()
    
    if not username:
        print("Username cannot be empty!")
        return

    # Check for duplicate usernames
    if username in users:
        print("Username already exists! Please try a different one.")
    else:
        password = input("Enter a password: ")
        users[username] = password
        print("Registration successful!")

def login():
    """Handles user login authentication."""
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    # Check if username exists and password matches
    if username in users and users[username] == password:
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Error: Invalid username or password.")

def view_users():
    """Displays a list of all registered usernames."""
    if not users:
        print("\nNo users registered yet.")
    else:
        print("\n--- Registered Usernames ---")
        for idx, username in enumerate(users.keys(), 1):
            print(f"{idx}. {username}")

def main():
    load_users()

    while True:
        print("\n" + "="*30)
        print("      LOGIN SYSTEM")
        print("="*30)
        print("1. Register")
        print("2. Login")
        print("3. View Registered Users")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            view_users()
        elif choice == '4':
            save_users()
            print("System closed. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
