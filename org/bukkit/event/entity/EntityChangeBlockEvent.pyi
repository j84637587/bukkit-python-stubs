from org.bukkit.Material import Material
from org.bukkit.block.Block import Block
from org.bukkit.block.data.BlockData import BlockData
from org.bukkit.entity.Entity import Entity
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.entity.EntityEvent import EntityEvent
from typing import Any

class EntityChangeBlockEvent(EntityEvent, Cancellable):
    """
    Called when any Entity changes a block and a more specific event is not available.
    """

    handlers: HandlerList = HandlerList()
    block: Block
    cancel: bool
    to: BlockData

    def __init__(self, what: Entity, block: Block, to: BlockData) -> None:
        """
        Initializes the event with the entity, block, and block data.

        :param what: The entity that is changing the block.
        :param block: The block that is changing.
        :param to: The block data that the block is changing to.
        """
        ...

    def getBlock(self) -> Block:
        """
        Gets the block the entity is changing.

        :return: The block that is changing.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, otherwise false.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, otherwise false.
        """
        ...

    def getTo(self) -> Material:
        """
        Gets the Material that the block is changing into.

        :return: The material that the block is changing into.
        """
        ...

    def getBlockData(self) -> BlockData:
        """
        Gets the data for the block that would be changed into.

        :return: The data for the block that would be changed into.
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