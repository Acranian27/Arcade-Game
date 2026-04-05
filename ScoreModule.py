"""
# Purpose:
Take game data and convert it into a score for the user.

# To Do:
- Retrieve user data
- Apply a formula to generate a score
- Store highscores

"""
import math

#SECT –––––– DEFINE KEY VARIABLES ––––––
WordleHighscore = 0
ConnectionsHighscore = 0

def GetHighscores(): #BRIEF - Used in the main menu
    global WordleHighscore
    global ConnectionsHighscore

    return WordleHighscore, ConnectionsHighscore

def AdjustHighscore(score, game): #BRIEF - Verify the highscore is the highest score
    #SECT –––––– RETRIEVE CURRENT HIGHSCORES ––––––
    global WordleHighscore
    global ConnectionsHighscore

    #SECT –––––– UPDATE APPROPRIATE SCORES ––––––
    if game == "Wordle" and WordleHighscore < score: #BRIEF - Ensures that only the targetted game's highscore is updated
        WordleHighscore = score
    elif game == "Connections" and ConnectionsHighscore < score: #BRIEF - ^^
        ConnectionsHighscore = score

def CalculateScore(time, attempts, game): #BRIEF - Generate a fitting score
    if game == "Wordle" and attempts != 6:
        Score = round((10000 / math.sqrt(time * attempts)), 0)

    elif game == "Connections" and attempts != 4:
        Score = round((100000 / math.sqrt(time * attempts)), 0)

    else: #BRIEF - If the user didn't failed the game they get 0
        Score = 0

    return Score

def ScoreFunc(time, attempts, game):
    #SECT –––––– CALCULATE NEW SCORES ––––––
    Score = CalculateScore(time, attempts, game)

    AdjustHighscore(Score, game)

    #SECT –––––– RETURN NEW SCORES ––––––
    if game == "Wordle":
        return Score, WordleHighscore

    elif game == "Connections":
        return Score, ConnectionsHighscore
