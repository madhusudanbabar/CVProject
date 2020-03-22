# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:12:23 2020

@author: krypton
"""


#%% imports
import cv2

#%% properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))


#%% 
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #*'DIVX' for win *'VIDX' for UNIX
writer = cv2.VideoWriter("krypton.avi", fourcc,fps,(width,height))


#%%

while True:
    
    ret, frame = cap.read()
    writer.write(frame)
    cv2.imshow("Krypton: Computer Vision",frame)
    if cv2.waitKey(1) & 0xFF == ord('k'):
        break
    
cap.release()
writer.release()
cv2.destroyAllWindows()
