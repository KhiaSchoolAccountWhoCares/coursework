from src.classes.game import Game
from scenes.level_scene import LevelScene

import pygame
import ctypes
import sys
# Function to set DPI awareness on Windows def set_dpi_awareness():


def main():
    if sys.platform == 'win32':
        ctypes.windll.user32.SetProcessDPIAware()
    game = Game("Angular [TEST]")
    game.run(LevelScene(game))
    pass

if __name__ == "__main__":
    main()