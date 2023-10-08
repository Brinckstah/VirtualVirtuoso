import mediapipe as mp
import cv2
import time
import pygame

time_of_last_gesture = 0
# Todo adjustable waiting time?
waiting_time_between_gestures = 2.0

pygame.mixer.init()


def play_sound(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()


# Find response based on recognized result
def gesture_response(result):
    global time_of_last_gesture
    current_time = time.time()

    # If the elapsed time is less than the cooldown duration, do nothing
    if current_time - time_of_last_gesture < waiting_time_between_gestures:
        return

    right_hand_gesture = None
    left_hand_gesture = None

    first_gesture = result.gestures[0][0].category_name
    second_gesture = result.gestures[1][0].category_name

    if result.handedness[0][0].index == 0:
        # right_hand = 0
        right_hand_gesture = first_gesture
        # left_hand = 1
        left_hand_gesture = second_gesture
    elif result.handedness[1][0].index == 1:
        # left_hand = 0
        left_hand_gesture = first_gesture
        # right_hand = 1
        right_hand_gesture = second_gesture

    # Hvis høyre hånd er closed fist, akkord
    if right_hand_gesture == 'Closed_Fist':
        print("hello")
        if left_hand_gesture != 'Closed_Fist':
            if left_hand_gesture == 'Victory':
                play_sound(C_Chord)

            elif left_hand_gesture == 'Thumb_Up':
                play_sound(D_Chord)

            elif left_hand_gesture == 'Thumb_Down':
                play_sound(E_Chord)

            elif left_hand_gesture == 'Pointing_Up':
                play_sound(F_Chord)

            elif left_hand_gesture == 'Open_Palm':
                play_sound(G_Chord)

            time_of_last_gesture = current_time


    # Hvis høyre hånd er open palm, tone
    elif right_hand_gesture == 'Open_Palm':
        print("open")
        if left_hand_gesture != 'Closed_Fist':
            if left_hand_gesture == 'Victory':
                play_sound(C_Tone)

            elif left_hand_gesture == 'Thumb_Up':
                play_sound(D_Tone)

            elif left_hand_gesture == 'Thumb_Down':
                play_sound(E_Tone)

            elif left_hand_gesture == 'Pointing_Up':
                play_sound(F_Tone)

            elif left_hand_gesture == 'Open_Palm':
                play_sound(G_Tone)

            time_of_last_gesture = current_time


# Creates aliases for cleaner code
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode


model_path = 'models/gesture_recognizer.task'
C_Chord = 'sounds/C-Chord.mp3'
D_Chord = 'sounds/D-Chord.mp3'
E_Chord = 'sounds/E-Chord.mp3'
F_Chord = 'sounds/F-Chord.mp3'
G_Chord = 'sounds/G-Chord.mp3'

C_Tone = 'sounds/C.mp3'
D_Tone = 'sounds/D.mp3'
E_Tone = 'sounds/E.mp3'
F_Tone = 'sounds/F.mp3'
G_Tone = 'sounds/G.mp3'


def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print('gesture recognition result: {}'.format(result))


def playsound(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    # print('gesture recognition result: {}'.format(result))
    if len(result.gestures) == 2:
        gesture_response(result)


# Setting gesture recognizer options
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=playsound,
    num_hands=2
)


# Initialize OpenCV video capture
VideoCapture = cv2.VideoCapture(0)

start_time = time.time()

with GestureRecognizer.create_from_options(options) as recognizer:
    while VideoCapture.isOpened():
        ret, frame = VideoCapture.read()

        # Checks if there is an issue with frame capture, and breaks if there is
        if not ret:
            break

        # Convert the BGR frame to RGB.
        # OpenCV reads image data in BGR, while mediaPipe expects RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create mediaPipe image object.
        # SRGB = standard RGB
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

        # Calculate frame timestamp for recognized
        frame_timestamp_ms = int((time.time() - start_time) * 1000)

        # Recognize gesture
        recognizer.recognize_async(mp_image, frame_timestamp_ms)

        # Show the current frame
        cv2.imshow('Gesture Recognition', frame)

        # Press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Close the VideoCapture
VideoCapture.release()
cv2.destroyAllWindows()