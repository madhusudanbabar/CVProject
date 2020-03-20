# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 00:29:07 2020

@author: krypton
"""

#%% imports

import cv2 

img = cv2.imread("../DATA/00-puppy.jpg")
cv2.imshow("puppy", img)
cv2.waitKey()
