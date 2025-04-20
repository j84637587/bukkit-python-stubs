from org.bukkit import World
from org.bukkit.event import HandlerList
from org.bukkit.event.world import WorldEvent
from typing import Any

class WorldLoadEvent(WorldEvent):
    """
    Called when a World is loaded
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, world: World) -> None:
        super().__init__(world)

    def get_handlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def get_handler_list() -> HandlerList:
        return WorldLoadEvent.handlers