from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
# Read CSV data
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
card_list = df.to_dict(orient="records")
current_card = {}


# Flips card to the answer.
def next_card():
    # Flips the card and displays the answer.
    canvas.itemconfig(card_background, image=back_flash)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

# Changes the card to the next main topic

def change_card():
    global current_card, delay
    # Cancels any previous delay so overlap doesn't occur.
    window.after_cancel(delay)
    # Find a random card and save it globally.
    random_card = random.choice(card_list)
    current_card = random_card
    # Changes canvas information based on card
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_flash)
    # Create a new delay for next card flip
    delay = window.after(3000, next_card)


# Save list of words needed to learn. Removes flashcards that are known.
def save_word():
    card_list.remove(current_card)
    new_df = pd.DataFrame(card_list)
    new_df.to_csv("data/words_to_learn.csv", index=False)
    change_card()


# UI Setup
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
delay = window.after(3000, next_card)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_flash = PhotoImage(file="images/card_front.png")
back_flash = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image=front_flash)

# Canvas text
title_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 250, text="", fill="black", font=("Ariel", 40, "bold"))

canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)

# Buttons
wrong_pic = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_pic, command=change_card)
wrong_btn.grid(column=0, row=1)

right_pic = PhotoImage(file="images/right.png")
right_btn = Button(image=right_pic, command=save_word)
right_btn.grid(column=1, row=1)

# Displays the first card on initial program run.
change_card()

window.mainloop()
