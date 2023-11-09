import mediapipe as mp
from mediapipe.tasks import python
import cv2
import time
import pygame


pygame.mixer.init()


last_played_y_coordinate = -1


def play_sound(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()


def find_right_and_left_gesture(result):
    # TODO: Verify that indexation is correct
    right_hand_gesture = None
    left_hand_gesture = None

    first_gesture = result.gestures[0][0].category_name
    second_gesture = result.gestures[1][0].category_name

    if result.handedness[0][0].category_name == "Right":
        # right_hand = 0
        right_hand_gesture = first_gesture
        # left_hand = 1
        left_hand_gesture = second_gesture

    elif result.handedness[0][0].category_name == "Left":
        # left_hand = 0
        left_hand_gesture = first_gesture
        # right_hand = 1
        right_hand_gesture = second_gesture

    return right_hand_gesture, left_hand_gesture


def find_y_coordinate(result, landmark):
    y_coordinate = 0
    index = 0

    if landmark == "Thumb":
        index = 4
    elif landmark == "Index":
        index = 8

    if result.handedness[0][0].category_name == "Right":
        y_coordinate = result.hand_landmarks[0][index].y
    elif result.handedness[0][0].category_name == "Left":
        y_coordinate = result.hand_landmarks[1][index].y

    return y_coordinate


def is_picking(result):
    try:
        index_tip = None
        hand = None

        if result.handedness[0][0].category_name == "Right":
            index_tip = result.hand_landmarks[0][8].x
            hand = 0

        elif result.handedness[0][0].category_name == "Left":
            index_tip = result.hand_landmarks[1][8].x
            hand = 1

        if (index_tip > result.hand_landmarks[hand][6].x and
                index_tip > result.hand_landmarks[hand][12].x and
                index_tip > result.hand_landmarks[hand][16].x and
                index_tip > result.hand_landmarks[hand][20].x):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def hello_from_the_other_side(result, landmark):
    y_coordinate = find_y_coordinate(result, landmark)

    if last_played_y_coordinate > 0.5:
        if y_coordinate <= 0.5:
            return True
        else:
            return False

    elif last_played_y_coordinate <= 0.5:
        if y_coordinate > 0.5:
            return True
        else:
            return False


def up_or_down_strum():
    if last_played_y_coordinate > 0.5:
        return 0
    else:
        return 1


# Find response based on recognized result
def gesture_response(result):
    global last_played_y_coordinate
    right_hand_gesture, left_hand_gesture = find_right_and_left_gesture(result)

    # Hvis høyre hånd er closed fist, akkord
    if right_hand_gesture == 'Thumb_Up':
        if not hello_from_the_other_side(result, "Thumb"):
            return
        if left_hand_gesture == 'Victory':

            #if up_or_down_strum() == 0:
            play_sound(C_Chord)

            #elif up_or_down_strum() == 1:
            #    print("Up")

            last_played_y_coordinate = find_y_coordinate(result, "Thumb")

        elif left_hand_gesture == 'Thumb_Up':
            play_sound(G_Chord)
            last_played_y_coordinate = find_y_coordinate(result, "Thumb")

        elif left_hand_gesture == 'Thumb_Down':
            play_sound(F_Chord)
            last_played_y_coordinate = find_y_coordinate(result, "Thumb")

        elif left_hand_gesture == 'Pointing_Up':
            play_sound(Am_Chord)
            last_played_y_coordinate = find_y_coordinate(result, "Thumb")

        elif left_hand_gesture == 'Open_Palm':
            play_sound(Bdim_Chord)
            last_played_y_coordinate = find_y_coordinate(result, "Thumb")

    elif is_picking(result):
        if not hello_from_the_other_side(result, "Index"):
            return

        if left_hand_gesture == 'Victory':
            play_sound(C_Tone)
            last_played_y_coordinate = find_y_coordinate(result, "Index")

        elif left_hand_gesture == 'Thumb_Up':
            play_sound(D_Tone)
            last_played_y_coordinate = find_y_coordinate(result, "Index")

        elif left_hand_gesture == 'Thumb_Down':
            play_sound(E_Tone)
            last_played_y_coordinate = find_y_coordinate(result, "Index")

        elif left_hand_gesture == 'Pointing_Up':
            play_sound(F_Tone)
            last_played_y_coordinate = find_y_coordinate(result, "Index")

        elif left_hand_gesture == 'Open_Palm':
            play_sound(G_Tone)
            last_played_y_coordinate = find_y_coordinate(result, "Index")


# Creates aliases for cleaner code
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode


model_path = 'models/gesture_recognizer.task'
C_Chord = 'sounds/Cmaj.mp3'
Dmin_Chord = 'sounds/Dmin.mp3'
Emin_Chord = 'sounds/Emin.mp3'
F_Chord = 'sounds/Fmaj.mp3'
G_Chord = 'sounds/Gmaj.mp3'
Am_Chord = 'sounds/Amin.mp3'
Bdim_Chord = 'sounds/Bdim.mp3'

C_Tone = 'sounds/C.mp3'
D_Tone = 'sounds/D.mp3'
E_Tone = 'sounds/E.mp3'
F_Tone = 'sounds/F.mp3'
G_Tone = 'sounds/G.mp3'


def playsound(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    # print('gesture recognition result: {}'.format(result))
    if len(result.gestures) == 2:
        gesture_response(result)


def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print('gesture recognition result: {}'.format(result))


# Setting gesture recognizer options
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=playsound,
    num_hands=2
)


y_threshold = 240

# Initialize OpenCV video capture
VideoCapture = cv2.VideoCapture(0)

start_time = time.time()

with GestureRecognizer.create_from_options(options) as recognizer:
    while VideoCapture.isOpened():
        ret, frame = VideoCapture.read()

        # Checks if there is an issue with frame capture, and breaks if there is
        if not ret:
            break

        y, x, channels = frame.shape

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

        # Draw a horizontal line to facilitate dynamic right hand detection
        cv2.line(frame, (0, int(0.5*y)), (int(x), int(0.5*y)), (0, 255, 0), 3)

        # Show the current frame
        cv2.imshow('Gesture Recognition', frame)

        # Press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Close the VideoCapture
VideoCapture.release()
cv2.destroyAllWindows()
