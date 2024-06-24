import cv2
'''
A classifier(namely, a cascade of boosted classifiers working with haar-like features)
is trained with a few hundred sample views of a particular object(i.e a face or a car),
called positive examples, that are scaled to the same size(say, 20x20), and negative examples
- arbitary images of the same size.                                      
'''

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread("family.jpg")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # print(faces)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # cv2.destroyAllWindows()

cap.release()