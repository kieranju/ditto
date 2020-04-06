from enum import Enum
import collections

Point = collections.namedtuple('Point', ['x', 'y'])
Size = collections.namedtuple('Size', ['width', 'height'])

class MButton(Enum):
    LEFT = 1
    RIGHT = 2

class KKey(Enum):
    ESCAPE = 1
    NUM_ROW_1 = 2
    NUM_ROW_2 = 3
    NUM_ROW_3 = 4
    NUM_ROW_4 = 5
    NUM_ROW_5 = 6
    NUM_ROW_6 = 7
    NUM_ROW_7 = 8
    NUM_ROW_8 = 9
    NUM_ROW_9 = 10
    NUM_ROW_0 = 11
    HYPHEN = 12
    EQUALS = 13
    BACKSPACE = 14
    TAB = 15
    A = 16
    B = 17
    C = 18
    D = 19
    E = 20
    F = 21
    G = 22
    H = 23
    I = 24
    J = 25
    K = 26
    L = 27
    M = 28
    N = 29
    O = 30
    P = 31
    Q = 32
    R = 33
    S = 34
    T = 35
    U = 36
    V = 37
    W = 38
    X = 39
    Y = 40
    Z = 41
    LEFT_BRACKET = 42
    RIGHT_BRACKET = 43
    ENTER = 44
    CONTROL = 45
    SEMICOLON = 46
    APOSTROPHE = 47
    GRAVE = 48
    SHIFT = 49
    BACK_SLASH = 50
    FORWARD_SLASH = 51
    COMMA = 52
    PERIOD = 53
    ALT = 54
    SPACE = 55
    F1 = 56
    F2 = 57
    F3 = 58
    F4 = 59
    F5 = 60
    F6 = 61
    F7 = 62
    F8 = 63
    F9 = 64
    F10 = 65
    F11 = 66
    F12 = 67
    UP = 68
    RIGHT = 69
    DOWN = 70
    LEFT = 71

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

    def m_tap(self, button: MButton):
        """Press and release the specified mouse button."""
        pass

    def k_press(self, key: KKey):
        """Press the specified keyboard key."""
        pass

    def k_release(self, key: KKey):
        """Release the specified keyboard key."""
        pass

    def k_tap(self, button: KKey):
        """Press and release the specified keyboard key."""
        pass

__all__ = ['MButton', 'KKey', 'OperatorInterface']
