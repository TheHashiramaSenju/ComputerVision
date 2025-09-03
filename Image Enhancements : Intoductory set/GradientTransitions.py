import numpy as np 
import matplotlib.pyplot as plt

#making images like gradients


img = []
# Red
for i in range(256):  # from Black to Red
    t = []
    for j in range(1920):
        t.append([i,0,0])
    img.append(t)
for i in range(256,0,-1):# from Red to Black using range in the opposite direction from 256 it’ll                decrement till it reaches 0
    t = []
    for j in range(1920):
        t.append([i,0,0])
    img.append(t)

# Green
for i in range(256): # from Black to Green
    t = []
    for j in range(1920):
        t.append([0,i,0])
    img.append(t)
for i in range(256,0,-1): # from Green to Black
    t = []
    for j in range(1536):
        t.append([0,i,0])
    img.append(t)


#Blue    
for i in range(256):  # from Black to Blue
    t = []
    for j in range(1536):
        t.append([0,0,i])
    img.append(t)
for i in range(256,0,-1):# from Blue to Black
    t = []
    for j in range(1536):
        t.append([0,0,i])
    img.append(t)
img = np.array(img)
plt.imshow(img)

#check order of colours and how they fill in the respective gradients
