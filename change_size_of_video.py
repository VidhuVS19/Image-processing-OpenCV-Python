import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)
cap.set(3, 1280)#every property has a set number 
cap.set(4, 720)
#3 is for width; 4 is for height
#The above is for resolution, and a bigger value than 
#default resolution will max out the resolution

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):#isOpened checks if the file path is correct or if the camera index exists and returns t/f
    ret, frame = cap.read()
    
    if ret:  
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#prints the width of the frame/video
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#prints the height of the frame/video
        
        # out.write(frame)#this happens before the grayscaling
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#to convert the captured frames(and in turn the video) to grayscale
        gray_flipped = cv2.flip(gray, 1)
        #2nd parameter=flip code
        #flip code: A flag to specify how to flip the array; 
        #0 means flipping around the x-axis and 
        #positive value (for example, 1) means flipping around y-axis.(mirror)
        #Negative value (for example, -1) means flipping around both axes.
        cv2.imshow('frame', gray_flipped)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    else:
        break;

cap.release()
cv2.destroyAllWindows()    