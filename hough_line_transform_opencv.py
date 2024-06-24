import cv2
import numpy as np

'''
Two types of hough line transform:
1. Standard Hough Tranform(HoughLines method)
2. Probabilistic Hough Line transform(HoughLinesP method)

Hough transformation Algorithm:
1. Edge detection, e.g. using Canny edge detector.
2. Mapping of Edge points to the Hough space and storage in an accumulator.
2. Interpretation of the accumulator to yield lines of infinite length. The
interpretation is done by thresholding and possibly other constraints.
4. Conversion of inifinite line to finite lines.
'''

img = cv2.imread("sudoku.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#canny edge detection prefers grayscale image
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
#2nd: rho=Distance resolution of the accumulator in pixels
#3rd: theta=Angle resolution of the accumulator in radians
#4th: threshold=Accumulator threshold parameter. Only those lines
#               are returned that get enough votes(>threshold)
#lines will be in polar coordinates

for line in lines:
    #polar coordinates to cartesian
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)


cv2.imshow('image',img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()