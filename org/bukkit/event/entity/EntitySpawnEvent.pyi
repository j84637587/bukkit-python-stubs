from org.bukkit.Location import Location
from org.bukkit.entity.Entity import Entity
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.entity.EntityEvent import EntityEvent
from typing import Any

class EntitySpawnEvent(EntityEvent, Cancellable):
    """
    Called when an entity is spawned into a world.
    <p>
    If an Entity Spawn event is cancelled, the entity will not spawn.
    """

    handlers: HandlerList = HandlerList()
    canceled: bool

    def __init__(self, spawnee: Entity) -> None:
        """
        Initializes the EntitySpawnEvent with the given spawnee entity.

        :param spawnee: The entity that is being spawned.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, False to allow it.
        """
        ...

    def getLocation(self) -> Location:
        """
        Gets the location at which the entity is spawning.

        :return: The location at which the entity is spawning.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handler list for this event.

        :return: The handler list for this event.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: The static handler list for this event.
        """
        ...