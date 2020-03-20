# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:51:49 2020

@author: krypton
"""


#%% imports 
import numpy as np
import matplotlib.pyplot as plt
import cv2
%matplotlib inline

#%%

def load_img():
    img = cv2.imread("../DATA/bricks.jpg").astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

#%% 
def disp_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img)

#%% display image
i = load_img()
disp_img(i)

#%% gamma
gamma = 2
res = np.power(i, gamma)   
disp_img(res)

#%% reset code
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text = "krypton", org = (10,600), fontFace = font, fontScale = 10, color = (255, 0, 0),thickness = 5)
disp_img(img)

#%% kernel
kernel = np.ones((5,5),dtype=np.float32)/25
kernel

dst = cv2.filter2D(img, -1, kernel)
dst
disp_img(dst)

#%% reset code
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text = "krypton", org = (10,600), fontFace = font, fontScale = 10, color = (255, 0, 0),thickness = 5)
disp_img(img)

#%% builtin blur kernel

blurred = cv2.blur(img, (5,5))
disp_img(blurred)


blurred = cv2.blur(img, (10,10))
disp_img(blurred)


#%% reset code
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text = "krypton", org = (10,600), fontFace = font, fontScale = 10, color = (255, 0, 0),thickness = 5)
disp_img(img)

#%% guassian blur

gblur = cv2.GaussianBlur(img,(5,5),9)
disp_img(gblur)


#%% reset code
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text = "krypton", org = (10,600), fontFace = font, fontScale = 10, color = (255, 0, 0),thickness = 5)
disp_img(img)

#
