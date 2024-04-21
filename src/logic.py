from random import choice
import os
import sys

pythonPath = os.path.dirname(sys.executable)

try:
    from PIL import Image, ImageTk
except ImportError:
    os.system(f"{pythonPath} -m pip install pillow")
    import PIL
try:
    from playsound import playsound
except ImportError:
    os.system(f"{pythonPath} -m pip install playsound")
    from playsound import playsound

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # auto changes the directory so that it can access the text file

os.chdir("..")  # go up one directory
os.chdir("assets")  # go into the assets folder

stage = 0  # the stage of the game

with open("words.txt", 'r') as f:
    words = f.read().split()  # wordlist

word = choice(words)  # get a random word (not cryptographically secure)
print(word)


def checkGuess(guess):
    if guess not in word:
        # if the letter isnt in the word, return false
        reduceHealth()
        return False
    elif guess in word:
        # returns all instances of the letter in the word
        indexes = [i for i, letter in enumerate(word) if letter == guess]
        return indexes


def displayStage():
    stages = [
        ImageTk.PhotoImage(Image.open("p0.png")),
        ImageTk.PhotoImage(Image.open("p1.png")),
        ImageTk.PhotoImage(Image.open("p2.png")),
        ImageTk.PhotoImage(Image.open("p3.png")),
        ImageTk.PhotoImage(Image.open("p4.png")),
        ImageTk.PhotoImage(Image.open("p5.png")),
        ImageTk.PhotoImage(Image.open("p6.png")),
        ImageTk.PhotoImage(Image.open("p7.png")),
        ImageTk.PhotoImage(Image.open("p8.png")),
        ImageTk.PhotoImage(Image.open("p9.png")),
        ImageTk.PhotoImage(Image.open("p10.png"))
    ]
    return stages[stage]


def isAlive():
    if stage < 10:
        return True
    else:
        return False


def reduceHealth():
    global stage
    stage + 1


def endSound(ending):
    try:
        if ending == True:
            playsound("win.wav")
        else:
            playsound("lose.wav")
    except Exception:
       pass