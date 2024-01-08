# ------------------------------------------------
# Safira Sari
# COMP 348 - Principles of Programming Languages
# A2 - Python: The Great Guessing Game
# ------------------------------------------------


# This class maintains information about a specific game for report

class Game:
     
     currentGameID = 0

     # Constructor
     
     def __init__(self, word, status, badGuesses, missedLetters, score):
          Game.currentGameID += 1
          self.gameID = Game.currentGameID
          self.word = word
          self.status = status
          self.badGuesses = badGuesses
          self.missedLetters = missedLetters
          self.score = score


     # Accessors

     def getGameID(self):
          return self.gameID

     def getWord(self):
          return self.word

     def getStatus(self):
          return self.status

     def getBadGuesses(self):
          return self.badGuesses

     def getMissedLetters(self):
          return self.missedLetters

     def getScore(self):
          return self.score


     # Mutators
     
     def setWord(self, newWord):
          self.word = newWord

     def setStatus(self, newStatus):
          self.status = newStatus

     def setBadGuesses(self, newBadGuesses):
          self.badGuesses = newBadGuesses

     def setMissedLetters(self, newMissedLetters):
          self.missedLetters = newMissedLetters

     def setScore(self, newScore):
          self.score = newScore


     # FUNCTION DEFINITIONS

     # Generate the header for the game report

     @staticmethod
     def generateHeader():
          print("\n++\n++ Game Report \n++\n")
          print("Game\tWord\tStatus\tBad Guesses\tMissed Letters\tScore")
          print("----\t----\t------\t-----------\t--------------\t-----")


     # Generates a row that summarizes the player's game

     def generateRow(self):
          print(str(self.gameID) + "\t" + self.word + "\t" + self.status + "\t"
                + str(self.badGuesses) + "\t\t" + str(self.missedLetters) + "\t\t" + str(self.score))

     

     
          
