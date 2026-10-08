import json
from datetime import datetime


MENU_FILE = "menu_data.json"


# ==============================
# DEFAULT MENU
# ==============================

user_menu = {
    "starters": {
        "Veg Spring Roll": 120,
        "Paneer Tikka": 180,
        "Veg Manchurian": 150,
        "Chilli Paneer": 170,
        "French Fries": 100
    },

    "main Course": {
        "Butter Paneer Masala": 220,
        "Shahi Paneer": 210,
        "Kadai Paneer": 200,
        "Dal Makhani": 180,
        "Mix Veg": 160
    },

    "breads": {
        "Tandoori Roti": 20,
        "Butter Naan": 40,
        "Garlic Naan": 50,
        "Lachha Paratha": 45
    },

    "rice": {
        "Plain Rice": 90,
        "Jeera Rice": 120,
        "Veg Pulao": 150,
        "Veg Biryani": 180
    },

    "fast Food": {
        "Veg Burger": 80,
        "Cheese Burger": 100,
        "Veg Pizza": 200,
        "Pasta": 150,
        "Noodles": 120
    },

    "drinks": {
        "Cold Drink": 40,
        "Lassi": 60,
        "Mango Shake": 80,
        "Coffee": 50,
        "Tea": 20
    },

    "desserts": {
        "Gulab Jamun": 60,
        "Rasgulla": 60,
        "Ice Cream": 80,
        "Chocolate Cake": 120,
        "Jalebi": 70
    }
}


# ==============================
# READ MENU FROM JSON
# ==============================

def read_menu():
    global user_menu

    try:
        with open(MENU_FILE, "r") as file:
            data = json.load(file)

            if isinstance(data, dict):
                user_menu = data

    except FileNotFoundError:
        write_menu()

    except json.JSONDecodeError:
        print("Menu file is empty or corrupted.")
        write_menu()

    except Exception as error:
        print("Error while reading menu:", error)


# ==============================
# WRITE MENU TO JSON
# ==============================

def write_menu():
    try:
        with open(MENU_FILE, "w") as file:
            json.dump(user_menu, file, indent=4)

    except Exception as error:
        print("Error while saving menu:", error)


# ==============================
# SHOW MENU
# ==============================


def show_menu():

    read_menu()

    print("\n==============================================")
    print("                  MENU")
    print("==============================================")

    print(f"{'CATEGORY':<15} {'ITEM':<20} {'PRICE':>10}")
    print("----------------------------------------------")

    for category, items in user_menu.items():

        for item, price in items.items():
            print(f"{category:<15} {item:<20} ₹{price:>8}")

    print("==============================================")



# ==============================
# ADD ITEM
# ==============================

def add_item():

    while True:

        try:

            category = input("Enter category: ").strip()

            if not category:
                print("Category cannot be empty!")
                continue

            # Allow spaces in category
            if not category.replace(" ", "").isalpha():
                print("Category must contain only letters!")
                continue

            category = category.lower()

            # Create category if it doesn't exist
            if category not in user_menu:
                user_menu[category] = {}

            item = input("Enter item name: ").strip()

            if not item:
                print("Item name cannot be empty!")
                continue

            # Allow spaces in item name
            if not item.replace(" ", "").isalpha():
                print("Item name must contain only letters!")
                continue

            # Check duplicate item
            if item in user_menu[category]:
                print("Item already exists!")
                continue

            price = input("Enter price: ").strip()

            if not price:
                print("Price cannot be empty!")
                continue

            if not price.isdigit():
                print("Price must be a valid number!")
                continue

            if price.startswith("0"):
                print("Price cannot start with zero!")
                continue

            total_price = int(price)

            user_menu[category][item] = total_price

            write_menu()

            print("\n........ ITEM ADDED ........")
            print("Item:", item)
            print("Category:", category)
            print("Price:", total_price)

            break

        except Exception as error:

            print("Error:", error)


# ==============================
# DELETE ITEM
# ==============================

def delete_item():

    while True:

        try:

            category = input("Enter category: ").strip()

            if not category:
                print("Category cannot be empty!")
                continue

            if not category.replace(" ", "").isalpha():
                print("Category must contain only letters!")
                continue

            category = category.lower()

            if category not in user_menu:
                print("Category not found!")
                continue

            item = input("Enter item name: ").strip()

            if not item:
                print("Item name cannot be empty!")
                continue

            if item not in user_menu[category]:
                print("Item not found in this category!")
                continue

            # Delete the selected item
            del user_menu[category][item]

            write_menu()

            print("\n........ ITEM DELETED ........")
            print(f"{item} deleted from {category}.")

            break

        except Exception as error:

            print("Error:", error)


# ==============================
# UPDATE ITEM
# ==============================

def update_item():

    while True:

        try:

            category = input("Enter category: ").strip()

            if not category:
                print("Category cannot be empty!")
                continue

            if not category.replace(" ", "").isalpha():
                print("Category must contain only letters!")
                continue

            category = category.lower()

            if category not in user_menu:
                print("Category not found!")
                continue

            item = input("Enter item name: ").strip()

            if not item:
                print("Item name cannot be empty!")
                continue

            if item not in user_menu[category]:
                print("Item not found in this category!")
                continue

            price = input("Enter new price: ").strip()

            if not price:
                print("Price cannot be empty!")
                continue

            if not price.isdigit():
                print("Price must be a valid number!")
                continue

            if price.startswith("0"):
                print("Price cannot start with zero!")
                continue

            new_price = int(price)

            user_menu[category][item] = new_price

            write_menu()

            print("\n........ ITEM UPDATED ........")
            print(f"{item} in {category}")
            print(f"New price: ₹{new_price}")

            break

        except Exception as error:

            print("Error:", error)


# ==============================
# SEARCH ITEM
# ==============================

def search_item():

    while True:

        try:

            item_name = input("Enter item name to search: ").strip()

            if not item_name:
                print("Item name cannot be empty!")
                continue

            if not item_name.replace(" ", "").isalpha():
                print("Item name must contain only letters!")
                continue

            found = False

            for category, items in user_menu.items():

                for item, price in items.items():

                    if item.lower() == item_name.lower():

                        print("\n========== ITEM FOUND ==========")
                        print("Item:", item)
                        print("Category:", category)
                        print("Price: ₹", price)
                        print("================================")

                        found = True
                        break

                if found:
                    break

            if not found:
                print("\nItem not found!")

            break

        except Exception as error:

            print("Error:", error)


# ==============================
# ADMIN MENU
# ==============================

def admin_menu():

    while True:

        try:

            print("\n================================")
            print("         MANAGE MENU")
            print("================================")
            print("1. Show Menu")
            print("2. Add Item")
            print("3. Delete Item")
            print("4. Update Item")
            print("5. Search Item")
            print("6. Exit")
            print("================================")

            choice = input("Enter your choice: ").strip()

            if not choice:
                print("Input cannot be empty!")
                continue

            if not choice.isdigit():
                print("Please enter numbers only!")
                continue

            choice = int(choice)

            if choice == 1:

                show_menu()

            elif choice == 2:

                add_item()

            elif choice == 3:

                delete_item()

            elif choice == 4:

                update_item()

            elif choice == 5:

                search_item()

            elif choice == 6:

                print("Exiting Manage Menu...")
                break

            else:

                print("Please enter a valid choice between 1 and 6!")

        except Exception as error:

            print("Error:", error)