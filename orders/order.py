import json
from datetime import datetime


# ==========================================
# ORDER FILE
# ==========================================

ORDER_FILE = "order_data.json"


class Order:

    def __init__(self):

        self.customer_data = []
        self.load_orders()

    # ==========================================
    # LOAD ORDERS
    # ==========================================

    def load_orders(self):

        try:

            with open(ORDER_FILE, "r") as file:
                self.customer_data = json.load(file)

        except FileNotFoundError:

            self.customer_data = []

        except json.JSONDecodeError:

            self.customer_data = []

    # ==========================================
    # SAVE ORDERS
    # ==========================================

    def write_order(self):

        with open(ORDER_FILE, "w") as file:

            json.dump(
                self.customer_data,
                file,
                indent=4
            )

    # ==========================================
    # VALIDATE TABLE
    # ==========================================

    def valid_table(self):

        total_table = 10

        while True:

            table_number = input(
                "Enter the table number (1-10): "
            ).strip()

            if not table_number:

                print("Input can't be empty!")
                continue

            if not table_number.isdigit():

                print("Please enter a valid table number!")
                continue

            if table_number.startswith("0"):

                print("Input can't start with zero!")
                continue

            table = int(table_number)

            if table < 1 or table > total_table:

                print(
                    f"Please enter a table number between 1 and {total_table}."
                )
                continue

            return table

    # ==========================================
    # VALIDATE SEATS
    # ==========================================

    def valid_seats(self):

        total_seats = 50

        while True:

            seats_number = input(
                "Enter the number of seats: "
            ).strip()

            if not seats_number:

                print("Input can't be empty!")
                continue

            if not seats_number.isdigit():

                print("Please enter a valid number of seats!")
                continue

            if seats_number.startswith("0"):

                print("Input can't start with zero!")
                continue

            seats = int(seats_number)

            if seats < 1 or seats > total_seats:

                print(
                    f"Please enter seats between 1 and {total_seats}."
                )
                continue

            return seats

    # ==========================================
    # TAKE ORDER
    # ==========================================

    def order_items(self):

        ordered_items = []
        total = 0

        print("\n******** PLACE YOUR ORDER ********")
        print("===================================")

        while True:

            item_name = input(
                "\nEnter item name (or 'done' to finish): "
            ).strip()

            if not item_name:

                print("Input cannot be empty!")
                continue

            if item_name.lower() == "done":

                break

            # ----------------------------------
            # Ask price
            # ----------------------------------

            price_input = input(
                f"Enter price for {item_name}: "
            ).strip()

            if not price_input:

                print("Price cannot be empty!")
                continue

            try:

                price = float(price_input)

            except ValueError:

                print("Please enter a valid price!")
                continue

            if price <= 0:

                print("Price must be greater than 0!")
                continue

            # ----------------------------------
            # Quantity
            # ----------------------------------

            quantity_input = input(
                f"Enter quantity for {item_name}: "
            ).strip()

            if not quantity_input:

                print("Quantity cannot be empty!")
                continue

            if not quantity_input.isdigit():

                print("Please enter a valid quantity!")
                continue

            if quantity_input.startswith("0"):

                print("Quantity can't start with zero!")
                continue

            quantity = int(quantity_input)

            if quantity <= 0:

                print("Quantity must be greater than 0!")
                continue

            item_total = price * quantity

            total += item_total

            ordered_items.append(
                {
                    "item": item_name,
                    "quantity": quantity,
                    "price": price,
                    "total": item_total
                }
            )

            print(
                f"{item_name} added successfully!"
            )

            print(
                f"Item total: ₹{item_total:.2f}"
            )

        return ordered_items, total

    # ==========================================
    # TAKE ORDER
    # ==========================================

    def take_order(self):

        print("\n******** ORDER ********")
        print("=======================")

        # Customer name
        while True:

            name = input(
                "Enter customer name: "
            ).strip()

            if not name:

                print("Name can't be empty!")
                continue

            if not name.replace(" ", "").isalpha():

                print(
                    "Name should contain only alphabets!"
                )
                continue

            break

        # Table
        table_number = self.valid_table()

        # Seats
        seats = self.valid_seats()

        # Order items
        items, total = self.order_items()

        # If no item was ordered
        if not items:

            print("\nNo items were ordered.")
            return

        # Create order
        customer = {

            "name": name,

            "table_number": table_number,

            "seats_number": seats,

            "order": items,

            "total": total,

            "order_time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        self.customer_data.append(customer)

        self.write_order()

        print("\n===================================")
        print("       ORDER SUCCESSFUL!")
        print("===================================")

        print("Customer:", name)
        print("Table:", table_number)
        print("Seats:", seats)
        print(f"Total: ₹{total:.2f}")

        print("===================================")

    # ==========================================
    # SHOW ORDERS
    # ==========================================

    def show_orders(self):

        self.load_orders()

        print("\n******** ALL ORDERS ********")
        print("============================")

        if not self.customer_data:

            print("No orders found.")
            return

        for number, order in enumerate(
            self.customer_data,
            start=1
        ):

            print(f"\nOrder #{number}")
            print("----------------------------")

            print("Customer:",
                  order["name"])

            print("Table:",
                  order["table_number"])

            print("Seats:",
                  order["seats_number"])

            print("Order items:")

            for item in order["order"]:

                print(
                    f"  {item['item']} "
                    f"x {item['quantity']} "
                    f"= ₹{item['total']:.2f}"
                )

            print(
                f"Total: ₹{order['total']:.2f}"
            )

            print(
                "Time:",
                order["order_time"]
            )

    # ==========================================
    # CANCEL ORDER
    # ==========================================

    def cancel_order(self):

        self.load_orders()

        if not self.customer_data:

            print("\nNo orders available to cancel.")
            return

        self.show_orders()

        print("\n============================")

        choice = input(
            "Enter order number to cancel: "
        ).strip()

        if not choice.isdigit():

            print("Please enter a valid number!")
            return

        order_number = int(choice)

        if (
            order_number < 1
            or order_number > len(self.customer_data)
        ):

            print("Invalid order number!")
            return

        removed_order = self.customer_data.pop(
            order_number - 1
        )

        self.write_order()

        print("\nOrder cancelled successfully!")

        print(
            "Customer:",
            removed_order["name"]
        )

        print(
            "Table:",
            removed_order["table_number"]
        )