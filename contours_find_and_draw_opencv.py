import numpy as np
import cv2

img = cv2.imread('OpenCV_logo.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(img.shape)
# print("Top left = ",img[0,0])
# print(img.all)
img = cv2.resize(img, (512,512))
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# dilated = cv2.dilate(thresh, None, iterations = 3)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#contours is a python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object
#hierarchy is the optional output vector which is containing the information about the image topology

print("Number of contours = "+ str(len(contours)))

print(contours[0])

cv2.drawContours(img, contours, -1, (0,255,0), 3)
#3rd=index of the contour to draw. -1 says draw all contours; 5th=thickness


cv2.imshow("Image", img)
# cv2.imshow("GRAY Image", imgray)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()