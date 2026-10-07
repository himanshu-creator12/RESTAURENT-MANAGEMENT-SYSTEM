import json
from datetime import datetime


# ==========================================
# BOOKING DATA
# ==========================================

BOOKING_FILE = "booking_data.json"

customer_booking_data = []


# ==========================================
# WRITE DATA
# ==========================================

def write_data():

    with open(BOOKING_FILE, "w") as file:
        json.dump(customer_booking_data, file, indent=4)


# ==========================================
# READ DATA
# ==========================================

def read_data():

    try:
        with open(BOOKING_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


# Load existing booking data
customer_booking_data = read_data()


# ==========================================
# SEAT BOOKING
# ==========================================

def user_input(max_seats):

    while True:

        try:

            user_seats = input(
                "Enter the number of seats you want to book: "
            ).strip()

            if not user_seats:
                print("Input can't be empty!")
                continue

            if not user_seats.isdigit():
                print("Only numbers are allowed!")
                continue

            if user_seats.startswith("0"):
                print("Input can't be 0 or start with zero!")
                continue

            booked = int(user_seats)

            if booked > max_seats:
                print(
                    f"Only {max_seats} seats are available "
                    "for the selected tables."
                )
                continue

            print("Seats booked successfully!")
            print(f"Seats booked: {booked}")
            print("=================================")

            return booked

        except Exception as error:

            print("Error:", error)


# ==========================================
# BOOKING TIME
# ==========================================

def user_time():

    while True:

        try:

            seat_hour = input(
                "How many hours do you want to reserve the table (1/2): "
            ).strip()

            if not seat_hour:
                print("Input can't be empty!")
                continue

            if not seat_hour.isdigit():
                print("Only numbers are allowed!")
                continue

            if seat_hour.startswith("0"):
                print("Input can't start with 0!")
                continue

            hour = int(seat_hour)

            if hour == 1:

                timing = one_hour()
                return f"{hour} hour", timing

            elif hour == 2:

                timing = two_hour()
                return f"{hour} hours", timing

            else:

                print(
                    "Invalid input. Please enter 1 or 2."
                )

        except Exception as error:

            print("Error:", error)


# ==========================================
# ONE HOUR BOOKING
# ==========================================

def one_hour():

    timings = {
        1: "7:00 AM - 8:00 AM",
        2: "8:00 AM - 9:00 AM",
        3: "9:00 AM - 10:00 AM",
        4: "10:00 AM - 11:00 AM",
        5: "11:00 AM - 12:00 PM",
        6: "12:00 PM - 1:00 PM",
        7: "1:00 PM - 2:00 PM",
        8: "2:00 PM - 3:00 PM",
        9: "3:00 PM - 4:00 PM",
        10: "4:00 PM - 5:00 PM",
        11: "5:00 PM - 6:00 PM",
        12: "6:00 PM - 7:00 PM",
        13: "7:00 PM - 8:00 PM",
        14: "8:00 PM - 9:00 PM"
    }

    while True:

        print("\n<< ONE HOUR BOOKING TIMINGS >>")
        print("=================================")

        for number, timing in timings.items():
            print(f"{number}. {timing}")

        print("=================================")

        choice = input("Enter your choice (1-14): ").strip()

        if not choice.isdigit():
            print("Input must be a number!")
            continue

        choice = int(choice)

        if choice in timings:

            print(
                f"**** Booking timing {timings[choice]} ****"
            )
            print("----------- BOOKING CONFIRMED! -----------")
            print("===========================================")

            return timings[choice]

        else:

            print("Invalid choice!")
            print("Booking is available only from 7:00 AM to 9:00 PM.")


# ==========================================
# TWO HOUR BOOKING
# ==========================================

def two_hour():

    timings = {
        1: "7:00 AM - 9:00 AM",
        2: "9:00 AM - 11:00 AM",
        3: "11:00 AM - 1:00 PM",
        4: "1:00 PM - 3:00 PM",
        5: "3:00 PM - 5:00 PM",
        6: "5:00 PM - 7:00 PM",
        7: "7:00 PM - 9:00 PM"
    }

    while True:

        print("\n<< TWO HOUR BOOKING TIMINGS >>")
        print("=================================")

        for number, timing in timings.items():
            print(f"{number}. {timing}")

        print("=================================")

        choice = input("Enter your choice (1-7): ").strip()

        if not choice.isdigit():
            print("Input must be a number!")
            continue

        choice = int(choice)

        if choice in timings:

            print(
                f"**** Booking timing {timings[choice]} ****"
            )
            print("----------- BOOKING CONFIRMED! -----------")
            print("===========================================")

            return timings[choice]

        else:

            print("Invalid choice!")
            print("Booking is available only from 7:00 AM to 9:00 PM.")


# ==========================================
# TABLE BOOKING
# ==========================================

def booking_table():

    total_table = 10

    while True:

        try:

            user_table = input(
                "Enter the number of tables you want to book: "
            ).strip()

            if not user_table:
                print("Input can't be empty!")
                continue

            if not user_table.isdigit():
                print("Only numbers are allowed!")
                continue

            if user_table.startswith("0"):
                print("Input can't be 0 or start with zero!")
                continue

            booked = int(user_table)

            if booked > total_table:
                print(
                    f"Only {total_table} tables are available!"
                )
                continue

            print("Tables booked successfully!")
            print(f"Tables booked: {booked}")
            print(
                f"Remaining tables: {total_table - booked}"
            )
            print("=================================")

            return booked

        except Exception as error:

            print("Error:", error)


# ==========================================
# CREATE CUSTOMER BOOKING
# ==========================================

def custmor_seats():

    print("\n........<< SEAT BOOKING >>.......")

    book_data = {}

    # Customer name
    while True:

        name = input("Enter customer name: ").strip()

        if not name:
            print("Name can't be empty!")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name should contain only alphabets!")
            continue

        break

    book_data["name"] = name

    # Table booking
    tables = booking_table()

    book_data["table"] = tables

    # Maximum 5 seats per table
    max_seats = tables * 5

    book_data["seats"] = user_input(max_seats)

    # Booking duration and time
    duration, timing = user_time()

    book_data["duration"] = duration
    book_data["timing"] = timing

    # Date and time
    book_data["date_time"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Save booking
    customer_booking_data.append(book_data)

    write_data()

    print("\n******* SEAT BOOKING SUCCESSFULLY *******")
    print("=========================================")

    return book_data


# ==========================================
# VIEW BOOKING DATA
# ==========================================

def data_vew():

    while True:

        try:

            print("\n******** BOOKING DATA ********")
            print("==============================")
            print("1. SEARCH BOOKING")
            print("2. VIEW ALL BOOKING")
            print("3. EXIT")
            print("==============================")

            staff_input = input(
                "Enter your choice: "
            ).strip()

            if not staff_input.isdigit():
                print("Only numbers are allowed!")
                continue

            staff_input = int(staff_input)

            # SEARCH
            if staff_input == 1:

                user_name = input(
                    "Enter the customer name: "
                ).strip()

                found = False

                for booking in customer_booking_data:

                    if booking["name"].lower() == user_name.lower():

                        print("\n***** BOOKING FOUND *****")
                        print("=========================")
                        print(
                            json.dumps(
                                booking,
                                indent=4
                            )
                        )
                        print("=========================")

                        found = True

                if not found:
                    print("**** BOOKING NOT FOUND ****")

            # VIEW ALL
            elif staff_input == 2:

                print("\n***** ALL BOOKING DATA *****")
                print("============================")

                if not customer_booking_data:
                    print("No bookings found.")

                else:
                    print(
                        json.dumps(
                            customer_booking_data,
                            indent=4
                        )
                    )

                print("============================")

            # EXIT
            elif staff_input == 3:

                print("Exiting booking data...")
                break

            else:

                print("Invalid input!")

        except Exception as error:

            print("Error:", error)