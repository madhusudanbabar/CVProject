# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:59:19 2020

@author: krypton
"""

#%% imports 
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%%
img = cv2.imread("../DATA/00-puppy.jpg")
plt.imshow(img, cmap="gray")

fix = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(fix)

gray = cv2.imread("../DATA/00-puppy.jpg", cv2.IMREAD_GRAYSCALE)
plt.imshow(gray)
plt.imshow(gray, cmap="gray")
plt.imshow(gray, cmap="magma")

#%%

res = cv2.resize(fix,(800,1000))
plt.imshow(res)

flip = cv2.flip(fix,-1)
plt.imshow(flip)

#%%

cv2.imwrite("k.jpg",flip)
