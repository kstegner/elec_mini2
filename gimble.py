import msvcrt
import hellousb
import time

hello = hellousb.hellousb()

KEY_W = chr(119)
KEY_A = chr(97)
KEY_S = chr(115)
KEY_D = chr(100)

TILT_VAL = 0
PAN_VAL =0

INC_VAL = 2**9

MAX = 2**16 - 1
MIN = 0

while True:
	if msvcrt.kbhit():
		key = msvcrt.getch()

		if key == KEY_W:
			TILT_VAL += INC_VAL
		elif key == KEY_S:
			TILT_VAL -= INC_VAL
		elif key == KEY_D:
			PAN_VAL -= INC_VAL
		elif key == KEY_A:
			PAN_VAL += INC_VAL
	if PAN_VAL > MAX:
		PAN_VAL = MAX
	if PAN_VAL < MIN:
		PAN_VAL = MIN
	if TILT_VAL > MAX:
		TILT_VAL = MAX
	if TILT_VAL < MIN:
		TILT_VAL = MIN
		
	hello.set_vals(PAN_VAL, TILT_VAL)