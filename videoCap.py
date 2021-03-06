# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:54:25 2020

@author: krypton
"""


#%% imports
import cv2

#%%
cap = cv2.VideoCapture(0)

width = cv2.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cv2.get(cv2.CAP_PROP_FRAME_HEIGHT)

#%%

while True:
    
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("video", gray)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()