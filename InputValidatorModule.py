"""
# Purpose:
This is meant to get a validate a user input so that it doesn't crash other modules.

# To Do:
- Retrieve the destination of the input -> COMPLETE
- Retrieve a user input -> COMPLETE
- Compare the user input to a set of requirements -> COMPLETE FOR: MainMenu, Wordle, Connections
- Return the input to the required module -> COMPLETE

"""

def UserInput(destination, approvedInputs):
    #SECT –––––– LOOP UNTIL VALID INPUT ––––––
    while True:
        #SUBSECT –––––– KEY VARIABLES ––––––
        ValidFormat = True
        Input = input("Input: ").upper() #BRIEF - All comparisons done in uppercase

        if Input == "H" or Input == "Q":
            return Input

        #SUBSECT –––––– MAIN MENU VALIDATION ––––––
        if destination == "MainMenu":
            if not len(Input) == 1: #BRIEF - Only 1 letter long
                print("Your input be exactly one character long.")
                ValidFormat = False

            elif not Input in approvedInputs: #BRIEF - Verify it corresponds to a button
                print("Your input must be one of the letters next to the buttons.")
                ValidFormat = False

        #SUBSECT –––––– WORDLE VALIDATION ––––––
        elif destination == "Wordle":
            if not len(Input) == 5: #BRIEF - Only 5 letters long
                print("Your input must be exactly five characters long.")
                ValidFormat = False

            elif not Input in approvedInputs: #BRIEF - Verify it is a real word and not "AAAAA" for eg
                print("Your input must be an actual word.\nThis means no numbers or symbols.")
                ValidFormat = False

        #SUBSECT –––––– CONNECTIONS VALIDATION ––––––
        elif destination == "Connections":
            UnstrippedList = Input.split(",")
            Words = []

            for word in UnstrippedList: #BRIEF - Ensures each word has no extra spaces
                Words.append(word.strip())

            if not len(Words) == 4: #BRIEF - Only 4 words long
                print("Your input must contain exactly 4 words/phrases, separated by commas.")
                ValidFormat = False

            for word in Words: #BRIEF - Verify it is a word within one of the 4 groups
                if not word in approvedInputs:
                    print("Your input must contain words/phrases as presented to you.")
                    ValidFormat = False
                    break #BRIEF - Ensures the print is only outputted once

            Input = Words

        if ValidFormat: #BRIEF - If anything is not how the program wants it, nothing is returned and it loops again
            return Input
