# Project 2 : CALCULATOR A simple calculator is a basic application

import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""

        self.text_input = tk.StringVar()

        self.create_buttons()

    def create_buttons(self):
        # Entry widget to show expression
        entry = tk.Entry(self.root, font=('arial', 20, 'bold'), textvariable=self.text_input, bd=10, insertwidth=4, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self.root, text=button, padx=20, pady=20, font=('arial', 18, 'bold'), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Equal button
        tk.Button(self.root, text='=', padx=20, pady=20, font=('arial', 18, 'bold'), command=self.evaluate).grid(row=row_val, column=0, columnspan=4)

    def click_event(self, key):
        if key == 'C':
            self.expression = ""
            self.text_input.set("")
        else:
            self.expression += str(key)
            self.text_input.set(self.expression)

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.text_input.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.expression = ""
            self.text_input.set("")


def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
