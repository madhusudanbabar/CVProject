# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:24:13 2020

@author: krypton
"""


#%% imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%%

blank_img = np.zeros((400,400,3))
type(blank_img)

#%%
plt.imshow(blank_img)

#%% drawing rectangle

cv2.rectangle(blank_img,(10,10),(100,100),color=(255,0,0),thickness=2)

#%% drawing circle
cv2.circle(blank_img,(200,200),100, color=(0,255,0),thickness=2)
