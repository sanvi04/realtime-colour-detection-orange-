import cv2
import numpy as np

from limits1 import get_limits
orange=[16,126,230 ]
cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()

    hsvimage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=orange)
    mask =cv2.inRange(hsvimage,lowerLimit,upperLimit)
    cv2.imshow('original',frame)
    cv2.imshow('frame',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()

cv2.destroyAllWindows()

