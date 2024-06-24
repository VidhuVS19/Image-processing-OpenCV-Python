import cv2
from matplotlib import pyplot as plt
import numpy as np
import math


def softmax_and_color(arr):
    arr[1]=0
    if arr[0]>127: arr[0]=0; #arr[2]=255
    else: arr[2]=0; #arr[0]=255
    # esum=0
    # for i in range(len(arr)):
    #     esum += math.exp(arr[i])
    # for i in range(len(arr)):
    #     arr[i]=math.exp(arr[i])/esum*255
    return arr

img = cv2.imread("kirby.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

kernel = np.transpose(np.array([[-1,-2,-1],[0,0,0],[1,2,1]], np.float32))/4
test = np.ones((3,3))
# newtest = np.convolve(kernel,test)
# kernel =[-1,0,1]
# kernel = np.abs(kernel)
print(test)
print(kernel)
# print(newtest)

change = cv2.filter2D(img, -1, kernel)
# change = np.convolve(img, kernel)
# change = np.convolve(kernel, img)

# print(img[220][0])
# print(img[220][1])
# print(img[220][2])
# print("----------------")
# print(change[220][0])
# print(change[220][1])
# print(change[220][2])

# height, width = change.shape[:2]


# for i in range(height):
#     for j in range(width):
#         if np.all(change[i][j]!=[0,0,0]):
#             change[i][j]=softmax_and_color(change[i][j])


titles =['image', 'Change']
images = [img, change]

for i in range(len(images)):
    plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()