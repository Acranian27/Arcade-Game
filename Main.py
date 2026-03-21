"""
# Purpose:
Host the main logic of the program.

# To Do:
- Call UI to display options
- Retrieve a user input
- Compare the user input to different modules keybind
- Call the module that matches the user input
- Run forever unless the user inputs as such

"""

from InputValidatorModule import UserInput # Call a function to retrieve a valid user input
from UIModule import MainMenuButtons # Call a function to output the main menu options

def Main():
    while True:
        MainMenuButtons()
        Choice = UserInput("MainMenu")

        # Those with "pass" will have modules called  once the modules are created
        if Choice == "W":
            print("You've chosen Wordle, lets begin!")
            pass

        elif Choice == "C":
            print("You've chosen Connections, lets begin!")
            pass

        elif Choice == "H":
            print("You've chosen to ask for help.")
            pass

        elif Choice == "S":
            print("You've chosen to view your scores.")
            pass

        elif Choice == "Q":
            print("You've chosen to quit, hope you had fun!\nBye for now...")
            break

Main()