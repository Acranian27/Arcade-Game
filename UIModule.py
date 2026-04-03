"""
# Purpose:
This is meant to host the UI for the program.

# To Do:
- Output the buttons for the main menu -> COMPLETE
- Output the UI for Wordle -> COMPLETE
- Output the UI for Connections
- Output the information for 'Help Menu' and 'Show Scores'

"""
import time, random

#SECT –––––– KEY COLOURS ––––––
ResetColour = "\033[0m"
GreenBackground = "\033[42m\033[1;38m"
YellowBackground = "\033[43m\033[1;38m"
BlueBackground = "\033[44m\033[1;38m"
PurpleBackground = "\033[45m\033[1;38m"
GreyBackground = "\033[47m\033[1;38m"
BoldWhite = "\033[1;38m"

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

PreviousGuesses = [" -  -  -  -  - \n"] * 6

# Outputs the colouring of the letter based on it's correctness
def WordleUI(guess, states, attempt):
    global PreviousGuesses
    if attempt == 1:
        PreviousGuesses = [" -  -  -  -  - \n"] * 6

    CurrentWord = []

    # Gives each letter a unique colour based on their state
    for i, letter in enumerate(guess):
        if states[i] == "green":
            CurrentWord.append(f"{GreenBackground} {letter} {ResetColour}")

        elif states[i] == "yellow":
            CurrentWord.append(f"{YellowBackground} {letter} {ResetColour}")

        else:
            CurrentWord.append(f"{GreyBackground} {letter} {ResetColour}")

    PreviousGuesses[attempt - 1] = f'{"".join(CurrentWord)}\n'
    print("".join(PreviousGuesses))
    time.sleep(0.5)

def ConnectionsUI(gameStats, use):
    #SECT –––––– KEY VALUES ––––––
    RemainingWords = []
    GuessedGroups = []

    #SECT –––––– CALCULATE GUESSED GROUPS ––––––
    for group in gameStats['Groups']:
        if not group['Guessed']:
            for word in group['WordsWithin']:
                RemainingWords.append(word)
        else:
            GuessedGroups.append(group)

    #SECT –––––– KEY PRINTS ––––––
    for group in GuessedGroups: #BRIEF - GuessedGroups will display the name of the group and its words underneath
        #SUBSECT –––––– DETERMINE BACKGROUND COLOUR ––––––
        match group["Difficulty"]: #BRIEF - Checks if group["Difficulty"] matches with any case below
            case "P":
                Background = PurpleBackground
            case "B":
                Background = BlueBackground
            case "G":
                Background = GreenBackground
            case "Y":
                Background = YellowBackground
            case _:
                Background = ""

        #SUBSECT –––––– PRINT GUESSED GROUPS ––––––
        print(f"{Background}{BoldWhite}{''.join((group['Name'],  ' ' * (39 - len(group['Name']))))}{ResetColour}")
        print(f"{''.join((group['WordsWithin'][0], ' ' * (19 - len(group['WordsWithin'][0]))))} {''.join((group['WordsWithin'][1], ' ' * (19 - len(group['WordsWithin'][1]))))}\n"
              f"{''.join((group['WordsWithin'][2], ' ' * (19 - len(group['WordsWithin'][2]))))} {''.join((group['WordsWithin'][3], ' ' * (19 - len(group['WordsWithin'][3]))))}\n")
        time.sleep(1)

    #SUBSECT –––––– PRINT UNGUESSED WORDS ––––––
    for i in range(0, len(RemainingWords), 4):
        print(''.join((RemainingWords[i], ' ' * (19 - len(RemainingWords[i])))), ''.join((RemainingWords[i+1], ' ' * (19 - len(RemainingWords[i+1])))), ''.join((RemainingWords[i+2], ' ' * (19 - len(RemainingWords[i+2])))), ''.join((RemainingWords[i+3], ' ' * (19 - len(RemainingWords[i+3])))))
        #BRIEF - It will be the word followed by the amount of characters left from 19-len(word) as spaces (keeps each column in-line and consistent)

    #SUBSECT –––––– PRINT EXTRA ROUND INFO ––––––
    if use != "END": #BRIEF - On the after the last guess, this doesn't need to be shown, just the connections board
        print(f"\nThis is attempt {gameStats['Attempt']}, and you have {gameStats['LivesRemaining']} lives remaining.")