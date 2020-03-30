# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:23:01 2020

@author: krypton
"""


#%% imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%%
road = cv2.imread("../DATA/road_image.jpg")
road_copy = road.copy()

#%%
road.shape[:2]

#%% 
marker_image = np.zeros(road.shape[:2], dtype=np.int32)
segments = np.zeros(road.shape, dtype=np.uint8)
segments

#%%
from matplotlib import cm

#%%
cm.tab10(0)

#%%
def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)

#%%
colors = []
for i in range(10):
    colors.append(create_rgb(i))
    
colors


#%% global variables 
#color_choice
current_marker = 1

#marker updated by watershed 
marks_udated = False
n_markers = 10

#%% callback function
def mouse_callback(event, x, y, flags, params):
    global marks_udated
    
    if event == cv2.EVENT_LBUTTONDOWN:
        #markers passed to watershed algo
        cv2.circle(marker_image, (x,y), 10, (current_marker), -1)
        
        #user sees on road
        cv2.circle(road_copy, (x, y), 10, colors[current_marker], -1)
        marks_udated = True
        
#%% while true
cv2.namedWindow("road image")
cv2.setMouseCallback("road image", mouse_callback)

while True:
    cv2.imshow("watershed segments", segments)
    cv2.imshow("road image", road_copy)
    
    k = cv2.waitKey(1)
    
    if k == ord('k'):
        break
    elif k == ord('c'):
        road_copy = road.copy()
        
        marker_image = np.zeros(road.shape[:2], dtype=np.int32)
        segments = np.zeros(road.shape, dtype=np.uint8)
        
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))
        
        
        
    if marks_udated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(road, marker_image_copy)
        
        segments = np.zeros(road.shape, dtype=np.uint8)
   
        for color_ind in range(n_markers):
            #coloring segments
            segments[marker_image_copy==(color_ind)] = colors[color_ind]
            
        
cv2.destroyAllWindows()
