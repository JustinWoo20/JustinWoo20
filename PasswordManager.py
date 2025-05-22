import tkinter as tk
import random
from tkinter import messagebox
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letter_list = [random.choice(letters) for _ in range(random.randint(6, 10))]
    number_list = [random.choice(numbers) for _ in range(random.randint(3, 5))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(1, 3))]
    password_list = letter_list + number_list + symbol_list
    random.shuffle(password_list)
    new_password = "".join(password_list)

    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty.")
        return

    is_ok = messagebox.askokcancel(title="Login Information", message=f"These are the details you entered. \n"
                                                              f"Website: {website}\n"
                                                              f"Email: {email}\n"
                                                              f"Password: {password}\n"
                                                              f"Would you like to save this information?")
    if is_ok:
        with open("super secret text file.txt", mode="a") as secret_file:
            secret_file.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#lock picture
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
def label_maker(input_text, row):
    #make labels
    label = tk.Label(text=input_text)
    label.grid(column=0, row=row)

label_maker("Website", 1)
label_maker("Email/Username:", 2)
label_maker("Password:", 3)

# entries
website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = tk.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(tk.END, "justinw86420@gmail.com")
password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)


# Generate password button
generate_password_button = tk.Button(text="Generate Password", command=generate_password)

generate_password_button.grid(row=3, column=2)

add_to_file = tk.Button(text="Add", width=36, command=save)
add_to_file.grid(row=4, column=1, columnspan=2)



window.mainloop()
