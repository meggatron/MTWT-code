#Ensure you have tk installed, run the following in Terminal
#pip install tk
#If you don't have pip installed tyr the following in Terminal: sudo easy_install pip
#If that doesn't work try the following in Terminal (use the verson of Python you are in: python3 --version
#python3.12 -m pip install tk

import random
import tkinter as tk
from tkinter import Label, Button

def draw_cards():
    card_names = list(cards.keys())
    random.shuffle(card_names)
    reading = card_names[:3]

    # Clear the previous result (comment this out to see what it does)
    result_label.config(text="")

    # Display the drawn cards with their meanings in the GUI
    for card in reading:
        result_label.config(text=f"{card}: {cards[card]}\n" + result_label.cget("text"))

# Read card data from the file
with open('tarot-cards.txt') as var:
    lines = var.readlines()
    cards = dict(line.strip().split(': ', 1) for line in lines)

# Create the main window
root = tk.Tk()
root.title("Meghan's Tarot Card Reading")

# Set a fixed size for the window
root.geometry("400x400")

# Create a label to display the result
result_label = Label(root, text="", wraplength=400, justify=tk.LEFT)
result_label.pack(pady=10)

# Create a button to draw cards
draw_button = Button(root, text="Draw Cards", command=draw_cards)
draw_button.pack(side=tk.BOTTOM, pady=(0, 20))

# Start the Tkinter event loop
root.mainloop()
