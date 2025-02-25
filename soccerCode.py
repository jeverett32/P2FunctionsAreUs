# This is my original code for assignment A4 

# initialize lists 
Soccer = {}
Season = []
Games = []

# gather inputs/set information 
HomeTm = input("Enter the name of your home team: ")
GameCt = int(input("Enter the number of teams "+ HomeTm + " will play against (1-10): "))

Soccer[HomeTm] = Season

Win = 0
Loss = 0 
Num = 1


# Gather game-specific information (name, scores, etc)
for Ct in range(GameCt):
    OpTm = input(f"Enter the name of the away team for game {Num}: ")
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
Season.append([Games])
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