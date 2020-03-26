# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:26:07 2020

@author: krypton
"""


#%% imports
import cv2
import matplotlib.pyplot as plt
import numpy as np

#%%
flat_chess = cv2.imread("../DATA/flat_chessboard.png")
plt.imshow(flat_chess)

#%% findChessBoardCorners
found, corners = cv2.findChessboardCorners(flat_chess,(7,7))
cv2.drawChessboardCorners(flat_chess, (7, 7), corners, found)
plt.imshow(flat_chess)

#%% 
dots = cv2.imread("../DATA/dot_grid.png")
plt.imshow(dots)

#%% circlesgrid
found, corners = cv2.findCirclesGrid(dots,(10, 10),cv2.CALIB_CB_SYMMETRIC_GRID)
cv2.drawChessboardCorners(dots, (10, 10), corners, found)
plt.imshow(dots)
