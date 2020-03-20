# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:55:39 2020

@author: krypton
"""


#%% imports

import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% load_img 

def load_img():
    blank_img = np.zeros((600,600),dtype=float)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(blank_img, text="ABCDE", org=(50, 350), fontFace=font, fontScale=5, color=(255,0,250),thickness=20)
    return img
    
#%% disp_img

def disp_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap="gray")
    
    
#%% load and disp
img = load_img()
plt.imshow(img)

#%% kernel

kernel = np.ones((5,5),dtype=np.uint8)
res = cv2.erode(img, kernel, iterations = 4)
disp_img(res)

#%% img 
img = load_img()
white_noise = np.random.randint(low=0, high=2, size=(600,600))
white_noise = white_noise * 255
disp_img(white_noise)

#%% final image 
fin = white_noise + img 
disp_img(fin)

#%% morph

opening = cv2.morphologyEx(fin,cv2.MORPH_OPEN, kernel)
disp_img(opening)

#%%
img = load_img()
black_noise = np.random.randint(0,2,(600,600))
black_noise = black_noise * -255
bnimg = img + black_noise
bnimg[bnimg== -255] = 0
disp_img(bnimg)

#%% closing 
closing = cv2.morphologyEx(bnimg,cv2.MORPH_CLOSE,kernel)
disp_img(closing) 

#%% load
img = load_img()
disp_img(img)

#%% grad
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT,kernel)
disp_img(grad)
