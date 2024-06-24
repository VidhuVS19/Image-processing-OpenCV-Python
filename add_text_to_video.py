import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1280)
cap.set(4, 720)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):#isOpened checks if the file path is correct or if the camera index exists and returns t/f
    ret, frame = cap.read()
    
    if ret:  
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+str(cap.get(3)) + '  Height: '+str(cap.get(4))
        
        datet = str(datetime.datetime.now())

        frame = cv2.putText(frame, datet, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    else:
        break;

cap.release()
cv2.destroyAllWindows()    