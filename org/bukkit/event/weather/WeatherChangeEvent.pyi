from org.bukkit import World
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull

class WeatherChangeEvent(WeatherEvent, Cancellable):
    """
    Stores data for weather changing in a world
    """

    handlers: HandlerList = HandlerList()
    canceled: bool
    to: bool

    def __init__(self, world: NotNull[World], to: bool) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    """
    Gets the state of weather that the world is being set to

    @return: true if the weather is being set to raining, false otherwise
    """
    def toWeatherState(self) -> bool:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...