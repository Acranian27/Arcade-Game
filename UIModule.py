"""
# Purpose:
This is meant to host the UI for the program.

# To Do:
- Output the buttons for the main menu -> COMPLETE
- Output the UI for Wordle -> COMPLETE
- Output the UI for Connections -> COMPLETE

"""
import time, random

#SECT –––––– KEY COLOURS ––––––
RESET_COLOUR = "\033[0m"
GREEN_BACKGROUND = "\033[42m\033[1;38m"
YELLOW_BACKGROUND = "\033[43m\033[1;38m"
BLUE_BACKGROUND = "\033[44m\033[1;38m"
PURPLE_BACKGROUND = "\033[45m\033[1;38m"
GREY_BACKGROUND = "\033[47m\033[1;38m"
BOLD_RED = "\033[1;31m"
BOLD_WHITE = "\033[1;38m"

def MainMenuButtons():
    #SECT –––––– PRINT BUTTONS ––––––
    print(
        "\n"
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
          "\ne.g. for « Wordle [W] », input 'W'")

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
            CurrentWord.append(f"{GREEN_BACKGROUND} {letter} {RESET_COLOUR}")

        elif states[i] == "yellow":
            CurrentWord.append(f"{YELLOW_BACKGROUND} {letter} {RESET_COLOUR}")

        else:
            CurrentWord.append(f"{GREY_BACKGROUND} {letter} {RESET_COLOUR}")

    #SECT –––––– PRINT GUESSES ––––––
    PreviousGuesses[attempt - 1] = f'{"".join(CurrentWord)}\n' #BRIEF - Saves the coloured word to be visible every following round
    print("\n" + "".join(PreviousGuesses))
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
    eg. MEMBER OF A CLASSIC BACKING BAND    -> Pretend this is highlighted the difficulty colour
    eg. BANSHEE             HEARTBREAKER       
    eg. PIP                 WAILER   
    
    *For the remaining groups: (Pretend not in order)
    eg. HEART               KIDNEY              LIVER               LUNG               
    eg. AERIAL              ARABESQUE           ROUNDOFF            SPLIT              
    eg. CLOVER              HORSESHOE           MOON                RAINBOW  
    
    *It makes everything neat and organised, also making it somewhat recognisable to the original.
    *The ":<20" basically just ensures that if the word/phrase is less than 20 characters,
    *it'll fill the rest of the line with empty spaces to keep everything consistent
    """
    print("")
    for group in GuessedGroups: #BRIEF - GuessedGroups will display the name of the group and its words underneath
        #SUBSECT –––––– DETERMINE BACKGROUND COLOUR ––––––
        match group["Difficulty"]: #BRIEF - More efficient if statement for == operations
            case "P":
                Background = PURPLE_BACKGROUND
            case "B":
                Background = BLUE_BACKGROUND
            case "G":
                Background = GREEN_BACKGROUND
            case "Y":
                Background = YELLOW_BACKGROUND
            case _: #BRIEF - Should be impossible but just in case someone meddles with text file data
                Background = ""
                print(f"{BOLD_RED}WARNING: group['Difficulty'] contained an invalid value.{RESET_COLOUR}")

        #SUBSECT –––––– PRINT GUESSED GROUPS ––––––
        print(f"{Background}{BOLD_WHITE}{group['Name']:<40}{RESET_COLOUR}")
        print(f"{group['WordsWithin'][0]:<20}{group['WordsWithin'][1]:<20}")
        print(f"{group['WordsWithin'][2]:<20}{group['WordsWithin'][3]:<20}\n")
        time.sleep(1)

    #SUBSECT –––––– PRINT UNGUESSED WORDS ––––––
    random.shuffle(RemainingWords)
    for i in range(0, len(RemainingWords), 4):
        print(f"{RemainingWords[i]:<20}{RemainingWords[i+1]:<20}{RemainingWords[i+2]:<20}{RemainingWords[i+3]:<20}")
        #BRIEF - It will be the word followed by the amount of characters left from 20-len(word) as spaces (keeps each column in-line and consistent)

    #SUBSECT –––––– PRINT EXTRA ROUND INFO ––––––
    if use != "END": #BRIEF - On the after the last guess, this doesn't need to be shown, just the connections board
        print(f"\nThis is attempt {gameStats['Attempt']}, and you have {gameStats['LivesRemaining']} lives remaining.")