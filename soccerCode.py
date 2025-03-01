# This should make the game work

# import the functions from soccerFunctions.py
from soccerFunctions import *

get_player_name()

iChoice = menu()

dictSoccer = {}

# Initialize variables for wins and losses
HomeTm = ""
OpTm = ""
iWins = 0
iLosses = 0
GameCt = 0

while iChoice in [1, 2, 3] :
    # Menu Option 1
    if iChoice == 1 :
        HomeTm = HomeSelection()
        print(HomeTm)
        iChoice = menu()
    # Menu Option 2
    elif iChoice == 2 :
        # Get initial input
        GameCt = input("Enter the number of teams "+ HomeTm + " will play against (1-7): ")
        # Keep looping until input is valid (a number)
        while not GameCt.isdigit():  
            print("Invalid input. Please enter a valid number of games.")
            # Ask again for input
            GameCt = input("How many games? ")
        # Convert to integer after validation
        GameCt = int(GameCt) 
        dictSoccer[HomeTm] = []
        for Ct in range(GameCt):
            OpTm = OpponentSelection()
            print(f"{HomeTm} is playing against {OpTm}")
        dictSoccer, iWins, iLosses = play_game(dictSoccer, HomeTm, iWins, iLosses, GameCt)
        iChoice = menu()
    # Menu Option 3
    elif iChoice == 3 :
        seasoninfo(dictSoccer, iWins, iLosses)
        iChoice = menu()
# Menu Option 4
if iChoice == 4 :
    print("Exiting Program. Goodbye!")
else:
    print("Invalid choice. Please try again.")
    iChoice = menu()
