import cv2
import numpy as np

# img = cv2.imread('Desktop wallpaper.png', 0)

img = np.zeros([512,512,3], np.uint8)

#The following code creates a gradient from black to white(left to right)
k=0
for i in range(0,512):
    for j in range(0,512):
        img[j][i]=[k,k,k]
    if i%2==0: k+=1

# cv2.imwrite("Gradient.png",img)

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#That underscore is another variable because the threshold functions returns 2 values, one being a boolean which is caught by _ 
_, th2 = cv2.threshold(img,127,255, cv2.THRESH_BINARY_INV)

#cv2.THRESH_TRUNC makes it so that all the values above the specified threshold become the same value as the threshold
#cv2.THRESH_TOZERO makes it so that all the values below the threshold becomes 0 and the rest remains the same
#cv2.THRESH_TOZERO_INV makes it so that the values above threshold becomes zero

cv2.imshow('Image', img)
cv2.imshow('Binary',th1)
cv2.imshow('Inverse Binary', th2)

cv2.waitKey(0)
cv2.destroyAllWindows()