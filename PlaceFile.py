from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Place")

Uname = ttk.Label(root, text="Username")
Uname.place(x=0,y=0)
nameEntry = ttk.Entry(root)
nameEntry.place(x=65,y=0)

password = ttk.Label(root, text="Password")
password.place(x=0,y=20)
passEntry = ttk.Entry(root)
passEntry.place(x=65, y=20)

login = ttk.Button(root, text="Login")
login.place(x=50,y=50)

root,mainloop()