import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
Morhological transformations are some simple operations based on the image shape
Morphological transformations are normally performed on binary image
When these are performed, 2 things are required:
1. Original Image
2. Kernel(which decides the nature of the transformation)

Kernel: It tells you how to change the value of any given pixel by
combining it with the different amounts of the neighbouring pixels
'''

img = cv2.imread('Desktop wallpaper.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img,127,255, cv2.THRESH_BINARY_INV)

kernal = np.ones((4,4), np.uint8)

#the argument is kernel, 'kernal' is simply a variable name
dilation = cv2.dilate(mask, kernal, iterations=2)#increases white area(because kernal is a matrix of 1)
erosion = cv2.erode(mask, kernal, iterations=5)#erodes border of white area(because kernal is a matrix of 1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)#erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)#dilation performed by erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)# dilation MINUS erosion
top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)# input image MINUS opening
black_hat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernal)


titles =['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg','top hat','Black Hat']
images = [img, mask, dilation, erosion, opening, closing, mg, top_hat, black_hat]

for i in range(len(images)):
    plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()