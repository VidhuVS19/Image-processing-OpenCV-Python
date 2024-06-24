import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
Homogeneous filter(HF): Each output pixel is a mean of the neighbours pixels
(All pixels contribute with equal weight)
Kernel for HF = 1/(nrows*ncols) * [Matrix of 1s]

Low Pass Filter(LPF): Helps in removing the noise / in blurring etc.

High Pass Filter(HPF): Helps in finding edges in the images

Gaussian Filter: This uses a matrix in which th middle value is the highest and the values decreases as the distance from the middle value increases
(Designed for removing high frequency noise)

Median filter: Replaces each pixel value with the median of the neighbouring pixels.
This method is great for dealing with "salt and pepper noise"

Bilateral filter: For preserving the edges
Noise removal while keeping the edge sharp

'''

img = cv2.imread('Desktop Wallpaper.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25
print(kernel)


dst = cv2.filter2D(img, -1, kernel)#dst=destination image
#-1 here is given for the desired depth argument

blur = cv2.blur(img, (50,50))
gb = cv2.GaussianBlur(img, (55,55), 0)#gb=gaussian blur; third argument is sigma x value; ksize should be odd
median = cv2.medianBlur(img, 55)#the size should be odd and not 1
bilateralFilter = cv2.bilateralFilter(img, 55, 75, 75)
#2nd: diameter of each pixel neighbourhood; 3rd: filter sigma color; 4th: filter sigma coordinate space

titles =['image', '2D Convolution','blur','gaussian blur', 'median blur','bilateralFilter']
images = [img, dst, blur, gb, median, bilateralFilter]

for i in range(len(images)):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()