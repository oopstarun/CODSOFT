from tkinter import *
import pyperclip
import random

root = Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y',
             'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S',
             'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4',
             '5', '6', '7', '8', '9', '0',
             '!', '@', '#', '$', '%', '^',
             '&', '*', '(', ')', '-', '_',
             '=', '+', '[', ']', '{', '}',
             ';', ':', "'", '"', ',', '<',
             '.', '>', '/', '?']

    Password = ""
    for x in range(passlen.get()):
        Password += random.choice(pass1)
    passstr.set(Password)

label_style = {'font': ('Calibri', 20, 'bold'), 'bg': '#f0f0f0'}
entry_style = {'font': ('Arial', 14), 'width': 20, 'bd': 2, 'relief': SOLID}
button_style = {'font': ('Arial', 14, 'bold'), 'bg': '#4CAF50', 'fg': 'white', 'activebackground': '#45a049', 'activeforeground': 'white', 'bd': 2, 'relief': SOLID}

Label(root, text="Password Generator", **label_style).pack(pady=10)
Label(root, text="Enter Password Length", **label_style).pack(pady=5)
Entry(root, textvariable=passlen, **entry_style).pack(pady=5)
Button(root, text="Generate", command=generate, **button_style).pack(pady=10)
Entry(root, textvariable=passstr, font=('Arial', 14), bd=2, relief=SOLID, width=40).pack(pady=5)
Button(root, text="Copy to Clipboard", command=lambda: pyperclip.copy(passstr.get()), **button_style).pack(pady=10)

root.mainloop()
