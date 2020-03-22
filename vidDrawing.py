# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:47:33 2020

@author: krypton
"""


#%% imports
import cv2

#%% vidCap object

cap = cv2.VideoCapture(0)

#%% properties

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

x = width // 2
y = height // 2
w = width // 4
h = height // 4
#%% displaying frames

while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (x, y),(x+w,y+h), (255,0,0), 2)
    cv2.imshow("krypton: computer vision", frame)
    if cv2.waitKey(1) & 0xFF == ord('k'):
        break
    
cap.release()
cv2.destroyAllWindows()
