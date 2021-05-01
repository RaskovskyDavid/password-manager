from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    # shuffle mix the letters
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_emailuser.get()
    password = entry_password.get()
    if len(website) != 0 and len(email) != 0 and len(password) != 0:
        is_ok = messagebox.askokcancel(title="", message=f"These are the details entered:\nEmail: {email}"
                                                         f"\nPassword {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")


# ---------------------------- UI SETUP ------------------------------- #

# Creating a new window and configurations
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website: ")
label_website.grid(column=0, row=1)

label_email_username = Label(text="Email/Username: ")
label_email_username.grid(column=0, row=2)

label_password = Label(text="Password: ")
label_password.grid(column=0, row=3)

# Button
button_generate_password = Button(text="Generate Password", command=gen_password)
button_generate_password.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan="2")

# Entries
entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan="2")
entry_website.focus()

entry_emailuser = Entry(width=35)
entry_emailuser.grid(column=1, row=2, columnspan="2")
entry_emailuser.insert(0, "default@mail.com")

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

window.mainloop()
