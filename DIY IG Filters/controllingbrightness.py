import cv2 as cv
import numpy as np
cam = cv.VideoCapture(0)
pixels = float(10)

while True:
    
    _, img = cam.read()
    img = cv.flip(img, 1)
    
    img_1 = img + pixels
    img_1[img_1 <  0 ] = 0     #For negative values
    img_1[img_1 > 255] = 255   # For values > 255
    img_1 = img_1.astype(np.uint8)	#Keeping the type of image same as og
    
    img_2 = img + (2*pixels) 	#2x brighter than img_1
    img_2[img_2 <  0 ] = 0
    img_2[img_2 > 255] = 255
    img_2 = img_2.astype(np.uint8)
    
    img_3 = img + (3*pixels) 	#3x than img_1
    img_3[img_3 <  0 ] = 0
    img_3[img_3 > 255] = 255
    img_3 = img_3.astype(np.uint8)
    
    
    cv.imshow("Original",img)
    cv.imshow("Filter-1",img_1)
    cv.imshow("Filter-2",img_2)
    cv.imshow("Filter-3",img_3)
    
    if cv.waitKey(1) == 27:
        cam.release()
        break