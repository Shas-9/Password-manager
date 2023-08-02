import pyperclip
from customtkinter import *
from PIL import Image
from tkinter import messagebox
import random
import json

# Function to generate password
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
    ' '.join(password)
    str(password)

    #password_entry.insert(0, password)
    pyperclip.copy(password)
    return password

generate_password()
