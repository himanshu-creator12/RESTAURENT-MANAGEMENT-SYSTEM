from menu.menu import Menu
from orders.order import Order
from table_booking.booking import custmor_seats, data_vew
from billing.bill import Billing


def user_menu():

    menu = Menu()
    order = Order()
    billing = Billing()

    while True:

        try:

            print("\n================================")
            print("           USER MENU")
            print("================================")
            print("1. VIEW MENU")
            print("2. ORDER")
            print("3. BOOKING")
            print("4. GENERATE BILL")
            print("5. SEARCH ITEMS")
            print("6. BOOKING VIEW")
            print("7. EXIT")
            print("================================")

            user_input = input(
                "Enter your choice (1 to 7): "
            ).strip()

            print("=" * 30)

            # Empty input
            if not user_input:

                print("Input can't be empty!")
                continue

            # Only numbers
            if not user_input.isdigit():

                print(
                    "Enter numbers only. "
                    "Alphabet is not allowed!"
                )
                continue

            # Convert to integer
            user_choice = int(user_input)

            # Zero or negative-style invalid choice
            if user_choice < 1 or user_choice > 7:

                print(
                    "Please enter a valid choice "
                    "between 1 and 7!"
                )
                continue

            # ==================================
            # VIEW MENU
            # ==================================

            if user_choice == 1:

                menu.show_menu()

            # ==================================
            # ORDER
            # ==================================

            elif user_choice == 2:

                order.take_order()

            # ==================================
            # BOOKING
            # ==================================

            elif user_choice == 3:

                custmor_seats()

            # ==================================
            # GENERATE BILL
            # ==================================

            elif user_choice == 4:

                billing.generate_bill()

            # ==================================
            # SEARCH ITEMS
            # ==================================

            elif user_choice == 5:

                menu.search_item()

            # ==================================
            # VIEW BOOKING
            # ==================================

            elif user_choice == 6:

                data_vew()

            # ==================================
            # EXIT
            # ==================================

            elif user_choice == 7:

                print("\nExiting User Menu...")
                break

        except Exception as error:

            print("Error:", error)