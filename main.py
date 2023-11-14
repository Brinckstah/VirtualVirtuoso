import mediapipe as mp
from mediapipe.tasks import python
import cv2
import time
import chord_strum
import config
import gesture_recognition
import single_string_chords
import queue
import threading

string_distance = 0.05
frame_queue = queue.Queue()



# Creates aliases for cleaner code
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

model_path = 'models/gesture_recognizer.task'


def playsound(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    try:
        if len(result.gestures) == 2:

            right_hand_gesture, left_hand_gesture = gesture_recognition.find_right_and_left_gesture(result)

            if right_hand_gesture == 'Pointing_Up':
                config.mode = 1

            elif right_hand_gesture == 'Victory':
                config.mode = 2
            if config.mode == 1:
                chord_strum.gesture_response(right_hand_gesture, left_hand_gesture, result)
            elif config.mode == 2:
                single_string_chords.tone_selector(result, left_hand_gesture)

    except Exception as e:
        print(e)
        pass


def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print('gesture recognition result: {}'.format(result))


def dummy_callback_function(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    pass

# Setting gesture recognizer options
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    num_hands=2,
    result_callback=dummy_callback_function
)


def gesture_recognition_and_audio_playback(frame_queue: queue.Queue):
    def process_result_callback(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
        playsound(result, output_image, timestamp_ms)

    options.result_callback = process_result_callback
    recognizer = GestureRecognizer.create_from_options(options)

    while True:
        if not frame_queue.empty():
            break
        first_frame = frame_queue.get()

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=first_frame)
        timestamp = int(time.time() * 1000)

        recognizer.recognize_async(mp_image, timestamp)


gesture_thread = threading.Thread(target=gesture_recognition_and_audio_playback, args=(frame_queue,))
gesture_thread.start()


y_threshold = 240

# Initialize OpenCV video capture
VideoCapture = cv2.VideoCapture(0)
VideoCapture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
VideoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


start_time = time.time()


while VideoCapture.isOpened():
    ret, frame = VideoCapture.read()

    # Checks if there is an issue with frame capture, and breaks if there is
    if not ret:
        break

    y, x, _ = frame.shape

        # Convert the BGR frame to RGB.
        # OpenCV reads image data in BGR, while mediaPipe expects RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_queue.put(frame_rgb)


    # Draw a horizontal line to facilitate dynamic right hand detection
    cv2.line(frame, (0, int(0.5 * y)), (int(x), int(0.5 * y)), (0, 255, 0), 1)
    cv2.line(frame, (0, int((0.5 + string_distance) * y)), (int(x), int((0.5 + string_distance) * y)), (0, 255, 0),
                 1)
    cv2.line(frame, (0, int((0.5 + 2 * string_distance) * y)), (int(x), int((0.5 + 2 * string_distance) * y)),
                 (0, 255, 0), 1)
    cv2.line(frame, (0, int((0.5 + 3 * string_distance) * y)), (int(x), int((0.5 + 3 * string_distance) * y)),
                 (0, 255, 0), 1)
    cv2.line(frame, (0, int((0.5 + 4 * string_distance) * y)), (int(x), int((0.5 + 4 * string_distance) * y)),
                 (0, 255, 0), 1)
    cv2.line(frame, (0, int((0.5 + 5 * string_distance) * y)), (int(x), int((0.5 + 5 * string_distance) * y)),
                 (0, 255, 0), 1)

        # Show the current frame
    cv2.imshow('Gesture Recognition', frame)

        # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the VideoCapture
VideoCapture.release()
cv2.destroyAllWindows()


#if __name__ == '__main__':
 #   app.main()
