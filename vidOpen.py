# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:30:57 2020

@author: krypton
"""


#%% imports

import cv2

#%%

cap = cv2.VideoCapture("krypton.avi")

if cap.isOpened == False:
    print("Error! unable to open file or wrong codec used while recording")
    
while cap.isOpened():
    ret, frame = cap.read()
        
    if ret == True:
        cv2.imshow("krypton: computer vision", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('k'):
            break
        
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
        