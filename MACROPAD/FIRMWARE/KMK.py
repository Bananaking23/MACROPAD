#this are examples, i will change if i get it as i find it easier 
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation, DiodeScanner
from kmk.extensions.led import RGB, AnimationModes
import board

keyboard = KMKKeyboard()

#matrix
rows = [board.d1, board.d2, board.d3]
cols = [board.d8, board.d9, board.d10]

scanner = DiodeScanner(rows=rows, cols=cols, diode_orientation=DiodeOrientation.COL2ROW)
keyboard.scanner = scanner

#led
keyboard.rgb = RGB(
    pixel_pin=board.GP6,
    num_pixels=2,
)
keyboard.rgb.pixels[0] = (255, 0, 0)  
keyboard.rgb.pixels[1] = (0, 0, 255)  
keyboard.rgb.show()

#capacitive touch button
CAP_TOUCH_PIN = board.A3  # GPIO29 / A3
from kmk.extensions.capacitive import CapTouch

cap_touch = CapTouch(pin=CAP_TOUCH_PIN)
keyboard.extensions.append(cap_touch)

#layers
keyboard.keymap = [               
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I
    ],
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I
    ]
]

#start it 
if __name__ == "__main__":
    keyboard.go()
