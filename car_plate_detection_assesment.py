# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:48:32 2020

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
    
    plate_rects = model.detectMultiScale(plate)
    
    for x, y, w, h in plate_rects:
        cv2.rectangle(plate, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    return plate

#%%

res = detect_plate(img)

display(res)

