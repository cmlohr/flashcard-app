import pandas
import random
from tkinter import *

BLACK = "#191919"
YELLOW = "#ffd369"
GREY = "#393e46"
WHITE = "#eeeeee"


# todo: tick and cross button
# todo: back_card
# todo: link data to cards
# todo: figure out how to switch out cards





# GUI
wd = Tk()
wd.title("Flashcards")
wd.config(padx=50, pady=50, bg=BLACK)
can = Canvas(height=700, width=900, bg=BLACK, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
can.create_image(455, 300, image=card_front)
# can.grid(column=1, row=0)
can.pack()




wd.mainloop()