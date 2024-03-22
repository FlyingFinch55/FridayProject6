from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Pack")

display = ttk.Label(root, state= DISABLED)
display.pack()

one = ttk.Button(root,text="1")
one.pack()

two = ttk.Button(root, text="2")
two.pack()

three = ttk.Button(root,text="3")
three.pack()

four = ttk.Button(root, text="4")
four.pack

five = ttk.Button(root, text="5")
five.pack()

six = ttk.Button(root, text="6")
six.pack()

seven = ttk.Button(root, text="7")
seven.pack()

eight = ttk.Button(root, text="8")
eight.pack() #lol

nine = ttk.Button(root, text="9")
nine.pack()

zero = ttk.Button(root, text="0")
zero.pack()

add = ttk.Button(root, text="+")
add.pack()

sub = ttk.Button(root, text="-")
sub.pack()

multi = ttk.Button(root, text="X")
multi.pack()

div = ttk.Button(root, text="/")
div.pack()

root,mainloop()