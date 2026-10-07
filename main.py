from Authentication.auth import User

from menu.menu import (
    show_menu,
    add_item,
    update_item,
    delete_item,
    search_item
)

from orders.order import Order
from billing.bill import Billing
from inventory.inventory import Inventory

from table_booking.booking import custmor_seats, data_vew


class Restaurant:

    def __init__(self):

        self.order = Order()
        self.billing = Billing()
        self.inventory = Inventory()

    def run(self):

        while True:

            print("\n================================")
            print("    RESTAURANT MANAGEMENT SYSTEM")
            print("================================")

            print("1. Show Menu")
            print("2. Add Menu Item")
            print("3. Update Menu Item")
            print("4. Delete Menu Item")
            print("5. Take Order")
            print("6. Show Orders")
            print("7. Cancel Order")
            print("8. Generate Bill")
            print("9. Show Inventory")
            print("10. Add Inventory")
            print("11. Show Tables")
            print("12. Book Table")
            print("13. Cancel Table Booking")
            print("14. Exit")

            choice = input("\nEnter your choice: ").strip()

            # =========================
            # SHOW MENU
            # =========================
            if choice == "1":

                show_menu()

            # =========================
            # ADD MENU ITEM
            # =========================
            elif choice == "2":

                add_item()

            # =========================
            # UPDATE MENU ITEM
            # =========================
            elif choice == "3":

                update_item()

            # =========================
            # DELETE MENU ITEM
            # =========================
            elif choice == "4":

                delete_item()

            # =========================
            # TAKE ORDER
            # =========================
            elif choice == "5":

                self.order.take_order()

            # =========================
            # SHOW ORDERS
            # =========================
            elif choice == "6":

                self.order.show_orders()

            # =========================
            # CANCEL ORDER
            # =========================
            elif choice == "7":

                self.order.cancel_order()

            # =========================
            # GENERATE BILL
            # =========================
            elif choice == "8":

               self.billing.generate_bill(self.order.customer_data)

            # =========================
            # SHOW INVENTORY
            # =========================
            elif choice == "9":

                self.inventory.show_inventory()

            # =========================
            # ADD INVENTORY
            # =========================
            elif choice == "10":

               self.inventory.add_stock()
            # =========================
            # SHOW TABLE / BOOKING DATA
            # =========================
            elif choice == "11":

                data_vew()

            # =========================
            # BOOK TABLE
            # =========================
            elif choice == "12":

                custmor_seats()

            # =========================
            # CANCEL TABLE BOOKING
            # =========================
            elif choice == "13":

                print("\nCancel Table Booking is not available yet.")

            # =========================
            # EXIT
            # =========================
            elif choice == "14":

                print("\nThank you for using Restaurant Management System!")
                break

            else:

                print("\nInvalid choice!")


# =================================
# SIGN IN
# =================================

print("\n================================")
print("             SIGN IN")
print("================================")

user = User.signin()

if user:

    print("\nAccess granted!")
    print("Logged in as:", user.role)

   
if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.run()
else:

    print("\nAccess denied!")