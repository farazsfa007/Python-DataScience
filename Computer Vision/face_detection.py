import cv2

cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('eye_detect.xml')

while True:
    #Reading The file
    ret,frame=cap.read()

    # Detecting the facees
    detected_faces=face_detector.detectMultiScale(frame,1.1,5)

    for (x,y,w,h) in detected_faces:
        cv2.rectangle(frame,(x,y),(x+y,y+h),(255,0,0),3)

    cv2.imshow('using webcam',frame)

    if cv2.waitKey(10) & 0xFF == ord ('q'):
        break

cv2.destroyAllWindows()
cap.releace()