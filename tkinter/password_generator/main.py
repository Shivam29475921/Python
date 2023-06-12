from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

DEFAULT_EMAIL = "shivamdas16122002@gmail.com"
FONT = ("Courier", 12)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(index=0, string=f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_info():
    e1 = website_entry.get()
    e2 = email_entry.get()
    e3 = password_entry.get()

    # new data stores the entries in json format
    new_data = {
        e1: {
            "email": e2,
            "password": e3,
        }
    }

    if len(e1) == 0 or len(e2) == 0 or len(e3) == 0:
        messagebox.showerror(title="No input", message="Dont submit an empty form you dumbass")
    else:
        proceed = messagebox.askokcancel(title=e1, message=f"Details entered:\nemail/username: "
                                         f"{e2}\npassword: {e3}\nProceed?")
        if proceed:
            # storing passwords to a json file
            try:
                with open('passwords.json', mode='r') as file:
                    # updated data stores the json contents as a dict
                    updated_data = json.load(file)

            except FileNotFoundError:
                with open('passwords.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)

            else:
                # updating the updated data with new data
                updated_data.update(new_data)
                # dumping the updated dict
                with open('passwords.json', mode='w') as file:
                    # dumping the new updated data into the json file
                    json.dump(updated_data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(index=0, string=DEFAULT_EMAIL)
                password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    user_entry = website_entry.get()
    try:
        with open('passwords.json', mode='r') as file:
            password_data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Warning", message="No file found to search through")
    else:
        if user_entry.lower() in password_data:
            messagebox.showinfo(title=f"{user_entry}",
                                message=f"Email:{password_data[user_entry.lower()]['email']}"
                                f"\nPassword:{password_data[user_entry.lower()]['password']}")
            pyperclip.copy(password_data[user_entry.lower()]['password'])
        else:
            messagebox.showerror(title="Warning", message=f"{user_entry} not found in your local storage")


# ---------------------------- UI SETUP ------------------------------- #
# window


window = Tk()
window.title("Password generator")
window.config(padx=50, pady=50)


# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
background = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=background)
canvas.grid(column=1, row=0)

# entries and labels and buttons

website_text = Label(text="Website:", font=FONT)
website_text.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_text = Label(text="Email/Username:", font=FONT)
email_text.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.insert(index=0, string=DEFAULT_EMAIL)
email_entry.grid(column=1, row=2, columnspan=2)

password_text = Label(text="Password:", width=20, font=FONT)
password_text.grid(column=0, row=3)

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3, columnspan=2)

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_password_btn = Button(text="Add", width=30, command=add_info)
add_password_btn.grid(column=1, row=4, columnspan=2)

search_password_btn = Button(text="Search", command=search_password)
search_password_btn.grid(column=2, row=1)

window.mainloop()
