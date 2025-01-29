from enum import Enum
from tkinter import RIGHT
import pygame

from src.classes.event import GameEvent

class InputAction:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__pressed_event: GameEvent = GameEvent(0)
        self.__released_event: GameEvent = GameEvent(0)
        self.__binds: list[InputBind] = []
    def update(self)->None:
        pass

class InputBind:
    def __init__(self)->None:
        self.__pressed: bool = False
    def update(self)->None:
        pass
    def clear_pressed(self)->None:
        self.__pressed = False
    def mark_pressed(self)->None:
        self.__pressed = True
    def get_pressed(self)->bool:
        return self.__pressed

class KeyPressBind(InputBind):
    def __init__(self)->None:
        super().__init__()
        self.__keys: list[int] = []
    def add_key(self, keys: tuple[int])->None:
        for key in keys:
            if not (key in self.__keys):
                self.__keys.append(key)
    def update(self)->None:
        for key in self.__keys:
            if key in pygame.key.get_pressed():
                self.mark_pressed()
                break

class MouseButtonBind(InputBind):
    LEFT: int = 0
    MIDDLE: int = 1
    RIGHT: int = 2  
    def __init__(self, button_id: int = LEFT) -> None:
        super().__init__()
        if button_id > self.MIDDLE or button_id < self.LEFT:
            raise BaseException("Invalid Button ID")
        self.__mouse_button_id: int = button_id
    def update(self)->None:
        button_presses = pygame.mouse.get_pressed(3)
        if button_presses[self.__mouse_button_id]:
            self.mark_pressed()
        pass

class ScrollWheelBind(InputBind):
    pass

class InputManager:
    def __init__(self)->None:
        self.__key_down_event = GameEvent(3)
        self.__key_up_event = GameEvent(3)
        self.__mouse_down_event = GameEvent(2)
        self.__mouse_up_event = GameEvent(2)
        self.__mouse_motion_event = GameEvent(2)
        self.__scroll_wheel_event = GameEvent(1)
    
    def get_key_down_event(self)->GameEvent:
        return self.__key_down_event
    def get_key_up_event(self)->GameEvent:
        return self.__key_up_event
    def get_mouse_down_event(self)->GameEvent:
        return self.__mouse_down_event
    def get_mouse_up_event(self)->GameEvent:
        return self.__mouse_up_event
    def get_mouse_motion_event(self)->GameEvent:
        return self.__mouse_motion_event
    def get_scroll_wheel_event(self)->GameEvent:
        return self.__scroll_wheel_event
    
    def handle_events(self, event: pygame.event.Event)->bool:
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                self.__mouse_down_event.fire(event.pos, event.button)
            case pygame.MOUSEBUTTONUP:
                self.__mouse_up_event.fire(event.pos, event.button)
            case pygame.KEYDOWN:
                self.__key_down_event.fire(event.key, event.unicode, event.scancode)
            case pygame.KEYUP:
                self.__key_up_event.fire(event.key, event.unicode, event.scancode)
            case pygame.MOUSEMOTION:
                self.__mouse_motion_event.fire(event.pos, event.rel)
            case pygame.MOUSEWHEEL:
                self.__scroll_wheel_event.fire(event.y)
            case _:
                return False
        return True

    def assure_action(self, action: InputAction)->None:
        pass
    def is_action_pressed(self, action: str)->bool:
        return False
    def is_action_just_pressed(self, action: str)->bool:
        return False
    def get_vector(self, actions: tuple[str, str, str, str])->pygame.Vector2:
        return pygame.Vector2(0, 0)
    pass