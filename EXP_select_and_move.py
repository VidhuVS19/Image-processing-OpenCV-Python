import cv2
import numpy as np

image_name="lena.jpg"
img = cv2.imread(image_name)
flag=False
selected=False
x0=y0=x1=y1=left_dist=right_dist=up_dist=down_dist=0
movement_flag=False

def movement(event,x,y):
    global image_name,selected,movement_flag,x0,y0,x1,y1,left_dist,right_dist,up_dist,down_dist
    # print("HELLO 1")
    if event==cv2.EVENT_LBUTTONDOWN:
        print(f"x={x} y={y} x0={x0} y0={y0} x1={x1} y1={y1}")
        if min(x0,x1)<x<max(x0,x1) and min(y0,y1)<y<max(y0,y1):
            # print("HELLO 3")
            img=cv2.imread(image_name)
            left_dist = y-min(y0,y1)
            right_dist = max(y0,y1)-y
            up_dist = x-min(x0,x1)
            down_dist = max(x0,x1)-x
            movement_flag=True
        else: '''print("HELLO 4")''';selected=False
    if event==cv2.EVENT_LBUTTONUP:
        # print("HELLO 5")
        movement_flag=False
    if movement_flag:
        # print("HELLO 2")
        img = cv2.imread(image_name)
        selected_part = img[y0:y1, x0:x1]
        img[y-left_dist:y+right_dist,x-up_dist:x+down_dist]=selected_part
        cv2.imshow("img",img)



def selection(event,x,y,flags,param):
    global flag,image_name,selected,x0,y0,x1,y1
    if selected:
        movement(event,x,y)
    if flag and not selected:
        img = cv2.imread(image_name)
        cv2.rectangle(img,(x0,y0),(x,y),(0,255,255),1)
        cv2.imshow("img",img)
    if event==cv2.EVENT_LBUTTONDOWN and not selected:
        x0=x;y0=y
        flag=True
    if event==cv2.EVENT_LBUTTONUP and not selected:
        x1=x;y1=y
        selected=True
        flag=False


cv2.imshow("img",img)
cv2.setMouseCallback('img',selection)

if cv2.waitKey(0)==27: cv2.destroyAllWindows()
#27 is ASCII for Esc key
