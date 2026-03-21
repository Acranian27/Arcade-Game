"""
# Purpose:
This is meant to get a validate a user input so that it doesn't crash other modules.

# To Do:
- Retrieve the destination of the input -> COMPLETE
- Retrieve a user input -> COMPLETE
- Compare the user input to a set of requirements -> COMPLETE FOR: MainMenu, Wordle
- Return the input to the required module -> COMPLETE

"""

def UserInput(Destination):

    # Run until the user inputs something in a valid format
    while True:

        ValidFormat = True
        Input = input("Input: ").upper() # All comparisons done in uppercase

        if Destination == "MainMenu":
            if not len(Input) == 1:
                print("Your input be exactly one character long.")
                ValidFormat = False

            else:
                if not Input in "WCHSQ":
                    print("Your input must be one of the letters next to the buttons.")
                    ValidFormat = False

        if Destination == "Wordle":
            for letter in Input:
                if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    print("Your input must contain only letters.")
                    ValidFormat = False
                    break # Ensures the print is only outputted once

            if not len(Input) == 5:
                print("Your input must be exactly five characters long.")
                ValidFormat = False

        if ValidFormat:
            return Input
