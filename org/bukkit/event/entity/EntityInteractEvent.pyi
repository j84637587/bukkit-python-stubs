from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class EntityInteractEvent(EntityEvent, Cancellable):
    """
    Called when an entity interacts with an object
    """

    handlers: HandlerList = HandlerList()
    block: Block
    cancelled: bool

    def __init__(self, entity: Entity, block: Block) -> None:
        """
        Initializes the EntityInteractEvent with the given entity and block.

        :param entity: The entity interacting with the block.
        :param block: The block being interacted with.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Returns whether the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, False to allow it.
        """
        ...

    def getBlock(self) -> Block:
        """
        Returns the involved block.

        :return: The block clicked with this item.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Returns the handler list for this event.

        :return: The handler list.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Returns the static handler list for this event.

        :return: The static handler list.
        """
        ...