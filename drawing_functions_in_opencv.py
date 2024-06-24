import numpy as np
import cv2

# img = cv2.imread('Desktop wallpaper.png', 1)

img = np.zeros([512,512,3], np.uint8)
#This uses numpy to create a black image

# print(img)

#this code draws a line on the image
img = cv2.line(img,(0,0),(255,255),(255,0,0),5)
img = cv2.arrowedLine(img,(0,0),(255,127),(255,0,0),5)
#1st parameter=image
#2nd=starting coordinates; 3rd=ending coordinates
#4th=colour in BGR format. (255,0,0) means 255B, 0G and 0R
#5th=thickness of the line

img = cv2.rectangle(img, (384,0), (510,128), (0,0,255),5)
#the two point coordinates are the coordinates of the 
#UPPER LEFT and LOWER RIGHT corners of the rectangle
#if the thickness value is given as -1 we get a filled rectangle

img = cv2.circle(img, (447,63), 63, (0,255,0), -1)
#parameters= img, centre coordinates, radius, colour, thickness

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "OpenCV", (10,500), font, 4, (255,255,255),10,cv2.LINE_AA)
#arguments=image, text, starting coordinates, font, font size, color, thickness, Line type

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()