from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range (randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range (randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range (randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)
    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_text = web_entry.get().capitalize()
    log_text = log_entry.get()
    pass_text = pass_entry.get()
    new_data = {
        web_text: {
            "email": log_text,
            "password": pass_text
        }
    }

    if len(web_text) == 0 or len(log_text) == 0 or len(pass_text) == 0:
        messagebox.showerror(title='Missing Info', message="Please don't leave any fields empty")
    else:
        try:
            with open('data.json', 'r') as lock_file:
                data = json.load(lock_file)
        except FileNotFoundError:
            data = {}
        except json.decoder.JSONDecodeError:
            data = {}
        data[web_text] = {
            "email": log_text,
            "password": pass_text
        }

        with open('data.json', 'w') as lock_file:
            json.dump(data, lock_file, indent=4)
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search_website():
    website = web_entry.get().capitalize()
    try:
        with open('data.json', 'r') as lock_file:
            data = json.load(lock_file)
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title='Empty File', message='No data found in the JSON file')
        return
    try:
        website_data = data[website]
        messagebox.showinfo(title=website, message=f'Email: {website_data["email"]}\nPassword: {website_data["password"]}')
    except KeyError:
        messagebox.showinfo(title='No Website', message='Website not found')



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
lock = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=lock)
canvas.grid(column=1, row=0)

#Label
website = Label(text='Website:', font=('Arial', 15))
website.grid(column=0, row=1)
website.focus()

login = Label(text='Email/Username:', font=('Arial', 15))
login.grid(column=0, row=2)

password = Label(text='Password:', font=('Arial', 15))
password.grid(column=0, row=3)

#Button
gen_pass = Button(text='Generate Password', command=generate_password)
gen_pass.grid(column=2, row=3)

add = Button(text='Add', width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

search = Button(text='Search', width=13, command=search_website)
search.grid(column=2,row=1)

#Entry
web_entry = Entry(width=18)
web_entry.grid(column=1, row=1)

log_entry = Entry(width=35)
log_entry.grid(column=1, row=2, columnspan=2)
log_entry.insert(0, 'your_email@email.com')

pass_entry = Entry(width=18)
pass_entry.grid(column=1, row=3)

window.mainloop()