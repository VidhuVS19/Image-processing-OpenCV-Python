import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.png",0)
_, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2)
#2nd= max value, 3rd=adaptive method, 5th=block sizeof neighbourhood area
#6th= value of C
#Threshold value is the mean of the neighbourhood area minus the constant C
#Gaussian: Threshold value is the weighted sum of the neighbourhood values minus the constant C,
#          where weights are the gaussian window

titles = ['Image','Simple Thresholding','Adaptive Mean', 'Adaptive Gaussian']
images = [img, th, th2, th3]

for i in range(len(images)):
    plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
# cv2.imshow('img',img)
# cv2.imshow('simple thresholding', th)

# cv2.waitKey(0)
# cv2.destroyAllWindows()