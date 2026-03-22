import numpy as np

g = 9.8
mass = 100
mu = 0.05

def compute_slope(track_function, x):
    dx = 0.01
    return (track_function(x + dx) - track_function(x - dx)) / (2 * dx)

def update_motion(x, v, dt, track_function):
    y = track_function(x)
    slope = compute_slope(track_function, x)
    theta = np.arctan(slope)

    normal = mass * g * abs(np.cos(theta))
    friction = mu * normal if abs(v) > 0 else 0
    gravity = -mass * g * np.sin(theta)

    net_force = gravity - friction * np.sign(v)
    a = net_force / mass

    v = v + a * dt
    x = x + v * dt

    return x, v, y, slope, theta, friction

def compute_energy(v, y):
    ke = 0.5 * mass * v**2
    pe = mass * g * y
    return ke, pe, ke + pe