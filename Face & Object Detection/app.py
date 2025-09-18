import cv2

# Cascade Classifier - specifying the trained data (xml file)

# Face Detection
face_cascade = cv2.CascadeClassifier('Face & Object Detection/haarcascade_frontalface_default.xml')

# Capturing Video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    """
    detectMultiScale() - scans and detects objects on the basis of trained data (xml file provided)

    scaleFactor - Parameter specifying how much the image size is reduced at each image scale.
    lower value - detects more faces and zooms more, but slower
    higher value - detects less faces and zooms less, but faster
    1.1 is balanced

    minNeighbors - checking for multiple neighbors for a rectangle to be considered that object (here face).
    lower value - (=<3) Loose checking, Detects more object but may be inaccurate
    higher value - (>=6) Strict checking, Detects less object but more accurate, might miss small object (faces)
    5 is balanced Safe Checking
    """

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Drawing rectangle around the object (here face)
        """
        (x,y) = top left corner of face
        (x+w, y+h) = bottom right corner of face
        faces = [
        (100, 150, 80, 80), Face 1
        (250, 120, 90, 90)  Face 2
        ]

        x = how far from left
        y = how far from top
        w = width of face
        h = height of face
        """

    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()