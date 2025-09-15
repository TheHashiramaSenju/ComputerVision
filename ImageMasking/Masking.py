import numpy as np
import cv2 as cv 

camera = cv.VideoCapture(0)
lower = np.array([0,0,0]) 
upper = np.array([60,60,60])
while True:  
    _ , img = camera.read()
    mask = cv.blur(img, (4,4)) 
    mask = cv.inRange(mask, lower, upper)
    cv.imshow("Frame" , img)
    cv.imshow("Mask" , mask)
    if (cv.waitKey(1) == 27):
        camera.release()
    break