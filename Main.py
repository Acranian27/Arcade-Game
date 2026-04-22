"""
# Purpose:
Host the main logic of the program.

# To Do:
- Call UI to display options -> COMPLETE
- Retrieve a user input -> COMPLETE
- Compare the user input to different modules keybind -> COMPLETE
- Call the module that matches the user input -> COMPLETE
- Run forever unless the user inputs as such -> COMPLETE

"""
import time

from InputValidatorModule import UserInput
from UIModule import MainMenuButtons
from WordleModule import WordleMain
from ConnectionsModule import ConnectionsMain
from ScoreModule import GetConnectionsHighscore, GetWordleHighscore

#SECT –––––– COLOURS ––––––
YellowRegular = "\033[0;33m"
ResetColour = "\033[0m"

def HelpMenu() -> None:
    print(f"{YellowRegular}Remember, if you need help at any point in this program, type 'H' in an input.\n"
          "This will toggle the help menu and give you meaningful advice.\n")
    time.sleep(3)
    print("Or instead, input 'Q' to quit whatever module you are in, or to exit the program completely.\n")
    time.sleep(2)
    print("Once you enter inside a game, inputting 'H' will provide instructions and tips for that game.\n")
    time.sleep(2)
    print(f"Good luck and have fun!{ResetColour}\n")

def Main() -> None:
    while True:
        MainMenuButtons() #BRIEF - Shows the available options to the user
        Choice: str = UserInput("MainMenu", "WCHSQ")

        #SECT –––––– CHOOSE MODULE ––––––
        if Choice == "W":
            print("\nYou've chosen Wordle, lets get started!\n")
            WordleMain()
            time.sleep(1.5)

        elif Choice == "C":
            print("\nYou've chosen Connections, lets get started!\n")
            ConnectionsMain()
            time.sleep(1.5)

        elif Choice == "H":
            print(f"\nYou've chosen to ask for help.\n")
            HelpMenu()
            time.sleep(1.5)

        elif Choice == "S":
            print("\nYou've chosen to view your scores.\n")
            time.sleep(0.5)

            print("Your Wordle highscore is:", GetWordleHighscore())
            time.sleep(0.5)

            print("Your Connections highscore is:", GetConnectionsHighscore())
            time.sleep(0.5)

        elif Choice == "Q":
            print("You've chosen to quit, hope you had fun!\nBye for now...")
            time.sleep(0.5)
            break

Main()