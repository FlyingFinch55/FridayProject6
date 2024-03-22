from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Pack")

display = ttk.Entry(root, state=DISABLED)
display.pack(side=TOP)


#All the frams are right here together
famePackOne = ttk.LabelFrame(root)
famePackOne.pack()
famePackTwo = ttk.LabelFrame(root)
famePackTwo.pack()
famePackThree = ttk.LabelFrame(root)
famePackThree.pack()
famePackFour = ttk.LabelFrame(root)
famePackFour.pack()
famePackFive = ttk.LabelFrame(root)
famePackFive.pack()

#First row
one = ttk.Button(famePackOne,text="1")
one.pack(side=LEFT)
two = ttk.Button(famePackOne, text="2")
two.pack(side=LEFT)
three = ttk.Button(famePackOne,text="3")
three.pack(side=LEFT)

#Second row
four = ttk.Button(famePackTwo, text="4")
four.pack(side=LEFT)
five = ttk.Button(famePackTwo, text="5")
five.pack(side=LEFT)
six = ttk.Button(famePackTwo, text="6")
six.pack(side=LEFT)

#Third row
seven = ttk.Button(famePackThree, text="7")
seven.pack(side=LEFT)
eight = ttk.Button(famePackThree, text="8")
eight.pack(side=LEFT) #lol
nine = ttk.Button(famePackThree, text="9")
nine.pack(side=LEFT)

#Zero in a row by its selft
zero = ttk.Button(famePackFour, text="0")
zero.pack()

#Fourth row
add = ttk.Button(famePackFive, text="+")
add.pack(side=LEFT)
sub = ttk.Button(famePackFive, text="-")
sub.pack(side=LEFT)
multi = ttk.Button(famePackFive, text="X")
multi.pack(side=LEFT)
div = ttk.Button(famePackFive, text="/")
div.pack(side=LEFT)

root,mainloop()