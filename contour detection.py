# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:46:59 2020

@author: krypton
"""


#%% imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%%
img = cv2.imread("../DATA/internal_external.png", 0)
img.shape
plt.imshow(img, cmap="gray")

#%% contours
contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
type(contours)
len(contours)
type(hierarchy)
hierarchy

#%% external contours
external_contours = np.zeros(img.shape)

#%%
for i in range(len(contours)):
    
    if hierarchy[0][i][3] == -1:
        
        cv2.drawContours(external_contours, contours, i, 255, -1)
        
#%% disp contours
plt.imshow(external_contours, cmap="gray")


#%% internal cntours
internal_contours = np.zeros(img.shape)

#%%
for i in range(len(contours)):
    
    if hierarchy[0][i][3] == 0:
        
        cv2.drawContours(internal_contours, contours, i, 255, -1)

#%% 
plt.imshow(internal_contours, cmap="gray")
