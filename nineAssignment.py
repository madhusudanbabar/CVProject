# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:13:38 2020

@author: krypton
"""

#%% imports
import cv2
import numpy as np

#%% 
img = cv2.imread("../DATA/dog_backpack.jpg")
type(img)

cv2.imshow("img", img)
