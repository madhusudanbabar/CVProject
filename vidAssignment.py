# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:27:03 2020

@author: krypton
"""


#%% imports
import cv2

#%% vidCap obj

cap = cv2.VideoCapture(0)

#%% properties

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

#%% global variables

center = (0,0)
isClicked = False

#%% callback function 

def create_circle(event, x, y, flags, params):
    global center, isClicked
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x,y)
        isClicked = True
        
    if event == cv2.EVENT_LBUTTONUP:
        isClicked = False
        #center = (0,0)
        
#%% Assigning callbacks
cv2.namedWindow("krypton: video assesment")
cv2.setMouseCallback("krypton: video assesment", create_circle)


#%%

while True:
    ret, frames = cap.read()
    
    if isClicked:
        cv2.circle(frames, center, 1, (255,0,255),-1)
    
    else:
        cv2.circle(frames, center, 15, (255, 0, 255), 1)
    
    cv2.imshow("krypton: video assesment", frames)
    if cv2.waitKey(1) & 0xFF == ord('k'):
        break
    

cap.release()
cv2.destroyAllWindows()