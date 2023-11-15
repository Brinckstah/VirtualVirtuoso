import config
import sound
import gesture_recognition
from chord_strum import hello_from_the_other_side


def single_tone(left_hand_gesture, result):
    if gesture_recognition.is_picking(result):

        if not hello_from_the_other_side(result, "Index"):
            return

        y_coordinate = gesture_recognition.find_y_coordinate(result, "Index")

        if left_hand_gesture == 'Victory':
            sound.channel1.play(sound.C_2)

        elif left_hand_gesture == 'ILoveYou':
            sound.channel1.play(sound.D_3)

        elif gesture_recognition.is_pinky_up(result):
            sound.channel1.play(sound.C_3)

        elif left_hand_gesture == 'Closed_Fist':
            sound.channel1.play(sound.F_3)

        elif left_hand_gesture == 'Pointing_Up':
            sound.channel1.play(sound.C_4)

        elif left_hand_gesture == 'Open_Palm':
            sound.channel1.play(sound.D_4)

        elif gesture_recognition.is_gesture_L(result):
            sound.channel1.play(sound.E_5)

        else:
            print("Invalid chord")
            return

        config.last_played_y_coordinate = y_coordinate
