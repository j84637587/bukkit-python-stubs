from typing import List
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.event import HandlerList

class BlockPistonExtendEvent(BlockPistonEvent):
    """
    Called when a piston extends
    """
    
    handlers: HandlerList = HandlerList()
    length: int
    blocks: List[Block]

    def __init__(self, block: Block, length: int, direction: BlockFace) -> None:
        """
        @param block: The block that is being extended.
        @param length: The length of the extension.
        @param direction: The direction of the extension.
        """
        ...

    def __init__(self, block: Block, blocks: List[Block], direction: BlockFace) -> None:
        """
        @param block: The block that is being extended.
        @param blocks: The list of blocks being moved.
        @param direction: The direction of the extension.
        """
        ...

    @Deprecated(since="1.8")
    def get_length(self) -> int:
        """
        Get the amount of blocks which will be moved while extending.

        @return: the amount of moving blocks
        @deprecated: slime blocks make the value of this method
                     inaccurate due to blocks being pushed at the side
        """
        ...

    def get_blocks(self) -> List[Block]:
        """
        Get an immutable list of the blocks which will be moved by the
        extending.

        @return: Immutable list of the moved blocks.
        """
        ...

    def get_handlers(self) -> HandlerList:
        """
        @return: The handler list for this event.
        """
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        @return: The static handler list for this event.
        """
        ...