import cv2
import mediapipe as mp
import pyautogui
import numpy as np
from pynput.mouse import Controller, Button

mouse = Controller()

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    model_complexity=1
)

screen_width, screen_height = pyautogui.size()

def get_angle(a, b, c):
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(np.degrees(radians))
    return angle

def get_distance(landmark_list):
    if len (landmark_list) < 2:
        return
    (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]
    L = np.hypot(x2 - x1, y2 - y1)
    return np.interp(L, [0, 1], [0, 1000])

def find_finger_tip(processed):
    if processed.multi_hand_landmarks:
        hand_landmarks = processed.multi_hand_landmarks[0]
        return hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]  # Index finger tip

    return None

def move_mouse(index_finger_tip):
    if index_finger_tip is not None:
        x = int(index_finger_tip.x * screen_width)
        y = int(index_finger_tip.y * screen_height)
        pyautogui.moveTo(x, y)

def is_left_click(landmarks_list, thumb_index_distance):
    return (get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 50 and
            get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) > 90 and
            thumb_index_distance > 50)

def is_right_click(landmarks_list, thumb_index_distance):
    return (get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) > 90 and
            get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 50 and
            thumb_index_distance > 50)

def is_double_click(landmarks_list, thumb_index_distance):
    return (get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 50 and
            get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 50 and
            thumb_index_distance > 50)

def is_screenshot(landmarks_list, thumb_index_distance):
    return (get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 50 and
            get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 50 and
            thumb_index_distance < 50)

def detect_gestures(frame, landmarks_list, processed):
    if len(landmarks_list) >= 21:
        index_finger_tip = find_finger_tip(processed)
        thumb_index_distance = get_distance([landmarks_list[4], landmarks_list[5]]) # Thumb tip and index finger base

        if thumb_index_distance < 50 and get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) > 90:
            move_mouse(index_finger_tip)

        # Left Click
        elif is_left_click(landmarks_list, thumb_index_distance):
            mouse.press(Button.left)
            mouse.release(Button.left)
            cv2.putText(frame, "Left Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Right Click
        elif is_right_click(landmarks_list, thumb_index_distance):
            mouse.press(Button.right)
            mouse.release(Button.right)
            cv2.putText(frame, "Right Click", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Double Click
        elif is_double_click(landmarks_list, thumb_index_distance):
            pyautogui.doubleClick()
            cv2.putText(frame, "Double Click", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Screenshot
        # elif is_screenshot(landmarks_list, thumb_index_distance):

def main():
    cap =  cv2.VideoCapture(0)
    draw = mp.solutions.drawing_utils

    try:
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            frame  =  cv2.flip(frame, 1)
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed = hands.process(frameRGB)
            
            landmarks_list = []

            if processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0]
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

                for lm in hand_landmarks.landmark:
                    landmarks_list.append((lm.x, lm.y))

            detect_gestures(frame, landmarks_list, processed)

            cv2.imshow("Hand Tracking Virtual Mouse", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()