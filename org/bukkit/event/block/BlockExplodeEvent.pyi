from typing import List
from org.bukkit import ExplosionResult
from org.bukkit.block import Block, BlockState
from org.bukkit.event import Cancellable, HandlerList

class BlockExplodeEvent(BlockEvent, Cancellable):
    """
    Called when a block explodes.
    <p>
    Note that due to the nature of explosions, {@link #getBlock()} will always be
    an air block. {@link #getExplodedBlockState()} should be used to get
    information about the block state that exploded.
    """

    handlers: HandlerList

    def __init__(self, what: Block, block_state: BlockState, blocks: List[Block], yield: float, result: ExplosionResult) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    """
    Returns the result of the explosion if it is not cancelled.

    @return the result of the explosion
    """
    def getExplosionResult(self) -> ExplosionResult:
        ...

    """
    Returns the captured BlockState of the block that exploded.

    @return the block state
    """
    def getExplodedBlockState(self) -> BlockState:
        ...

    """
    Returns the list of blocks that would have been removed or were removed
    from the explosion event.

    @return All blown-up blocks
    """
    def blockList(self) -> List[Block]:
        ...

    """
    Returns the percentage of blocks to drop from this explosion

    @return The yield.
    """
    def getYield(self) -> float:
        ...

    """
    Sets the percentage of blocks to drop from this explosion

    @param yield The new yield percentage
    """
    def setYield(self, yield: float) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...