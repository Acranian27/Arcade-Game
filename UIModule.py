"""
# Purpose:
This is meant to host the UI for the program.

# To Do:
- Output the buttons for the main menu -> COMPLETE
- Output the UI for Wordle -> COMPLETE
- Output the UI for Connections
- Output the information for 'Help Menu' and 'Show Scores'

"""
import time

# Colours:
ResetColour = "\033[0m"
GreenBackground = "\033[42m\033[1;38m"
YellowBackground = "\033[43m\033[1;38m"
GreyBackground = "\033[47m\033[1;38m"

def MainMenuButtons():

    print(
        "- - - - - - - - - - - - -"
        "\n« Wordle [W] »\n"
        "- - - - - - - - - - - - -"
        "\n« Connections [C] »\n"
        "- - - - - - - - - - - - -"
        "\n« Help Menu [H] »\n"
        "- - - - - - - - - - - - -"
        "\n« Show Scores [S] »\n"
        "- - - - - - - - - - - - -"
        "\n« Quit Program [Q] »\n"
        "- - - - - - - - - - - - -"
    )
    time.sleep(1)

    print("\nSelect any of the options above by inputting the keybind in the square brackets."
          "\ne.g. for « Wordle [W] », input 'W'\n")

# Outputs the colouring of the letter based on it's correctness

PreviousGuesses = [" -  -  -  -  - \n"] * 6

def WordleUI(Guess, States, Attempt):

    CurrentWord = []

    # Gives each letter a unique colour based on their state
    for i, letter in enumerate(Guess):
        if States[i] == "green":
            CurrentWord.append(f"{GreenBackground} {letter} {ResetColour}")

        elif States[i] == "yellow":
            CurrentWord.append(f"{YellowBackground} {letter} {ResetColour}")

        else:
            CurrentWord.append(f"{GreyBackground} {letter} {ResetColour}")

    PreviousGuesses[Attempt - 1] = f'{"".join(CurrentWord)}\n'
    print("".join(PreviousGuesses))
    time.sleep(0.5)
