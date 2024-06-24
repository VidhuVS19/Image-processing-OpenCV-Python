import cv2
import numpy as np

img = np.zeros((729,729,3),np.uint8)

x_coor=[];y_coor=[]

def make_image():
    img=np.zeros((729,729,3),np.uint8)
    for i in range(0,len(x_coor)-1,2):
        cv2.rectangle(img,(x_coor[i],y_coor[i]),(x_coor[i+1],y_coor[i+1]),(255,255,0),1)
    return img


flag=False

def click_event(event,x,y,flags,param):
    global flag,x_coor,y_coor
    if flag:
        img = make_image()
        cv2.rectangle(img,(x_coor[-1],y_coor[-1]),(x,y),(255,255,0),1)
        cv2.imshow('img',img)
    if event == cv2.EVENT_LBUTTONDOWN: 
        x_coor.append(x);y_coor.append(y)
        flag=True
    if event == cv2.EVENT_LBUTTONUP: 
        x_coor.append(x);y_coor.append(y)
        flag=False


cv2.imshow('img',img)
cv2.setMouseCallback('img', click_event)

if cv2.waitKey(0)==27: cv2.destroyAllWindows()