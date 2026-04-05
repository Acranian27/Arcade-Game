"""
# Purpose:
Host the main logic of the program.

# To Do:
- Call UI to display options -> COMPLETE
- Retrieve a user input -> COMPLETE
- Compare the user input to different modules keybind -> COMPLETE
- Call the module that matches the user input -> PARTIALLY COMPLETE
- Run forever unless the user inputs as such -> COMPLETE

"""
import time

from InputValidatorModule import UserInput
from UIModule import MainMenuButtons
from WordleModule import WordleMain
from ConnectionsModule import ConnectionsMain

def Main():
    while True:
        MainMenuButtons() #BRIEF - Shows the available options to the user
        Choice = UserInput("MainMenu", "WCHSQ")

        #SECT –––––– CHOOSE MODULE ––––––
        if Choice == "W":
            print("You've chosen Wordle, lets begin!\n")
            WordleMain()
            time.sleep(1.5)

        elif Choice == "C":
            print("You've chosen Connections, lets begin!\n")
            ConnectionsMain()
            time.sleep(1.5)

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