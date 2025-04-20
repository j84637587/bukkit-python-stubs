from org.bukkit.entity import Entity
from org.bukkit.entity import Item
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class EntityDropItemEvent(EntityEvent, Cancellable):
    """
    Thrown when an entity creates an item drop.
    """

    handlers: HandlerList

    def __init__(self, entity: Entity, drop: Item) -> None:
        """
        Initializes the event with the given entity and item drop.

        :param entity: The entity that created the item drop.
        :param drop: The item that was dropped.
        """
        ...

    def getItemDrop(self) -> Item:
        """
        Gets the Item created by the entity.

        :return: Item created by the entity.
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

    def getHandlers(self) -> HandlerList:
        """
        Gets the handler list for this event.

        :return: The handler list.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: The static handler list.
        """
        ...