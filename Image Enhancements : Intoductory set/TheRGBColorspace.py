import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

plt.imshow([[255,255,255]]) #the reference of "why" had been give in the respective guide (notes.md) 
plt.imshow([[0,0,0]]) 


#for a complete Red image
#Creating a complete Red Image
arr = np.array([[[ 255 , 0 , 0 ] , [ 255 , 0 , 0 ] ,[ 255 , 0 , 0 ]], #[[R, G, B]]
                [[ 255 , 0 , 0 ] , [ 255 , 0 , 0 ] ,[ 255 , 0 , 0 ]],
                [[ 255 , 0 , 0 ] , [ 255 , 0 , 0 ] ,[ 255 , 0 , 0 ]]])
plt.imshow(arr)

#for a complete greeen image 
#Creating a Green Image
arr = np.array([[[ 0, 255 , 0 ] , [ 0, 255 , 0 ] ,[ 0, 255 , 0 ]],
                [[ 0, 255 , 0 ] , [ 0, 255 , 0 ] ,[ 0, 255 , 0 ]],
                [[ 0, 255 , 0 ] , [ 0, 255 , 0 ] ,[ 0, 255 , 0 ]]])
plt.imshow(arr)

#for a complete blue image 
arr = np.array([[[ 0, 0, 255 ] , [ 0, 0 , 255 ] ,[ 0, 0 , 255 ]],
                [[ 0, 0 , 255 ] , [ 0, 0 , 255 ] ,[ 0, 0 , 255 ]],
                [[ 0, 0 , 255 ] , [ 0, 0 , 255 ] ,[ 0, 0 , 255 ]]])
plt.imshow(arr)

