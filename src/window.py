import tkinter as tk
import logic
from PIL import Image, ImageTk
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # auto changes the directory so that it can access the text file

os.chdir("..")  # go up one directory
os.chdir("assets")  # go into the assets folder

guessed = []
win = False
lose = False

# External functions
def updateWord(letter, index):
    word = lbl_word.cget("text")
    for i in index:
        word = list(word)
        word[i*2] = letter # this is because you can't change a single character in a string
        word = ''.join(word) # something abt immutability
        # Source: https://stackoverflow.com/questions/10631473/str-object-does-not-support-item-assignment
    lbl_word.config(text=word)

def updateGuessedLetters(letter):
    previous = lbl_GuessedLetters.cget("text")
    letters = previous + letter + "\n"
    lbl_GuessedLetters.config(text=letters)

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
        updateWord(guess, indexes)
        if "_" not in lbl_word.cget("text"):
            # logic.endSound(True)
            lbl_GuessedLetters.config(text="U\nWin!")
            win = True
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

images = [
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

# Element definitions
lbl_GuessedLetters = tk.Label(frame_guessed_letters, text="Failed\nLetters:\n", justify=tk.CENTER, font=("Helvetica", 20))
lbl_GuessedLetters.grid(column=0, row=0, sticky='w', padx=15)

# frame for everything else
frame_other_components = tk.Frame(window)
frame_other_components.grid(column=1, row=1, sticky='nsew') # nses so it can expand everywheere

lbl_word = tk.Label(frame_other_components, text="_ _ _ _ _", font=("Helvetica", 60))
lbl_word.grid(column=0, row=1)

frame_entry = tk.Frame(frame_other_components)
frame_entry.grid(column=0, row=2, sticky='w')


lbl_EntryTitle = tk.Label(frame_entry, text="Letter:")
entry_guesser = tk.Entry(frame_entry)

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

# input:  The window object
# process:  Recursively sets the background of all elements to white
# output:  None or in other words, the winodow with a white background

def set_bg_white(window): # Set the background of all elements to white so that the image isn't out of place.
    for child in window.winfo_children():
        child.configure(bg='white')
        set_bg_white(child)

set_bg_white(window) # Call the function

window.mainloop()
