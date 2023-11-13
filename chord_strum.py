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


# Find response based on recognized result
def gesture_response(right_hand_gesture, left_hand_gesture, result):
    if right_hand_gesture == 'Thumb_Up':
        if not hello_from_the_other_side(result, "Thumb"):
            return
        if left_hand_gesture == 'Victory':
            if gesture_recognition.up_or_down_strum() == 0:
                sound.channel1.play(sound.Cmaj_Chord)

            elif gesture_recognition.up_or_down_strum() == 1:
                sound.channel1.play(sound.C_R)

            config.last_played_y_coordinate = gesture_recognition.find_y_coordinate(result, "Thumb")

        elif left_hand_gesture == 'Love_You_Gesture':
            if gesture_recognition.up_or_down_strum() == 0:
                sound.channel1.play(sound.Dmin_Chord)

            elif gesture_recognition.up_or_down_strum() == 1:
                sound.channel1.play(sound.D_R)

            config.last_played_y_coordinate = gesture_recognition.find_y_coordinate(result, "Thumb")

        elif left_hand_gesture == 'Thumb_Down':
            if gesture_recognition.up_or_down_strum() == 0:
                sound.channel1.play(sound.Emin_Chord)

            elif gesture_recognition.up_or_down_strum() == 1:
                sound.channel1.play(sound.E_R)

            config.last_played_y_coordinate = gesture_recognition.find_y_coordinate(result, "Thumb")

        elif left_hand_gesture == 'Thumb_Up':
            if gesture_recognition.up_or_down_strum() == 0:
                sound.channel1.play(sound.Fmaj_Chord)

            elif gesture_recognition.up_or_down_strum() == 1:
                sound.channel1.play(sound.F_R)

            config.last_played_y_coordinate = gesture_recognition.find_y_coordinate(result, "Thumb")

        elif left_hand_gesture == 'Pointing_Up':
            if gesture_recognition.up_or_down_strum() == 0:
                sound.channel1.play(sound.Gmaj_Chord)

            elif gesture_recognition.up_or_down_strum() == 1:
                sound.channel1.play(sound.G_R)

            config.last_played_y_coordinate = gesture_recognition.find_y_coordinate(result, "Thumb")

        elif left_hand_gesture == 'Open_Palm':
            if gesture_recognition.up_or_down_strum() == 0:
                sound.channel1.play(sound.Amin_Chord)

            elif gesture_recognition.up_or_down_strum() == 1:
                sound.channel1.play(sound.A_R)

            config.last_played_y_coordinate = gesture_recognition.find_y_coordinate(result, "Thumb")

    elif gesture_recognition.is_picking(result):
        if left_hand_gesture == 'Victory':
            single_string_chords.tone_selector(result, "C")

        elif left_hand_gesture == 'Thumb_Up':
            single_string_chords.tone_selector(result, "D")

        elif left_hand_gesture == 'Thumb_Down':
            single_string_chords.tone_selector(result, "E")

        elif left_hand_gesture == 'Pointing_Up':
            single_string_chords.tone_selector(result, "F")

        elif left_hand_gesture == 'Open_Palm':
            single_string_chords.tone_selector(result, "G")

        elif left_hand_gesture == 'Love_You_Gesture':
            single_string_chords.tone_selector(result, "A")

        elif left_hand_gesture == 'Closed_Fist':
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