"""
# Purpose:
This is meant to host the UI for the program.

# To Do:
- Output the buttons for the main menu -> COMPLETE
- Output the UI for Wordle -> COMPLETE
- Output the UI for Connections -> COMPLETE
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
    #SECT –––––– PRINT BUTTONS ––––––
    time.sleep(1)
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

    #SECT –––––– PRINT INSTRUCTIONS ––––––
    print("\nSelect any of the options above by inputting the keybind in the square brackets."
          "\ne.g. for « Wordle [W] », input 'W'\n")

PreviousGuesses = [" -  -  -  -  - \n"] * 6

def WordleUI(guess, states, attempt):
    #SECT –––––– CREATE SAVE FOR GUESSES ––––––
    global PreviousGuesses
    if attempt == 1: #BRIEF - Ensures that the previous guesses are reset every round
        PreviousGuesses = [" -  -  -  -  - \n"] * 6

    CurrentWord = [] #BRIEF - Stores each coloured letter

    #SECT –––––– ALLOCATE APPROPRIATE LETTER COLOUR ––––––
    for i, letter in enumerate(guess):
        if states[i] == "green":
            CurrentWord.append(f"{GreenBackground} {letter} {ResetColour}")

        elif states[i] == "yellow":
            CurrentWord.append(f"{YellowBackground} {letter} {ResetColour}")

        else:
            CurrentWord.append(f"{GreyBackground} {letter} {ResetColour}")

    #SECT –––––– PRINT GUESSES ––––––
    PreviousGuesses[attempt - 1] = f'{"".join(CurrentWord)}\n' #BRIEF - Saves the coloured word to be visible every following round
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
    """
    *This section is definitely the most unreadable bit but below is a demonstration of how it'll look.
    *For GuessedGroups:
    eg. MEMBER OF A CLASSIC BACKING BAND    -> Pretend this is highlighted the difficulty colour (101-111)
    eg. BANSHEE             HEARTBREAKER       
    eg. PIP                 WAILER   
    
    *For the remaining groups: (Pretend not in order)
    eg. HEART               KIDNEY              LIVER               LUNG               
    eg. AERIAL              ARABESQUE           ROUNDOFF            SPLIT              
    eg. CLOVER              HORSESHOE           MOON                RAINBOW  
    
    *Because python is weird, especially when it comes to ANSI colours, "".join() needs to be used.
    *The "RemainingWords[i], ' ' * (19 - len(RemainingWords[i]))" basically just makes sure that it will always be 19 characters long.
    *It takes the word, and adds (19 - number of letters of the word) spaces to the end.
    *It makes everything neat and organised, also making it somewhat recognisable to the original.
    """
    print("")
    for group in GuessedGroups: #BRIEF - GuessedGroups will display the name of the group and its words underneath
        #SUBSECT –––––– DETERMINE BACKGROUND COLOUR ––––––
        match group["Difficulty"]: #BRIEF - More efficient if statement for == operations
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
    random.shuffle(RemainingWords)
    print("")
    for i in range(0, len(RemainingWords), 4):
        print(''.join((RemainingWords[i], ' ' * (19 - len(RemainingWords[i])))), ''.join((RemainingWords[i+1], ' ' * (19 - len(RemainingWords[i+1])))), ''.join((RemainingWords[i+2], ' ' * (19 - len(RemainingWords[i+2])))), ''.join((RemainingWords[i+3], ' ' * (19 - len(RemainingWords[i+3])))))
        #BRIEF - It will be the word followed by the amount of characters left from 19-len(word) as spaces (keeps each column in-line and consistent)

    #SUBSECT –––––– PRINT EXTRA ROUND INFO ––––––
    if use != "END": #BRIEF - On the after the last guess, this doesn't need to be shown, just the connections board
        print(f"\nThis is attempt {gameStats['Attempt']}, and you have {gameStats['LivesRemaining']} lives remaining.")