import pyperclip
from customtkinter import *
from PIL import Image
from tkinter import messagebox
import random
import json


# generate password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for letter in range(nr_letters)]
    password_number = [random.choice(numbers) for number in range(nr_numbers)]
    password_symbol = [random.choice(symbols) for symbol in range(nr_symbols)]

    password = password_symbol + password_number + password_letter
    random.shuffle(password)
    password = "".join(password)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# save password
def save_pass():
    website = website_entry.get()
    password = password_entry.get()
    email = username_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'"These are the details you entered:'
                                                              f' \nEmail: {email}\nPassword:{password}\nIs it ok to '
                                                              f'save?"')
        if is_ok:
            try:
                with open("data.json", mode="r") as datafile:
                    # Reading old data
                    data = json.load(datafile)
            except FileNotFoundError:  # Need to create data.json when run for first time
                with open("data.json", "w") as datafile:
                    json.dump(new_data, datafile, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as datafile:
                    # saving the updated data
                    json.dump(data, datafile, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# Search password
def search():
    website = website_entry.get()
    with open("data.json", "r") as datafile:
        data = json.load(datafile)
        email = data.get(website).get("email")
        password = data.get(website).get("password")

    messagebox.showinfo(title="Email and password", message=f"Email: {email}\n"
                                                            f"Password: {password}")
    pyperclip.copy(password)


# Window and Image
window = CTk()
set_appearance_mode("Dark")
window.geometry("600x500")

myimage = CTkImage(dark_image=Image.open("logo.png"), size=(270, 280))

# Labels
image_label = CTkLabel(master=window, image=myimage, text="")
image_label.grid(row=0, column=0, columnspan=3)

website_label = CTkLabel(text="Website:", master=window,
                         width=150, height=40, font=("Roboto", 15))
website_label.grid(row=1, column=0)

username_label = CTkLabel(text="Email/Username:", master=window,
                          width=150, height=40, font=("Roboto", 15))
username_label.grid(row=2, column=0)

password_label = CTkLabel(text="Password:", master=window,
                          width=150, height=40, font=("Roboto", 15))
password_label.grid(row=3, column=0)

# Entries
website_entry = CTkEntry(width=255, master=window, border_width=2,
                         height=35)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

username_entry = CTkEntry(width=400, master=window, border_width=2,
                          height=35)
username_entry.grid(row=2, column=1, columnspan=2)
# TODO: have most commonly used email already written and when cursor is
#  on the entry, display popup to most commonly used emails


password_entry = CTkEntry(width=255, master=window, border_width=2,
                          height=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = CTkButton(text="Generate Password", master=window,
                                     font=("Roboto", 13), command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = CTkButton(master=window, text="Add", width=255,
                       font=("Roboto", 15), command=save_pass)
add_button.grid(row=4, column=1)

search_password_button = CTkButton(text="Search", master=window, font=("Roboto", 15), command=search)
search_password_button.grid(row=1, column=2)

window.mainloop()
