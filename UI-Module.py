"""
# Purpose:
This is meant to host the UI for the program.

# To Do:
- Output the buttons for the main menu -> COMPLETE
- Output the information for 'Help Menu' and 'Show Scores'

"""

def OutputButtons(Stage):

    if Stage == "Main":

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

    print("\nSelect any of the options above by inputting the keybind in the square brackets."
          "\ne.g. for « Wordle [W] », input 'W'\n")
