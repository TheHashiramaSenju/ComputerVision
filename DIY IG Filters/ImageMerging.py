import cv2 as cv
def merge(foreground_path, background_path, a, b):
    
    background = []

    img        = cv.imread(foreground_path)
    background = cv.imread(background_path)
        
    background = cv.resize(background, (img.shape[1], img.shape[0]))

    final = cv.addWeighted(img, a, background, b , 0)

    cv.imshow('Original',img)
    cv.waitKey(0)

    cv.imshow('Processed',final)
    cv.waitKey(0)

merge('img_4.png', 'b4.jpeg', .5, .5)