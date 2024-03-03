from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = None
try:
    words_df = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    words_df = pandas.read_csv("./data/french_words.csv")
finally:
    words_list = words_df.to_dict(orient="records")

#----------------------- CARD LERNED -----------------------#

def card_lerned():
    words_list.remove(current_card)
    pandas.DataFrame(words_list).to_csv("words_to_learn.csv", index=False)
    next_card()

#----------------------- DISPLAY ENGLISH WORD -----------------------#

def flip_card():
    canvas.itemconfig(card_imgage, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card.get("English"), fill="white")

#----------------------- DISPLAY RANDOM WORD -----------------------#

def next_card():
    global after_timer, current_card
    window.after_cancel(after_timer)
    # {"French": "french_word","English": "english_word"}
    current_card = random.choice(words_list)
    canvas.itemconfig(card_imgage, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card.get("French"), fill="black")
    after_timer = window.after(3000, flip_card)

#----------------------- UI -----------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_imgage = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
known_button = Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=card_lerned)
known_button.grid(row=1, column=1)

after_timer = window.after(3000, flip_card)
next_card()

window.mainloop()