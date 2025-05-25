import tkinter as tk
import pandas
import random

#Colors
GREEN = "#DDF6D2"
FONT = ("Ariel", 40, "italic")


# ---------------------Flashcards ------------------------------
words_to_learn = pandas.read_csv("Word List.csv")
words_dict = words_to_learn.to_dict("records")
try:
    known_words_df = pandas.read_csv("Known Words.csv")
    known_words = known_words_df.to_dict("records")
except FileNotFoundError:
    known_words = []

words_dict = [word for word in words_dict if word not in known_words]
correct_words = []


current_word = {}
def generate_word():
    global timer, current_word
    window.after_cancel(timer)
    canvas.itemconfig(current_side, image=flashcard_front)
    random_set = random.choice(words_dict)
    current_word = random_set
    canvas.itemconfig(card_title, text="Japanese", fill="black")
    canvas.itemconfig(card_word, text=random_set["Japanese"], fill="black")
    timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")
    canvas.itemconfig(current_side, image=flashcard_back)

def mark_correct():
    correct_words.append(current_word)
    total_known_words = known_words + correct_words
    pandas.DataFrame(total_known_words).drop_duplicates().to_csv("Known Words.csv", index=False)
    generate_word()

# ----------------------UI Setup --------------------------------
window = tk.Tk()
window.title("Japanese Flashcards")
window.config(padx=50, pady=50, bg=GREEN)

canvas = tk.Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
flashcard_front = tk.PhotoImage(file="flash-card-project-start/images/card_front.png")
flashcard_back = tk.PhotoImage(file="flash-card-project-start/images/card_back.png")
current_side = canvas.create_image(400, 263)

card_title = canvas.create_text(400, 150, font=FONT)
card_word = canvas.create_text(400, 300, font=FONT)
canvas.grid(row=0, columnspan=2, column=0)


right_image = tk.PhotoImage(file="flash-card-project-start/images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=mark_correct)
right_button.grid(row=1, column=1)

wrong_image = tk.PhotoImage(file="flash-card-project-start/images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

timer = window.after(3000, flip_card)
generate_word()

window.mainloop()
