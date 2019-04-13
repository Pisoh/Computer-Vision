#this program detects faces

import cv2, time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#WEBCAM sees the image and stores it in the img variable
#img = cv2.imread("faith.jpeg")
video = cv2.VideoCapture(0)

while True:
    check, img = video.read()


    #img is converted to a gray scale for processing
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Detecting faces and getting the coordinates
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1,
                                          minNeighbors=5)

    #Drawing rectangle to show face
    for x,y,w,h in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

#Printing the face out.
    resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
    print(type(faces))
    print(faces)

    cv2.imshow("Gray", resized)
    key = cv2.waitKey(1)
    if key == ord('m'):
        break

cv2.destroyAllWindows()