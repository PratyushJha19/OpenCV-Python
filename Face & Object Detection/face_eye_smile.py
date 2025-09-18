import cv2

face_cascade = cv2.CascadeClassifier('Face & Object Detection/haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('Face & Object Detection/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('Face & Object Detection/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        """ Region of Interest - roi
        roi_gray - gray scale image of the face detecting the area inside the face rectangle
        """

        eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)
        if len(eyes) > 0:
           cv2.putText(frame, 'Eyes Detected', (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)

        smile = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)
        if len(smile) > 0:
            cv2.putText(frame, 'Smile Detected', (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow('Face, Eye and Smile Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows