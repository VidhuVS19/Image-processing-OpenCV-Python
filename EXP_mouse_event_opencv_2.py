import numpy as np
import cv2

choice = input()

click_count=0
points = []

def click_event(event, x, y, flags, param):
    global click_count
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 1, (0,255,255), -1)
        cv2.imshow('image',img)
        if click_count>0:
            cv2.line(img, points[-1], (x, y), (0,255,255), 1)
            cv2.imshow('image',img)
        points.append((x,y))
        click_count+=1

def click_triangle(event, x, y, flags, param):
    global click_count
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 1, (0,255,255), -1)
        cv2.imshow('image',img)
        if click_count>0:
            cv2.line(img, points[-1], (x, y), (0,255,255), 1)
            if len(points)>1:
                cv2.line(img, points[-2],(x,y),(0,255,255),1)
                point = (int((x+points[-1][0]+points[-2][0])/3),int((y+points[-1][1]+points[-2][1])/3))
                text = str(point)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, text,point, font, 1, (255,255,255),2)
            cv2.imshow('image',img)
        points.append((x,y))
        click_count+=1


img = np.zeros([512,512,3], np.uint8)
cv2.imshow('image',img)

if choice=='line':
    cv2.setMouseCallback('image', click_event)
elif choice=='tri':
    cv2.setMouseCallback('image',click_triangle)
else:
    print("Give a valid choice: 'line' or 'tri'")

cv2.waitKey(0)
cv2.destroyAllWindows()