from org.bukkit.block.data import BlockData
from typing import Protocol

class Display(Protocol):
    pass

class BlockDisplay(Display, Protocol):
    """Represents a block display entity."""

    def get_block(self) -> BlockData:
        """Gets the displayed block.

        Returns:
            BlockData: the displayed block
        """
        ...

    def set_block(self, block: BlockData) -> None:
        """Sets the displayed block.

        Args:
            block (BlockData): the new block
        """
        ...