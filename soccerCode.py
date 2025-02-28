# This is my original code for assignment A4 
# initialize lists 
Soccer = {}
Season = []
Games = []

TeamOptions = ["Utah State", "BYU", "UCLA", "Florida State", "Notre Dame", "BSU", "USC", "Penn State"] 


# gather inputs/set information 

from Q3Fx import HomeSelection, OpponentSelection
from get_player_name_function import get_player_name
from Q5Fx import seasoninfo

player_name= get_player_name()

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
    HmScr =0 
    OpScr = 0 

    import random

    while HmScr == OpScr:
        HmScr = random.randrange(0, 10)
        OpScr = random.randrange(0, 10)

    if HmScr > OpScr:
        Win +=1
        Result = "Win"
    else:
        Loss +=1
        Result = "Loss"
    Num += 1
    Games.append([HmScr, OpTm, OpScr, Result])
    # append each score to the list of games

# append games to the season
Season.append([Games])

# Call seasoninfo() to display the results of the season
seasoninfo(Soccer, Win, Loss)