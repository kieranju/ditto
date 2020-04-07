from msb.definitions import operator
from msb.operator.definitions import MButton, KKey

from time import perf_counter
from numpy import random, linspace
from scipy import interpolate

def m_move(destination_x, destination_y, time_between_points=0.0001):
    cp = random.randint(3, 5)  # Number of control points, must be at least 2
    origin_x, origin_y = operator.m_location_get()

    # Distribute control points between start and destination evenly
    x = linspace(origin_x, destination_x, num=cp, dtype='int')
    y = linspace(origin_y, destination_y, num=cp, dtype='int')

    # Randomize inner points a bit (+-RND at most)
    RND = 10
    xr = random.randint(-RND, RND, size=cp)
    yr = random.randint(-RND, RND, size=cp)
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    # Approximate using Bezier spline
    degree = 1 if cp > 3 else cp - 1  # Degree of b-spline, 3 is recommended, must be less than number of control points
    tck, u = interpolate.splprep([x, y], k=degree)
    u = linspace(0, 1, num=max(operator.s_size()))
    points = interpolate.splev(u, tck)

    # Move mouse
    delay = perf_counter()
    for point in zip(*(i.astype(int) for i in points)):
        operator.m_location_set(*point)
        while perf_counter() < delay: pass
        delay = perf_counter() + time_between_points

def m_press(button: MButton):
    operator.m_press(button)

def m_release(button: MButton):
    operator.m_release(button)

def k_press(key: KKey):
    operator.k_press(key)

def k_release(key: KKey):
    operator.k_release(key)

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
#     delay = perf_counter()

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

#             delay = perf_counter() + (average_time_per_char + letter_variance)
#             while perf_counter() < delay: pass

#         # Phrase is finito
#         if index == word_count:
#             break

#         # Add a space, wait, then continue the phrase
#         pyautogui.press('space')
#         delay = perf_counter() + word_delay
#         while perf_counter() < delay: pass
