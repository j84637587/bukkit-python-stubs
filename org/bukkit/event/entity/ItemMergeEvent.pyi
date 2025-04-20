from org.bukkit.entity import Item
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class ItemMergeEvent(EntityEvent, Cancellable):
    """
    Event called when two items merge.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    target: Item

    def __init__(self, item: Item, target: Item) -> None:
        """
        Initializes the ItemMergeEvent.

        :param item: The main Item being merged.
        :param target: The Item being merged with.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Returns whether the event is cancelled.

        :return: True if the event is cancelled, otherwise false.
        """
        ...

    def setCancelled(self, cancelled: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancelled: True to cancel the event, otherwise false.
        """
        ...

    def getEntity(self) -> Item:
        """
        Gets the Item entity that is being merged.

        :return: The main Item being merged.
        """
        ...

    def getTarget(self) -> Item:
        """
        Gets the Item entity the main Item is being merged into.

        :return: The Item being merged with.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: The HandlerList for this event.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static HandlerList for this event.

        :return: The static HandlerList for this event.
        """
        ...