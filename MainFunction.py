# Zaniel Murdock
#Create the main function

# Call the other functions
# Function 1
from get_player_name_function import get_player_name

# Function 2
from P2_menu import menu

# Function 3
from Q3Fx import HomeSelection
from Q3Fx import OpponentSelection

# Function 4
from soccerCode import play_game

# Function 5
from P5_print_info import seasoninfo

# Compile main function
def main() :
    print(get_player_name())
    print(menu())
    print(HomeSelection())
    print(OpponentSelection())
    print(play_game())
    print(seasoninfo())

# This is the main code
main()
