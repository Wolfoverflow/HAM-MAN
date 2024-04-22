from random import choice
import os
import sys

pythonPath = os.path.dirname(sys.executable)

try:
    from PIL import Image, ImageTk # Installs Pillow if not installed
except ImportError:
    os.system(f"{pythonPath} -m pip install pillow")
    print("Installed Pillow, please restart the program")
    sys.exit()

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # auto changes the directory so that it can access the text file

os.chdir("..")  # go up one directory
os.chdir("assets")  # go into the assets folder

stage = 0  # the stage of the game

with open("words.txt", 'r') as f:
    words = f.read().split()  # wordlist

word = choice(words)  # get a random word (not cryptographically secure)

print(word) # was for debugging, now for when you get tired of guessing


def checkGuess(guess):
    if guess not in word:
        # if the letter isnt in the word, return false
        return False
    elif guess in word:
        # returns all instances of the letter in the word
        indexes = [i for i, letter in enumerate(word) if letter == guess]
        return indexes



def getStage():
    return stage


def isAlive():
    print(stage)
    if stage < 10:
        return True
    else:
        return False


def reduceHealth():
    global stage
    stage += 1


# def endSound(ending):
#     if ending == True:
#         sound = AudioSegment.from_wav("win.mp3")
#         play(sound)
#     else:
#         sound = AudioSegment.from_wav("lose.mp3")
#         play(sound)
