import cv2
import numpy as np

# def masked(img1,kernel):
#     ans=[0,0,0]
#     for i in range(img1.shape[0]):
#         for j in range(img1.shape[1]):
#             ans[0]+=np.float32(img1[i][j][0])*np.float32(kernel[i][j])
#             ans[1]+=np.float32(img1[i][j][1])*np.float32(kernel[i][j])
#             ans[2]+=np.float32(img1[i][j][2])*np.float32(kernel[i][j])
#     for i in range(3):
#         if ans[i]<0: ans[i]=0
#         if ans[i]>255: ans[i]=255
#         # ans[i]=np.uint8(ans[i])
#     ans = [np.uint8(ans[0]),np.uint8(ans[1]),np.uint8(ans[2])]
#     # print(kernal)
#     return ans

def masked(color,kernel,i,j):
    ans=0
    try: 
        ans = np.sum(np.multiply(np.float32(color),kernel))
    except Exception:
        print(Exception)
        print(color," ", kernal)
        print(f"i={i} j={j}")
        exit(0)
    if ans<0: ans=0
    if ans>255: ans=255
    ans = np.uint8(ans)
    return ans

def padding(img,ksize):
    r,c,ch = img.shape
    padded = np.zeros((r+(ksize//2)*2,c+(ksize//2)*2,ch),np.uint8)
    for i in range((ksize//2),r+(ksize//2),1):
        for j in range((ksize//2),c+(ksize//2),1):
            padded[i][j]=img[i-ksize//2][j-ksize//2]
    return padded

def filtering(img, ksize, kernal):
    ksize=kernal.shape[0]
    padded = padding(img,ksize)
    #cv2.imshow("padded",padded)
    # kernal = np.ones((ksize,ksize,3),np.float32)
    # ksize=kernal.shape[0]
    kernalsum=0
    for i in range(ksize): 
        for j in range(ksize): kernalsum+=kernal[i][j]
    print(kernalsum)
    if kernalsum: kernal=kernal/kernalsum
    rows,cols,channels=padded.shape
    blur=np.copy(img)
    for i in range(rows-ksize):
        for j in range(cols-ksize):
            temp=padded[i:(i+ksize),j:(j+ksize)]
            b,g,r = cv2.split(temp)
            blur[i][j]=[masked(b,kernal,i,j),masked(g,kernal,i,j),masked(r,kernal,i,j)]
    return blur

img = cv2.imread("family.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# ksize = int(input("Enter kernal size: "))
kernal_sharpen=np.array([[0,-1,0],
                 [-1,5,-1],
                 [0,-1,0]])
ksize_sharpen = kernal_sharpen.shape[0]

ksize=3
kernal = np.ones((ksize,ksize),np.float32)
img0=np.copy(img)
img1=np.copy(img)

kernal_edges = np.array([[-1,-1,-1],
                        [-1,8,-1],
                        [-1,-1,-1]])
ksize_edges = kernal_edges.shape[0]
# cv2.imshow("img0",img)

blur = filtering(img, ksize,kernal)

sharpen = filtering(img0, ksize_sharpen, kernal_sharpen)

edges = filtering(np.copy(img), ksize_edges, kernal_edges)

cv2.imshow("img",img1)
cv2.imshow("blur",blur)
cv2.imshow("sharpen",sharpen)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()