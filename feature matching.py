# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:53:24 2020

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
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(reeses, None)  
kp2, des2 = orb.detectAndCompute(cereals, None) 

#%% 
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) 

#%%
matches = bf.match(des1, des2)

#%% 
matches = sorted(matches, key=lambda x:x.distance)

#%% 
reeses_matches = cv2.drawMatches(reeses, kp1, cereals, kp2, matches[:25], None, flags=2)
display(reeses_matches)