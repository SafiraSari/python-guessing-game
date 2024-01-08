# ------------------------------------------------
# Safira Sari
# COMP 348 - Principles of Programming Languages
# A2 - Python: The Great Guessing

# This simple file parses the command line and starts the guessing game

import sys
from Guess import Guess


def main():
    if len(sys.argv) != 2:
        print("Incorrect number of arguments")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode in ["play", "test"]:
        
        
        words = Guess(mode)
        words.play()
        
    else:
        print("Invalid mode")
        sys.exit(1)



if __name__ == "__main__":
    main()

    
