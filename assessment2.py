# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:24:08 2020

@author: krypton
"""



#%% imports 
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%%
def disp_img(img):
    fig = plt.figure(figsize=(12,15))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap="gray")
    
#%%

giraffes = cv2.imread("../DATA/giraffes.jpg")
giraffes = cv2.cvtColor(giraffes, cv2.COLOR_BGR2RGB)
disp_img(giraffes)

#%% bin threshold

res, bin = cv2.threshold(giraffes, 127,256,cv2.THRESH_BINARY)
disp_img(bin)

#%%
giraffes = cv2.imread("../DATA/giraffes.jpg")
giraffes = cv2.cvtColor(giraffes, cv2.COLOR_BGR2HSV)
disp_img(giraffes)

#%% kernel

kernel = np.ones((4,4),dtype=np.float32)/10

#%%
conv = cv2.filter2D(giraffes,10,kernel)
disp_img(conv)

#%% sobels

#%% kernel
kernel = np.ones((5,5),dtype=np.uint8)
gir = cv2.imread("../DATA/giraffes.jpg",0)
sobelX = cv2.Sobel(gir,cv2.CV_64F,1,0,ksize=5)
disp_img(sobelX)

#%% histograms

color = ( "b", "g", "r")
for i, col in enumerate(color):
    histr = cv2.calcHist([giraffes],[i],None,[256],[0,256])
    plt.plot(histr,col)

