import single_string_chords
import sound
import gesture_recognition
import pygame
import config

pygame.mixer.init()


def hello_from_the_other_side(result, landmark):

    y_coordinate = gesture_recognition.find_y_coordinate(result, landmark)

    if config.last_played_y_coordinate > 0.5:
        if y_coordinate <= 0.5:
            return True
        else:
            return False

    elif config.last_played_y_coordinate <= 0.5:
        if y_coordinate > 0.5:
            return True
        else:
            return False


def up_or_down(y_coordinate):
    if y_coordinate < 0.5:
        return 0
    else:
        return 1


# Find response based on recognized result
def gesture_response(right_hand_gesture, left_hand_gesture, result):
    if right_hand_gesture == 'Thumb_Up':
        if not hello_from_the_other_side(result, "Thumb"):
            return
        y_coordinate = gesture_recognition.find_y_coordinate(result, "Thumb")
        direction = up_or_down(y_coordinate)
        if left_hand_gesture == 'Victory':
            if direction == 0:
                sound.channel1.play(sound.Cmaj_Chord)

            elif direction == 1:
                sound.channel1.play(sound.C_R)

        elif left_hand_gesture == 'ILoveYou':
            if direction == 0:
                sound.channel1.play(sound.Dmin_Chord)

            elif direction == 1:
                sound.channel1.play(sound.D_R)

        elif gesture_recognition.is_pinky_up(result):
            if direction == 0:
                sound.channel1.play(sound.Emin_Chord)

            elif direction == 1:
                sound.channel1.play(sound.E_R)

        elif left_hand_gesture == 'Closed_Fist':
            if direction == 0:
                sound.channel1.play(sound.Fmaj_Chord)

            elif direction == 1:
                sound.channel1.play(sound.F_R)

        elif left_hand_gesture == 'Pointing_Up':
            if direction == 0:
                sound.channel1.play(sound.Gmaj_Chord)

            elif direction == 1:
                sound.channel1.play(sound.G_R)

        elif left_hand_gesture == 'Open_Palm':
            if direction == 0:
                sound.channel1.play(sound.Amin_Chord)

            elif direction == 1:
                sound.channel1.play(sound.A_R)

        elif gesture_recognition.is_gesture_L(result):
            if direction == 0:
                sound.channel1.play(sound.Bdim_Chord)

            elif direction == 1:
                sound.channel1.play(sound.B_R)

        else:
            return
        config.last_played_y_coordinate = y_coordinate

    elif gesture_recognition.is_picking(result):
        if left_hand_gesture == 'Victory':
            single_string_chords.tone_selector(result, "C")

        elif left_hand_gesture == 'ILoveYou':
            single_string_chords.tone_selector(result, "D")

        elif gesture_recognition.is_pinky_up(result):
            single_string_chords.tone_selector(result, "E")

        elif left_hand_gesture == 'Closed_Fist':
            single_string_chords.tone_selector(result, "F")

        elif left_hand_gesture == 'Pointing_Up':
            single_string_chords.tone_selector(result, "G")

        elif left_hand_gesture == 'Open_Palm':
            single_string_chords.tone_selector(result, "A")

        elif gesture_recognition.is_gesture_L(result):
            single_string_chords.tone_selector(result, "B")

            """
        if left_hand_gesture == 'Victory':
            sound.play_sound(sound.C_Tone)
            last_played_y_coordinate = gesture_recognition.find_y_coordinate(result, "Index")

        elif left_hand_gesture == 'Thumb_Up':
            sound.play_sound(sound.D_Tone)
            last_played_y_coordinate = gesture_recognition.find_y_coordinate(result, "Index")

        elif left_hand_gesture == 'Thumb_Down':
            sound.play_sound(sound.E_Tone)
            last_played_y_coordinate = gesture_recognition.find_y_coordinate(result, "Index")

        elif left_hand_gesture == 'Pointing_Up':
            sound.play_sound(sound.F_Tone)
            last_played_y_coordinate = gesture_recognition.find_y_coordinate(result, "Index")

        elif left_hand_gesture == 'Open_Palm':
            sound.play_sound(sound.G_Tone)
            last_played_y_coordinate = gesture_recognition.find_y_coordinate(result, "Index")
            """
