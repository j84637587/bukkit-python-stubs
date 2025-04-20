from typing import Any
from org.bukkit.block import Block
from org.bukkit.block.data import BlockData
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from org.jetbrains.annotations import NotNull

class FluidLevelChangeEvent(BlockEvent, Cancellable):
    """
    Called when the fluid level of a block changes due to changes in adjacent
    blocks.
    """

    handlers: HandlerList = ...
    cancelled: bool
    newData: BlockData

    def __init__(self, theBlock: Block, newData: BlockData) -> None:
        ...

        def getNewData(self) -> BlockData:
        """
        Gets the new data of the changed block.

        :return: new data
        """
        ...

    def setNewData(self, newData: BlockData) -> None:
        """
        Sets the new data of the changed block. Must be of the same Material as
        the old one.

        :param newData: the new data
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancelled: bool) -> None:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...