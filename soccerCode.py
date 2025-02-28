# This is my original code for assignment A4 
# initialize lists 

#Meagan Brown
#Creating a function that explains how the game will work
#Collects the name of the player
#Returns the name to be used in the program later.
#Create a function
def get_player_name():
    #A welcome introduction to explain how the game will work
    print("Welcome to the Soccer Team Tournament Matchup!")
    print("\n   How to Play:")
    print("   1. Choose your team from the list provided.")
    print("   2. Select an opponent to challenge.")
    print("   3. The selected teams will play against each other in an intense match.")
    print("   4. Check out the final score and see which team comes out on top.\nMay the best team win!")
    #Collect the player's name
    name=input("\nTo start, enter your name: ")
    #Personalized welcome message
    print(f"Welcome, {name}! Get ready to play!")
    #Returning name to be used in the program
    return name
#Call the function to get the player's name
player_name= get_player_name()

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
    play_game(HomeTm, OpTm)



def play_game(HomeTm, OpTm):
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
        "home_team" : home_team,
        "home_score" : home_score,
        "opponent_team" : opponent_team,
        "opponent_score" : opponent_team,
        "result" : result
    }
    Season.append(games)
    return result
# append games to the season

# Display season record 
print(f'\nGame Results:')

# loop through each game to print out scores 
rounds = 0
for rounds in range(GameCt):
    print(f"{HomeTm}'s score: {Games[rounds][0]} {Games[rounds][1]}'s score: {Games[rounds][2]}")
    rounds +=1

print(f"\nFinal season record: {Win} - {Loss} ")

# calculate and print game stats 
if GameCt >0:
    Percent = float(Win/(GameCt))
else: Percent = 0

if Percent >= 0.75:
    print("Qualified for the NCAA Women's Soccer Tournament")
elif Percent >=0.5:
    print("You had a good season")
else: print("Your team needs to practice!")
