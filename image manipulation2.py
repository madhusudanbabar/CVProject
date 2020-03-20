# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:39:47 2020

@author: krypton
"""



#%% imports
import cv2
import matplotlib.pyplot as plt

#%% orig images
img = cv2.imread("../DATA/dog_backpack.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

mask = cv2.imread("../DATA/watermark_no_copy.png")
mask= cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
plt.imshow(mask)

#%% image shapes
img.shape
mask.shape

mask = cv2.resize(mask,(250,250))
plt.imshow(img)
plt.imshow(mask)

x_off = 0
y_off = 0
x_end = x_off + mask.shape[1]
y_end = y_off + mask.shape[0]

img[y_off:y_end, x_off:x_end] = mask
plt.imshow(img)
