import cv2 as cv 

cam = cv.VideoCapture(0)

while True:
    _, img = cam.read()
    #image flipping
    img = cv.flip(img, 1)
    #image cropping
    frame = img[100:500, 400:800, :]
    
    cv.imshow("Frame", img)
    cv.imshow("Cropped", frame)
    
    key = cv.waitKey(20)
    if(key == 27):
        cam.release()
        break

    