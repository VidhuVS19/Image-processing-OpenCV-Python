import numpy as np
import cv2
from matplotlib import pyplot as plt


'''
Histograms tells whether the image was properly exposed
'''
# img = np.zeros((200,200), np.uint8)
img = cv2.imread('lena.jpg')
# cv2.rectangle(img, (0,100), (200,200), (255), -1)#(255)=color white

hist = cv2.calcHist([img], [0], None, [256], [0,256])
#1st= source, given in square brackets
#2nd=index of channels for which we create the histogram(it's zero because image is in grayscale), for color [0],[1],[2]
#3rd=image mask
#4th=hist size(representation of bin count)
#5th=range of x axis

plt.plot(hist)

b,g,r = cv2.split(img)
# hist_b = cv2.calcHist([b],[0], None, [256], [0,256])
# hist_g = cv2.calcHist([g],[0], None, [256], [0,256])
# hist_r = cv2.calcHist([r],[0], None, [256], [0,256])

# plt.plot(hist_b)

cv2.imshow('image',img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

plt.hist(img.ravel(), 256, [0, 256])
#2nd=max value of a pixel
#3rd=range of the pixels
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])


plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()