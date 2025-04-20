from org.bukkit import World
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.world import WorldEvent
from typing import Any

class WorldUnloadEvent(WorldEvent, Cancellable):
    """
    Called when a World is unloaded
    """

    handlers: HandlerList = HandlerList()
    
    def __init__(self, world: World) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...