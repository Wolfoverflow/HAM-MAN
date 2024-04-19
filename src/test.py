import tkinter as tk
from PIL import Image, ImageTk
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # auto changes the directory so that it can access the text file
os.chdir("..") # go up one directory
os.chdir("assets") # go into the assets folder

# Initialize Tkinter
root = tk.Tk()
canvas = tk.Canvas(root, width=683, height=384)
canvas.pack()

# Load and convert images
images = [
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
    # Add more images as needed
]

# Function to display the next image in the sequence
def display_next_image(index):
    if index < len(images):
        canvas.create_image(350, 150, image=images[index])
        root.after(1000, display_next_image, index + 1) # Display the next image after 1 second

# Start the animation
display_next_image(0)

# Run the Tkinter main loop
root.mainloop()
