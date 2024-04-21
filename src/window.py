import tkinter as tk
import logic

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

# Window definition
window = tk.Tk()
window.configure(bg='white')
window.geometry("800x600")

# frame for guessed letters so it doesnt move everyting else
frame_guessed_letters = tk.Frame(window)
frame_guessed_letters.grid(column=0, row=0, sticky='ns')

# Element definitions
lbl_GuessedLetters = tk.Label(frame_guessed_letters, text="Failed\nLetters:\n", justify=tk.CENTER, font=("Helvetica", 20))
lbl_GuessedLetters.grid(column=0, row=0, sticky='w', padx=15)

# frame for everything else
frame_other_components = tk.Frame(window)
frame_other_components.grid(column=1, row=0, sticky='nsew') # nses so it can expand everywheere

lbl_word = tk.Label(frame_other_components, text="_ _ _ _ _", font=("Helvetica", 60))
lbl_word.grid(column=0, row=0)

frame_entry = tk.Frame(frame_other_components)
frame_entry.grid(column=0, row=1, sticky='w')

lbl_EntryTitle = tk.Label(frame_entry, text="Letter:")
entry_guesser = tk.Entry(frame_entry)

lbl_EntryTitle.grid(column=0, row=0, sticky='e')
entry_guesser.grid(column=1, row=0, sticky='w')

# Stage Display
stage = logic.displayStage()  # Keep a reference to the image object
display_Hangman = tk.Canvas(window, width=683, height=384)
display_Hangman.create_image(350, 150, image=stage)
display_Hangman.grid(column=1, row=0)


window.mainloop()