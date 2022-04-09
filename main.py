import tkinter as tk
import tkinter as ttk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('The Crypt')
        self.create_widgets()

    def encryption_magic(self):
        disposal = askstring('Encryption Password', 'Please provide a strong password')
        print(disposal)
        
    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.v1 = tk.IntVar()
        self.alpha_check = tk.IntVar()
        self.special_check = tk.IntVar()

        # label
        ttk.Label(text='User:').grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(text='Passwd:').grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(text='Lenght').grid(row=3, column=0, padx=5, pady=5)
        ttk.Label(text='A-aZ-z').grid(row=4, column=0, padx=5, pady=5)
        ttk.Label(text='@#!*').grid(row=5, column=0, padx=5, pady=5)

        # User Entry
        self.user_entry = ttk.Entry(self, width=40)
        self.user_entry.grid(row=0, column=1, columnspan=2, padx=5)

        # Password Entry
        self.passwd_entry = ttk.Entry(self, width=40)
        self.passwd_entry.grid(row=1, column=1, columnspan=2, padx=5)

        # Slider Entry
        self.slide_entry = ttk.Scale(self, variable=self.v1, from_=1, to=32, orient=HORIZONTAL)
        self.slide_entry.grid(row=3, column=1)

        # Checknutton
        self.alpha_entry = ttk.Checkbutton(self, variable=self.alpha_check, text='')
        self.alpha_entry.grid(row=4, column=1)

        # Checkbutton
        self.special_entry = ttk.Checkbutton(self, variable=self.special_check, text='')
        self.special_entry.grid(row=5, column=1)

        # button
        self.send_button = ttk.Button(text='Add', command=self.validate_data).grid(row=0, column=4, padx=5)

    def askMe(self, slide):
        res = messagebox.askquestion('askquestion', f'Password is {slide} chars long, are you ok?')
        if res == 'yes':
            messagebox.showinfo('Response', 'You are ok')
        elif res == 'no':
            messagebox.showinfo('Response', 'You are not ok')
        else:
            messagebox.showwarning('error', 'Something went wrong!')

    def validate_data(self):
        user = self.user_entry.get()
        passwd = self.passwd_entry.get()
        slide = self.v1.get()
        alpha = self.alpha_check.get()
        special = self.special_check.get()
        if user != "":
            print(user)
        else:
            messagebox.showerror('Error', 'User Please')
        if passwd == "":
            if slide <= 7:
                self.askMe(slide)
            else:
                self.encryption_magic()
        else:
            messagebox.showwarning('Missing data', "No Password provided, I'll create one")
            self.encryption_magic()


if __name__ == '__main__':
    app = App()
    app.mainloop()