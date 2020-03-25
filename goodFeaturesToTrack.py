# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:53:15 2020

@author: krypton
"""


#%% imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% real chess
real_chess = cv2.imread("../DATA/real_chessboard.jpg")
real_chess = cv2.cvtColor(real_chess, cv2.COLOR_BGR2RGB)


#%%
flat_chess = cv2.imread("../DATA/flat_chessboard.png")
flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2RGB)

#%% gray
gray_flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_RGB2GRAY)
plt.imshow(gray_flat_chess, cmap="gray")


#%% gray_real_chess
gray_real_chess = cv2.cvtColor(real_chess, cv2.COLOR_RGB2GRAY)
plt.imshow(gray_real_chess, cmap="gray")

#%% 
corners = cv2.goodFeaturesToTrack(gray_flat_chess, 64, 0.01, 10 )
corners = np.int0(corners)

#%% 
for i in corners:
    x, y = i.ravel()
    cv2.circle(flat_chess, (x,y), 3, (255,0,0), -1)

plt.imshow(flat_chess)

#%%
corners = cv2.goodFeaturesToTrack(gray_real_chess, 80, 0.01, 10 )
corners = np.int0(corners)

#%% 
for i in corners:
    x, y = i.ravel()
    cv2.circle(real_chess, (x,y), 3, (255,0,0), -1)

plt.imshow(real_chess)
