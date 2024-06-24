import numpy as np
import cv2

#To list all the events:
# events = [i for i in dir(cv2) if 'EVENT' in i]
# for event in events:
#     print(event)

font = cv2.FONT_HERSHEY_SIMPLEX

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ',y)
        cv2.putText(img, str(x) + ', ' + str(y), (x,y), font, 0.5, (255,255,0), 2)
        cv2.imshow('image', img)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]# 0 is the channel for blue(BGR)
        green = img[y, x, 1]# 1 is channel for green
        red = img[y, x, 2]# 2 is channel for red
        strBGR = str(blue)+', '+str(green)+', '+str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0,255,255),2)
        cv2.imshow('image',img)

img = np.zeros([512,512,3], np.uint8)
cv2.imshow('image', img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
