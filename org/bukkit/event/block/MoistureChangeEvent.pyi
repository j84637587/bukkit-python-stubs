from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from typing import Any

class MoistureChangeEvent(BlockEvent, Cancellable):
    """
    Called when the moisture level of a soil block changes.
    """

    handlers: HandlerList
    cancelled: bool
    newState: BlockState

    def __init__(self, block: Block, newState: BlockState) -> None:
        """
        Initializes a new MoistureChangeEvent.

        :param block: The block that is affected.
        :param newState: The new state of the affected block.
        """
        ...

    def getNewState(self) -> BlockState:
        """
        Gets the new state of the affected block.

        :return: new block state
        """
        ...

    def isCancelled(self) -> bool:
        ...
    
    def setCancelled(self, cancel: bool) -> None:
        ...
    
    def getHandlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def getHandlerList() -> HandlerList:
        ...