import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Desktop wallpaper.png', -1)
cv2.imshow('image',img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#This is required because opencv reads an image in the BGR format and matplotlib reads it in RGB format
#omission of this line will change the colors in matplotlib window, since B values will become R values and vice versa(due to BGR to RGB)

plt.imshow(img)
# plt.xticks([]), plt.yticks([])#These remove the coordinate axes of x and y
plt.show()

'''
For showing multiple images in one window:
titles = [] #These keeps the titles of each image
images = [] #this stores the variables in which the images are stored

for i in range(len(images)):
    plt.subplot(rows, columns, i+1)
        #rows is the number of rows the images will be in, columns is no. of columns
    plt.imshow(images[i], 'gray')
        #gray is for grayscaling
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
'''

cv2.waitKey(0)
cv2.destroyAllWindows()

