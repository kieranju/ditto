from enum import Enum
import collections

Point = collections.namedtuple('Point', ['x', 'y'])
Size = collections.namedtuple('Size', ['width', 'height'])

class MButton(Enum):
    LEFT, RIGHT = range(2)

class KKey(Enum):
    ESCAPE, NUM_ROW_1, NUM_ROW_2, NUM_ROW_3, NUM_ROW_4, NUM_ROW_5, NUM_ROW_6, NUM_ROW_7, NUM_ROW_8, NUM_ROW_9, NUM_ROW_0, HYPHEN, EQUALS, BACKSPACE, TAB, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, LEFT_BRACKET, RIGHT_BRACKET, ENTER, CONTROL, SEMICOLON, APOSTROPHE, GRAVE, SHIFT, BACK_SLASH, FORWARD_SLASH, COMMA, PERIOD, ALT, SPACE, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, UP, RIGHT, DOWN, LEFT = range(71)

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
