# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:59:33 2020

@author: krypton
"""


#%% imports
import cv2

#%% vidCap object

cap = cv2.VideoCapture(0)

#%% global variables

pt1 = (0, 0)
pt2 = (0, 0)
topLeft_clicked = False
bottomRight_clicked = False

#%% callback function
def draw_rect(event, x, y, flags, params):
    global pt1, pt2, topLeft_clicked, bottomRight_clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        #RESET THE POINTS
        if topLeft_clicked and bottomRight_clicked:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            bottomRight_clicked = False
            
        if not topLeft_clicked:
            pt1 = (x, y)
            topLeft_clicked = True
            
        elif not bottomRight_clicked:
            pt2 = (x, y)
            bottomRight_clicked = True
    pass


#%% connecting to the callback

cv2.namedWindow("krypton: computer vision")
cv2.setMouseCallback("krypton: computer vision", draw_rect)

#%% displaying frames

while True:
    ret, frame = cap.read()
    
    if topLeft_clicked:
        cv2.circle(frame, pt1, 1, (0,0,255), -1)
        
    if topLeft_clicked and bottomRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (255,0,255), 1)
    
    cv2.imshow("krypton: computer vision", frame)
    if cv2.waitKey(1) & 0xFF == ord('k'):
        break
    
cap.release()
cv2.destroyAllWindows()
