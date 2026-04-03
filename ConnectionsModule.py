"""
# Purpose:
This is meant to host the Connections game logic and processing necessary to run the game.

# To Do:
- Select random groups and the words within that the user needs to guess -> Complete
- Retrieve a user input -> Complete
- Compare the user input to the random words -> Complete
- Run this module until the user guesses all 4 groups or after 4 incorrect attempts -> Complete
- Get a score based on this
- Return to the main module

"""
import random, time
from InputValidatorModule import UserInput
from UIModule import ConnectionsUI

with open("ConnectionsData.txt", "r") as file: #BRIEF - Accesses file of connections groups and words
    #SECT –––––– DEFINITIONS ––––––
    GroupsList = [] #BRIEF - Stores every group
    Iterable = -1 #BRIEF - Used to give an index to each group

    #SECT –––––– STORE FILE DATA ––––––
    while True:
        Iterable += 1
        line = file.readline()

        if line == "": #BRIEF - Empty line means file is fully read
            break
        #SUBSECT –––––– STORE GROUPS ––––––
        Difficulty, NameWords = line.split("-", 1) #BRIEF - Each line is structured -> DIFFICULTY-GROUPNAME;WORD1,WORD2,WORD3,WORD4
        Name, Words = NameWords.split(";")

        ThisGroup = { #BRIEF - Store information about the group
            "Name": Name,
            "WordsWithin": Words.replace("\n","").split(","), #BRIEF - \n at the end of each line
            "Difficulty": Difficulty,
            "ID": Iterable,
            "Guessed": False
        }

        GroupsList.append(ThisGroup)

def ChoseGroups(): #BRIEF - Chose 4 groups when the round begins
    #SECT –––––– KEY VALUES ––––––
    ChosenGroups = []
    ChosenDifficulties = []

    #SECT –––––– SELECT GROUPS ––––––
    while len(ChosenGroups) != 4:
        ID = random.randint(0, len(GroupsList))
        Diff = GroupsList[ID]["Difficulty"]

        if Diff not in ChosenDifficulties: #BRIEF - Prevents the same difficulty appearing twice (also prevents the same group from being chosen twice)
            ChosenDifficulties.append(Diff)
            ChosenGroups.append(GroupsList[ID])

    return ChosenGroups

def CheckGuess(groups, guess): #BRIEF - Determines the correctly guessed group
    #SECT –––––– GUESS VERIFICATION ––––––
    for group in groups:
        Correct = 0 #BRIEF - Reset correct every group because all words must be in the same group
        for word in guess:
            if word in group["WordsWithin"]:
                Correct += 1

        #SECT –––––– CHANGE GUESSED ATTRIBUTE ––––––
        if Correct == 4: #BRIEF - All 4 words were in the same group
            group["Guessed"] = True

def RemainingWords(groups): #BRIEF - Gets the words in each group and stores them in a list
    #SECT –––––– KEY VALUES ––––––
    LeftOver = []

    #SECT –––––– APPEND UNGUESSED WORDS ––––––
    for group in groups:
        if not group["Guessed"]: #BRIEF - Remaining groups must not have been guessed yet
            for word in group["WordsWithin"]:
                LeftOver.append(word)

    return LeftOver

def ConnectionsMain():
    #SECT –––––– CONSTANT VALUES ––––––
    GROUPS = ChoseGroups() #BRIEF - Contains the 4 groups to be guessed
    MAX_LIVES = 4 #BRIEF - The max amount of attempts that don't correctly guess a group

    #SECT –––––– OTHER KEY VALUES ––––––
    Attempts = 1
    LivesLost = 0


    print("To begin, enter 4 words/phrases separated by commas.")
    time.sleep(1.5)

    #SECT –––––– GAME LOOP ––––––
    while True:
        #SUBSECT –––––– UI IMPORTING ––––––
        GameStats = {  # BRIEF - Used to import data to the UI module
            "LivesRemaining": MAX_LIVES - LivesLost,
            "Attempt": Attempts,
            "Groups": GROUPS
        }

        ConnectionsUI(GameStats, "IN-GAME")
        time.sleep(1)

        #SUBSECT –––––– CHECK GUESS ––––––
        Guess = UserInput("Connections", RemainingWords(GROUPS))

        CheckGuess(GROUPS, Guess) #BRIEF - Change the "Guessed" value of a group to True if correctly guessed

        #SUBSECT –––––– UPDATE END-GAME VARIABLES ––––––
        Correct = 0
        for group in GROUPS: #BRIEF - Calculates the number of correctly guess groups
            if group["Guessed"]:
                Correct += 1

        CorrectGuesses = Correct

        Attempts += 1
        LivesLost = Attempts - CorrectGuesses

        #SUBSECT –––––– END-GAME CONDITIONS ––––––
        if CorrectGuesses == 4 or LivesLost == MAX_LIVES: #BRIEF - No groups left to guess or all lives have been used.
            break

    #SECT –––––– SHOW FINAL STATS ––––––
    if CorrectGuesses == 4:
        print("\nCongratulations on guessing all 4 groups!")
    else:
        print("\nUnlucky, these were the 4 groups:")

    for group in GROUPS: #BRIEF - Make sure that all groups will be visible
        if not group["Guessed"]:
            group["Guessed"] = True

    GameStats = {  # BRIEF - Used to import data to the UI module
        "LivesRemaining": MAX_LIVES - LivesLost,
        "Attempt": Attempts,
        "Groups": GROUPS
    }

    ConnectionsUI(GameStats, 'END')
