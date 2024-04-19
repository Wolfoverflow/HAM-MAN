import tkinter as tk
import logic
import PIL

guessed = []
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

def submitGuess():
    global guessed
    guess = entry_guesser.get()
    if len(guess) > 1 or not guess.isalpha() or len(guess) == 0:
        return
    indexes = logic.checkGuess(guess)
    if indexes:
        updateWord(guess, indexes)
        if "_" not in lbl_word.cget("text"):
            lbl_GuessedLetters.config(text="You Win!")





# TODO: make a proper win screen






    else:
        if guess in guessed:
            return
        guessed.append(guess)
        updateGuessedLetters(guess)
    entry_guesser.delete(0, tk.END)

# Window definition
window = tk.Tk()
window.geometry("600x800")

# Element definitions
lbl_GuessedLetters = tk.Label(text="Failed Letters:\n")
lbl_GuessedLetters.grid(column=0, row=0, sticky='w')

lbl_word = tk.Label(text="_ _ _ _ _", font=("Helvetica", 60))
lbl_word.grid(column=0, row=1)

lbl_EntryTitle = tk.Label(text="Letter:")
entry_guesser = tk.Entry(window)
lbl_EntryTitle.grid(column=0, row=2, sticky='w')
entry_guesser.grid(column=1, row=2)

btn_Submit = tk.Button(text="Submit", command=lambda: submitGuess()) # Sends the guess to the logic class
btn_Submit.grid(column=0, row=3, sticky='w')

window.mainloop()  # Open the window

