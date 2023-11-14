import config


def up_or_down_strum():
    if config.last_played_y_coordinate > 0.5:
        return 0
    else:
        return 1


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


def is_gesture_L(result):
    try:
        index_tip_y = None
        thumb_tip_x = None
        thumb_ip_x = None
        hand = None

        if result.handedness[0][0].category_name == "Right":
            index_tip_y = result.hand_landmarks[0][8].y
            thumb_tip_x = result.hand_landmarks[0][4].x
            thumb_ip_x = result.hand_landmarks[0][3].x
            hand = 0

            print(index_tip_y, thumb_tip_x, thumb_ip_x)

        elif result.handedness[0][0].category_name == "Left":
            index_tip_y = result.hand_landmarks[1][8].y
            thumb_tip_x = result.hand_landmarks[1][4].x
            thumb_ip_x = result.hand_landmarks[1][3].x
            hand = 1

            print(index_tip_y, thumb_tip_x, thumb_ip_x, "left")

        if not (index_tip_y < result.hand_landmarks[hand][6].y and
                index_tip_y < result.hand_landmarks[hand][12].y and
                index_tip_y < result.hand_landmarks[hand][16].y and
                index_tip_y < result.hand_landmarks[hand][20].y):
            return False

        if not (thumb_tip_x < thumb_ip_x):
            return False

        return True

    except Exception as e:
        print(e)
        return False
