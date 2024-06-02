import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == 'Add':
            result = add(num1, num2)
        elif operation == 'Subtract':
            result = subtract(num1, num2)
        elif operation == 'Multiply':
            result = multiply(num1, num2)
        elif operation == 'Divide':
            result = divide(num1, num2)
        
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        messagebox.showerror("Error", e)


root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='#f0f0f0')

tk.Label(root, text="Number 1:", font=('Arial', 14), bg='#f0f0f0').grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root, width=20, font=('Arial', 14))
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number 2:", font=('Arial', 14), bg='#f0f0f0').grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root, width=20, font=('Arial', 14))
entry_num2.grid(row=1, column=1, padx=10, pady=10)

button_style = {'font': ('Arial', 14), 'bg': '#4CAF50', 'fg': 'white', 'activebackground': '#45a049', 'activeforeground': 'white'}
tk.Button(root, text="Add", command=lambda: calculate('Add'), **button_style).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Subtract", command=lambda: calculate('Subtract'), **button_style).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Multiply", command=lambda: calculate('Multiply'), **button_style).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Divide", command=lambda: calculate('Divide'), **button_style).grid(row=3, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ", font=('Arial', 24), bg='#f0f0f0', fg='#333')
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

root.mainloop()
