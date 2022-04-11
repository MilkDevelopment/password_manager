from tkinter import *
from turtle import width
from tkinter import messagebox
import random
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password=0) or len(email=0):
        messagebox.showerror(title="Oops", message="Please fill out all the fields")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Make sure your details are correct: \nEmailL: {email}" f"\nPassword: {password} \nSave Information?")

        if is_ok:
            password_file = open("Password Manager/passwords.txt", "a")
            password_file.write(f"Website:{website} | Email:{email} | Password:{password} \n")
            password_file.close()

            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width=200, highlightthickness=0)
background_img = PhotoImage(file="Password Manager/logo.png")

canvas.create_image(100, 100, image=background_img)
canvas.grid(column=1,row=0)

#Buttons
add_button = Button(text="Add Password", width=36, command=save)
add_button.grid(column=1,row=4, columnspan=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2,row=3)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
Password_label = Label(text="Password:")
Password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

window.mainloop()