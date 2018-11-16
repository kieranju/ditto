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

    # TODO: Calculate average time to reach destination
    # TODO: The average time to reach across the screen on a 1080p monitor is 0.2 - 0.4 seconds
    # destinationDistance = distance.euclidean([origin_x, origin_y], [destination_x, destination_y])

    # Approximate using Bezier spline
    degree = 1 if cp > 3 else cp - 1  # Degree of b-spline, 3 is recommended, must be less than number of control points
    tck, u = scipy.interpolate.splprep([x, y], k=degree)
    u = scipy.linspace(0, 1, num=max(pyautogui.size()))
    points = scipy.interpolate.splev(u, tck)

    # Move mouse
    time_gate = time.perf_counter()
    for point in zip(*(i.astype(int) for i in points)):
        pyautogui.moveTo(*point)
        while time.perf_counter() < time_gate: pass
        timeGate = time.perf_counter() + time_between_points
