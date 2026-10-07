import json
import os

FILE = "data/users.json"


def load_users():

    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as file:
            return json.load(file)

    except:
        return []


def save_users(users):

    os.makedirs("data", exist_ok=True)

    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)


def register():

    print("\n========== REGISTER ==========")

    users = load_users()

    username = input("Enter username: ").strip()

    if username == "":
        print("Username cannot be empty.")
        return

    password = input("Enter password: ").strip()

    if password == "":
        print("Password cannot be empty.")
        return

    for user in users:

        if user["username"] == username:
            print("Username already exists.")
            return

    print("\n1. Admin")
    print("2. Staff")

    role_choice = input("Select role: ").strip()

    if role_choice == "1":
        role = "Admin"

    elif role_choice == "2":
        role = "Staff"

    else:
        print("Invalid role.")
        return

    users.append({
        "username": username,
        "password": password,
        "role": role
    })

    save_users(users)

    print("Registration successful!")


def login():

    print("\n========== LOGIN ==========")

    users = load_users()

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for user in users:

        if (
            user["username"] == username
            and user["password"] == password
        ):

            print("Login successful!")
            return user

    print("Invalid username or password.")

    return None