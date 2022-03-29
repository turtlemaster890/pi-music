from mpmath import mp
import math
import musicalbeeps
digits = 50
mp.dps = digits
piRemaining = mp.pi

player = musicalbeeps.Player(volume = 0.3, mute_output = False)

def mapIntToNote(value):
    if value == 1:
        return "C"
    if value == 2:
        return "D"
    if value == 3:
        return "E"
    if value == 4:
        return "F"
    if value == 5:
        return "G"
    if value == 6:
        return "A"
    if value == 7:
        return "B"
    if value == 8:
        return "C5"
    if value == 9:
        return "D5"
    if value == 0:
        return "E5"

for i in range(digits):
    digit = math.floor(piRemaining)
    note = mapIntToNote(digit)
    player.play_note(note, 0.25)
    print(i)
    piRemaining -= digit
    piRemaining *= 10

