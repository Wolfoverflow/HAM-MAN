import tkinter as tk

root = tk.Tk()
root.title("Test")
root.geometry("300x200")

label = tk.Label(root, text="Hello, World!")
label.pack()

print(label.cget("text"))

root.mainloop()