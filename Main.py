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
import time

from InputValidatorModule import UserInput # Call a function to retrieve a valid user input
from UIModule import MainMenuButtons # Call a function to output the main menu options
from WordleModule import WordleMain

def Main():
    while True:
        MainMenuButtons()
        Choice = UserInput("MainMenu")

        # Those with "pass" will have modules called  once the modules are created
        if Choice == "W":
            print("You've chosen Wordle, lets begin!\n")
            WordleMain()
            time.sleep(1.5)

        elif Choice == "C":
            print("You've chosen Connections, lets begin!\n")
            pass

        elif Choice == "H":
            print("You've chosen to ask for help.\n")
            pass

        elif Choice == "S":
            print("You've chosen to view your scores.\n")
            pass

        elif Choice == "Q":
            print("You've chosen to quit, hope you had fun!\nBye for now...")
            break

Main()