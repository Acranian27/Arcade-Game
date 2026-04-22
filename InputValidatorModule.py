"""
# Purpose:
This is meant to get a validate a user input so that it doesn't crash other modules.

# To Do:
- Retrieve the destination of the input -> COMPLETE
- Retrieve a user input -> COMPLETE
- Compare the user input to a set of requirements -> COMPLETE FOR: MainMenu, Wordle, Connections
- Return the input to the required module -> COMPLETE

"""

import time

def MainMenuValidation(input: str, approvedInputs: str) -> str:
    ValidFormat = True

    if not len(input) == 1:  # BRIEF - Only 1 letter long
        print("\nYour input be exactly one character long.")
        ValidFormat = False

    elif not input in approvedInputs:  # BRIEF - Verify it corresponds to a button
        print("\nYour input must be one of the letters next to the buttons.")
        ValidFormat = False

    return input, ValidFormat

def WordleValidation(input: str, approvedInputs: list) -> str:
    ValidFormat = True

    if not len(input) == 5:  # BRIEF - Only 5 letters long
        print("\nYour input must be exactly five characters long.")
        ValidFormat = False

    elif not input in approvedInputs:  # BRIEF - Verify it is a real word and not "AAAAA" for eg
        print("\nYour input must be an actual word.\nThis means no numbers or symbols.")
        ValidFormat = False

    return input, ValidFormat

def ConnectionsValidation(input: str, approvedInputs: list) -> list:
    UnstrippedList = input.split(",")
    Words = []
    ValidFormat = True

    for word in UnstrippedList:  # BRIEF - Ensures each word has no extra spaces
        Words.append(word.strip())

    if not len(Words) == 4:  # BRIEF - Only 4 words long
        print("\nYour input must contain exactly 4 words/phrases, separated by commas.")
        ValidFormat = False

    else:
        for word in Words:  # BRIEF - Verify it is a word within one of the 4 groups
            if not word in approvedInputs:
                print("\nYour input must contain words/phrases as presented to you.")
                ValidFormat = False
                break  # BRIEF - Ensures the print is only outputted once

    return Words, ValidFormat

def UserInput(destination: str, approvedInputs: list) -> str or list: #BRIEF - It will be a string for all modules except for Connections.
    #SECT –––––– LOOP UNTIL VALID INPUT ––––––
    while True:
        #SUBSECT –––––– KEY VARIABLES ––––––
        ValidFormat = True
        Input = input("Input: ").upper().strip() #BRIEF - All comparisons done in uppercase

        #SUBSECT –––––– VALIDATE BASED ON DESTINATION ––––––
        if Input == "H" or Input == "Q": #BRIEF - No matter the program, these two inputs are always accepted
            return Input

        elif destination == "MainMenu":
            Input, ValidFormat = MainMenuValidation(Input, approvedInputs)

        elif destination == "Wordle":
            Input, ValidFormat = WordleValidation(Input, approvedInputs)

        elif destination == "Connections":
            Input, ValidFormat = ConnectionsValidation(Input, approvedInputs)

        if ValidFormat: #BRIEF - If anything is not how the program wants it, ValidFormat == False
            return Input

        time.sleep(0.5)
