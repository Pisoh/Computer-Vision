#This program trains the computer to recognize pictures

import cv2
import numpy as np
from PIL import Image
import os

#Path for face image database

path = 'dataset'

recognizer = cv2.face.createLBPHFaceRecognizer()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Function to get the images and label data

def getImagesAndLabel(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        PIL_image = Image.open(imagePath).convert('L')  #Convert it to gray scale

        img_numpy = np.array(PIL_image, 'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples, ids
print("\n [INFO] Training faces. It will take a few seconds. Wait ... ")
faces, ids = getImagesAndLabel(path)
recognizer.train(faces, np.array(ids))

#Save the model into trainer/trainer.yml
recognizer.save('trainner/trainer.yml')
#Print the number of faces trained and end the program
print("\n [INFO] {0} faces trained. Exiting program".format(len(np.unique(ids))))
