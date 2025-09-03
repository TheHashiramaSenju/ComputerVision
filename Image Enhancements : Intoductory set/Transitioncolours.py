import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

#Different Shades of Red
plt.imshow(np.array([[[ 30 , 0 , 0 ] , [ 60 , 0 , 0 ] ,[ 90 , 0 , 0 ]],
                    [[ 120 , 0 , 0 ] , [ 150 , 0 , 0 ] ,[ 180 , 0 , 0 ]],
                    [[ 210 , 0 , 0 ] , [ 240 , 0 , 0 ] ,[ 255 , 0 , 0 ]]])) 

# we already knew that the array of array inside the matrix makes eac corresponds to specific balance of RGB, so we gradually increase the colors and 
#hence providing a good gradient effect for the images


#here we can see the demonstration 
#Merging all the images
plt.imshow(np.array([[[ 0 , 70 , 0] , [ 0 ,150, 0 ] ,[ 0 ,255,0 ]], # correspond to gradients of green
        [[ 70 , 0 , 0 ] , [ 150 , 0 , 0 ] ,[ 255 , 0 , 0 ]],#corresponds to gradient of red
        [[ 0  , 0 , 70 ] , [ 0 , 0 ,150] ,[ 0 , 0 , 255]]])) #corresponds to gradient of blue




