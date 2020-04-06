# from msb.definitions import pyautogui
# from msb.operator.definitions import KKey, MButton, OperatorInterface, Size, Point

# import ctypes
# import math

# send_input = ctypes.windll.user32.SendInput
# set_cursor_pos = ctypes.windll.user32.SetCursorPos

# PUL = ctypes.POINTER(ctypes.c_ulong)
# class KeyBdInput(ctypes.Structure):
#     _fields_ = [
#         ("wVk", ctypes.c_ushort),
#         ("wScan", ctypes.c_ushort),
#         ("dwFlags", ctypes.c_ulong),
#         ("time", ctypes.c_ulong),
#         ("dwExtraInfo", PUL)
#     ]

# class HardwareInput(ctypes.Structure):
#     _fields_ = [
#         ("uMsg", ctypes.c_ulong),
#         ("wParamL", ctypes.c_short),
#         ("wParamH", ctypes.c_ushort)
#     ]

# class MouseInput(ctypes.Structure):
#     _fields_ = [
#         ("dx", ctypes.c_long),
#         ("dy", ctypes.c_long),
#         ("mouseData", ctypes.c_ulong),
#         ("dwFlags", ctypes.c_ulong),
#         ("time",ctypes.c_ulong),
#         ("dwExtraInfo", PUL)
#     ]

# class Input_I(ctypes.Union):
#     _fields_ = [
#         ("ki", KeyBdInput),
#         ("mi", MouseInput),
#         ("hi", HardwareInput)
#     ]

# class Input(ctypes.Structure):
#     _fields_ = [
#         ("type", ctypes.c_ulong),
#         ("ii", Input_I)
#     ]

# M_BUTTON = {
#     MButton.LEFT: 'left',
#     MButton.RIGHT: 'right',
# }

# class Operator(OperatorInterface):
#     def s_size(self) -> Size:
#         return pyautogui.size()

#     def m_location_get(self) -> Point:
#         return pyautogui.position()

#     def m_location_set(self, x: int, y: int):
#         set_cursor_pos(x, y)

#     def m_press(self, button: MButton):
#         pyautogui.mouseDown(*self.m_location_get(), M_BUTTON[button])

# # def key_down(key_code):
# #     # Let pyautogui handle non-hex values
# #     if (isinstance(key_code, str)):
# #         pyautogui.keyDown(key_code)
# #         return

# #     extra = ctypes.c_ulong(0)
# #     ii_ = Input_I()
# #     ii_.ki = KeyBdInput(0, key_code, 0x0008, 0, ctypes.pointer(extra))
# #     x = Input(ctypes.c_ulong(1), ii_)
# #     send_input(1, ctypes.pointer(x), ctypes.sizeof(x))

# # def key_up(key_code):
# #     # Let pyautogui handle non-hex values
# #     if (isinstance(key_code, str)):
# #         pyautogui.keyUp(key_code)
# #         return

# #     extra = ctypes.c_ulong(0)
# #     ii_ = Input_I()
# #     ii_.ki = KeyBdInput(0, key_code, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
# #     x = Input(ctypes.c_ulong(1), ii_)
# #     send_input(1, ctypes.pointer(x), ctypes.sizeof(x))

# # def key_press(key_name, duration=0.15):
# #     duration_variance_limit = 0.015
# #     duration_variance = random.uniform(-duration_variance_limit, duration_variance_limit)

# #     key_down(key_name)
# #     duration = duration + duration_variance
# #     delay = perf_counter() + duration
# #     while perf_counter() < delay: pass
# #     key_up(key_name)

# # DirectX scan codes https://gist.github.com/dretax/fe37b8baf55bc30e9d63
# # KEY_CODE = {
# #     'escape': 0x01,
# #     '1': 0x02,
# #     '2': 0x03,
# #     '3': 0x04,
# #     '4': 0x05,
# #     '5': 0x06,
# #     '6': 0x07,
# #     '7': 0x08,
# #     '8': 0x09,
# #     '9': 0x0A,
# #     '0': 0x0B,
# #     '-': 0x0C,
# #     '=': 0x0D,
# #     'backspace': 0x0E,
# #     'tab': 0x0F,
# #     'q': 0x10,
# #     'w': 0x11,
# #     'e': 0x12,
# #     'r': 0x13,
# #     't': 0x14,
# #     'y': 0x15,
# #     'u': 0x16,
# #     'i': 0x17,
# #     'o': 0x18,
# #     'p': 0x19,
# #     'left_bracket': 0x1A,
# #     'right_bracket': 0x1B,
# #     'enter': 0x1C,
# #     'control': 0x1D,
# #     'a': 0x1E,
# #     's': 0x1F,
# #     'd': 0x20,
# #     'f': 0x21,
# #     'g': 0x22,
# #     'h': 0x23,
# #     'j': 0x24,
# #     'k': 0x25,
# #     'l': 0x26,
# #     'semicolon': 0x27,
# #     'apostrophe': 0x28,
# #     'grave': 0x29,
# #     'shift': 0x2A,
# #     'back_slash': 0x2B,
# #     'z': 0x2C,
# #     'x': 0x2D,
# #     'c': 0x2E,
# #     'v': 0x2F,
# #     'b': 0x30,
# #     'n': 0x31,
# #     'm': 0x32,
# #     'comma': 0x33,
# #     'period': 0x34,
# #     'forward_slash': 0x35,
# #     'alt': 0x38,
# #     'space': 0x39,
# #     'f1': 0x3B,
# #     'f2': 0x3C,
# #     'f3': 0x3D,
# #     'f4': 0x3E,
# #     'f5': 0x3F,
# #     'f6': 0x40,
# #     'f7': 0x41,
# #     'f8': 0x42,
# #     'f9': 0x43,
# #     'f10': 0x44,
# #     'f11': 0x57,
# #     'f12': 0x58,
# #     'up': 'up',
# #     'right': 'right',
# #     'down': 'down',
# #     'left': 'left',
# # }
