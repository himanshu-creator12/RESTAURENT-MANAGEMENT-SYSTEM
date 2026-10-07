class User:

    users = {
        "101": {
            "name": "Admin",
            "role": "Admin",
            "password": "Abc@123"
        },
        "102": {
            "name": "Staff",
            "role": "Staff",
            "password": "Staff@123"
        }
    }

    @classmethod
    def signin(cls):

        print("\n========== SIGN IN ==========")

        user_id = input("Enter your ID: ")
        password = input("Enter password: ")

        if user_id not in cls.users:
            print("ERROR: User ID not found!")
            return None

        user = cls.users[user_id]

        if user["password"] == password:

            print("\nSUCCESS: Sign in successful!")
            print("Welcome:", user["name"])
            print("Role:", user["role"])

            return User(
                user["name"],
                user["role"],
                user_id,
                user["password"]
            )

        else:
            print("ERROR: Incorrect password!")
            return None

    def __init__(self, name, role, user_id, password):
        self.name = name
        self.role = role
        self.user_id = user_id
        self.password = password