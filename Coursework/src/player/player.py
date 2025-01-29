import pygame
from pygame import Color, Surface, Vector2
from src.classes.entity import Entity

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.__colour = Color("white")
    def __draw(self, surface: Surface, delta: float)-> None:
        pygame.draw.circle(surface, self.__colour, self.get_position(), 32 * min(self._scale.x, self._scale.y))
        return super().draw(surface, delta)