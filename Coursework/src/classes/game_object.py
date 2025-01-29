from src.classes.event import GameEvent

class GameObject:
    def __init__(self):
        self.__active: bool = True
        self.__activity_toggled_event: GameEvent = GameEvent(0)
    def set_activity(self, activity: bool)->None:
        previous_activity = self.__active
        self.__active = activity
        if previous_activity != activity:
            self.__activity_toggled_event.fire()
    def update(self, delta: float)->None:
        pass