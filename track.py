from vpython import *
import numpy as np

track_length = 50

def track_function(x):
    return 15 + 8*np.sin(0.2*x) + 3*np.sin(0.5*x) - 0.1*x

def draw_track():
    # Rails
    for x in np.arange(0, track_length, 0.5):
        y = track_function(x)
        sphere(pos=vector(x, y, -1), radius=0.15, color=color.gray(0.5))
        sphere(pos=vector(x, y, 1), radius=0.15, color=color.gray(0.5))

        if x % 2 < 0.25:
            box(pos=vector(x, y-0.2, 0),
                size=vector(0.3, 0.1, 2.2),
                color=color.gray(0.3))

    # Pillars
    for x in np.arange(2, track_length, 5):
        y = track_function(x)
        if y > 5:
            cylinder(pos=vector(x, 0, 0),
                     axis=vector(0, y-0.5, 0),
                     radius=0.3,
                     color=color.gray(0.7))
            box(pos=vector(x, 0.2, 0),
                size=vector(1, 0.4, 1),
                color=color.gray(0.5))

    # Ground
    box(pos=vector(track_length/2, -0.5, 0),
        size=vector(track_length+10, 0.5, 20),
        color=color.green)