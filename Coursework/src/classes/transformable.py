from pygame import Rect, Vector2

from src.classes.event import GameEvent


class Transformable:
    def __init__(self) -> None:
        self.__position: Vector2 = Vector2(0,0)
        self.__position_event: GameEvent = GameEvent(0)
        self.__scale: Vector2 = Vector2(1, 1)
        self.__scale_event: GameEvent = GameEvent(0)
        self.__rotation: float = 0
        self.__rotation_event: GameEvent = GameEvent(0)
    #Neutral means that the scale and rotaton are neutral
    def is_neutral(self)->bool:
        return self.__scale == Vector2(1, 1) and self.__rotation == 0
    def get_position(self)->Vector2:
        return self.__position
    def get_position_event(self)->GameEvent:
        return self.__position_event
    def set_position(self, pos: Vector2)->None:
        if self.__position == pos:
            return
        self.__position = pos
        self.__position_event.fire()
    def get_scale(self)->Vector2:
        return self.__scale
    def get_scale_event(self)->GameEvent:
        return self.__scale_event
    def set_scale(self, scale: Vector2)->None:
        if self.__scale == scale:
            return
        self.__scale = scale
        self.__scale_event.fire()
    def get_rotation(self)->float:
        return self.__rotation
    def get_rotation_event(self)->GameEvent:
        return self.__rotation_event
    def set_rotation(self, rotation: float)->None:
        if self.__rotation == rotation:
            return
        self.__rotation = rotation
        self.__rotation_event.fire()
    def get_rect(self, size: Vector2)->Rect:
        return Rect(self.__position, Vector2(size * self.__scale))