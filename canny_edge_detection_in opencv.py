import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
Canny edge detector is an edge detection operator that uses a multi-stage
algorithm to detect a wide range of edges in images

5 STEPS of algorithm:
1. Noise reduction- Apply Gaussian filter to smooth the image
2. Gradient calculation- Find intensity gradients of the image
3. Non-maximum suppression- to get rid of spurious response to edge detection
4. Double threshold- to determine the potential edge
5. Edge Tracking by Hysteresis- to finalise the detection of edges by suppressing all the other edges that are weak or not connected to strong edges
'''

img = cv2.imread('Desktop Wallpaper.png', 0)

canny = cv2.Canny(img, 100, 200)
#2nd = threshold1; 3rd = threshold2

titles = ['image', 'canny']
images = [img, canny]

for i in range(len(images)):
    plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()