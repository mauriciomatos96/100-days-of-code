from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_image)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_tittle, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():

    canvas.itemconfig(card_tittle, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()






window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_tittle = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_text = canvas.create_text(400, 263, text="Word ", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=0)

wrong_button_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)

next_card()












window.mainloop()

