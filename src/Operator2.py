#    Operator2.py

def DisplayMenuTypes():

    from Operator3 import DisplayFoodMenu
    print("\n PLease Select Menu Type :")
    print("\n<<<============================================>>>")
    
    try:
        for index in range(len(MenuTypes)):
            print(f"\n{index + 1}. {MenuTypes[index]}")
            
        MenuChoice = int(input("\nEnter your Menu Type :"))
        print("\n<<<============================================>>>")

        if  1 <= MenuChoice <= len(MenuTypes):
             print(f"\nYou have selected {MenuTypes[MenuChoice -1]}")
             print("\nMenu Loading...")
             DisplayFoodMenu(MenuChoice)

        else:
            print("\nYou Entered Invalid Choice. Want to Exit Or Continue:\n1. Continue\n2. Exit")
            ExitOrContinue_Choice = int(input("\nEnter Your Choice :"))

            if ExitOrContinue_Choice == 1:
                print("\nContinuing to Menu...")
                DisplayMenuTypes()

            else:
                print("\nExiting...Thank You For Visiting...")
                print("\n<<< Hope To See you Again At Foodie's Paradise >>>")

    except ValueError:
        print("\nInvalid Input. Please enter a number corresponding to the menu types.")
        DisplayMenuTypes()

    except Exception as e:
        print(f"\nAn error orrured: {e}")


MenuTypes = ["Vegitarian", "Non-Vegitarian","Fast Food", "Sweet Shop", "Ice Cream"]
