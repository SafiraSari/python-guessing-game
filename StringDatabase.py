# ------------------------------------------------
# Safira Sari - 40249017
# COMP 348 - Principles of Programming Languages
# A2 - Python: The Great Guessing Game
# ------------------------------------------------


# This file is responsible for the disk I/O and	random selection of the word.

import random

class StringDatabase:

    # Constructor
    
    def __init__(self, filePath):
        self.filePath = filePath
        self.listWords = self.storeWords()


    # Read file and store words in a list
    
    def storeWords(self):
        
        try:    
            with open(self.filePath, "r") as file:
                listWords = file.read().split()
    
            return listWords
                
        except FileNotFoundError:
            print("File 'four_letters.txt' could not be found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    # Choose a random word from list

    def chooseRandomWord(self):
        word = random.choice(self.listWords)
        
        if word is not None:
            return word


    # Mutator
    
    def setFilePath(self, newFilePath):
        self.filePath = newFilePath


    # Accessor
    
    def getFilePath(self):
        return self.filePath


    def getListWords(self):
        return self.listWords

    



    

