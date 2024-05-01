import random
import tkinter as tk
from tkinter import Label, Button, Frame
#This line imports the Image class from Pillow for working with images and the ImageTk module for converting images to Tkinter PhotoImage objects.
#These modules are often used together to display images in a Tkinter-based application.
from PIL import Image, ImageTk

def draw_cards():
    card_names = list(cards.keys())
    random.shuffle(card_names)
    reading = card_names[:3]

    # Clear the previous result and images
    for label in card_labels + image_labels:
        label.destroy()

    # Display the drawn cards with their meanings, significance, and images in the GUI
    for i, card in enumerate(reading):
        # Load and display the card image
        image = Image.open(f"tarot_cards/{card}.jpg")
        image = image.resize((200, 300))  # Adjust the size of the displayed image
        photo = ImageTk.PhotoImage(image)
        image_label = Label(content_frame, image=photo, bg=background_color)
        image_label.image = photo
        image_label.grid(row=0, column=i, padx=20)
        image_labels.append(image_label)

        # Display the text below the card 
        label_card = Label(content_frame, text=card, font=("Arial", 12), anchor="w", bg=background_color, fg=font_color)
        label_card.grid(row=2, column=i, pady=2)
        label_meaning = Label(content_frame, text=cards[card], font=("Arial", 12), anchor="w", bg=background_color, fg=font_color)
        label_meaning.grid(row=3, column=i, pady=2)
        card_labels.extend([label_card, label_meaning])

    # Update the content frame to ensure it's properly displayed
    content_frame.update_idletasks()
    content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

with open('tarot-cards.txt') as var:
    cards = dict(line.strip().split(': ', 1) for line in var.readlines())

# Set colors
background_color = "white"
font_color = "black"

root = tk.Tk()
root.title("Tarot Card Reading")

# Set a fixed size for the window
root.geometry("800x500")

# Set background color for the root window
root.configure(bg="lightgrey")

# Create a frame to hold the content
content_frame = Frame(root, bg=background_color, borderwidth=0, highlightthickness=0)

# Create two empty lists to store the card labels and image labels
card_labels = []
image_labels = []

draw_button = Button(root, text="Draw Cards", command=draw_cards, font=("Arial", 14), bg=background_color, borderwidth=2, highlightthickness=2, highlightbackground="lightgrey", highlightcolor=background_color)
draw_button.pack(side=tk.BOTTOM, pady=(0, 20))

# Start the Tkinter event loop
root.mainloop()
