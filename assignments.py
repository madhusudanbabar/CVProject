# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:44:12 2020

@author: krypton
"""


#%% imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%%
#open the image of dog
img = cv2.imread("../DATA/dog_backpack.jpg")

#%% display with correct color scheme
fix = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(fix)

#%% flip the image vertically
flip = cv2.flip(fix,-1)
plt.imshow(flip)

#%% draw an empty rectangle on the face of dog
temp = fix.copy()
cv2.rectangle(temp,(250,400),(600,700),(255,0,0),thickness=5)
plt.imshow(temp)

#%% multiple circles with function

def create_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),15)
        
img=cv2.imread("../dog_backpack.jpg")
cv2.namedWindow(winname="backpack")
cv2.setMouseCallback("backpack", create_circle)

while True:
    cv2.imshow("backpack",img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()


