# this program detects faces

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)
video.set(3,640)     #Sets the width
video.set(4,480)     #Sets the height

while True:
    ret, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     #Converts the image to gray scale.

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,   #Detecting faces
                                          minNeighbors=5,
                                          minSize=(20, 20)
                                          )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow('Video', frame)

    k = cv2.waitKey(1)
    if k == 27 :       #Press esc to quite
        break

video.release()
cv2.destroyAllWindows()