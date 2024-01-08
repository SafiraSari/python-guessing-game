# ------------------------------------------------
# Safira Sari - 40249017
# COMP 348 - Principles of Programming Languages
# A2 - Python: The Great Guessing Game
# ------------------------------------------------


# This class represents the core application logic itself

import os
from StringDatabase import StringDatabase
from Game import Game


class Guess:

    def __init__(self, mode):
        self.currentWord = self.generateWord()
        self.currentWordList = list(self.currentWord.strip(" "))
        self.currentGuess = ["-","-","-","-"]
        self.status = "Gave up"
        self.numMissedLetter = 0# Number of missing letters in word
        self.listGame = []          
        self.listScore = []
        self.numWrongGuess = 0# Number of incorrect guesses/attempts
        self.numWrongLetter = 0# Number of letters guessed incorrectly
        self.lettersGuessed = []
        self.mode = mode

        self.letterFrequency = {
            "a": 8.17,
            "b": 1.49,
            "c": 2.78,
            "d": 4.25,
            "e": 12.70,
            "f": 2.23,
            "g": 2.02,
            "h": 6.09,
            "i": 6.97,
            "j": 0.15,
            "k": 0.77,
            "l": 4.03,
            "m": 2.41,
            "n": 6.75,
            "o": 7.51,
            "p": 1.93,
            "q": 0.10,
            "r": 5.99,
            "s": 6.33,
            "t": 9.06,
            "u": 2.76,
            "v": 0.98,
            "w": 2.36,
            "x": 0.15,
            "y": 1.97,
            "z": 0.07,
        }


    # FUNCTION DEFINITIONS


    # Generates a random word from the StringDatabase class

    def generateWord(self):
        sb = StringDatabase("four_letters.txt")
        word = sb.chooseRandomWord()
        return word


    # Display info of the game

    def gameDisplay(self):
        print("\n++ \n++ The great guessing game \n++ \n")

        if self.mode == "test":
            print("Current Word: " + self.currentWord)
        
        print("Current Guess: " + self.displayList(self.currentGuess))
        print("Letters guessed: " + self.displayListSpace(self.lettersGuessed))

        print("\ng = guess, t = tell me, l for a letter, and q to quit")


    # Prompt user to enter a key to continue

    def keyContinue(self):
        userKey = input("\nPress any key to continue... ")
        os.system('cls' if os.name == 'nt' else 'clear')


    # Tells user the correct word

    def tellMe(self):
        print("\n@@\n@@ FEEDBACK: You should've guessed this... '" + self.currentWord +"'\n@@")

        
    # Compares the user's guess with the correct word

    def guessWord(self, userGuess):
        if (userGuess == self.currentWord):
            self.status = "Success"
            self.finishGame()
            print("\n@@\n@@ FEEDBACK: You're correct !!\n@@")
        else:
            self.numWrongGuess += 1
            print("\n@@\n@@ FEEDBACK: Try again.... :/ \n@@")
        

    # Add a letter to the list of letters guessed

    def addLetterGuessed(self, letter):
        self.lettersGuessed.append(letter)


    # Check if the user guessed a letter correctly

    def guessLetter(self, letter):
        numOfLetter = self.currentWordList.count(letter)

        if (numOfLetter == 0):
            self.numWrongLetter += 1
            print("\n@@\n@@ FEEDBACK: Not a match\n@@")
        else:
            for x in range(4):
                if (letter == self.currentWordList[x]):
                    self.currentGuess[x] = letter
            
            print("\n@@\n@@ FEEDBACK: Nice! You found " + str(numOfLetter) + " letters\n@@")


    # Return a concatenated string of the list
        
    def displayList(self, listToPrint):
        output = ""
        for x in range(len(listToPrint)):
            output += (listToPrint[x])
        return output


    # Return a string of the list separated by a space character

    def displayListSpace(self, listToPrint):
        output = ""
        for x in range(len(listToPrint)):
            output += (listToPrint[x] + " ")
        return output


    # Determine the player's score for a single game

    def generateScore(self):
        score = 0

            
        for x in range(len(self.currentGuess)):
            if self.currentGuess[x] == "-":
                missedLetter = self.currentWordList[x]
                self.numMissedLetter += 1
                self.letterFrequency[missedLetter]
                score += self.letterFrequency.get(missedLetter,0)


        if self.status == "Success":    
            if self.numWrongLetter != 0:
                score = score / self.numWrongLetter        # reduce score depending on # wrong letters guessed

            score = score * (( 10 - self.numWrongGuess)/10) # reduce score depending on # wrong guesses
        

        if self.status == "Gave up":    # Negative score if user gave up
            score = score * -1


        score = round(score,2)          # Round score to 2 decimals
        self.listScore.append(score)    # Store score in a list 

        return score


    # End game - create a game object and store in a list

    def finishGame(self):
        s = self.generateScore()
        
        g = Game(self.currentWord,self.status, self.numWrongGuess, self.numWrongLetter, s)
        self.listGame.append(g)


    # Generates a report for all games once finished playing

    def generateReport(self):
        Game.generateHeader()

        for x in range(len(self.listGame)):
            self.listGame[x].generateRow()
        

    # Determine the player's final score for all games

    def generateFinalScore(self):
        finalScore = 0
        
        for x in range(len(self.listScore)):
            finalScore += (self.listScore[x])

        finalScore = round(finalScore, 2)
        
        return finalScore


    # Reset the game with a new word

    def resetGame(self):
        self.currentWord = self.generateWord()
        self.currentWordList = list(self.currentWord.strip(" "))
        self.currentGuess = ["-","-","-","-"]
        self.status = "Gave up"
        self.numMissedLetter = 0
        self.numWrongGuess = 0
        self.numWrongLetter = 0
        self.lettersGuessed = []
    

    # Quit the program

    def quitProgram(self):
        quit()



    # -----------------------
    #       GAME START
    # -----------------------


    # Main execution of the program - starts to play the game

    def play(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        
        while True:
            
            self.gameDisplay()
            userOption = input("\nEnter Option: ")     


            # Match-Case statement for the user's choice
            
            match userOption:
                
                case "g":   # User would like to make a guess

                    userGuess = input("\nMake your guess: ")
                    userGuess = userGuess.lower()
                    self.guessWord(userGuess)

                    if self.status == "Success":    # Correct guess
                        self.resetGame()
                    
                    self.keyContinue()

                
                case "t":   # User would like to give up
                    
                    self.tellMe()
                    self.finishGame()
                    self.resetGame()
                    
                    self.keyContinue()

                

                case "l":   # User would like to guess a letter
                    
                    userLetter = input("\nEnter a letter: ")

                    if userLetter in self.lettersGuessed:
                        print("You have already guessed that letter")

                    else:
                        self.addLetterGuessed(userLetter)
                        self.guessLetter(userLetter)

                    self.keyContinue()
                    

                case "q":   # User would like to quit the program

                    self.generateReport()
                    
                    print("\nFinal Score: " + str(self.generateFinalScore()))
                    print("\nThank you for playing! Now quitting...")
                    break
                    
                
                case _:     # User entered an invalid option
                    
                    userOption = input("\nInvalid option. Please re-enter. ")
                    os.system('cls' if os.name == 'nt' else 'clear')


