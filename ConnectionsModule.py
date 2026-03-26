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
import random
from InputValidatorModule import UserInput

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

# Chooses 4 random groups from the list, based on the index
def SelectConnections():
    Indexes = []
    # Select an index until 4 indexes are in the list
    while not len(Indexes) == 4:
        index = random.randint(0, len(Groups) - 1)
        # Prevent the same group from being chosen twice
        if not index in Indexes:
            Indexes.append(index)

    return Indexes

def GetWords(Indexes):
    Words = []

    for index in Indexes:
        GroupOfWords = GroupWords[index].split(",")
        for word in GroupOfWords:
            Words.append(word)

    return Words

def GetGroupNames(Indexes):
    Names = []

    for index in Indexes:
        GroupOfWords = Groups[index].split(",")
        for name in GroupOfWords:
            Names.append(name)

    return Names

def ConnectionsMain():

    Indexes = SelectConnections()
    Attempts = 0
    Correct = False
    SelectedWords = GetWords(Indexes)

    print(SelectedWords)
    print("To begin, enter 4 words/phrases separated by commas.")

    while Attempts < 4 and not Correct:

        Guess = UserInput("Connections", SelectedWords)
        print(Guess)

        for index in Indexes:
            Correct = 0

            for word in Guess:
                if word in GroupWords[index]:
                    print(GroupWords[index], word)
                    Correct += 1
                    print("That word was in the group.")

            if Correct == 4:
                Correct = True
                break
            else:
                print("Not all your words were in the same group.")


