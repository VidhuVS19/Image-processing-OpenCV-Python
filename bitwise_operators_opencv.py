import cv2
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2 = cv2.imread("Desktop wallpaper.png")
# img2 = cv2.resize(img2, (500,250))



img3 = np.zeros(img2.shape, np.uint8)
img3.fill(255)
img3 = cv2.rectangle(img3, (img2.shape[1]//2,0), (img2.shape[1],img2.shape[0]), (0,0,0), -1)

# bitAnd = cv2.bitwise_and(img2, img1)
# bitOr = cv2.bitwise_or(img2, img1)
# bitXor = cv2.bitwise_xor(img2, img1)
bitXor = cv2.bitwise_xor(img2, img3)

# cv2.imshow("img2", img2)
# cv2.imshow("img3", img3)
# cv2.imshow("bitAnd", bitAnd)
# cv2.imshow("bitOr", bitOr)
cv2.imshow("bitXor", bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()