# Operator3.py

import json
import os

def DisplayFoodMenu(MenuChoice):

    from goodbye import GoodByeMessages
    from Operator4 import finalizeOrder
    from Operator2 import DisplayMenuTypes
    from Operator1 import DisplayWelcomeMessage

    if MenuChoice not in SelectionDic:
        print("\nInvalid Menu Choice")
        return
    
    MenuChoiceName = SelectionDic[MenuChoice]
    print(f"\nDisplaying {MenuChoiceName} Menu Items:")

    try:
        if not os.path.exists("json/FoodMenu.json"):
            print("\nPath Not Found... ERROR 404")
            return
        
        with open("json/FoodMenu.json", "r") as f:
            food_menu = json.load(f)

        items = food_menu[MenuChoiceName]
        itemNum = 1

        for item in items:
            print(f"\n{itemNum}. {item} - Price: {items[item]}Rs/-")
            itemNum += 1
        
        ItemChoice = int(input("\nSelect the Food Item :"))
        print("\nSelected Item is Add in Cart.\n1. Add more Items from this Menu.\n2. Change Menu Type.\n3. Finalize order\n4. Exit From Here")
        ThisMenuChangeMenuFinalizeExitChoice = int(input("\nEnter Your Choice :"))
        print("\nIf You Entered wrong Choice System will be return on home screen")

        if ThisMenuChangeMenuFinalizeExitChoice == 1:
            DisplayFoodMenu(MenuChoice)
        elif ThisMenuChangeMenuFinalizeExitChoice == 2:
            DisplayMenuTypes()
        elif ThisMenuChangeMenuFinalizeExitChoice == 3:
            finalizeOrder()
        elif ThisMenuChangeMenuFinalizeExitChoice == 4:
            GoodByeMessages()
        else:
            print("\nInvalid Choice...!")
            DisplayWelcomeMessage()

    except Exception as e:
        print(f"\nERROR OCCURRED: {e}")


SelectionDic = {
    1: "Vegitarian",
    2: "Non_Vegitarian",
    3: "Fast_Food",
    4: "Sweet_Shop",
    5: "Ice_Cream"
}
