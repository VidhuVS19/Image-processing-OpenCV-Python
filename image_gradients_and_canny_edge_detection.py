import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
An image gradient is a directional change in the intesity of the color of an image
This is used to find edges

3 methods:
Laplacian derivative
Sobel x method
Sobel y method

Sobel is joint gaussian and differentiation operations
'''

img = cv2.imread('Desktop wallpaper.png', cv2.IMREAD_GRAYSCALE)

#ksize=kernel size
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
#cv2.CV_64F is a data type, 64 bit float, beacuse it will involve negative values as well
lap = np.uint8(np.absolute(lap))#conversion to unsigned 8 bit integer is necessary to display it as an image
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)#3rd=dx; 4th=dy
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image','laplacian','sobelX','sobelY','sobelCombined']
images=[img, lap,sobelX,sobelY,sobelCombined]

for i in range(len(images)):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()