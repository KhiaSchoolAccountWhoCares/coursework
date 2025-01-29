from typing import Any
import pygame

from src.classes.event import GameEvent
from src.classes.input_manager import InputManager
from src.classes.scene import Scene

class Game:
    def __init__(self, title: str = "Game"):
        pygame.init()
        self.__running = False
        self.__screen = pygame.display.set_mode((480 * 2, 270 * 2))
        pygame.display.set_caption(title)
        self.__clock = pygame.time.Clock()
        self.__current_scene: Scene = Scene()
        self.__clear_colour = pygame.Color("cornflowerblue")
        self.__input_manager = InputManager()
        self.__window_resized = GameEvent(1)
        self.__target_fps: int = 60
    
    def __update(self, delta: float):
        self.__current_scene.update(delta)

    def __draw(self, delta: float):
        self.__screen.fill(self.__clear_colour)
        self.__current_scene.draw(delta)
        pygame.display.flip()
    
    def __execute_frame(self):
        delta_time = self.__clock.tick(self.__target_fps) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
                break
            if self.__input_manager.handle_events(event): 
                break

        self.__update(delta_time)
        self.__draw(delta_time)
    
    def get_screen(self)->pygame.Surface:
        return self.__screen
    
    def get_clock(self)->pygame.time.Clock:
        return self.__clock

    def quit(self):
        self.__running = False
    
    def run(self, scene):
        if self.__running:
            return
        self.__current_scene = scene
        self.__running = True

        while self.__running:
            self.__execute_frame()
        