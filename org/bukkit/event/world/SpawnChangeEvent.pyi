from org.bukkit import Location
from org.bukkit import World
from org.bukkit.event import HandlerList
from org.bukkit.event.world import WorldEvent
from typing import Any

class SpawnChangeEvent(WorldEvent):
    """
    An event that is called when a world's spawn changes. The world's previous
    spawn location is included.
    """

    handlers: HandlerList = HandlerList()
    previousLocation: Location

    def __init__(self, world: World, previousLocation: Location) -> None:
        super().__init__(world)
        self.previousLocation = previousLocation

    """
    Gets the previous spawn location

    @return Location that used to be spawn
    """
    def getPreviousLocation(self) -> Location:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    def getHandlers(self) -> HandlerList:
        ...