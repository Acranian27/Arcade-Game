"""
# Purpose:
This is meant to host the Connections game logic and processing necessary to run the game.

# To Do:
- Select random groups and the words within that the user needs to guess
- Retrieve a user input
- Compare the user input to the random words
- Run this module until the user guesses all 4 groups or after 4 incorrect attempts
- Get a score based on this
- Return to the main module

"""

# Gathers the list of possible words and groups from ConnectionsData.txt
with open("ConnectionsData.txt", "r") as file:

    Groups = []
    GroupWords = []

    while True:
        line = file.readline() # file.readline() reads every single character in that line of the file

        # An empty string means the file is completely read through
        if line == "":
            break

        # Each line is structured -> GROUPNAME:WORD1,WORD2,WORD3,WORD4
        name, words = line.split(":")
        Groups.append(name)
        GroupWords.append(words.replace("\n","")) # Each line has \n at the end so it must be removed
