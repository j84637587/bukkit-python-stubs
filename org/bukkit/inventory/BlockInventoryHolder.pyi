from org.bukkit.block import Block
from typing import Protocol

class InventoryHolder(Protocol):
    pass

class BlockInventoryHolder(InventoryHolder, Protocol):
    """
    Represents a block inventory holder - either a BlockState, or a regular
    Block.
    """

    def get_block(self) -> Block:
        """
        Gets the block associated with this holder.

        :return: the block associated with this holder
        :raises IllegalStateException: if the holder is a block state and is not placed
        """
        ...