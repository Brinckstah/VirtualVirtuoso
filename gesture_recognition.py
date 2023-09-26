import mediapipe as mp
import cv2
import time
import pygame

pygame.mixer.init()


def play_sound(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()


# Find response based on recognized result
def gesture_response(result):
    if result.handedness[0][0].category_name == "Right":
        hand = 0
    elif result.handedness[0][0].category_name == "Left":
        hand = 1
    # TODO: Some sort of error handling?
    else:
        return

    gesture_name = result.gestures[0][0].category_name

    if gesture_name == 'Victory' and hand == 0:
        play_sound(guitar_1)




# Creates aliases for cleaner code
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode


model_path = 'C:/Users/Thomas/ikt213g23h/prosjekt/VirtualVirtuoso/models/gesture_recognizer.task'
guitar_1 = 'C:/Users/Thomas/ikt213g23h/prosjekt/VirtualVirtuoso/sounds/guitar-1.mp3'


def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print('gesture recognition result: {}'.format(result))


def playsound(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    # Check if gestures are detected in the result
    if result.gestures:
        # Access the first detected gesture's category_name
        gesture_response(result)


# Setting gesture recognizer options
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=playsound)


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
