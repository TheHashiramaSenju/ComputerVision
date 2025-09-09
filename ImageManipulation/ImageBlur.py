import cv2 
  
# path 
path = r'mylogo.png'
image = cv2.imread(path)  
window_name = 'Image'
  
# ksize
ksize = (10, 10)
  
# Using cv2.blur() method 
image = cv2.blur(image, ksize) 
  
# Displaying the image 
cv2.imshow(window_name, image) 
path = r'mylogo.png'
  
# Reading an image in default mode 
image = cv2.imread(path) 
  
# Window name in which image is displayed 
window_name = 'Image'
  
# ksize
ksize = (30, 30)
  
# Using cv2.blur() method 
image = cv2.blur(image, ksize, cv2.BORDER_DEFAULT) 
  
# Displaying the image 
cv2.imshow(window_name, image) 