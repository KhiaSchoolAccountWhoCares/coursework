from pygame import SRCALPHA, Color, Surface, Vector2
from src.classes.event import GameEvent
from src.classes.transformable import Transformable

class RenderObject:
    def __init__(self) -> None:
        self.__visible = True
        self.__visibility_toggled = GameEvent(0)
    def set_visibility(self, visibility: bool)->None:
        previous_visibility = self.__visible
        self.__visible = visibility
        if previous_visibility != visibility:
            self.__visibility_toggled.fire()
    def get_visible(self)->bool:
        return self.__visible
    def get_visibility_event(self)->GameEvent:
        return self.__visibility_toggled
    def draw(self, surface: Surface, delta: float)-> None:
        if not self.__visible:
            return
        pass