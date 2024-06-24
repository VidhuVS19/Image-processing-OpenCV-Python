import cv2
import numpy as np

'''
Template matching is searching for a template image in another image
'''

img = cv2.imread("Desktop wallpaper.png")
# cropped = img[100:200, 100:200]
# cv2.imwrite("Cropped wp.png", cropped)
#The commented out code was run to get a cropped image

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cropped_image = cv2.imread("Cropped wp.png",0)
w, h = cropped_image.shape[::-1]#-1 gives width and height in reverse order


res = cv2.matchTemplate(img2, cropped_image, cv2.TM_CCOEFF_NORMED)
print(res)

threshold = 0.99
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1]+h), (0,0,255),2)
    print(pt)
    print(pt[0]+w,' ',pt[1]+h)

cv2.imshow("template matching",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
