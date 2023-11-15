import config
import gesture_recognition
import sound


def tone_selector(result, current_chord):
    string_distance = 0.05
    y_coordinate = gesture_recognition.find_y_coordinate(result, "Index")

    # Check if the y_coordinate has crossed a string boundary since the last check
    if y_coordinate < 0.5:
        if config.last_played_y_coordinate >= 0.5:
            sound.channel1.play(sound.chord_tones[current_chord][0])

    elif y_coordinate < 0.5 + string_distance:
        if config.last_played_y_coordinate <= 0.5:
            sound.channel1.play(sound.chord_tones[current_chord][0])

        elif config.last_played_y_coordinate >= 0.5 + string_distance:
            sound.channel2.play(sound.chord_tones[current_chord][1])

    elif y_coordinate < 0.5 + 2 * string_distance:
        if config.last_played_y_coordinate <= 0.5 + string_distance:
            sound.channel2.play(sound.chord_tones[current_chord][1])

        elif config.last_played_y_coordinate >= 0.5 + 2 * string_distance:
            sound.channel3.play(sound.chord_tones[current_chord][2])

    elif y_coordinate < 0.5 + 3 * string_distance:
        if config.last_played_y_coordinate < 0.5 + 2 * string_distance:
            sound.channel3.play(sound.chord_tones[current_chord][2])

        elif config.last_played_y_coordinate >= 0.5 + 3 * string_distance:
            sound.channel4.play(sound.chord_tones[current_chord][3])

    elif y_coordinate < 0.5 + 4 * string_distance:
        if config.last_played_y_coordinate < 0.5 + 3 * string_distance:
            sound.channel4.play(sound.chord_tones[current_chord][3])

        elif config.last_played_y_coordinate >= 0.5 + 4 * string_distance:
            sound.channel5.play(sound.chord_tones[current_chord][4])

    elif y_coordinate < 0.5 + 5 * string_distance:
        if config.last_played_y_coordinate < 0.5 + 4 * string_distance:
            sound.channel5.play(sound.chord_tones[current_chord][4])

        elif config.last_played_y_coordinate >= 0.5 + 5 * string_distance:
            sound.channel6.play(sound.chord_tones[current_chord][5])
    elif y_coordinate >= 0.5 + 5 * string_distance:
        if config.last_played_y_coordinate < 0.5 + 5 * string_distance:
            sound.channel6.play(sound.chord_tones[current_chord][5])

    else:
        return

    # Update the last played y-coordinate.
    config.last_played_y_coordinate = y_coordinate
