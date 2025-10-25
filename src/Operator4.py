# Operator4.py

import json
import os

BILL_FILE_PATH = "json/bill_maker.json"

def initialize_bill_file():
    if not os.path.exists(BILL_FILE_PATH):
        with open(BILL_FILE_PATH, "w") as f:
            json.dump([], f)


def BillMaker(MenuChoiceName, ItemName, ItemPrice, ItemQuantity):
    try:
        initialize_bill_file()

        with open(BILL_FILE_PATH, "r") as f:
            order_data = json.load(f)

        # Check if item already exists → just update quantity
        found = False
        for item in order_data:
            if item["name"] == ItemName:
                item["quantity"] += ItemQuantity
                item["total"] = item["quantity"] * item["unit_price"]
                found = True
                break

        # If not found, add as new item
        if not found:
            order_data.append({
                "category": MenuChoiceName,
                "name": ItemName,
                "quantity": ItemQuantity,
                "unit_price": ItemPrice,
                "total": ItemPrice * ItemQuantity
            })

        # Save changes
        with open(BILL_FILE_PATH, "w") as f:
            json.dump(order_data, f, indent=4)

        print(f"\n✅ Added {ItemQuantity} x {ItemName} (₹{ItemPrice}/unit) to cart.")

    except Exception as e:
        print(f"Error adding item: {e}")


def finalizeOrder():
    try:
        initialize_bill_file()

        with open(BILL_FILE_PATH, "r") as f:
            order_data = json.load(f)

        if not order_data:
            print("\n🛒 Your cart is empty.")
            return

        print("\n<<<  YOUR FINAL BILL  >>>")
        print(f"{'Item Name':25} {'Qty':>5} {'Unit':>10} {'Total':>10}")
        print("-" * 55)

        grand_total = 0
        for item in order_data:
            print(f"{item['name']:25} {item['quantity']:>5} {item['unit_price']:>10} {item['total']:>10}")
            grand_total += item["total"]

        print("-" * 55)
        print(f"{'GRAND TOTAL':>45} {grand_total:>10}")

        confirm = input("\nFinalize and clear cart? (y/n): ").lower()
        if confirm == "y":
            with open(BILL_FILE_PATH, "w") as f:
                json.dump([], f)
            print("\n✅ Order finalized and cleared. Thank you for visiting!")
        else:
            print("\n✅ Order finalized and saved for record.")

    except Exception as e:
        print(f"Error finalizing order: {e}")
