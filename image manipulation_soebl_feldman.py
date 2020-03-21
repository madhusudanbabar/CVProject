# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 09:57:29 2020

@author: krypton
"""

#%% imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% disp_img
def disp_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap="gray")

#%% 
img = cv2.imread("../DATA/sudoku.jpg", 0)
disp_img(img)

#%% sobel operator
#### X direction
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)    
disp_img(sobelX)

#### Y direction
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1,ksize=5)    
disp_img(sobelY)

#%% laplace operator

laplacian = cv2.Laplacian(img, cv2.CV_64F)
disp_img(laplacian)

#%% blended
blend = cv2.addWeighted(sobelX, .5, sobelY, .5, 0)
disp_img(blend)

#%% thresholding
ret, thresh = cv2.threshold(img, 100,255, cv2.THRESH_BINARY)
disp_img(thresh)

#%% morphological gradient operator

kernel = np.ones((4,4), dtype=np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
disp_img(gradient)
