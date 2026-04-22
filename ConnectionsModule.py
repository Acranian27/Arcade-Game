"""
# Purpose:
This is meant to host the Connections game logic and processing necessary to run the game.

# To Do:
- Select random groups and the words within that the user needs to guess -> Complete
- Retrieve a user input -> Complete
- Compare the user input to the random words -> Complete
- Run this module until the user guesses all 4 groups or after 4 incorrect attempts -> Complete
- Get a score based on this -> COMPLETE

"""
import random, time
from InputValidatorModule import UserInput
from UIModule import ConnectionsUI
from ScoreModule import ScoreFunc, GetConnectionsHighscore

#SECT –––––– COLOURS ––––––
YELLOW_REGULAR = "\033[0;33m"
RESET_COLOUR = "\033[0m"

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

def HelpMenu() -> None:
    print(f"\n\n{YELLOW_REGULAR}It seems that you want some help.")
    print("Connections is a fairly simple game once you understand the rules.\n")
    time.sleep(2)
    print("You are presented with 16 words, and there are 4 hidden groups.\n"
          "You do not know what these groups are, but you have to guess 4 words in the same group.\n"
          "Once you do this, the group name will be revealed.\n")
    time.sleep(4)
    print("This is then repeated for the next 3 groups until either you guessed them all or ran out of lives.\n"
          "That's right, you get 3 incorrect guesses, and any more means you lose.\n")
    time.sleep(4)
    print(f"Now that you know how to play Connections, lets get guessing!{RESET_COLOUR}")

def ChoseGroups() -> list: #BRIEF - Chose 4 groups when the round begins
    #SECT –––––– KEY VALUES ––––––
    ChosenGroups = []
    ChosenDifficulties = []

    #SECT –––––– SELECT GROUPS ––––––
    while len(ChosenGroups) != 4:
        ID = random.randint(0, len(GroupsList))
        Diff = GroupsList[ID]["Difficulty"]

        if Diff not in ChosenDifficulties: #BRIEF - Prevents the same difficulty appearing twice (also prevents the same group from being chosen twice)
            ChosenDifficulties.append(Diff)

            GroupsList[ID]["Guessed"] = False #BRIEF - Ensures that the group's "Guessed" data is set correctly
            ChosenGroups.append(GroupsList[ID])


    return ChosenGroups

def CheckGuess(groups: list, guess: list) -> None: #BRIEF - Determines the correctly guessed group
    #SECT –––––– GUESS VERIFICATION ––––––
    for group in groups:
        PreviouslyGuessedWords = [] #BRIEF - Ensure that each word guessed is unique
        Correct = 0 #BRIEF - Reset correct every group because all words must be in the same group
        for word in guess:
            if word in group["WordsWithin"] and word not in PreviouslyGuessedWords:
                Correct += 1
                PreviouslyGuessedWords.append(word)

        #SECT –––––– CHANGE GUESSED ATTRIBUTE ––––––
        if Correct == 4: #BRIEF - All 4 words were in the same group
            group["Guessed"] = True

def RemainingWords(groups) -> list: #BRIEF - Gets the words in each group and stores them in a list
    #SECT –––––– KEY VALUES ––––––
    LeftOver = []

    #SECT –––––– APPEND UNGUESSED WORDS ––––––
    for group in groups:
        if not group["Guessed"]: #BRIEF - Remaining groups must not have been guessed yet
            for word in group["WordsWithin"]:
                LeftOver.append(word)

    return LeftOver

def ConnectionsMain() -> None:
    #SECT –––––– CONSTANT VALUES ––––––
    GROUPS: list = ChoseGroups() #BRIEF - Contains the 4 groups to be guessed
    MAX_LIVES = 4 #BRIEF - The max amount of attempts that don't correctly guess a group

    #SECT –––––– OTHER KEY VALUES ––––––
    Attempts = 1
    LivesLost = 0
    StartTime: float = time.time()
    CorrectGuesses = 0
    Score = 0


    print("To begin, enter 4 words/phrases separated by commas, or type 'H' for help.")
    time.sleep(1.5)

    #SECT –––––– GAME LOOP ––––––
    while True:
        #SUBSECT –––––– UI IMPORTING ––––––
        GameStats = {  # BRIEF - Used to export data to the UI module
            "LivesRemaining": MAX_LIVES - LivesLost,
            "Attempt": Attempts,
            "Groups": GROUPS
        }

        ConnectionsUI(GameStats, "IN-GAME")
        time.sleep(1)

        #SUBSECT –––––– CHECK GUESS ––––––
        Guess: list = UserInput("Connections", RemainingWords(GROUPS))

        if Guess == "Q": #BRIEF - Quit the module
            print("It seems you want to quit early, lets head back then.")
            break

        elif Guess == "H": #BRIEF - Give helpful information
            HelpMenu()

        else: #BRIEF - Run the actual game
            CheckGuess(GROUPS, Guess)  # BRIEF - Change the "Guessed" value of a group to True if correctly guessed

            # SUBSECT –––––– UPDATE END-GAME VARIABLES ––––––
            Correct = 0
            for group in GROUPS:  # BRIEF - Calculates the number of correctly guess groups
                if group["Guessed"]:
                    Correct += 1

            CorrectGuesses = Correct

            LivesLost = Attempts - CorrectGuesses

            # SUBSECT –––––– END-GAME CONDITIONS ––––––
            if CorrectGuesses == 4 or LivesLost == MAX_LIVES:  # BRIEF - No groups left to guess or all lives have been used.
                TotalTime: float = time.time() - StartTime
                Score = ScoreFunc(TotalTime, Attempts, "Connections", CorrectGuesses == 4)
                break

            Attempts += 1

    #SECT –––––– SHOW FINAL STATS ––––––
    if CorrectGuesses == 4:
        print("\nCongratulations on guessing all 4 groups!")
    else:
        print("\nUnlucky, these were the 4 groups:")

    for group in GROUPS: #BRIEF - Ensure all groups will be visible when the UI module is called
        if not group["Guessed"]:
            group["Guessed"] = True

    GameStats = {  # BRIEF - Used to export data to the UI module
        "LivesRemaining": MAX_LIVES - LivesLost,
        "Attempt": Attempts,
        "Groups": GROUPS
    }

    ConnectionsUI(GameStats, 'END')

    print("Your final score is:", Score)
    print("Your highscore is:", GetConnectionsHighscore())