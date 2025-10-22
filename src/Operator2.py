#    Operator2.py

from Operator3 import DisplayFoodMenu


def DisplayMenuTypes():
    print("\n PLease Select Menu Type :")
    print("<<<============================================>>>")
    
    try:
        for index in range(len(MenuTypes)):
            print(f"{index + 1}. {MenuTypes[index]}")
            
        MenuChoice = int(input("Enter your Menu Type :"))
        print("<<<============================================>>>")

        if  1 <= MenuChoice <= len(MenuTypes):
             print(f"You have selected {MenuTypes[MenuChoice -1]}")
             print("Menu Loading...")
             DisplayFoodMenu(MenuChoice)

        else:
            print("You Entered Invalid Choice. Want to Exit Or Continue:\n1. Continue\n2. Exit")
            ExitOrContinue_Choice = int(input("Enter Your Choice :"))

            if ExitOrContinue_Choice == 1:
                print("Continuing to Menu...")
                DisplayMenuTypes()

            else:
                print("Exiting...Thank You For Visiting...")
                print("<<< Hope To See you Again At Foodie's Paradise >>>")

    except ValueError:
        print("Invalid Input. Please enter a number corresponding to the menu types.")
        DisplayMenuTypes()

    except Exception as e:
        print(f"An error orrured: {e}")


MenuTypes = ["Vegitarian", "Non-Vegitarian","Fast Food", "Sweet Shop", "Ice Cream"]
