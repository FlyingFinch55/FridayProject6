from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Grid")

SignUpButton = ttk.Button(root, text= "Sign Up Now!")
SignUpButton.grid(row=0,column=1)


name = ttk.Label(root, text="Name")
name.grid(row=1, column=0)


email = ttk.Label(root,text= "Email")
email.grid(row=1,column=1)

password = ttk.Label(root, text="Password")
password.grid(row=1, column=2)


root,mainloop()