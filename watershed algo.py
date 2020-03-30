# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:37:24 2020

@author: krypton
"""


#%% imports 
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%%
def display(img, cmap="gray"):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot()
    ax.imshow(img, cmap="gray")
    
    
#%%
img = cv2.imread("../DATA/pennies.jpg")
display(img)

#%% blur 
img = cv2.medianBlur(img,35)
display(img)

#%% gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
display(gray)


#%% 
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
display(thresh)

#%% noise removal
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)
display(opening)

#%% 
sure_bg = cv2.dilate(opening, kernel, iterations=3)
display(sure_bg)

#%% dist_
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

display(dist_transform)

#%%
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(),255,0)
display(sure_fg)

#%%
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
display(unknown)

#%%
ret, markers = cv2.connectedComponents(sure_fg)
markers += 1
markers[unknown==255] = 0
display(markers)

markers = cv2.watershed(img, markers)
display(markers)

#%% contours 
contours, hierarchy = cv2.findContours(markers, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
sep = cv2.imread("../DATA/pennies.jpg")

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(sep, contours, i, (255,0,0),10)
        