# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:28:06 2020

@author: krypton
"""


#%% imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%%
flat_chess = cv2.imread("../DATA/flat_chessboard.png")
flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2RGB)

#%% 
plt.imshow(flat_chess)

#%% gray
gray_flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_RGB2GRAY)
plt.imshow(gray_flat_chess, cmap="gray")

#%% real chess
real_chess = cv2.imread("../DATA/real_chessboard.jpg")
real_chess = cv2.cvtColor(real_chess, cv2.COLOR_BGR2RGB)
plt.imshow(real_chess)

#%% gray_real_chess
gray_real_chess = cv2.cvtColor(real_chess, cv2.COLOR_RGB2GRAY)
plt.imshow(gray_real_chess, cmap="gray")

#%% gray
gray = np.float32(gray_flat_chess)
dst = cv2.cornerHarris(src=gray, blockSize=2, ksize=3, k=0.04)
dst = cv2.dilate(dst, None)

#%% 
flat_chess[dst>0.01*dst.max()] = [255, 0, 0]
plt.imshow(flat_chess)

#############################################################################

gray = np.float32(gray_real_chess)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
real_chess[dst>0.01*dst.max()] = [255, 0, 0]
plt.imshow(real_chess)
