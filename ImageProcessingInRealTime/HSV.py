import cv2 as cv

cam = cv.VideoCapture(0)
while True:
    ret, img = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    img = cv.flip(img, 1)  # flip horizontally

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Correct BGR Extraction (OpenCV uses BGR order)
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    # HSV Extraction
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]

    # Display frames
    cv.imshow("Frame", img)
    cv.imshow("Blue", b)
    cv.imshow("Green", g)
    cv.imshow("Red", r)
    cv.imshow("HSV", hsv)
    cv.imshow("Hue", h)
    cv.imshow("Saturation", s)
    cv.imshow("Value", v)

    key = cv.waitKey(20)
    if key == 27:  # ESC key to exit
        break

cam.release()
cv.destroyAllWindows()
