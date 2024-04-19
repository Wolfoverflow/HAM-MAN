from random import choice
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # auto changes the directory so that it can access the text file
os.chdir("..") # go up one directory
os.chdir("assets") # go into the assets folder

with open("words.txt", 'r') as f:
    words = f.read().split() # wordlist

word = choice(words) # get a random word (not cryptographically secure)
print(word)
def checkGuess(guess):
    if guess not in word:
        # if the letter isnt in the word, return false
        return False
    elif guess in word:
        # returns all instances of the letter in the word
        indexes = [i for i, letter in enumerate(word) if letter == guess]
        return indexes

