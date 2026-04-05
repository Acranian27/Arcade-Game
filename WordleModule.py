"""
# Purpose:
This is meant to host the Wordle game logic and processing necessary to run the game.

# To Do:
- Select a random word the user needs to guess -> COMPLETE
- Retrieve a user input -> COMPLETE
- Compare the user input to the random word -> COMPLETE
- Run this module until the user guesses correctly or after 6 incorrect attempts -> COMPLETE
- Get a score based on this

"""
import random, time
from InputValidatorModule import UserInput
from UIModule import WordleUI
from ScoreModule import ScoreFunc

#SECT –––––– COLOURS ––––––
YellowRegular = "\033[0;33m"
ResetColour = "\033[0m"

#SECT –––––– GATHER POSSIBLE WORDLES ––––––
with open("WordleData.txt", "r") as file:

    UncleanList = file.read().split("|")

    PossibleWordles = [] #BRIEF - The random word each round will be picked from this list
    for word in UncleanList:
        PossibleWordles.append(word.strip())

#SECT –––––– GATHER VALID INPUTS ––––––
with open("WordleVerificationData.txt", "r") as file:

    VerificationListRaw = file.read().split(",")

    ValidationList = [] #BRIEF - The user's input will be compared to the words stored in this list
    for word in VerificationListRaw:
        ValidationList.append(word.strip())

def SelectRandomWord(): #BRIEF - Chooses a random word

    index = random.randint(0, len(PossibleWordles) - 1)

    return PossibleWordles[index]

def DetermineStates(answer, guess): #BRIEF - Determines if each letter is green, yellow or grey based on its correctness
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
    LetterFrequency = {} #BRIEF - Stores the frequencies of each letter in the answer (eg. "a":1, "p":2, "l":1, "e":1)
    LetterStates = [""] * 6

    #SECT –––––– RECORD LETTER APPEARANCES (ANSWER) ––––––
    for letter in answer:
        if letter in LetterFrequency:
            LetterFrequency[letter] += 1
        else:
            LetterFrequency[letter] = 1
    print("LetterFrequency:",LetterFrequency) #DEBUG

    #SECT –––––– DETERMINE LETTER STATES (GUESS) ––––––
    for i in range(5): #BRIEF - Check for greens separately otherwise errors arise
        if guess[i] == answer[i]:
            LetterStates[i] = ("green") #BRIEF - Same letter and the same position in the answer
            LetterFrequency[guess[i]] -= 1

    for pos, letter in enumerate(guess): #BRIEF - Check for yellows and greys
        if letter in answer and LetterFrequency[letter] > 0 and LetterStates[pos] == "": #BRIEF - Make sure that it doesn't erase the "green" state
            LetterStates[pos] = ("yellow") #BRIEF - Same letter but incorrect position in the answer
            LetterFrequency[letter] -= 1

        elif LetterStates[pos] == "":#BRIEF - Make sure that it doesn't erase the "green" state
            LetterStates[pos] = ("grey") #BRIEF - Not in the word at all

    return LetterStates

def WordleMain():
    #SECT –––––– KEY VARIABLES ––––––
    RandomWord = SelectRandomWord()

    Attempts = 0
    Correct = False

    StartTime = time.time()
    Score = 0
    Highscore = 0

    print("To begin, enter a 5 letter word to guess the random word, or type 'H' for help.")

    #SECT –––––– GAME LOOP ––––––
    while True:
        #SUBSECT –––––– CHECK GUESS ––––––
        time.sleep(1)
        Guess = UserInput("Wordle", ValidationList)

        if Guess == "Q": #BRIEF - Q == Quit
            print("It seems you want to quit the game early, lets head back then.")
            break

        elif Guess != "H": #BRIEF - If they aren't asking for help, play the game
            States = DetermineStates(RandomWord, Guess)

            #SUBSECT –––––– UI IMPORTING ––––––
            Attempts += 1
            WordleUI(Guess, States, Attempts)

            #SUBSECT –––––– END-GAME CONDITIONS ––––––
            if Guess == RandomWord or Attempts == 6:
                TotalTime = time.time() - StartTime
                Score, Highscore = ScoreFunc(TotalTime, Attempts, "Wordle")
                break

        else: #BRIEF - Provide assistance if they dunno how to play
            print("".join(f"\n{YellowRegular}I can see you need some help.\n"))
            time.sleep(2)
            print("Wordle is a fun game where you guess a hidden 5-letter word.\n"
                  "You have 6 guess to find the hidden word before you lose.\n"
                  "Each round you guess a word and each letter is highlighted a different colour.\n")
            time.sleep(4)
            print("Green highlight means that the letter is correct and in the right position in the word.\n"
                  "Yellow highlight means that the letter is correct but in the wrong position in the word.\n"
                  "Finally, grey highlight means the letter is not present in the word at all.\n")
            time.sleep(4)
            print(f"Now that you know how to play Wordle, good luck guessing!{ResetColour}\n")

    #SECT –––––– FINAL OUTPUTS ––––––
    if Guess == RandomWord:
        print("Congratulations! You guessed the word correctly!\n")
    else:
        print(f"Tough luck, the word was {RandomWord}\n")

    print("Your highscore is:", Highscore)
    print("Your final score is:", Score)