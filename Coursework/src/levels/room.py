import pygame
import random
import time
from src.classes.game_object import GameObject

class Room(GameObject):
    position: pygame.Vector2
    size: pygame.Vector2
    connected_rooms: list
    def __init__(self, game, pos, size):
        super().__init__(game)
        self.position = pos
        self.size = size
    def update(self, delta: float) -> None:
        pass
    def draw(self, delta: float) -> None:
        pygame.draw.rect(self.game.screen, pygame.Color("red"), pygame.Rect(self.position.x * -0.5, self.position.y * 0.5, self.size.x, self.size.y))
    pass

class Level(GameObject):
    rooms: list[Room]
    spawn_room: Room
    boss_room: Room
    def fits_at(self, rooms, room)->bool:
        return False

    def generate(self, room_count: int)->None:
        random.seed(time.time())
        entry_count = random.randint(1, 4)
        starter_room: Room = Room(self.game, (0, 0), (32 * 8, 32 * 8))
        gen_rooms: list[Room] = []
        furthest_room: Room = starter_room
        for entry_id in range(entry_count):
            pass
    def draw(self, delta: float) -> None:
        for room in self.rooms:
            room.draw(delta)