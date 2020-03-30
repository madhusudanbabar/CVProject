# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:14:46 2020

@author: krypton
"""


#%% imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% disp

def display(img, cmap="gray"):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap="gray")
    
#%% 
reeses = cv2.imread("../DATA/reeses_puffs.png", 0)
display(reeses)

#%% 
cereals = cv2.imread("../DATA/many_cereals.jpg", 0)
display(cereals)

#%%
sift = cv2.xfeatures2d_SIFT.create()

#%% 
kp1, des1 = sift.detectAndCompute(reeses, None)
kp2, des2 = sift.detectAndCompute(cereals, None)
