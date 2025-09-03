import cv2 as cv
cam = cv.VideoCapture(0)
c = 1
while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture the frame")
        break
    
    frame = cv.flip(frame, 1 )
    cv.imshow("Frame", frame)
    
    key = cv.waitKey(30)
    
    if(key == 13):
        cv.imwrite("Selfie/Selfie"+str(c)+'.png', frame) #new name for each new selfies
        c = c+1
    
    if(key == 27):
        cam.release()
        break
