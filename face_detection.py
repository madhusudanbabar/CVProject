# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:22:14 2020

@author: krypton
"""


#%% imports 
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% 
nadia = cv2.imread("../DATA/Nadia_Murad.jpg", 0)
denis = cv2.imread("../DATA/Denis_Mukwege.jpg", 0)
solvay = cv2.imread("../DATA/solvay_conference.jpg", 0)
plt.imshow(nadia, cmap="gray")
plt.imshow(denis, cmap="gray")

#%% 
face_cascade = cv2.CascadeClassifier("../DATA/haarcascades/haarcascade_frontalface_default.xml")

#%% 
def detect_face(img):
    
    face_img = img.copy()
    
    face_rects = face_cascade.detectMultiScale(face_img)
    
    for(x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y),(x+w, y+h), (255, 255, 255), 10)
        
    return face_img

#%%

result = detect_face(solvay)

plt.imshow(result)

#%% 
def adj_detect_face(img):
    
    face_img = img.copy()
    
    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=5)
    
    for(x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y),(x+w, y+h), (255, 255, 255), 10)
        
    return face_img

#%%

result = adj_detect_face(solvay)

plt.imshow(result)

#%% 
eye_cascade = cv2.CascadeClassifier("../DATA/haarcascades/haarcascade_eye.xml")

#%% 
def detect_eyes(img):
    
    face_img = img.copy()
    
    eye_rects = eye_cascade.detectMultiScale(face_img)
    
    for(x, y, w, h) in eye_rects:
        cv2.rectangle(face_img, (x, y),(x+w, y+h), (255, 255, 255), 10)
        
    return face_img

#%% 
result = detect_eyes(nadia)
plt.imshow(result)


#%% live feed

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read(0)
    
    frame = detect_face(frame)
    
    cv2.imshow("face", frame)
    
    k = cv2.waitKey(1)
    
    if k == ord('k'):
        break
    
cap.release()
cv2.destroyAllWindows()