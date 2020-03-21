# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:58:43 2020

@author: krypton
"""


#%% imports 
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% 

rainbow = cv2.imread("../DATA/rainbow.jpg")
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

#%% 
img = rainbow
img.shape

mask = np.zeros(img.shape[:2],np.uint8)
plt.imshow(mask, cmap="gray")

mask[300:400,100:400] = 255

#%% 
masked_img = cv2.bitwise_and(img, img, mask=mask)
show_masked = cv2.cvtColor(masked_img, cv2.COLOR_BGR2RGB)
plt.imshow(show_masked)

#%%
hist_mask_values_red = cv2.calcHist([rainbow],channels=[2],mask=mask,histSize=[256],ranges=[0,256])
plt.plot(hist_mask_values_red)
plt.title("RED histgram for masked rainbow")
