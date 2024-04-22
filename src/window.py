import tkinter as tk
import os
from PIL import Image, ImageTk

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # auto changes the directory so that it can access the text file

import logic

os.chdir("..")  # go up one directory
os.chdir("assets")  # go into the assets folder

# Global variables, stores the guessed letters and the win/lose conditions
guessed = []
win = False
lose = False
word = ""

# Functions to be used outside of the window class

# Updates the word that is displayed on the screeen with the guessed letter

# input:  letter:  The letter to be added to the word index:  The index of the letter in the word
# process:  Updates the word displayed on the screen with the guessed letter
# output: writes the new text to the label
def updateWord(letter, index):
    changed = False
    word = lbl_word.cget("text")
    wordBackup = word
    for i in index:
        changed = True
        word = list(word)
        word[i*2] = letter # this is because you can't change a single character in a string
        word = ''.join(word) # something abt immutability
        # Source: https://stackoverflow.com/questions/10631473/str-object-does-not-support-item-assignment
    lbl_word.config(text=word)
    if word != wordBackup:
        changed = True
    return changed

# Updates the list of guessed letters that were incorrect

# input:  letter:  The letter to be added to the guessed letters
# process:  Adds the letter to the guessed letters
# output:  Writes the new text which as the guessed latter to the label
def updateGuessedLetters(letter):
    previous = lbl_GuessedLetters.cget("text")
    letters = previous + letter + "\n"
    lbl_GuessedLetters.config(text=letters)

# Checks if th user won or lost, and also manages the guessed letters and the users guesses

# input:  event:  The event when the enter key is pressed
# process:  Checks the guess and updates the screen accordingly, win/lose conditions are checked
# output:  updates the guessed letters or guessed word and displays if you win or lose
def submitGuess(event):
    global win
    global lose
    if win == True:
        return
    if lose == True:
        return

    global guessed
    guess = event.widget.get()
    if len(guess) > 1 or not guess.isalpha() or len(guess) == 0:
        entry_guesser.delete(0, tk.END)
        lbl_error.config(text="Invalid input")
        return
    indexes = logic.checkGuess(guess)
    lbl_error.config(text="")
    if indexes:
        guessed = updateWord(guess, indexes)
        if "_" not in lbl_word.cget("text"):
            # logic.endSound(True)
            lbl_GuessedLetters.config(text="U\nWin!")
            win = True
        if guessed == False:
            lbl_error.config(text="You already guessed that letter")
        entry_guesser.delete(0, tk.END)
        return
    else:
        if guess in guessed:
            lbl_error.config(text="You already guessed that letter")
            entry_guesser.delete(0, tk.END)
            return
        logic.reduceHealth()
        if not logic.isAlive():
            lose = True
            # logic.endSound(False)
            lbl_GuessedLetters.config(text="You lose...")
            display_Hangman.create_image(350, 150, image=images[10])
            return
        display_Hangman.create_image(350, 150, image=images[logic.getStage()])
        guessed.append(guess)
        updateGuessedLetters(guess)
    entry_guesser.delete(0, tk.END)

# Window definition
window = tk.Tk()
window.configure(bg='white')
window.geometry("800x600")

images = [ # Stores the images for the hangman to be access when required
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

# frame for guessed letters so it doesnt move everyting else
frame_guessed_letters = tk.Frame(window)
frame_guessed_letters.grid(column=0, row=0, sticky='ns')

# Label for displaying the incorrect letters that have been guessed and were wrong
lbl_GuessedLetters = tk.Label(frame_guessed_letters, text="Failed\nLetters:\n", justify=tk.CENTER, font=("Helvetica", 20))
lbl_GuessedLetters.grid(column=0, row=0, sticky='w', padx=15)

# frame for everything else
frame_other_components = tk.Frame(window)
frame_other_components.grid(column=1, row=1, sticky='nsew') # nses so it can expand everywheere

# shows the word with the letters that have been guessed
lbl_word = tk.Label(frame_other_components, text="_ _ _ _ _", font=("Helvetica", 60))
lbl_word.grid(column=0, row=1)

# The place for the user to enter ther guess
frame_entry = tk.Frame(frame_other_components)
frame_entry.grid(column=0, row=2, sticky='w')

# The text the goes beside the entry box so users know what it is for
lbl_EntryTitle = tk.Label(frame_entry, text="Letter:")
entry_guesser = tk.Entry(frame_entry)

# Placing the elements onto the screen in desired locations, including error messages.
lbl_EntryTitle.grid(column=0, row=0, sticky='e')
entry_guesser.grid(column=1, row=0, sticky='w')
lbl_error = tk.Label(frame_entry, text="", fg="red")
lbl_error.grid(column=2, row=0, sticky='w')

# Stage Display
stage = logic.getStage()  # Keep a reference to the image object
display_Hangman = tk.Canvas(window, width=683, height=384)
display_Hangman.create_image(350, 150, image=images[stage])
display_Hangman.grid(column=1, row=0)

entry_guesser.bind("<Return>", submitGuess) # Allows the user to press enter to submit the guess

# Literally just set the background to white, why is it not white by default honestly man.

# input:  The window object
# process:  Recursively sets the background of all elements to white
# output:  None or in other words, the winodow with a white background

def set_bg_white(window): # Set the background of all elements to white so that the image isn't out of place.
    for child in window.winfo_children():
        child.configure(bg='white')
        set_bg_white(child)

set_bg_white(window) # Call the function

window.mainloop()
