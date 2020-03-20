# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:38:25 2020

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

#%% resizing to square

img = cv2.resize(img,(500,500))
mask = cv2.resize(mask, (500,500))

plt.imshow(img)
plt.imshow(mask)

#%% blending on to of each other
blend = cv2.addWeighted(img, 1, mask, .5, .1)
plt.imshow(blend)
