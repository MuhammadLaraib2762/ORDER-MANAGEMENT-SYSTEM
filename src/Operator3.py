# Operator3.py

import json
import os


SelectionDic = {
    1: "Vegitarian",
    2: "Non_Vegitarian",
    3: "Fast_Food",
    4: "Sweet_Shop",
    5: "Ice_Cream"
}

def DisplayFoodMenu(MenuChoice):

    from Operator4 import BillMaker, finalizeOrder
    from Operator2 import DisplayMenuTypes

    global MenuChoiceName
    MenuChoiceName = SelectionDic.get(MenuChoice)

    if not MenuChoiceName:
        print("\nInvalid Menu Choice!")
        return

    if not os.path.exists("json/FoodMenu.json"):
        print("\nERROR 404: Menu file not found!")
        return

    with open("json/FoodMenu.json", "r") as f:
        food_menu = json.load(f)

    items = food_menu[MenuChoiceName]
    item_names = list(items.keys())

    while True:
        print(f"\n<<< {MenuChoiceName} MENU >>>")
        for i, item in enumerate(item_names, 1):
            print(f"{i}. {item} - ₹{items[item]}")

        print("\n0. Finalize Order")
        print("9. Change Menu Type")

        try:
            choice = int(input("\nSelect Item Number: "))

            if choice == 0:
                finalizeOrder()
                break
            elif choice == 9:
                DisplayMenuTypes()
                break
            elif 1 <= choice <= len(item_names):
                item_name = item_names[choice - 1]
                quantity = int(input(f"Enter quantity for {item_name}: "))
                BillMaker(MenuChoiceName, item_name, items[item_name], quantity)
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Invalid input, please enter a number.")
