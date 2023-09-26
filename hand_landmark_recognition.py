import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import pygame.mixer
from gestures import *

pygame.mixer.init()


def play_sound_nonblocking(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()


guitar_1 = ("C:/Users/Thomas/ikt213g23h/prosjekt/VirtualVirtuoso/sounds/guitar-1.mp3")

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize MediaPipe Hands.
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)  # Use 0 for the default camera.

while cap.isOpened():
    ret, image = cap.read()

    if not ret:
        continue

    # Convert the BGR image to RGB.
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and get the hand landmarks.
    results = hands.process(image_rgb)

    # If hand landmarks are found, draw them.
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, landmarks, mp_hands.HAND_CONNECTIONS
            )
        if is_thumbs_up(landmarks):
            cv2.putText(image, "Thumbs Up!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        elif is_finger_up(landmarks):
            cv2.putText(image, "Point to God, our father", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            play_sound_nonblocking(guitar_1)

    cv2.imshow('MediaPipe Hands', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

