# program : Project 11 : Password Generator

import random
import string
import pyperclip
from tkinter import *

def password_create():
    length = int(pass_len.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    output_pass.set(password)

def password_copy():
    pyperclip.copy(output_pass.get())

root = Tk()
root.geometry("400x300")
root.title("Password Generator")

output_pass = StringVar()
pass_len = IntVar(value=8)

Label(root, text="Password Generator", font="Arial 16 bold").pack(pady=10)
Label(root, text="Password Length:", font="Arial 12").pack()
Spinbox(root, from_=8, to=32, textvariable=pass_len, width=10, font="Arial 12").pack(pady=5)
Button(root, text="Generate Password", command=password_create, font="Arial 12", bg='lightblue').pack(pady=10)
Entry(root, textvariable=output_pass, width=30, font="Arial 12").pack(pady=10)
Button(root, text="Copy to Clipboard", command=password_copy, font="Arial 12", bg='lightgreen').pack(pady=10)

root.mainloop()
