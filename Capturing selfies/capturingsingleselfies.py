import cv2 as cv

cam = cv.VideoCapture(0)
cv.namedWindow("Selfie Capture") #for naming the window that opens

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv.flip(frame, 1)  # mirror image (horizontal flip)

    gray  = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    hsv = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
    
    cv.imshow("Selfie Capture", frame)

    key = cv.waitKey(1)

    if key % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif key % 256 == 32:
        # SPACE pressed - save the selfie
        img_name = f"selfie_{img_counter}.png" #now here we save the name here
        cv.imwrite(img_name, frame) # Here we use .imwrite() to capture the image
        print(f"{img_name} saved!") 
        img_counter += 1

cam.release()
cv.destroyAllWindows()
