class Billing:

    def generate_bill(self, orders):

        if not orders:
            print("\nNo orders available!")
            return

        print("\n========== BILL ==========")

        subtotal = 0

        for customer in orders:

            print("\nCustomer:", customer["name"])
            print("Table:", customer["table_number"])

            print("--------------------------")

            for item in customer["order"]:

                item_total = (
                    item["price"] *
                    item["quantity"]
                )

                subtotal += item_total

                print(
                    item["item"],
                    "x",
                    item["quantity"],
                    "=",
                    item_total
                )

        # 5% Tax
        tax = subtotal * 0.05

        # 10% Discount if bill is above 1000
        if subtotal >= 1000:
            discount = subtotal * 0.10
        else:
            discount = 0

        final_amount = subtotal + tax - discount

        print("--------------------------")
        print("Subtotal :", subtotal)
        print("Tax 5%   :", tax)
        print("Discount :", discount)
        print("Final Bill:", final_amount)
        print("==========================")