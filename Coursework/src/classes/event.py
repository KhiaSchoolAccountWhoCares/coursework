from typing import Any, Callable

#Represents a connection to an event.
#This being an object means the receiving function can be changed without accessing the event directly.
class EventConnection:
    #To create a connection you need an id and a function to be passed.
    def __init__(self, id: int, handler: Callable[..., None]) -> None:
        self.__connection_id = id
        self.__handler = handler

    def invalidate(self) -> None:
        self.__connection_id = -1

    def get_connection_id(self) -> int:
        return self.__connection_id
    #Returns the function used in this connection
    def get_handler(self) -> Callable[..., None]:
        return self.__handler

#An event that when fired will call all functions connected.
class GameEvent:
    def __init__(self, argument_count: int) -> None:
        self.__connections: dict[int, EventConnection] = dict()
        self.__counter: int = 0
        pass

    def subscribe(self, handler: Callable[..., None]) -> EventConnection:
        connection = EventConnection(self.__counter, handler)
        self.__connections[self.__counter] = connection
        self.__counter += 1
        return connection

    def unsubscribe(self, connection: EventConnection) -> None:
        if not (connection.get_connection_id() in self.__connections):
            return
        del self.__connections[connection.get_connection_id()]
        connection.invalidate()

    def clear_connections(self):
        self.__counter = 0

    def fire(self, *args: Any) -> None:
        for connection in self.__connections.values():
            handler = connection.get_handler()
            handler(args)
