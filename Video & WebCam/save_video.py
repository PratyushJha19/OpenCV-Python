import cv2

camera = cv2.VideoCapture(0) # 0 = default camera, 1 = 2nd camera, 'video.mp4' = video file

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the compression format (codec) and create videowriter object
codec = cv2.VideoWriter_fourcc(*'mp4v') # 'X','V','I','D' = .avi, 'M','J','P','G' = .avi, 'M','P','4','V' = .mp4

fps = 30.0

recorder = cv2.VideoWriter('video.mp4', codec, fps, (frame_width, frame_height))

while True:
    success, image = camera.read()

    if not success:
        print("Failed to grab frame")
        break

    recorder.write(image)
    cv2.imshow('Video Recording Live', image)

    if cv2.waitKey(1) & 0xFF == ord('q'): # wait for 'q' key to exit 113 = ASCII value of 'q'
        print("Quitting...")
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()
