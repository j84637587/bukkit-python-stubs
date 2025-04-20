from org.bukkit.World import World
from org.bukkit.event.Event import Event
from typing import Literal

class WorldEvent(Event):
    """
    Represents events within a world
    """

    def __init__(self, world: World, is_async: bool = False) -> None:
        ...

    """
    Gets the world primarily involved with this event

    @return World which caused this event
    """
    def get_world(self) -> World:
        ...