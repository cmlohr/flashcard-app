import pandas
import random
from tkinter import *

BLACK = "#191919"
YELLOW = "#ffd369"
GREY = "#393e46"
WHITE = "#e8e8e8"
SECS = 3000
current = {}
learn = {}

try:
    data = pandas.read_csv("./data/german_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/de_en.csv")
    learn = original_data.to_dict(orient="records")
else:
    learn = data.to_dict(orient="records")


def next_card():
    global current, flip
    wd.after_cancel(flip)
    current = random.choice(learn)
    canvas.itemconfig(cards, image=card_front)
    canvas.itemconfig(language, text="German")
    canvas.itemconfig(word, text=current['German'])
    flip = wd.after(SECS, func=flip_card)


def card_known():
    learn.remove(current)
    data = pandas.DataFrame(learn)
    data.to_csv("./data/german_words.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=current['English'])
    canvas.itemconfig(cards, image=card_back)


# GUI
wd = Tk()
wd.title("Flashcards")
wd.config(padx=50, pady=50, bg=GREY)

flip = wd.after(SECS, func=next_card)

canvas = Canvas(height=630, width=850, bg=GREY, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
cards = canvas.create_image(445, 300, image=card_front)

language = canvas.create_text(440, 150, text="Flash Cards", fill=WHITE, font=("System", 35, "italic"))
word = canvas.create_text(440, 260, text="German to English", fill=WHITE, font=("Courier", 25, "normal"))

canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="./images/cross.png")
cross_btn = Button(image=wrong_img, bg=GREY, highlightthickness=0, activebackground=YELLOW, command=next_card)
cross_btn.grid(column=0, row=1)

correct_img = PhotoImage(file="./images/tick.png")
tick_btn = Button(image=correct_img, bg=GREY, highlightthickness=0, activebackground=YELLOW, command=card_known)
tick_btn.grid(column=1, row=1)

wd.mainloop()
