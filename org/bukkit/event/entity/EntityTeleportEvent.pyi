from org.bukkit.Location import Location
from org.bukkit.entity.Entity import Entity
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.entity.EntityEvent import EntityEvent
from typing import Optional

class EntityTeleportEvent(EntityEvent, Cancellable):
    """
    Thrown when a non-player entity is teleported from one location to another.
    <br>
    This may be as a result of natural causes (Enderman, Shulker), pathfinding
    (Wolf), or commands (/teleport).
    """

    handlers: HandlerList = HandlerList()
    cancel: bool
    from_location: Location
    to_location: Optional[Location]

    def __init__(self, what: Entity, from_location: Location, to_location: Optional[Location]) -> None:
        """
        Initializes the EntityTeleportEvent.

        :param what: The entity being teleported.
        :param from_location: The location the entity is moving from.
        :param to_location: The location the entity is moving to.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Returns whether the event is cancelled.

        :return: True if the event is cancelled, otherwise false.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets whether the event is cancelled.

        :param cancel: True to cancel the event, otherwise false.
        """
        ...

    def getFrom(self) -> Location:
        """
        Gets the location that this entity moved from.

        :return: Location this entity moved from.
        """
        ...

    def setFrom(self, from_location: Location) -> None:
        """
        Sets the location that this entity moved from.

        :param from_location: New location this entity moved from.
        """
        ...

    def getTo(self) -> Optional[Location]:
        """
        Gets the location that this entity moved to.

        :return: Location the entity moved to.
        """
        ...

    def setTo(self, to_location: Optional[Location]) -> None:
        """
        Sets the location that this entity moved to.

        :param to_location: New Location this entity moved to.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: HandlerList for this event.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: HandlerList for this event.
        """
        ...