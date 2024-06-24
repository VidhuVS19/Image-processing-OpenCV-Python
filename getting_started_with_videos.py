import cv2

cap = cv2.VideoCapture(0)#the argument passed in this should either be the video file name in double quotes OR
#the number specifying which camera is to be used to capture the video. 0 is for default camera(it might be -1 in some devices)
#further numbers like 1,2,3 etc. are for when multiple cameras are attached to a single device, each camera is automatically indexed with a number

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
#20.0 is 20 frames per second, (640,480) is a tuple which specifies the size



#while(True):
while(cap.isOpened()):#isOpened checks if the file path is correct or if the camera index exists and returns t/f
    ret, frame = cap.read()
    #cap.read() returns true if there is a frame to capture, the captured frame is stored in the variable frame
    #and the boolean true or false is stored in ret
    
    if ret:  
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#prints the width of the frame/video
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#prints the height of the frame/video
        
        out.write(frame)#this happens before the grayscaling
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#to convert the captured frames(and in turn the video) to grayscale
        cv2.imshow('frame', gray)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    else:
        break;

cap.release()
out.release()
cv2.destroyAllWindows()    