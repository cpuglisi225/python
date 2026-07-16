"""
Password Manager with hashib module

A simple password manager prototype.
Users can register and authenticate using hashed passwords.

Passwords are stored as SHA-256 hashes in a local file database.

This project is for educational purposes and demonstrates:
- file handling
- password hashing
- basic user authentication
"""

import hashlib
import os


WIDTH = 40
LINE = '=' * WIDTH

FILE_DB = "password_db.txt"


def print_banner():
    print(LINE)
    print('PASSWORD MANAGER'.center(WIDTH))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def save_user(username: str, password_hash: str):
    with open(FILE_DB, "a", encoding="utf-8") as f:
        f.write(f"{username}:{password_hash}\n")


def find_user(username: str):
    if not os.path.exists(FILE_DB):
        return None

    with open(FILE_DB, "r", encoding="utf-8") as f:
        for line in f:
            user, password_hash = line.strip().split(":")

            if user == username:
                return password_hash

    return None


def register():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if find_user(username):
        print("User already exists!")
        return

    password_hash = hash_password(password)

    save_user(username, password_hash)

    print("Registration completed!")


def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    stored_hash = find_user(username)

    if stored_hash is None:
        print("User not found")
        return

    if stored_hash == hash_password(password):
        print("Login successful!")
    else:
        print("Wrong password")


def print_menu_options():
    print(LINE)
    print("Available options:")
    print("  [1] Register")
    print("  [2] Login")
    print("  [q] Quit")
    print(LINE)


def get_menu_option():

    print_menu_options()

    valid_options = {"1", "2", "q"}

    while True:
        choice = input("Choice: ").strip().lower()

        if choice in valid_options:
            return choice

        print("Invalid choice, try again.")


print_banner()

while True:

    selected_option = get_menu_option()

    if selected_option == "q":
        print("Goodbye!")
        break

    if selected_option == "1":
        register()

    elif selected_option == "2":
        login()

    input("Press Enter to continue...")

    clear_screen()
    print_banner()