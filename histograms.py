# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:25:10 2020

@author: krypton
"""


#%% imports 
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% 
dark_horse = cv2.imread("../DATA/horse.jpg")
show_horse = cv2.cvtColor(dark_horse, cv2.COLOR_BGR2RGB)

rainbow = cv2.imread("../DATA/rainbow.jpg")
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

bricks = cv2.imread("../DATA/bricks.jpg")
show_bricks = cv2.cvtColor(bricks, cv2.COLOR_BGR2RGB)

#%%
hist_values = cv2.calcHist([dark_horse],[1],None,[256],[0,256])
 
#%%
plt.plot(hist_values)

#%%
img = dark_horse
color = ("b", "g", "r")
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr, color=col)
    plt.xlim([0,56])
    plt.ylim([0,10000])