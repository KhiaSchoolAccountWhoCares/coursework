from pygame import Vector2
from src.classes.game_object import GameObject
from src.classes.render_object import RenderObject


class Entity(RenderObject, GameObject):
    def __init__(self):
        super().__init__()
        self._position: Vector2 = Vector2(0, 0)
        self._scale: Vector2 = Vector2(1, 1)
    def get_position(self)->Vector2:
        return self._position
    def get_scale(self)->Vector2:
        return self._scale