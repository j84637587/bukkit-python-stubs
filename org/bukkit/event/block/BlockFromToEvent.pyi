from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from typing import Optional

class BlockFromToEvent(BlockEvent, Cancellable):
    """
    Represents events with a source block and a destination block, currently
    only applies to liquid (lava and water) and teleporting dragon eggs.
    <p>
    If a Block From To event is cancelled, the block will not move (the liquid
    will not flow).
    """
    
    handlers: HandlerList = HandlerList()
    to: Optional[Block]
    face: BlockFace
    cancel: bool

    def __init__(self, block: Block, face: BlockFace) -> None:
        super().__init__(block)
        self.face = face
        self.cancel = False

    def __init__(self, block: Block, to_block: Block) -> None:
        super().__init__(block)
        self.to = to_block
        self.face = BlockFace.SELF
        self.cancel = False

    """
    Gets the BlockFace that the block is moving to.

    @return The BlockFace that the block is moving to
    """
    def getFace(self) -> BlockFace:
        ...

    """
    Convenience method for getting the faced Block.

    @return The faced Block
    """
    def getToBlock(self) -> Block:
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