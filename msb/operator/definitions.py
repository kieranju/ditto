from enum import Enum
import collections

Point = collections.namedtuple('Point', ['x', 'y'])
Size = collections.namedtuple('Size', ['width', 'height'])

class MButton(Enum):
    LEFT, RIGHT = range(2)

class KKey(Enum):
    TAB, SPACE, APOSTROPHE, HYPHEN, NUM_ROW_0, NUM_ROW_1, NUM_ROW_2, NUM_ROW_3, NUM_ROW_4, NUM_ROW_5, NUM_ROW_6, NUM_ROW_7, NUM_ROW_8, NUM_ROW_9, SEMICOLON, EQUALS, LEFT_BRACKET, BACK_SLASH, RIGHT_BRACKET, GRAVE, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, BACKSPACE, CONTROL, ENTER, SHIFT, FORWARD_SLASH, COMMA, PERIOD, ALT, ESCAPE, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, UP, RIGHT, DOWN, LEFT = range(71)

key_dictionary = {
    ' ': KKey.SPACE,
    '.': KKey.PERIOD,
    ',': KKey.COMMA,
    '\'': KKey.APOSTROPHE,
    '-': KKey.HYPHEN,
    '=': KKey.EQUALS,
    'a': KKey.A,
    'b': KKey.B,
    'c': KKey.C,
    'd': KKey.D,
    'e': KKey.E,
    'f': KKey.F,
    'g': KKey.G,
    'h': KKey.H,
    'i': KKey.I,
    'j': KKey.J,
    'k': KKey.K,
    'l': KKey.L,
    'm': KKey.M,
    'n': KKey.N,
    'o': KKey.O,
    'p': KKey.P,
    'q': KKey.Q,
    'r': KKey.R,
    's': KKey.S,
    't': KKey.T,
    'u': KKey.U,
    'v': KKey.V,
    'w': KKey.W,
    'x': KKey.X,
    'y': KKey.Y,
    'z': KKey.Z,
    '0': KKey.NUM_ROW_0,
    '1': KKey.NUM_ROW_1,
    '2': KKey.NUM_ROW_2,
    '3': KKey.NUM_ROW_3,
    '4': KKey.NUM_ROW_4,
    '5': KKey.NUM_ROW_5,
    '6': KKey.NUM_ROW_6,
    '7': KKey.NUM_ROW_7,
    '8': KKey.NUM_ROW_8,
    '9': KKey.NUM_ROW_9,
}

class OperatorInterface:
    def s_size(self) -> Size:
        """Get the screen size."""
        pass

    def m_location_get(self) -> Point:
        """Get the mouse coordinates."""
        pass

    def m_location_set(self, x: int, y: int):
        """Set the mouse coordinates."""
        pass

    def m_press(self, button: MButton):
        """Press the specified mouse button."""
        pass

    def m_release(self, button: MButton):
        """Release the specified mouse button."""
        pass

    def k_press(self, key: KKey):
        """Press the specified keyboard key."""
        pass

    def k_release(self, key: KKey):
        """Release the specified keyboard key."""
        pass
