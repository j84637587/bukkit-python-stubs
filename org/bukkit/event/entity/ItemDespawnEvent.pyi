from org.bukkit.Location import Location
from org.bukkit.entity.Item import Item
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.entity.EntityEvent import EntityEvent
from typing import Any

class ItemDespawnEvent(EntityEvent, Cancellable):
    """
    This event is called when a {@link org.bukkit.entity.Item} is removed from
    the world because it has existed for 5 minutes.
    <p>
    Cancelling the event results in the item being allowed to exist for 5 more
    minutes. This behavior is not guaranteed and may change in future versions.
    """

    handlers: HandlerList

    def __init__(self, despawnee: Item, loc: Location) -> None:
        """
        Initializes the ItemDespawnEvent.

        :param despawnee: The item that is despawning.
        :param loc: The location at which the item is despawning.
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

    def getEntity(self) -> Item:
        """
        Gets the item that is despawning.

        :return: The item that is despawning.
        """
        ...

    def getLocation(self) -> Location:
        """
        Gets the location at which the item is despawning.

        :return: The location at which the item is despawning.
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