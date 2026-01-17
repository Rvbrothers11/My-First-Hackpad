# Import board pin definitions
import board

# KMK core
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

# KMK modules
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

# Main keyboard instance
keyboard = KMKKeyboard()

# Enable macros
macros = Macros()
keyboard.modules.append(macros)

# Enable rotary encoders
encoder = EncoderHandler()
keyboard.modules.append(encoder)

# --------------------
# PUSH BUTTONS
# --------------------
PINS = [
    board.D4,  # SW1
    board.D5,  # SW2
    board.D6,  # SW3
    board.D7,  # SW4
    board.D11, # ROT1 button
    board.D8,  # ROT2 button
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # using pull-ups
)

# --------------------
# ROTARY ENCODERS
# --------------------
encoder.pins = (
    (board.D1, board.D2),   # Encoder 1: A, B
    (board.D10, board.D9),  # Encoder 2: A, B
)

# Encoder actions (CW, CCW)
encoder.map = [
    (KC.VOLU, KC.VOLD),     # Encoder 1
    (KC.RIGHT, KC.LEFT),   # Encoder 2
]

# --------------------
# KEYMAP
# Order must match PINS list
# --------------------
keyboard.keymap = [
    [
        KC.A,                            # SW1
        KC.DELETE,                       # SW2
        KC.MACRO("Hello world!"),        # SW3
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),  # SW4
        KC.ENTER,                        # ROT1 button
        KC.ESCAPE,                      # ROT2 button
    ]
]

# Start KMK
if __name__ == '__main__':
    keyboard.go()
