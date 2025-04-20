from typing import Optional
from org.bukkit import GameEvent
from org.bukkit import Location
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.world import WorldEvent
from com.google.common.base import Preconditions
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a generic Mojang game event.

Specific Bukkit events should be used where possible, this event is mainly
used internally by Sculk sensors.
"""
class GenericGameEvent(WorldEvent, Cancellable):
    handlers: HandlerList

    def __init__(self, event: GameEvent, location: Location, entity: Optional[Entity], radius: int, is_async: bool) -> None:
        ...

    """
    Get the underlying event.

    @return the event
    """
        def get_event(self) -> GameEvent:
        ...

    """
    Get the location where the event occurred.

    @return event location
    """
        def get_location(self) -> Location:
        ...

    """
    Get the entity which triggered this event, if present.

    @return triggering entity or null
    """
        def get_entity(self) -> Optional[Entity]:
        ...

    """
    Get the block radius to which this event will be broadcast.

    @return broadcast radius
    """
    def get_radius(self) -> int:
        ...

    """
    Set the radius to which the event should be broadcast.

    @param radius radius, must be greater than or equal to 0
    """
    def set_radius(self, radius: int) -> None:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

    def is_cancelled(self) -> bool:
        ...

        def get_handlers(self) -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...