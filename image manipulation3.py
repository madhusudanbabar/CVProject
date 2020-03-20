# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:49:47 2020

@author: krypton
"""


#%% imports
import cv2
import matplotlib.pyplot as plt
import numpy as np

#%% orig images
img = cv2.imread("../DATA/dog_backpack.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

copy = cv2.imread("../DATA/watermark_no_copy.png")
copy= cv2.cvtColor(copy, cv2.COLOR_BGR2RGB)
plt.imshow(copy)

#%% image shape
copy = cv2.resize(copy, (300,300))
copy.shape
img.shape

#%% offsets 

x_off = img.shape[1] - copy.shape[1]
y_off = img.shape[0] - copy.shape[0]

#%% roi 

roi = img[y_off:img.shape[0],x_off:img.shape[1]]
plt.imshow(roi)

#%% preparing gray image for mask
copy_gray = cv2.cvtColor(copy, cv2.COLOR_RGB2GRAY)
plt.imshow(copy_gray, cmap = "gray")

#%% inverse mask 
mask_inv = cv2.bitwise_not(copy_gray)
plt.imshow(mask_inv, cmap="gray")
mask_inv.shape

#%% adding back the 3 color channels to inv mask
white = np.full(mask_inv.shape,255,dtype=np.uint8)
plt.imshow(white,cmap="gray")

#%% bg
bg = cv2.bitwise_or(white, white, mask=mask_inv)
plt.imshow(bg, cmap="gray")

#%%
fg = cv2.bitwise_or(copy, copy, mask=mask_inv)
plt.imshow(fg)

#%% final roi

final_roi = cv2.bitwise_or(roi,fg)

img[y_off:y_off+copy.shape[0], x_off:x_off+copy.shape[1]] = final_roi

plt.imshow(img)
