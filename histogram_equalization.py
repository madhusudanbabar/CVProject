# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:08:54 2020

@author: krypton
"""



#%% imports 
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% 

gorilla = cv2.imread("../DATA/gorilla.jpg",0)


#%%
def disp_img(img):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap="gray")

#%%
disp_img(gorilla)

#%%
gorilla.shape

#%%
hist_values = cv2.calcHist([gorilla],channels=[0],mask=None, histSize=[256], ranges=[0,256])
plt.plot(hist_values)

#%%
eq_gorilla = cv2.equalizeHist(gorilla)
disp_img(eq_gorilla)

#%%
hist_values_eq = cv2.calcHist([eq_gorilla],channels=[0],mask=None, histSize=[256], ranges=[0,256])
plt.plot(hist_values_eq)
