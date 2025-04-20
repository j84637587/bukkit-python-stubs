from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from typing import Final

class BlockRedstoneEvent(BlockEvent):
    """
    Called when a redstone current changes
    """

    handlers: Final[HandlerList] = HandlerList()
    oldCurrent: int
    newCurrent: int

    def __init__(self, block: Block, oldCurrent: int, newCurrent: int) -> None:
        super().__init__(block)
        self.oldCurrent = oldCurrent
        self.newCurrent = newCurrent

    """
    Gets the old current of this block

    @return The previous current
    """
    def getOldCurrent(self) -> int:
        ...

    """
    Gets the new current of this block

    @return The new current
    """
    def getNewCurrent(self) -> int:
        ...

    """
    Sets the new current of this block

    @param newCurrent The new current to set
    """
    def setNewCurrent(self, newCurrent: int) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...