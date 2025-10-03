import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

prevTime = 0
currTime = 0

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                # if id == 4:  # Thumb tip
                #     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                # if id == 8:  # Index finger tip
                #     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                # if id == 12:  # Middle finger tip
                #     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                # if id == 16:  # Ring finger tip
                #     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                # if id == 20:  # Pinky tip
                #     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    currTime = time.time()
    fps = 1 / (currTime - prevTime)
    prevTime = currTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # show AFTER drawing
    cv2.imshow("Hand Tracking App", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
