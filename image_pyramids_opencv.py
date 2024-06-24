import cv2
import numpy as np
'''
Pyramid, or pyramid representation, is a type of multi-scale signal representation in which
a signal or an image is subject to repeated smoothing and subsampling.

Gaussian pyramid: Repeat filtering and subsample of an image: pyrUp() & pyrDown()
Laplacian pyramid: created from gp, no exclusive function
->A level in Laplacian Pyramid is formed by the difference between that level
in Gaussian pyramid and expanded version of its upper level in gaussian pyramid
'''

img = cv2.imread('lena.jpg')
lr1 = cv2.pyrDown(img)#lr =lower resolution
lr2 = cv2.pyrDown(lr1)
hr2 = cv2.pyrUp(lr2)#hr=higher resolution

layer = img.copy()
gp = [layer]#gp=gaussian pyramid

for i in range(6):
    print(i)
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i),layer)

layer =gp[5]
cv2.imshow("Upper level gp",layer)
lp = [layer]

for i in range(5,0,-1):#5,4,3,2,1
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

# cv2.imshow('img',img)
# cv2.imshow('1-Reduced Resolution pyrDown', lr1)
# cv2.imshow('2-Reduced Resolution pyrDown', lr2)
# cv2.imshow('hr2',hr2)
cv2.waitKey(0)
cv2.destroyAllWindows()