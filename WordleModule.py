"""
# Purpose:
This is meant to host the Wordle game logic and processing necessary to run the game.

# To Do:
- Select a random word the user needs to guess -> COMPLETE
- Retrieve a user input -> COMPLETE
- Compare the user input to the random word -> COMPLETE
- Run this module until the user guesses correctly or after 6 incorrect attempts -> COMPLETE
- Get a score based on this

"""
import random
from InputValidatorModule import UserInput
from UIModule import WordleUI

# Gathers the list of possible words from WordleData.txt
with open("WordleData.txt", "r") as file:

    FullSet = file.read() # file.read() returns every single character in the file
    UncleanList = FullSet.split("|") # Every word is separated by | with spaces on both sides

    # Cleans the unnecessary characters from the list
    CleanList = []
    for word in UncleanList:

        word = word.strip() # Remove unnecessary spaces
        CleanList.append(word)

# Chooses a random word from the list
def SelectRandomWord():

    index = random.randint(0, len(CleanList) - 1) # Python starts at zero not one

    return CleanList[index]

# Adds a state for each letter in Guess inside a list
def DetermineStates(Answer, Guess):

    LetterFrequency = {}
    LetterStates = []

    # Used to show the correct number of letters of the same type
    for letter in Answer:
        if letter in LetterFrequency:
            LetterFrequency[letter] += 1
        else:
            LetterFrequency[letter] = 1 # It must be defined before 1 can be added

    # Calculates the states for each letter
    for pos, letter in enumerate(Guess):
        if letter == Answer[pos]:
            LetterStates.append("green")
            LetterFrequency[letter] -= 1

        elif letter in Answer and LetterFrequency[letter] > 0:
            LetterStates.append("yellow")
            LetterFrequency[letter] -= 1

        else:
            LetterStates.append("grey")

    return LetterStates

# Calls the core functions to run Wordle
def WordleMain():

    RandomWord = SelectRandomWord()
    Attempts = 0
    Correct = False

    while Attempts < 6 and not Correct:

        Guess = UserInput("Wordle")
        States = DetermineStates(RandomWord, Guess)

        Attempts += 1
        WordleUI(Guess, States, Attempts)

        if Guess == RandomWord:
            Correct = True

    if Correct:
        print("Congratulations! You guessed the word correctly!")
    else:
        print("Tough luck, the word was", RandomWord)