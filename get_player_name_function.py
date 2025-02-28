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