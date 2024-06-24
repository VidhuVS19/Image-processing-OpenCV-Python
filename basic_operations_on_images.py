import numpy as np
import cv2
# from matplotlib import pyplot as plt

img = cv2.imread('Desktop wallpaper.png')
img2 = cv2.imread('OpenCV_logo.png')

print(img.shape)#returns a tuple of numbers of rows,columns and channels of the image
print(img.size)#returns Total number of pixels is accessed
print(img.dtype)# returns image datatype(like uint8)
b,g,r =cv2.split(img)

img = cv2.merge((b,g,r))

# cv2.imshow('blue',b)
# cv2.imshow('green',g)
# cv2.imshow('red',r)

roi = img[280:340, 330:390]#upperleft:bottomright(y1:y2, x1:x2)
img[273:333, 100:160] = roi

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .1, img2, .9, 0)#alpha=weight of 1st image; beta=weight of 2nd image; gamma=a scalar added; respectively

cv2.imshow("img2", img2)
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#ROI=Region of interest
#adding two images
#CHECK IN VIDEO 11