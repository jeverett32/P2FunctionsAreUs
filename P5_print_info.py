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

# # John Everett

# # Function to display the results of the season

# # Receives the dictionary of teams, the number of wins, and the number of losses
# def seasoninfo(dictTeams, iWins, iLosses):
#     # Add a line break for readability
#     print("\n")

#     # Assign the team name to the variable sTeamName and print a title for the results section
#     sTeamName = next(iter(dictTeams))
#     print(f"-----Results for {sTeamName}'s Season-----")

#     # Access the nested Games list inside Season
#     for key, values in dictTeams.items():
#         for team_list in values:  # Extract the inner list
#             for game_list in team_list:  # Iterate through the actual game entries
#                     for game in game_list  :
#                         print(f"Result of {key} vs. {game[1]}: {game[0]} - {game[2]} ({game[3]})")

#     # Prints the final season record
#     print(f"\nFinal season record: {iWins} - {iLosses}")
#     if iWins >= iLosses:
#         print(f"You had a great season. Good Job!\n")
#     else:
#         print(f"You had a losing season. Your team needs to practice!\n")