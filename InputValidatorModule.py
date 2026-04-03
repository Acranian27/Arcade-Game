"""
# Purpose:
This is meant to get a validate a user input so that it doesn't crash other modules.

# To Do:
- Retrieve the destination of the input -> COMPLETE
- Retrieve a user input -> COMPLETE
- Compare the user input to a set of requirements -> COMPLETE FOR: MainMenu, Wordle
- Return the input to the required module -> COMPLETE

"""

def UserInput(destination, approvedInputs):

    # Run until the user inputs something in a valid format
    while True:

        ValidFormat = True
        Input = input("Input: ").upper() # All comparisons done in uppercase
        #print("UserInput:", Input)  # DEBUG

        if destination == "MainMenu":
            if not len(Input) == 1:
                print("Your input be exactly one character long.")
                ValidFormat = False

            elif not Input in approvedInputs:
                print("Your input must be one of the letters next to the buttons.")
                ValidFormat = False

        elif destination == "Wordle":
            if not len(Input) == 5:
                print("Your input must be exactly five characters long.")
                ValidFormat = False

            elif not Input in approvedInputs:
                print("Your input must be an actual word.\nThis means no numbers or symbols.")
                ValidFormat = False

        elif destination == "Connections":
            UnstrippedList = Input.split(",")
            #print("UnstrippedList (Input):", UnstrippedList) #DEBUG
            Words = []

            for word in UnstrippedList:
                Words.append(word.strip())

            if not len(Words) == 4:
                print("Your input must contain exactly 4 words/phrases, separated by commas.")
                ValidFormat = False

            for word in Words:
                if not word in approvedInputs:
                    print("Your input must contain words/phrases as presented to you.")
                    ValidFormat = False
                    break # Ensures the print is only outputted once

            Input = Words
            #print(Input)
        if ValidFormat:
            return Input
