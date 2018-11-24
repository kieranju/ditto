import random
import scipy
import math
import time
from scipy import interpolate
from scipy.spatial import distance
from definitions import pyautogui

def mouse_to(destination_x, destination_y, time_between_points=0.0001):
    cp = random.randint(3, 5)  # Number of control points, must be at least 2
    origin_x, origin_y = pyautogui.position()

    # Distribute control points between start and destination evenly
    x = scipy.linspace(origin_x, destination_x, num=cp, dtype='int')
    y = scipy.linspace(origin_y, destination_y, num=cp, dtype='int')

    # Randomise inner points a bit (+-RND at most)
    RND = 10
    xr = scipy.random.randint(-RND, RND, size=cp)
    yr = scipy.random.randint(-RND, RND, size=cp)
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    # Approximate using Bezier spline
    degree = 1 if cp > 3 else cp - 1  # Degree of b-spline, 3 is recommended, must be less than number of control points
    tck, u = scipy.interpolate.splprep([x, y], k=degree)
    u = scipy.linspace(0, 1, num=max(pyautogui.size()))
    points = scipy.interpolate.splev(u, tck)

    # Move mouse
    delay = time.perf_counter()
    for point in zip(*(i.astype(int) for i in points)):
        pyautogui.moveTo(*point)
        while time.perf_counter() < delay: pass
        delay = time.perf_counter() + time_between_points

# TODO: add ability to make mistakes and delete them, then continue
def type_phrase(phrase, do_make_mistakes=True, words_per_minute=125):
    letter_variance_limit = 0.025  # Typing delay randomness 
    word_delay_upper_limit = 0.4   # Highest delay for the biggest words
    word_delay_slope = 5           # Effectiveness of a single letter on the word delay, less is more
    symbol_delay = 0.018           # Extra delay for special characters
    gross_word_size = 5            # Average typed characters per word
    
    words = phrase.split()
    word_count = len(words)
    gross_word_count = len(phrase) / gross_word_size
    time_correction = (word_delay_upper_limit / gross_word_size) * word_count  # accomodate for our induced randomness
    time_to_completion = ((gross_word_count / words_per_minute) * 60) - time_correction  # seconds
    average_time_per_char = time_to_completion / len(phrase)
    delay = time.perf_counter()
    
    for index, word in enumerate(words, start=1):
        word_length = len(word)
        word_delay = (word_length / (word_length + word_delay_slope)) * word_delay_upper_limit

        # Type the word
        for char in word:
            pyautogui.press(char)

            # Introduce typing delays
            letter_variance = random.uniform(-letter_variance_limit, letter_variance_limit)

            # Check for symbols
            char_contains_symbol = not char.isalnum()
            if char_contains_symbol:
                letter_variance += symbol_delay

            delay = time.perf_counter() + (average_time_per_char + letter_variance)
            while time.perf_counter() < delay: pass

        # Phrase is finito
        if index == word_count:
            break

        # Add a space, wait, then continue the phrase
        pyautogui.press('space')
        delay = time.perf_counter() + word_delay
        while time.perf_counter() < delay: pass

def key_press(key_name, duration=0.15):
    duration_variance_limit = 0.050
    duration_variance = random.uniform(-duration_variance_limit, duration_variance_limit)

    pyautogui.keyDown(key_name)
    duration = duration + duration_variance
    delay = time.perf_counter() + duration
    while time.perf_counter() < delay: pass
    pyautogui.keyUp(key_name)