import random
import scipy
import numpy
import time

from scipy import interpolate
from scipy.spatial import distance
from definitions import pyautogui

# # WINDOWS OS IMPLEMENTATION
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

# def m_move(x, y)
#     set_cursor_pos(int(x), int(y))

# def key_down(key_code):
#     # Let pyautogui handle non-hex values
#     if (isinstance(key_code, str)):
#         pyautogui.keyDown(key_code)
#         return

#     extra = ctypes.c_ulong(0)
#     ii_ = Input_I()
#     ii_.ki = KeyBdInput(0, key_code, 0x0008, 0, ctypes.pointer(extra))
#     x = Input(ctypes.c_ulong(1), ii_)
#     send_input(1, ctypes.pointer(x), ctypes.sizeof(x))

# def key_up(key_code):
#     # Let pyautogui handle non-hex values
#     if (isinstance(key_code, str)):
#         pyautogui.keyUp(key_code)
#         return

#     extra = ctypes.c_ulong(0)
#     ii_ = Input_I()
#     ii_.ki = KeyBdInput(0, key_code, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
#     x = Input(ctypes.c_ulong(1), ii_)
#     send_input(1, ctypes.pointer(x), ctypes.sizeof(x))

# def key_press(key_name, duration=0.15):
#     duration_variance_limit = 0.015
#     duration_variance = random.uniform(-duration_variance_limit, duration_variance_limit)

#     key_down(key_name)
#     duration = duration + duration_variance
#     delay = time.perf_counter() + duration
#     while time.perf_counter() < delay: pass
#     key_up(key_name)

# MACOS IMPLEMENTATION
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap

def m_event(type, x, y):
    event = CGEventCreateMouseEvent(None, type, (x, y), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, event)

def m_move(x, y):
    m_event(kCGEventMouseMoved, x, y)

def m_click(x, y):
    m_event(kCGEventLeftMouseDown, x, y)
    m_event(kCGEventLeftMouseUp, x, y)

def mouse_to(destination_x, destination_y, time_between_points=0.0001):
    cp = random.randint(3, 5)  # Number of control points, must be at least 2
    origin_x, origin_y = pyautogui.position()

    # Distribute control points between start and destination evenly
    x = numpy.linspace(origin_x, destination_x, num=cp, dtype='int')
    y = numpy.linspace(origin_y, destination_y, num=cp, dtype='int')

    # Randomize inner points a bit (+-RND at most)
    RND = 10
    xr = numpy.random.randint(-RND, RND, size=cp)
    yr = numpy.random.randint(-RND, RND, size=cp)
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    # Approximate using Bezier spline
    degree = 1 if cp > 3 else cp - 1  # Degree of b-spline, 3 is recommended, must be less than number of control points
    tck, u = scipy.interpolate.splprep([x, y], k=degree)
    u = numpy.linspace(0, 1, num=max(pyautogui.size()))
    points = scipy.interpolate.splev(u, tck)

    # Move mouse
    delay = time.perf_counter()
    for point in zip(*(i.astype(int) for i in points)):
        m_move(*point)
        while time.perf_counter() < delay: pass
        delay = time.perf_counter() + time_between_points

# # TODO: add ability to make mistakes and delete them, then continue
# def type_phrase(phrase, do_make_mistakes=True, words_per_minute=125):
#     letter_variance_limit = 0.025  # Typing delay randomness
#     word_delay_upper_limit = 0.4   # Highest delay for the biggest words
#     word_delay_slope = 5           # Effectiveness of a single letter on the word delay, less is more
#     symbol_delay = 0.018           # Extra delay for special characters
#     average_word_size = 5            # Average typed characters per word

#     words = phrase.split()
#     word_count = len(words)
#     average_word_count = len(phrase) / average_word_size
#     time_correction = (word_delay_upper_limit / average_word_size) * word_count  # accomodate for our induced randomness
#     time_to_completion = ((average_word_count / words_per_minute) * 60) - time_correction  # seconds
#     average_time_per_char = time_to_completion / len(phrase)
#     delay = time.perf_counter()

#     for index, word in enumerate(words, start=1):
#         word_length = len(word)
#         word_delay = (word_length / (word_length + word_delay_slope)) * word_delay_upper_limit

#         # Type the word
#         for char in word:
#             pyautogui.press(char)

#             # Introduce typing delays
#             letter_variance = random.uniform(-letter_variance_limit, letter_variance_limit)

#             # Check for symbols
#             char_contains_symbol = not char.isalnum()
#             if char_contains_symbol:
#                 letter_variance += symbol_delay

#             delay = time.perf_counter() + (average_time_per_char + letter_variance)
#             while time.perf_counter() < delay: pass

#         # Phrase is finito
#         if index == word_count:
#             break

#         # Add a space, wait, then continue the phrase
#         pyautogui.press('space')
#         delay = time.perf_counter() + word_delay
#         while time.perf_counter() < delay: pass
