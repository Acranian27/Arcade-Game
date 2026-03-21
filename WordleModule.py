"""
# Purpose:
This is meant to host the Wordle game logic and processing necessary to run the game.

# To Do:
- Select a random word the user needs to guess
- Retrieve a user input
- Compare the user input to the random word
- Run this module until the user guesses correctly or after 6 incorrect attempts
- Get a score based on this
- Return to the main module

"""

# Gathers the list of possible words from WordleData.txt
with open("WordleData.txt", "r") as file:

    FullSet = file.read() # file.read() returns every single character in the file
    UncleanList = FullSet.split("|") # Every word is separated by | with spaces on both sides

    # Cleans the unnecessary characters from the list
    CleanList = []
    for word in UncleanList:

        word = word.strip() # Remove unnecessary spaces
        CleanList.append(word)