import cv2

cap = cv2.VideoCapture(0) # 0 = default camera, 1 = 2nd camera, 'video.mp4' = video file

while True:
    ret, frame = cap.read() # ret = True/False, frame = 1st frame/image
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # wait for 'q' key to exit 113 = ASCII value of 'q'
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()