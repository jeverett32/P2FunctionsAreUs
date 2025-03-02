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
    print("   4. Check out the final score and see which team comes out on top.\n\nMay the best team win!")
    #Collect the player's name
    name=input("\nTo start, enter your name: ")
    #Personalized welcome message
    print(f"Welcome, {name}! Get ready to play!")
    #Returning name to be used in the program
    return name
# Aysha Entrikin
# This code displays a menu and stores the user input in a variable for future use in calling functions
def menu() :
    # print the menu
    # iChoice = 0
    # while iChoice != 4 :
    #     iChoice = 0
    print("\nMenu: ")
    print("1. Choose your team")
    print("2. Choose the opposing teams and Play the game")
    print("3. View the season record")
    print("4. Exit")
    # get user input but do not allow any input outside of the menu choices
    bCont = True
    while bCont == True :
        try :
            iChoice = int(input("\nChoose an option (1, 2, 3, or 4) "))
            bCont = False
        except ValueError :
            print("\nPlease enter a valid number ")
    # return the input
    return iChoice
# Kiera's function?
# Display list of all teams 
# #and allow the user to choose a team using a menu. 
# #Call the function again to let the user choose the opponent 
# # but do not display the team they chose previously. 
# # Remove that team from the list. 
# Allow the user to select an opponent, and return team name. 
# This function should receive a parameter but give it a default value if none is passed.
#  You can use this function for both choosing the home team and the opponent team.

TeamOptions = ["Utah State", "BYU", "UCLA", "Florida State", "Notre Dame", "BSU", "USC", "Penn State"] 
# this is the home team selection from a preset list 
def HomeSelection(TeamList = None):
    track = 1
    while track ==1:
        print("Here is a list of teams in the tournament: ")
        count = 1
        for Team in TeamOptions:
            print (f"{count}. {Team}")
            count += 1
        Choice = int(input("Please enter the number of the Home Team: "))
        if Choice > 0 and Choice <= len(TeamOptions):
            HomeTm = TeamOptions[Choice-1]
            TeamOptions.pop((Choice - 1))
            track = 2
        else:
            print("Invalid choice. Please try again.")
    return HomeTm
# this is a selection of the opposing team 
def OpponentSelection(TeamList = None):
    track = 1
    while track ==1:
        print("Here is a list of remaining teams in the tournament: ")
        count = 1
        for Team in TeamOptions:
            print (f"{count}. {Team}")
            count += 1
        Choice = int(input("Please enter the number of the opposing Team: "))
        if Choice > 0 and Choice <= len(TeamOptions):
            OpTm = TeamOptions[Choice-1]
            TeamOptions.pop((Choice - 1))
            track = 2
        else:
            print("Invalid choice. Please try again.")
    return OpTm

# Will's function
def play_game(dictSoccer, HomeTm, iWins, iLosses, iNumGames):
    import random
    for iGame in range(iNumGames):
        # Select an opponent
        OpTm = OpponentSelection()
        # Generate random scores for the
        iHomeScore = 0
        iOppScore = 0
        while iHomeScore == iOppScore:
            iHomeScore = random.randint(1, 10)
            iOppScore = random.randint(1, 10)
        # Determine Win/Loss
        if iHomeScore > iOppScore:
            sWin = "Win"
            iWins += 1
        else:
            sWin = "Loss"
            iLosses += 1
        # Append game record to the team's game list
        dictSoccer[HomeTm].append({
            'Opponent': OpTm, 
            'Home Score': iHomeScore, 
            'Opponent Score': iOppScore, 
            'Record': sWin})
    # Return the dictionary of games
    return dictSoccer, iWins, iLosses
# John Everett
# Function to display the results of the season
# Receives the dictionary of teams, the number of wins, and the number of losses
def seasoninfo(dictTeams, iWins, iLosses):
    # Add a line break for readability
    print("\n")
    # Assign the team name to the variable sTeamName and print a title for the results section
    sTeamName = next(iter(dictTeams))
    print(f"-----Results for {sTeamName}'s Season-----")
    # Access the nested Games list inside Season
    for key, values in dictTeams.items():
        for game_list in values:  # Extract the inner list
            for game in game_list:  # Iterate through the actual game entries
                print(f"Result of {key} vs. {game[1]}: {game[0]} - {game[2]} ({game[3]})")
    # Prints the final season record
    print(f"\nFinal season record: {iWins} - {iLosses}")
    if iWins >= iLosses:
        print(f"You had a great season. Good Job!\n")
    else:
        print(f"You had a losing season. Your team needs to practice!\n")
