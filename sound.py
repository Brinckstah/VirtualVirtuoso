import pygame

pygame.mixer.init()

Cmaj_Chord = pygame.mixer.Sound('sounds/Cmaj.mp3')
Dmin_Chord = pygame.mixer.Sound('sounds/Dmin.mp3')
Emin_Chord = pygame.mixer.Sound('sounds/Emin.mp3')
Fmaj_Chord = pygame.mixer.Sound('sounds/Fmaj.mp3')
Gmaj_Chord = pygame.mixer.Sound('sounds/Gmaj.mp3')
Amin_Chord = pygame.mixer.Sound('sounds/Amin.mp3')
Bdim_Chord = pygame.mixer.Sound('sounds/Bdim.mp3')

C_R = pygame.mixer.Sound('sounds/C_R.mp3')
D_R = pygame.mixer.Sound('sounds/D_R.mp3')
E_R = pygame.mixer.Sound('sounds/E_R.mp3')
F_R = pygame.mixer.Sound('sounds/F_R.mp3')
G_R = pygame.mixer.Sound('sounds/G_R.mp3')
A_R = pygame.mixer.Sound('sounds/A_R.mp3')
B_R = pygame.mixer.Sound('sounds/B_R.mp3')

C_2 = pygame.mixer.Sound('sounds/C_2.mp3')
C_3 = pygame.mixer.Sound('sounds/C_3.mp3')
C_4 = pygame.mixer.Sound('sounds/C_4.mp3')
C_5 = pygame.mixer.Sound('sounds/C_5.mp3')
C_6 = pygame.mixer.Sound('sounds/C_6.mp3')
D_3 = pygame.mixer.Sound('sounds/D_3.mp3')
D_4 = pygame.mixer.Sound('sounds/D_4.mp3')
D_5 = pygame.mixer.Sound('sounds/D_5.mp3')
D_6 = pygame.mixer.Sound('sounds/D_6.mp3')
E_1 = pygame.mixer.Sound('sounds/E_1.mp3')
E_2 = pygame.mixer.Sound('sounds/E_2.mp3')
E_5 = pygame.mixer.Sound('sounds/E_5.mp3')
F_3 = pygame.mixer.Sound('sounds/F_3.mp3')
G_1 = pygame.mixer.Sound('sounds/G_1.mp3')
G_6 = pygame.mixer.Sound('sounds/G_6.mp3')
A_2 = pygame.mixer.Sound('sounds/A_2.mp3')
B_4 = pygame.mixer.Sound('sounds/B_4.mp3')
mute_1 = pygame.mixer.Sound('sounds/1st muted.mp3')
mute_2 = pygame.mixer.Sound('sounds/2nd muted.mp3')
mute_last = pygame.mixer.Sound('sounds/last muted.mp3')


chord_tones = {
    'C': [mute_1, C_2, C_3, C_4, C_5, C_6],
    'D': [mute_1, mute_2, D_3, D_4, D_5, D_6],
    'E': [E_1, E_2, C_3, C_4, E_5, C_6],
    'F': [mute_1, mute_2, F_3, D_4, C_5, D_6],
    'G': [G_1, E_2, D_3, C_4, D_5, G_6],
    'A': [mute_1, A_2, C_3, D_4, C_5, C_6],
    'B': [mute_1, E_2, F_3, B_4, D_5, mute_last]
}

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)
channel5 = pygame.mixer.Channel(4)
channel6 = pygame.mixer.Channel(5)
