
import cv2 as cv

cam = cv.VideoCapture(0)
while True:

    _, img = cam.read(0)  
    img = cv.flip(img,1)               # Original Frame
    blr = cv.blur(img,(5,5))           # Blur on Original Frame
    edg = cv.Canny(img, 0,50)       # Edge Detection on Original Frame
    fin = cv.Canny(blr, 0,50)       # Edge Detection on Blur Frame
    cv.imshow("Original", img)
    cv.imshow("Blur"   , blr)
    cv.imshow("Edges"   , edg)
    cv.imshow("Final"   , fin)

    if (cv.waitKey(10) == 27):
      cam.release()
      break