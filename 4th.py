# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:00:49 2020

@author: krypton
"""


#%% imports
import numpy as np
import cv2
import matplotlib.pyplot as plt
#%matplotlib inline

#%%

img = cv2.imread("../DATA/00-puppy.jpg")


#%% 
#cv2.imshow("img", img)  
plt.imshow(img)

#%%

while True:
    cv2.imshow("puppy", img)
    if cv2.waitKey(1) & OxFF == ord('k'):
        break
    
cv2.destroyAllWindows()
