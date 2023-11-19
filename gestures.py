# New gesture. Checks if the index finger is extended to the right of the hand.
def is_picking(result):
    try:
        index_tip = None
        index_dip = None
        index_pip = None
        thumb_tip = None
        middle_finger_pip = None
        hand = None

        if result.handedness[0][0].category_name == "Right":
            index_tip = result.hand_landmarks[0][8].x
            index_dip = result.hand_landmarks[0][7].x
            index_pip = result.hand_landmarks[0][6].x
            thumb_tip = result.hand_landmarks[0][4].x
            middle_finger_pip = result.hand_landmarks[0][10].x
            hand = 0

        elif result.handedness[0][0].category_name == "Left":
            index_tip = result.hand_landmarks[1][8].x
            index_dip = result.hand_landmarks[1][7].x
            index_pip = result.hand_landmarks[1][6].x
            thumb_tip = result.hand_landmarks[1][4].x
            middle_finger_pip = result.hand_landmarks[1][10].x
            hand = 1

        if (index_tip > result.hand_landmarks[hand][6].x and
                index_tip > index_dip and
                index_tip > index_pip and
                index_tip > thumb_tip and
                index_tip > middle_finger_pip and
                index_tip > result.hand_landmarks[hand][12].x and
                index_tip > result.hand_landmarks[hand][16].x and
                index_tip > result.hand_landmarks[hand][20].x):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


# New gesture. Checks if the index finger and the thumb are extended, forming an L.
def is_gesture_L(result):
    try:
        index_tip_y = None
        index_dip_y = None
        thumb_tip_x = None
        thumb_tip_y = None
        thumb_ip_x = None
        hand = None

        if result.handedness[0][0].category_name == "Left":
            index_tip_y = result.hand_landmarks[0][8].y
            thumb_tip_x = result.hand_landmarks[0][4].x
            # Included check for thumb tip vs index finger tip
            thumb_tip_y = result.hand_landmarks[0][4].y
            thumb_ip_x = result.hand_landmarks[0][3].x
            hand = 0

        elif result.handedness[0][0].category_name == "Right":
            index_tip_y = result.hand_landmarks[1][8].y
            thumb_tip_x = result.hand_landmarks[1][4].x
            thumb_tip_y = result.hand_landmarks[1][4].y
            thumb_ip_x = result.hand_landmarks[1][3].x
            hand = 1

        if not (index_tip_y < result.hand_landmarks[hand][6].y and
                index_tip_y < result.hand_landmarks[hand][7].y and
                index_tip_y < result.hand_landmarks[hand][12].y and
                index_tip_y < result.hand_landmarks[hand][16].y and
                index_tip_y < result.hand_landmarks[hand][20].y and
                thumb_tip_y > result.hand_landmarks[hand][6].y):
            return False

        if not (thumb_tip_x < thumb_ip_x):
            return False

        return True

    except Exception as e:
        print(e)
        return False


# New gesture. Checks if the pinky is extended and the other fingers are not
def is_pinky_up(result):
    try:
        index_tip_y = None
        middle_tip_y = None
        ring_tip_y = None
        pinky_tip_y = None
        thumb_tip_y = None

        if result.handedness[0][0].category_name == "Left":
            thumb_tip_y = result.hand_landmarks[0][4].y
            index_tip_y = result.hand_landmarks[0][8].y
            middle_tip_y = result.hand_landmarks[0][12].y
            ring_tip_y = result.hand_landmarks[0][16].y
            pinky_tip_y = result.hand_landmarks[0][20].y

        elif result.handedness[0][0].category_name == "Right":
            thumb_tip_y = result.hand_landmarks[1][4].y
            index_tip_y = result.hand_landmarks[1][8].y
            middle_tip_y = result.hand_landmarks[1][12].y
            ring_tip_y = result.hand_landmarks[1][16].y
            pinky_tip_y = result.hand_landmarks[1][20].y

        if not (pinky_tip_y < thumb_tip_y and
                pinky_tip_y < index_tip_y and
                pinky_tip_y < middle_tip_y and
                pinky_tip_y < ring_tip_y):
            return False

        return True

    except Exception as e:
        print(e)
        return False
