"""
# Purpose:
Take game data and convert it into a score for the user.

# To Do:
- Retrieve user data -> COMPLETE
- Apply a formula to generate a score -> COMPLETE
- Store highscores -> COMPLETE

"""
import math

#SECT –––––– DEFINE KEY VARIABLES ––––––
WordleHighscore = 0
ConnectionsHighscore = 0

#SECT –––––– HIGHSCORE RETRIEVAL FOR OTHER MODULES ––––––
def GetWordleHighscore() -> int:
    global WordleHighscore

    return WordleHighscore

def GetConnectionsHighscore() -> int:
    global ConnectionsHighscore

    return ConnectionsHighscore

def AdjustHighscore(score: int, game: str) -> None:
    #SECT –––––– RETRIEVE CURRENT HIGHSCORES ––––––
    global WordleHighscore
    global ConnectionsHighscore

    #SECT –––––– UPDATE APPROPRIATE SCORES ––––––
    if game == "Wordle" and WordleHighscore < score:
        WordleHighscore = score
    elif game == "Connections" and ConnectionsHighscore < score:
        ConnectionsHighscore = score

def CalculateScore(time: float, attempts: int, game: str, win: bool) -> int: #BRIEF - Generate a fitting score
    if game == "Wordle" and win:
        Score = round((10000 / math.sqrt(time * attempts)), 0)

    elif game == "Connections" and win:
        Score = round((25000 / math.sqrt(time * attempts)), 0)

    else: #BRIEF - If the user failed the game they get 0
        Score = 0

    return int(Score)

def ScoreFunc(time: float, attempts: int, game: str, win: bool) -> int:
    #SECT –––––– CALCULATE NEW SCORE ––––––
    Score = CalculateScore(time, attempts, game, win)

    AdjustHighscore(Score, game)

    #SECT –––––– RETURN NEW SCORE ––––––
    return Score
