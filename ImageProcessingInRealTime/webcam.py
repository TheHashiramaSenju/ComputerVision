import cv2 as cv

for i in range(2):
    cap = cv.VideoCapture(i)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print(f"Camera at index {i} works!")
        else:
            print(f"Camera at index {i} opened but did not return a frame.")
    else:
        print(f"Camera at index {i} did not open.")
    cap.release()
