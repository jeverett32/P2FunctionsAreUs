# Aysha Entrikin
# This code displays a menu and stores the user input in a variable for future use in calling functions

def menu() :
    # print the menu
    print("Menu: ")
    print("1. Choose your team and the opposing teams")
    print("2. Play the game")
    print("3. View the season record")
    print("4. Exit")

    # get user input but do not allow any input outside of the menu choices
    while not iChoice in [1, 2, 3, 4] :
        iChoice = int(input("\nChoose an option (1, 2, 3, or 4) ")) 
    if iChoice not in [1, 2, 3, 4] :   
        print("\nPlease enter a valid number ")

    # return the input
    return iChoice