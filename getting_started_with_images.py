#imports opencv
import cv2

#read image 
#1: colour
#0: grayscale
#-1: exact same as the image
img = cv2.imread("Desktop Wallpaper.png",0)

'''
#shows the image img in a window named 'image', there needs to be a window name even if it is an empty string
cv2.imshow('image',img)
#waits for 5000 ms (5s) instead of immediately closing the window
cv2.waitKey(5000)
#closes all windows opened by the program
cv2.destroyAllWindows()
'''

#prints the matrix of values stored in img
print(img)

cv2.imshow('image',img)

pressed_key = cv2.waitKey(0)#Stores the key pressed in the variable

if pressed_key==27:#27 is ASCII for Esc key
    cv2.destroyAllWindows()
elif pressed_key==ord('s'):#ord() returns the unicode value of the character inside it
    cv2.imwrite("Gray wallpaper.jpg",img)
    cv2.destroyAllWindows()
