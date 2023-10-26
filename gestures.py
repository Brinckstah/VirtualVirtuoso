import mediapipe as mp

mp_hands = mp.solutions.hands


def is_thumbs_up(hand_landmarks):
    # Get the landmarks for the thumb's tip and base.
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_base = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC]

    # Check if the thumb's tip is above its base.
    if thumb_tip.y < thumb_base.y:
        # Check if other fingers are not extended.
        for finger in [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                       mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                       mp_hands.HandLandmark.RING_FINGER_TIP,
                       mp_hands.HandLandmark.PINKY_TIP]:
            if hand_landmarks.landmark[finger].y < thumb_base.y:
                return False
        return True
    return False


def is_finger_up(hand_landmarks):
    # Get the landmarks for the index finger's tip and base.
    pointer_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    pointer_base = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]

    # Check if the index finger's tip is above its base.
    if pointer_tip.y < pointer_base.y:
        # Check if other fingers (excluding index) are not extended.
        for finger in [mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                       mp_hands.HandLandmark.RING_FINGER_TIP,
                       mp_hands.HandLandmark.PINKY_TIP]:
            if hand_landmarks.landmark[finger].y < pointer_base.y:
                return False
        return True
    return False


def is_finger_down(hand_landmarks):
    # Get the landmarks for the index finger's tip and base.
    pointer_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    pointer_base = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]

    # Check if the index finger's tip is below its base.
    if pointer_tip.y > pointer_base.y:  # Use '>' for down
        return True
    else:
        return False
