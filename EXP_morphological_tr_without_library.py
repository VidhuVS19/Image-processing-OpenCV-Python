import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("family.jpg",0)
gray=img
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

kernal = np.ones((3,3),np.uint8)

dilate = cv2.dilate(thresh,kernal,iterations=1)
erode = cv2.erode(thresh, kernal,iterations=1)

def padding(img,ksize):
    r,c = img.shape
    padded = np.zeros((r+(ksize//2)*2,c+(ksize//2)*2),np.uint8)
    for i in range((ksize//2),r+(ksize//2),1):
        for j in range((ksize//2),c+(ksize//2),1):
            padded[i][j]=img[i-ksize//2][j-ksize//2]
    return padded

#kernal or even ksize is not really required here, which is strange
#which means I either haven't cracked the actual method, or the actual kernel
#or, AND this method is highly inefficient
#But it works, which shows that I atleast figured out some method to get a very similar result
def masked(img,kernal,ans):
    flag=ans #flag=0 is for dilation, flag=255 is for erosion
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if flag==0: 
                if img[i][j]>0: 
                    return 255
            if flag==255:
                if img[i][j]==0:
                    return 0
    # print(kernal)
    return flag

def dilation(grey,kernal,iter):
    #while iter in range(iter,0,-1):
        result = np.ones(grey.shape, np.uint8)
        padded = padding(grey, kernal.shape[0])
        ksize=kernal.shape[0]
        rows,cols=padded.shape
        for i in range(rows-ksize+1):
            for j in range(cols-ksize+1):
                temp=grey[i:i+ksize-1,j:j+ksize-1]
                result[i][j]=masked(temp,kernal,0)
        return result
        # grey=result
        # return grey

def erosion(grey,kernal,iter):
    #while iter in range(iter,0,-1):
        result = np.ones(grey.shape, np.uint8)
        padded = padding(grey, kernal.shape[0])
        ksize=kernal.shape[0]
        rows,cols=padded.shape
        for i in range(rows-ksize+1):
            for j in range(cols-ksize+1):
                temp=grey[i:i+ksize-1,j:j+ksize-1]
                result[i][j]=masked(temp,kernal,255)
        return result
        # grey=result
        # return grey

kernal_for_dil = np.zeros((3,3),np.uint8)

#dilation function isn't quite right, it is either dilating slightly less(with the same kernel) or slightly more with a bigger kernel
dilate_without_lib = dilation(thresh,kernal_for_dil,iter=1)#iteration is taking too much time so iter here is doing nothing
erode_without_lib = erosion(thresh,kernal,iter=1)
#erosion is also eroding slightly less than the library erode
#dilation and erosion are basically the same function except for 1 thing, the parameters being passed on to mask
#erode_without_lib=gray

images = [img,thresh,dilate,erode,dilate_without_lib,erode_without_lib]
titles = ["img","thresh","dilate","erode","dilate_without_lib","erode_without_lib"]

for i in range(len(images)):
    plt.subplot(2,3,i+1), plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()