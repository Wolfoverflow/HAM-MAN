import tkinter as tk
import logic
# import PIL

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

def submitGuess(event):
    global guessed
    guess = event.widget.get()
    if len(guess) > 1 or not guess.isalpha() or len(guess) == 0:
        entry_guesser.delete(0, tk.END)
        return
    indexes = logic.checkGuess(guess)
    if indexes:
        updateWord(guess, indexes)
        if "_" not in lbl_word.cget("text"):
            lbl_GuessedLetters.config(text="You Win!")
    else:
        if guess in guessed:
            entry_guesser.delete(0, tk.END)
            return
        guessed.append(guess)
        updateGuessedLetters(guess)
    entry_guesser.delete(0, tk.END)

def displayStage():
    logic.displayStage()

# Window definition
window = tk.Tk()
window.geometry("600x800")

# frame for guessed letters so it doesnt move everyting else
frame_guessed_letters = tk.Frame(window)
frame_guessed_letters.grid(column=0, row=0, sticky='ns')

# frame for everything else
frame_other_components = tk.Frame(window)
frame_other_components.grid(column=1, row=0, sticky='nsew') # nses so it can expand everywheere

frame_entry = tk.Frame(frame_other_components)
frame_entry.grid(column=0, row=2, sticky='w')

# Element definitions
lbl_GuessedLetters = tk.Label(frame_guessed_letters, text="Failed\nLetters:\n", justify=tk.CENTER, font=("Helvetica", 20))
lbl_GuessedLetters.grid(column=0, row=0, sticky='w', padx=15)

# Canvas definition
hangman_image = tk.Canvas(frame_other_components, width=683, height=384)
hangman_image.grid(column=0, row=0)

lbl_word = tk.Label(frame_other_components, text="_ _ _ _ _", font=("Helvetica", 60))
lbl_word.grid(column=0, row=1)

lbl_EntryTitle = tk.Label(frame_entry, text="Letter:")
lbl_EntryTitle.grid(column=0, row=0, sticky='e')

entry_guesser = tk.Entry(frame_entry)
entry_guesser.grid(column=1, row=0, sticky='w')

entry_guesser.bind("<Return>", submitGuess) # Allows the user to press enter to submit the guess

window.mainloop()  # Open the window
