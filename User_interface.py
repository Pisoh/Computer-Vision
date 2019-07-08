
#This program builds a user interface for the computer vision project.

from tkinter import *
from tkinter.filedialog import askopenfilename
import cv2
from face_recognition import know_face
#import face_dataset


window = Tk()

def getting_pic():

    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    face_id = age.get()
    face_name = name.get()
    complete = str("Picture saved successfully")

    #Initialize individual face count
    count = 0
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            count += 1

            #Save the captured image into the datasets folder

            cv2.imwrite("dataset/User" '.'+ str(face_name) + '.'+ str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])
            cv2.imshow('image', img)

        k = cv2.waitKey(100)    #Press 'Esc' to exit the video

        if k == 27:
            break
        elif count >= 30: #Take 30 face samples and stop video

            t1.insert(END, complete)
            break
    #Do a bit of cleanup

    cam.release()
    cv2.destroyAllWindows()


options = {'1', '2', '3', '4', '5', '6'}


window.minsize(width=300, height=300)
window.maxsize(width=300, height=300)

l1 = Label(window, text='Name')
l1.grid(row=0, column=0)

name = StringVar()
e1 = Entry(window, textvariable=name)
e1.grid(row=0, column=1)

l2 = Label(window, text='Age')
l2.grid(row=1, column=0)

age = StringVar()
e2 = Entry(window, textvariable=age)
e2.grid(row=1, column=1, columnspan=2)

l3= Label(window, text='Class')
l3.grid(row=2, column=0)

e3 = Entry(window)
e3.grid(row=2, column=1, columnspan=2)

l4 = Label(window, text='Image')
l4.grid(row=3, column=0)

#This button gets an image saved in the system and saves in the filename variable
b1 = Button(window, text="Take Pictures", command = getting_pic)
b1.grid(row=3, column=1)

b2 = Button(window, text="Launch Recognizer", command = know_face)
b2.grid(row = 4, column =1 )


t1 = Text(window, width=30, height=5)
t1.grid(row=5, column=1)

window.mainloop()

