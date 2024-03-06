from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"



# UI Setup
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Canvas
canvas = Canvas(width=800, height=528, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
front_flash = PhotoImage(file="images/card_front.png")
canvas.create_image(400,275, image=front_flash)
canvas.config(bg=BACKGROUND_COLOR)
# Canvas text
canvas.create_text(400, 150, text="title", fill="black", font=("Ariel", 40, "italic"))
canvas.create_text(400, 200, text="word", fill="black", font=("Ariel", 40, "bold"))

# Buttons
wrong_pic = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_pic)
wrong_btn.grid(column=0, row=1)

right_pic = PhotoImage(file="images/right.png")
right_btn = Button(image=right_pic)
right_btn.grid(column=1, row=1)



window.mainloop()