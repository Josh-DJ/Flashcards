from tkinter import *
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"



# Read CSV data
df = pd.read_csv("data/french_words.csv")
col1 = df.columns[0]
initial_word = df["French"].sample().values[0]

def change_card():
    random_word = df["French"].sample().values[0]
    canvas.itemconfig(word_text, text=f"{random_word}")


# UI Setup
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_flash = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image=front_flash)
# Canvas text
title_text = canvas.create_text(400, 150, text=f"{col1}", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 200, text=f"{initial_word}", fill="black", font=("Ariel", 40, "bold"))

canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)

# Buttons
wrong_pic = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_pic, command=change_card)
wrong_btn.grid(column=0, row=1)

right_pic = PhotoImage(file="images/right.png")
right_btn = Button(image=right_pic, command=change_card)
right_btn.grid(column=1, row=1)



window.mainloop()