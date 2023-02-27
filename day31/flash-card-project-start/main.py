from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# --------------- DET DATA ---------------- #
def get_data(data_dictionary):
    for data in data_dictionary:
        yield data

# --------------- READ DATA --------------- #
all_csv = 'data/french_words.csv'
to_learn_csv = 'data/to_learn_words.csv'
try:
    data = pd.read_csv(to_learn_csv)
except FileNotFoundError:
    data = pd.read_csv(all_csv)
finally:
    data_dict = data.to_dict(orient='records')
    words = get_data(data_dict)
    word = None

# -------------- BUTTON FUNC -------------- #
def next_word():
    global words, word, flip_timer
    window.after_cancel(flip_timer)
    word = next(words)
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=word.get('French'), fill='black')
    flip_timer = window.after(3000, flip_word)


def flip_word():
    global word
    if word:
        canvas.itemconfig(card_bg, image=card_back)
        canvas.itemconfig(title_text, text='English', fill='white')
        canvas.itemconfig(word_text, text=word.get('English'), fill='white')

def learned_words():
    global to_learn_csv
    if word:
        data_dict.remove(word)
        data = pd.DataFrame(data_dict)
        data.to_csv(to_learn_csv, index=False)
    next_word()
        
    
# ---------------- WINDOWS ---------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
right = PhotoImage(file='images/right.png')
wrong = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=526 ,background=BACKGROUND_COLOR, highlightthickness=0)
card_bg = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
word_text =canvas.create_text(400, 263, text='LFG', font=('Ariel', 60, 'italic'))
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right, highlightthickness=0, command=learned_words)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

flip_timer = window.after(3000, flip_word)

window.mainloop()