from typing import List
from org.bukkit.Location import Location
from org.bukkit.block.Block import Block
from org.bukkit.block.BlockFace import BlockFace
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.block.BlockPistonEvent import BlockPistonEvent
from typing import Any

class BlockPistonRetractEvent(BlockPistonEvent):
    """
    Called when a piston retracts
    """
    
    handlers: HandlerList = HandlerList()
    blocks: List[Block]

    def __init__(self, block: Block, blocks: List[Block], direction: BlockFace) -> None:
        super().__init__(block, direction)
        self.blocks = blocks

    """
    Gets the location where the possible moving block might be if the
    retracting piston is sticky.

    @return: The possible location of the possibly moving block.
    """
    @Deprecated(since="1.8")
    def get_retract_location(self) -> Location:
        ...

    """
    Get an immutable list of the blocks which will be moved by the
    extending.

    @return: Immutable list of the moved blocks.
    """
    def get_blocks(self) -> List[Block]:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...