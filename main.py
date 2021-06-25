# import os
from tkinter import *
import pandas as pd, random as rd

BACKGROUND_COLOR = "#B1DDC6"
WIDTH = 800
HEIGHT = 526
WORD_FONT = ("Arial", 60, "bold")
LANGUAGE_FONT = ("Arial", 40, "italic")
new_value_pair = {}


# ---------------------------- BUTTONS FUNCTION  ------------------------------- #
def flip_to_french():
    fr = new_value_pair['French']
    canvas.itemconfig(french_English_word, text=fr)
    canvas.itemconfig(card_language, text='French', fill='black')
    canvas.itemconfig(card_cover, image=card_front_image)
    canvas.itemconfig(french_English_word, text=fr, fill='black')

def new_card():
    global new_value_pair, flip_timer
    window.after_cancel(flip_timer)
    new_value_pair = rd.choice(french_english_dict)
    flip_to_french()
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_cover, image=card_back_image, )
    new_en = new_value_pair['English']
    canvas.itemconfig(card_language, text='English', fill='white')
    canvas.itemconfig(french_English_word, text=new_en, fill='white')


def wrong():

    new_card()


# ---------------------------- CONVERT CSV TO DICTIONARY ------------------------- #
try:
    df = pd.read_csv("data/french_words.csv")
except FileNotFoundError:
    print('File not found')
else:
    french_english_dict = df.to_dict(orient="records")
    word = french_english_dict[0]['French']

# ---------------------------- TKINTER SETUP  ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
check_symbol = PhotoImage(file='images/right.png')
wrong_symbol = PhotoImage(file='images/wrong.png')
# ---------------------------- CANVAS CARD   ------------------------------- #
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
card_cover = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

# ---------------------------- LABELS ON CANVAS  ------------------------------- #
card_language = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
# french_label.grid(row=0, column=0)
french_English_word = canvas.create_text(400, 263, text="", font=LANGUAGE_FONT)
# french_word = canvas.create_text(400, 263, text=fr, font=('Arial', 40, 'bold'))

# ----------BUTTONS ------------#
check_button = Button(image=check_symbol, highlightthickness=0, padx=50, command=new_card)
check_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_symbol, highlightthickness=0, padx=50, command=wrong)
wrong_button.grid(row=1, column=0)

new_card()
window.mainloop()
