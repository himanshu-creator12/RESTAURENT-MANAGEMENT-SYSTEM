import json
import pprint
from datetime import datetime

from menu.menu import admin_menu
from table_booking.booking import custmor_seats
from table_booking.booking import customer_booking_data
from orders.order import Order


# ==========================================
# STAFF DATA
# ==========================================

STAFF_FILE = "sign_data.json"


def read_staff_data():

    try:

        with open(STAFF_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        return []


def write_staff_data(data):

    with open(STAFF_FILE, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )


# ==========================================
# DELETE STAFF
# ==========================================

def delete_data():

    while True:

        try:

            data = read_staff_data()

            if not data:

                print("\nNo staff data available to delete.")
                return

            print("\n******** DELETE STAFF ********")
            print("==============================")

            delete_name = input(
                "Enter the staff name: "
            ).strip()

            if not delete_name:

                print("Name cannot be empty!")
                continue

            found = False

            for staff in data:

                if staff.get("name", "").lower() == delete_name.lower():

                    data.remove(staff)

                    print("\nDeleted data:")

                    pprint.pprint(
                        staff,
                        indent=2
                    )

                    print(
                        "\nData deleted successfully!"
                    )

                    found = True
                    break

            if not found:

                print(
                    "Staff member not found!"
                )

            write_staff_data(data)

            return

        except Exception as error:

            print("Error:", error)


# ==========================================
# ADMIN MANAGEMENT
# ==========================================

def admin_manage():

    while True:

        try:

            print("\n========== ADMIN MENU ==========")
            print("1. MANAGE MENU")
            print("2. ORDER")
            print("3. BOOKING")
            print("4. REPORT")
            print("5. VIEW ALL BOOKING DATA")
            print("6. DELETE STAFF")
            print("7. EXIT")
            print("================================")

            admin_input = input(
                "Enter your choice (1-7): "
            ).strip()

            if not admin_input:

                print("Input cannot be empty!")
                continue

            if not admin_input.isdigit():

                print("Only numbers are allowed!")
                continue

            admin_input = int(admin_input)

            if admin_input < 1 or admin_input > 7:

                print("Please enter a value between 1 and 7.")
                continue

            # ==================================
            # MANAGE MENU
            # ==================================

            if admin_input == 1:

                admin_menu()

            # ==================================
            # ORDER
            # ==================================

            elif admin_input == 2:

                order_system = Order()

                order_system.take_order()

            # ==================================
            # BOOKING
            # ==================================

            elif admin_input == 3:

                custmor_seats()

            # ==================================
            # REPORT
            # ==================================

            elif admin_input == 4:

                print("\n******** REPORT ********")
                print("=======================")
                print("Report feature is not available yet.")

            # ==================================
            # VIEW BOOKINGS
            # ==================================

            elif admin_input == 5:

                print("\n***** ALL BOOKING DATA *****")
                print("============================")

                if not customer_booking_data:

                    print("No booking data available.")

                else:

                    print(
                        json.dumps(
                            customer_booking_data,
                            indent=4
                        )
                    )

                print("============================")

            # ==================================
            # DELETE STAFF
            # ==================================

            elif admin_input == 6:

                delete_data()

            # ==================================
            # EXIT
            # ==================================

            elif admin_input == 7:

                print("\nExiting Admin Menu...")
                break

        except Exception as error:

            print("Error:", error)