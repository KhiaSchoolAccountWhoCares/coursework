from math import cos, pi, sin
from pygame import Vector2


def circle_points(n: int, length: float = 1, offset: float = 0)->list[Vector2]:
    points: list[Vector2] = []
    for side in range(0, n):
        angle = (((2 * pi) / (n)) * side) + offset
        #print((angle / (2 * pi)) * 360)
        points.append(Vector2(cos(angle), sin(angle)) * length)
    return points