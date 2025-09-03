import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Create 8x8 chessboard pattern (black and white squares)
chessboard = np.zeros((8, 8), dtype=np.uint8)  # Use uint8 type for images
for i in range(chessboard.shape[0]):
    for j in range(chessboard.shape[1]):
        if (i + j) % 2 == 0:
            chessboard[i, j] = 255  # white square with max value 255

# Save the chessboard image
cv.imwrite("chess_board.png", chessboard)

# Display the chessboard image using matplotlib
plt.imshow(chessboard, cmap='gray')
plt.title('8x8 Chess Board')
plt.axis('off')
plt.show()


# Create a high pixel density black image of resolution 1920x1080
img_black = np.zeros((1080, 1920), dtype=np.uint8)  # black image

# Save the black image
cv.imwrite("black_image.png", img_black)


# Create a gradient image - shades from black (0) to white (255) horizontally and vertically
gradient = np.zeros((256, 256), dtype=np.uint8)
for i in range(256):
    for j in range(256):
        gradient[i, j] = i  # shade changes row-wise (vertical gradient)

# Save the gradient image
cv.imwrite("shades.png", gradient)

# Display the gradient image using matplotlib
plt.imshow(gradient, cmap='gray')
plt.title('Shades of Black to White')
plt.axis('off')
plt.show()
