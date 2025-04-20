from org.bukkit.World import World
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.world.WorldEvent import WorldEvent
from typing import Any

class WorldInitEvent(WorldEvent):
    """
    Called when a World is initializing.
    <p>
    To get every world it is recommended to add following to the plugin.yml.
    <pre>load: STARTUP</pre>
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, world: World) -> None:
        super().__init__(world)

    def get_handlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def get_handler_list() -> HandlerList:
        return WorldInitEvent.handlers