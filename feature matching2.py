# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:12:36 2020

@author: krypton
"""


#%% imports 
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%%
def display(img, cmap="gray"):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot()
    ax.imshow(img, cmap="gray")
    
    
#%%
sep_coins = cv2.imread("../DATA/pennies.jpg")
display(sep_coins)

#%% gray
gray = cv2.cvtColor(sep_coins, cv2.COLOR_BGR2GRAY)

#%% blur 
blurred = cv2.medianBlur(gray,25)
display(blurred)

#%% 
ret, sep_tresh = cv2.threshold(blurred, 160, 255, cv2.THRESH_BINARY_INV)
display(sep_tresh)

#%% 
contours, hierarchy = cv2.findContours(sep_tresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(sep_coins, contours, i, (255, 0, 0),10)
        
#%% 
display(sep_coins)
