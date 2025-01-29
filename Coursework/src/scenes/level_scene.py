from pygame import Color
from src.classes.background import Background
from src.classes.fps import Fps
from src.classes.game import Game
from src.classes.scene import Scene
from player.player import Player

class LevelScene(Scene):
    def __init__(self, game: Game) -> None:
        super().__init__()
        print("hi")
        self.__player = Player()
        self.__background = Background()
        self.__fps = Fps(game)
        self.__game = game
    def update(self, delta: float) -> None:
        self.__player.update(delta)
        self.__background.update(delta)
    def draw(self, delta: float) -> None:
        self.__player.draw(self.__game.get_screen(), delta)
        self.__fps.draw(self.__game.get_screen(), delta)
