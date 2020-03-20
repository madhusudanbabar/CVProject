# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:36:42 2020

@author: krypton
"""


#%% imports
import cv2
import matplotlib.pyplot as plt

#%%
img = cv2.imread("../DATA/rainbow.jpg", 0)
plt.imshow(img, cmap="gray")

ret, thresh = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV)
plt.imshow(thresh, cmap="gray")
