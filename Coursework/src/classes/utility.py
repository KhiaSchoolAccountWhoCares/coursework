from pygame import Rect, Vector2


def centre_position(larger_size: Vector2, smaller_size: Vector2)->Vector2:
    return (larger_size * 0.5) - (smaller_size * 0.5)

def centre_offset(larger_size: Vector2, rect: Rect)->Rect:
    pos = centre_position(larger_size, Vector2(rect.size))
    return Rect((pos.x + rect.left, pos.y + rect.top), rect.size)