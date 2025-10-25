# Operator2.py

MenuTypes = ["Vegitarian", "Non-Vegitarian", "Fast Food", "Sweet Shop", "Ice Cream"]

def DisplayMenuTypes():

    from Operator3 import DisplayFoodMenu
    
    print("\nPlease Select Menu Type:")
    print("<<<============================================>>>")

    try:
        for index, menu in enumerate(MenuTypes, 1):
            print(f"{index}. {menu}")

        MenuChoice = int(input("\nEnter your Menu Type (1-5): "))
        print("\n<<<============================================>>>")

        if 1 <= MenuChoice <= len(MenuTypes):
            print(f"\nYou have selected {MenuTypes[MenuChoice - 1]}")
            DisplayFoodMenu(MenuChoice)
        else:
            print("\nInvalid choice! Try again.")
            DisplayMenuTypes()

    except ValueError:
        print("\nInvalid input! Enter a number.")
        DisplayMenuTypes()
