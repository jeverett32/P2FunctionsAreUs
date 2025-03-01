# This is my original code for assignment A4 
# initialize lists 

# import menu function and assign it to a variable to get the user's input
from P2_menu import menu
from get_player_name_function import get_player_name
from P5_print_info import seasoninfo

player_name= get_player_name()

menuChoice = menu()

Soccer = {}
Season = []
Games = []

TeamOptions = ["Utah State", "BYU", "UCLA", "Florida State", "Notre Dame", "BSU", "USC", "Penn State"] 


# gather inputs/set information 

from Q3Fx import HomeSelection, OpponentSelection

HomeTm = HomeSelection()
print(HomeTm)

GameCt = int(input("Enter the number of teams "+ HomeTm + " will play against (1-7): "))

Soccer[HomeTm] = Season

Win = 0
Loss = 0 
Num = 1


# Gather game-specific information (name, scores, etc)
for Ct in range(GameCt):
    
    OpTm = OpponentSelection()

    print(f"{HomeTm} is playing against {OpTm}")

    # for game # 


def play_game(HomeTm, OpTm):
    import random
    home_score = 0
    opponent_score = 0
    #generate the scores for the game
    while home_score == opponent_score:
        home_score = random.randint(0, 10)
        opponent_score = random.randint(0, 10)
    #calculate the result
    result = "W" if home_score > opponent_score else "L"
    #store the games
    games = {
        "home_team": HomeTm,
        "home_score" : home_score,
        "opponent_team" : OpTm,
        "opponent_score" : opponent_score,
        "result" : result
    }
    Season.append(games)
    return result
# append games to the season

play_game(HomeTm, OpTm)

# print results of the season
seasoninfo(Soccer, Win, Loss)
