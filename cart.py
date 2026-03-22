# cart.py
from vpython import *

wheel_radius = 0.3

def create_cart(track_function):
    cart_body = box(pos=vector(0, track_function(0)+0.8, 0),
                    size=vector(2.0, 1.0, 1.5),
                    color=color.red)

    cart_roof = pyramid(pos=vector(0, track_function(0)+1.3, 0),
                        size=vector(1.8, 0.4, 1.3),
                        color=color.blue)

    wheel_positions = [
        (-0.7, -0.4, 0.8),
        (0.7, -0.4, 0.8),
        (-0.7, -0.4, -0.8),
        (0.7, -0.4, -0.8)
    ]

    wheels = []
    for wx, wy, wz in wheel_positions:
        wheel = cylinder(pos=vector(wx, track_function(0)+wy, wz),
                         axis=vector(0, 0, 0.1),
                         radius=wheel_radius,
                         color=color.black)
        wheels.append(wheel)

    return cart_body, cart_roof, wheels, wheel_positions


def update_cart(x, y, slope, v, dt, wheels, wheel_positions, cart_body, cart_roof):
    rotation_angle = (v * dt) / wheel_radius

    cart_body.pos = vector(x, y + 0.8, 0)
    cart_roof.pos = vector(x, y + 1.3, 0)

    for i, wheel in enumerate(wheels):
        wx, wy, wz = wheel_positions[i]
        wheel.pos = vector(x + wx, y + 0.8 + wy, wz)
        wheel.rotate(angle=rotation_angle, axis=vector(0, 0, 1))

    cart_body.axis = vector(1, slope, 0)
    cart_roof.axis = vector(1, slope, 0)