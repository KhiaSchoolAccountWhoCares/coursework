from pygame import Color, Rect, Surface
import pygame
import pygame.freetype
from src.classes.game import Game
from src.classes.render_object import RenderObject


class Fps(RenderObject):
    def __init__(self, game: Game) -> None:
        super().__init__()
        self.__game = game
        self.__clock = game.get_clock()
        self.__font = pygame.freetype.SysFont(None, 16)
    def draw(self, surface: Surface, delta: float) -> None:
        fps_string = 'FPS: {0:.2f}'.format(self.__clock.get_fps())
        self.__font.render_to(surface, Rect(0, 0, 128, 16), fps_string)
    pass