class Inventory:

    def __init__(self):

        self.stock = {
            "Pizza": 20,
            "Burger": 20,
            "Pasta": 15,
            "Cold Drink": 30
        }

    def show_inventory(self):

        print("\n========== INVENTORY ==========")

        for item, quantity in self.stock.items():
            print(
                item,
                ":",
                quantity
            )

    def add_stock(self):

        item = input(
            "\nEnter item name: "
        )

        if item in self.stock:

            quantity = int(
                input("Enter quantity: ")
            )

            self.stock[item] += quantity

            print(
                "Stock updated successfully!"
            )

        else:
            print("Item not found!")

    def use_stock(self, item, quantity):

        if item in self.stock:

            if self.stock[item] >= quantity:

                self.stock[item] -= quantity

                return True

            else:

                print(
                    "Not enough stock!"
                )
                return False

        return False