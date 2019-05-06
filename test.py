
#This is just to test the functions

from tkinter import *

def calc_it():
    a = int(name.get())
    b = int(age.get())
    output = a + b
    t1.insert(END, output)

window = Tk()

name = StringVar()
E1 = Entry(window, textvariable = name)
E1.grid(row=0, column=0)

age = StringVar()
E2 = Entry(window, textvariable = age)
E2.grid(row=1, column=0)

b1 = Button(window, text="Calc", command = calc_it)
b1.grid(row=2,column=0)

t1 = Text(window, width=4, height=2)
t1.grid(row=3,column=0)

window.mainloop()