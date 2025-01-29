from math import ceil, pi
from pygame import Color, Rect, Surface, Vector2
import pygame
from src.classes.game_object import GameObject
from src.classes.render_object import RenderObject
import classes.polygon_builder

class Background(GameObject, RenderObject):
    def __init__(self):
        super().__init__()
        self.__radius: float = 48
        self.__circle_colour: Color = Color("darkgrey")
        self.__triangle_colour: Color = Color("grey")
        self.__separation: float = 2
        self.__surface = Surface(Vector2(self.__radius * 2, self.__radius * 2), pygame.SRCALPHA)
        self.__time = 0

    def draw(self, surface: Surface, delta: float) -> None:
        self.__time += delta
        pygame.draw.circle(self.__surface, self.__circle_colour, Vector2(48, 48), self.__radius)
        lines_triangle = classes.polygon_builder.circle_points(3, self.__radius)
        for i in range(len(lines_triangle)):
            lines_triangle[i] += Vector2(48, 48)
        pygame.draw.polygon(self.__surface, self.__triangle_colour, lines_triangle)
        rot_sur = pygame.transform.rotate(self.__surface, self.__time * 120)
        surface.blit(rot_sur, Vector2(0, 0))
    
    def update(self, delta: float) -> None:
        return super().update(delta)