import cv2
import numpy as np

img = cv2.imread("Desktop wallpaper.png")
rows,cols,channels=img.shape

gray = np.zeros((rows,cols),np.uint8)

for i in range(rows):
    for j in range(cols):
        try:
            gray[i][j]=np.uint8((img[i][j][0]/3+img[i][j][1]/3+img[i][j][2]/3))
        except Exception:
            print(f"{img[i][j][0]} {img[i][j][1]} {img[i][j][2]}")

thresh = np.zeros((rows,cols),np.uint8)
thresh_inv = thresh

for i in range(rows):
    for j in range(cols):
        thresh[i][j]=0 if gray[i][j]<127 else 255
for i in range(rows):
    for j in range(cols):
        thresh_inv[i][j]=255 if gray[i][j]<127 else 0


cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("thresh",thresh)
cv2.imshow("thresh_inv",thresh_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()