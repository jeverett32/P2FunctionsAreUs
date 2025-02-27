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



# print(f"{HomeTm} is playing against {OpTm}")