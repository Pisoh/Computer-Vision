
#This program builds a user interface for the computer vision project.

from tkinter import *
from tkinter.filedialog import askopenfilename
import cv2
import mysql.connector

global filename

def image_selection():
     filename = askopenfilename()
     t1.insert(END, filename)

def img_upload():
    t1.insert(END, filename)


options = {'1', '2', '3', '4', '5', '6'}

window = Tk()
window.minsize(width=300, height=300)
window.maxsize(width=300, height=300)

l1 = Label(window, text='Name')
l1.grid(row=0, column=0)

name = StringVar
e1 = Entry(window, textvariable=name)
e1.grid(row=0, column=1)

l2 = Label(window, text='Age')
l2.grid(row=1, column=0)

age = StringVar
e2 = Entry(window, textvariable=age)
e2.grid(row=1, column=1)

l3= Label(window, text='Class')
l3.grid(row=2, column=0)

#menubut = Menubutton(window, options)
#menubut.grid(row=2, column=0)

e3 = Entry(window)
e3.grid(row=2, column=1)

l4 = Label(window, text='Image')
l4.grid(row=3, column=0)

#This button gets an image saved in the system and saves in the filename variable
b1 = Button(window, text="Choose image", command = image_selection)
b1.grid(row=3, column=1)

b1 = Button(window, text='Upload', command=img_upload)
b1.grid(row=3, column=2)

t1 = Text(window, width=20, height=10)
t1.grid(row=4, column=1)

window.mainloop()