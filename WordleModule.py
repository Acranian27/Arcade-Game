"""
# Purpose:
This is meant to host the Wordle game logic and processing necessary to run the game.

# To Do:
- Select a random word the user needs to guess -> COMPLETE
- Retrieve a user input -> COMPLETE
- Compare the user input to the random word -> COMPLETE
- Run this module until the user guesses correctly or after 6 incorrect attempts -> COMPLETE
- Get a score based on this -> COMPLETE

"""
import random, time
from InputValidatorModule import UserInput
from UIModule import WordleUI
from ScoreModule import ScoreFunc, GetWordleHighscore

#SECT –––––– COLOURS ––––––
YELLOW_REGULAR = "\033[0;33m"
RESET_COLOUR = "\033[0m"

#SECT –––––– GATHER POSSIBLE WORDLES ––––––
with open("WordleData.txt", "r") as file:

    PossibleWordlesRaw: list = file.read().split(",")

    PossibleWordles: list = [] #BRIEF - The random word each round will be picked from this list
    for word in PossibleWordlesRaw:
        PossibleWordles.append(word.strip())


def HelpMenu() -> None:
    print("".join(f"\n{YELLOW_REGULAR}I can see you need some help.\n"))
    time.sleep(2)
    print("Wordle is a fun game where you guess a hidden 5-letter word.\n"
          "You have 6 guess to find the hidden word before you lose.\n"
          "Each round you guess a word and each letter is highlighted a different colour.\n")
    time.sleep(4)
    print("Green highlight means that the letter is correct and in the right position in the word.\n"
          "Yellow highlight means that the letter is correct but in the wrong position in the word.\n"
          "Finally, grey highlight means the letter is not present in the word at all.\n")
    time.sleep(4)
    print(f"Now that you know how to play Wordle, good luck guessing!{RESET_COLOUR}\n")

def SelectRandomWord() -> str: #BRIEF - Chooses a random word

    index: int = random.randint(0, len(PossibleWordles) - 1)

    return PossibleWordles[index]

def DetermineStates(answer: str, guess: str) -> list: #BRIEF - Determines if each letter is green, yellow or grey based on its correctness
    """
    *LetterFrequency is very much essential because it ensures that duplicate
    *   letters are accurately accounted for.

    eg. Lets use the example of the answer: "spike" and the guess: "paper".
    eg. Both letter "p" in paper would receive a yellow state even though "p" only
    eg.    appears in spike once.
    eg. With LetterFrequency, only the first "p" is given a yellow state since the
    eg.    LetterFrequency["p"] will be 0 when the second "p" is tested.
    """

    #SECT –––––– KEY VALUES ––––––
    LetterFrequency: dict = {} #BRIEF - Stores the frequencies of each letter in the answer (eg. "a":1, "p":2, "l":1, "e":1)
    LetterStates: list = [""] * 6

    #SECT –––––– RECORD LETTER APPEARANCES (ANSWER) ––––––
    for letter in answer:
        if letter in LetterFrequency:
            LetterFrequency[letter] += 1
        else:
            LetterFrequency[letter] = 1

    #SECT –––––– DETERMINE LETTER STATES (GUESS) ––––––
    for i in range(5): #BRIEF - Check for greens separately to prevent inconsistent colouring
        if guess[i] == answer[i]:
            LetterStates[i] = ("green") #BRIEF - Same letter and the same position in the answer
            LetterFrequency[guess[i]] -= 1

    for pos, letter in enumerate(guess):
        if letter in answer and LetterFrequency[letter] > 0 and LetterStates[pos] == "": #BRIEF - Ensure green tag is not overriden
            LetterStates[pos] = ("yellow") #BRIEF - Same letter but incorrect position in the answer
            LetterFrequency[letter] -= 1

        elif LetterStates[pos] == "":#BRIEF - Ensure green tag is not overriden
            LetterStates[pos] = ("grey") #BRIEF - Not in the word at all

    return LetterStates

def WordleMain() -> None:
    #SECT –––––– KEY VARIABLES ––––––
    RandomWord: str = SelectRandomWord()

    Attempts = 0
    Correct = False

    StartTime: float = time.time()
    Score = 0

    print("To begin, enter a 5 letter word to guess the random word, or type 'H' for help.")

    #SECT –––––– GAME LOOP ––––––
    while True:
        #SUBSECT –––––– CHECK GUESS ––––––
        time.sleep(1)
        Guess: str = UserInput("Wordle", PossibleWordles)

        if Guess == "Q": #BRIEF - Quit the module
            print("It seems you want to quit the game early, lets head back then.")
            break

        elif Guess == "H": #BRIEF - Give helpful information
            HelpMenu()

        else: #BRIEF - Run the actual game
            States: list = DetermineStates(RandomWord, Guess)

            # SUBSECT –––––– UI IMPORTING ––––––
            Attempts += 1
            WordleUI(Guess, States, Attempts)

            # SUBSECT –––––– END-GAME CONDITIONS ––––––
            if Guess == RandomWord or Attempts == 6: #BRIEF - Guessed the hidden word or ran out of attempts
                TotalTime: float = time.time() - StartTime
                Score = ScoreFunc(TotalTime, Attempts, "Wordle", Guess == RandomWord)
                break

    #SECT –––––– FINAL OUTPUTS ––––––
    time.sleep(1)

    if Guess == RandomWord:
        print("Congratulations! You guessed the word correctly!\n")
    else:
        print(f"Tough luck, the word was {RandomWord}\n")

    time.sleep(1)

    print("Your final score is:", Score)
    print("Your highscore is:", GetWordleHighscore())