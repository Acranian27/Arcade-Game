"""
# Purpose:
This is meant to host the Connections game logic and processing necessary to run the game.

# To Do:
- Select random groups and the words within that the user needs to guess -> Complete
- Retrieve a user input -> Partially Complete
- Compare the user input to the random words -> Complete
- Run this module until the user guesses all 4 groups or after 4 incorrect attempts -> Complete
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
        GroupOfWords = GroupWords[int(index)].split(",")
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

# Returns the groups that still need to be guessed
def RemainingGroups(Indexes, CompletedIndexes):
    UnguessedIndexes = []
    # Calculate the groups left to guess
    for i in Indexes:
        if not i in CompletedIndexes:
            UnguessedIndexes.append(i)

    if len(UnguessedIndexes) == 0:
        return 0
    else:
        return UnguessedIndexes

def CorrectGuess(Indexes, Guess, Validity): #BRIEF - Determines if the user guessed a group completely
    # SECT –––––– GUESS VERIFICATION ––––––
    for index in Indexes:
        Correct = 0 #BRIEF - Reset correct every group because all words must be in the same group
        for word in Guess:
            if word in GroupWords[index]:
                Correct += 1
                print("That word was in the group.")

        #SECT –––––– CHOOSE RETURN VALUES ––––––
        if Correct == 4: #BRIEF - All 4 words were in the same group
            print("You guessed a group correctly.")
            if Validity: #BRIEF - Is the index wanted or the fact that it was a correct guess?
                return True
            else:
                return index

    if Validity: #BRIEF - No index to return because no group was guessed correctly
        return False
    else:
        return None #BRIEF - Not possible unless code is meddled with


def ConnectionsMain():
    #SECT –––––– CONSTANT VALUES ––––––
    Indexes = SelectConnections()
    Lives = 4

    #SECT –––––– OTHER KEY VALUES ––––––
    Attempts = 0
    UnguessedIndexes = Indexes #BRIEF - Placeholder for first round
    CompletedIndexes = []

    print("To begin, enter 4 words/phrases separated by commas.")

    while True:
        #SECT –––––– REMAINING WORDS ––––––
        OrderedList = GetWords(UnguessedIndexes) #BRIEF - Remaining words
        print("Ordered:",OrderedList)

        PresentedList = OrderedList
        random.shuffle(PresentedList) #BRIEF - Remaining words in a shuffled order
        print("Shuffled:",PresentedList)

        #SECT –––––– ATTEMPT TRACKING ––––––
        Attempts += 1
        print("Attempt:", Attempts)

        #SECT –––––– GUESS CALCULATIONS ––––––
        Guess = UserInput("Connections", OrderedList)
        print(Guess)

        Success = CorrectGuess(Indexes, Guess, True)
        if Success: #BRIEF - Only append if there was a correct guess
            CompletedIndexes.append(CorrectGuess(Indexes, Guess, False))

        #SECT –––––– END-GAME VALUES CALCULATIONS ––––––
        LivesLost = Attempts - len(CompletedIndexes)
        UnguessedIndexes = RemainingGroups(Indexes,CompletedIndexes) #BRIEF - Set to the indexes not in CompletedIndexes

        print("Lives lost:", LivesLost)
        print("Unguessed indexes:", UnguessedIndexes)

        #SECT –––––– END-GAME CONDITIONS ––––––
        if UnguessedIndexes == 0 or LivesLost == Lives: #BRIEF - No groups left to guess or all lives have been used.
            break
