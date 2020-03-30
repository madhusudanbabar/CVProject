# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:00:41 2020

@author: krypton
"""


#%% imports 
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% read_img car_plate.jpg
img = cv2.imread("../DATA/car_plate.jpg")

#%% display function
def display(img):
    fig = plt.figure(figsize=(12, 10))
    ax= fig.add_subplot(111)
    ax.imshow(img, cmap="gray")
    
#%% 
display(img)

#%% 
model = cv2.CascadeClassifier("../DATA/haarcascades/haarcascade_russian_plate_number.xml")

#%% def 
def detect_plate(img):
    
    plate = img.copy()
    
    roi = img.copy()
    
    plate_rects = model.detectMultiScale(plate, scaleFactor=1.3, minNeighbors=3)
    
    for x, y, w, h in plate_rects:
        cv2.rectangle(plate, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    roi = roi[y:y+h, x:x+w]
    
    blurred_roi = cv2.medianBlur(roi, 7)
    
    plate[y:y+h, x:x+w] = blurred_roi
        
    return plate

#%%

res = detect_plate(img)

display(res)
