import cv2
import numpy as np

def get_limits(color):
    color = np.uint8([[color]])
    hsvcolor = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)

    lowerLimit=np.array([5,75,25],dtype=np.uint8)
    upperLimit=np.array([25,255,255],dtype=np.uint8)
    return lowerLimit, upperLimit

