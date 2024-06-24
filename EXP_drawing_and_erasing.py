#ERASING NOT WORKING
import cv2
import numpy as np

frame = np.zeros((729,729,3),np.uint8)
frame.fill(255)
flag=False

x_coor=[];y_coor=[]
x_coor_er=[];y_coor_er=[]#erasing

def erasing(x,y):
    global frame
    cv2.circle(frame,(x,y),5,(255,255,255),-1)
    cv2.imshow("frame",frame)
    return frame


def drawing():
    global x_coor,y_coor
    frame = np.zeros((729,729,3),np.uint8)
    frame.fill(255)
    for x,y in zip(x_coor,y_coor):
        cv2.circle(frame,(x,y),2,(0,0,255),-1)
    cv2.imshow("frame",frame)
    return frame


def click_event(event,x,y,flags,param):
    global flag,x_coor,y_coor
    if event==cv2.EVENT_:
        frame=drawing(x,y)
    if flag:
        frame=drawing()
        x_coor.append(x);y_coor.append(y)
        cv2.circle(frame,(x,y),2,(0,0,255),-1)
        cv2.imshow("frame",frame)
    if event==cv2.EVENT_LBUTTONDOWN:
        x_coor.append(x);y_coor.append(y)
        flag=True
    if event==cv2.EVENT_LBUTTONUP:
        flag=False


cv2.imshow("frame",frame)

cv2.setMouseCallback("frame",click_event)

if cv2.waitKey(0)==27: cv2.destroyAllWindows()