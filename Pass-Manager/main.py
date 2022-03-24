from tkinter import *
import pyperclip
import random
import string
import json
import signal
import sys

def sigint_handler(signal, frame):
    print('Bye!!')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    symbols = string.punctuation
    numbers = string.digits
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    characters = [symbols, numbers, lower_case, upper_case]
    password = []
    for f in range(10):
        thing = random.choice(characters)
        password.append(random.choice(thing))
    password_entry.insert(0, ''.join(password))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    password = password_entry.get()
    email = info_entry.get()
    website = website_entry.get()
    if password=='' or email=='' or website=='':
        raise Exception("Don't leave the entry blank!")

    new_data = {
        website: {
            "email": email,
            "password": password
            }
        }

    with open('data.json', mode='r') as data_file:
        data = json.load(data_file)
        data.update(new_data)
    with open('data.json', mode='w') as data_file:
        json.dump(data, data_file, indent=4)
    copy = pyperclip.copy(password)
    paste = pyperclip.paste()
    website_entry.delete(0, END)
    password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=20, pady=20)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100,image=img)
canvas.grid(row=0, column=1)

# Setting the labels

website_name_label = Label(text="Website:")
website_name_label.grid(column=0, row=1)

info = Label(text="Email/Username:")
info.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

#Making the necessary entries for input

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

info_entry = Entry(width=35)
info_entry.grid(row=2, column=1, columnspan=2)
info_entry.insert(0, 'daddy@gmail.com')

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# Making the buttons

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

screen.mainloop()