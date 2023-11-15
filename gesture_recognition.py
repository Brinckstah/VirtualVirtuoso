def find_right_and_left_gesture(result):
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
