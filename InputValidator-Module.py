"""
# Purpose:
This is meant to get a validate a user input so that it doesn't crash other modules.

# To Do:
- Retrieve the destination of the input -> COMPLETE
- Retrieve a user input -> COMPLETE
- Compare the user input to a set of requirements -> Partly Complete
- Return the input to the required module -> COMPLETE

"""

def UserInput(Destination):

    while True:

        ValidFormat = True
        Input = input("Input: ")

        if Destination == "Wordle":
            for letter in Input:
                if letter not in "abcdefghijklmnopqrstuvwxyz":
                    print("Your input must contain only letters.")
                    ValidFormat = False

            if not len(Input) == 5:
                print("Your input must be exactly 5 characters long.")
                ValidFormat = False

        if ValidFormat:
            return Input
