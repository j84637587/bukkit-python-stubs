from org.bukkit import Material
from org.bukkit.block.data import BlockData
from typing import Protocol

class BlockDataMeta(Protocol):
    """
    Interface representing metadata for items that have block data.
    """

    def has_block_data(self) -> bool:
        """
        Returns whether the item has block data currently attached to it.

        Returns:
            bool: whether block data is already attached
        """
        ...

    def get_block_data(self, material: Material) -> BlockData:
        """
        Returns the currently attached block data for this item or creates a new
        one if one doesn't exist.

        The state is a copy, it must be set back (or to another item) with
        set_block_data(BlockData)

        Args:
            material (Material): the material we wish to get this data in the context of

        Returns:
            BlockData: the attached data or new data
        """
        ...

    def set_block_data(self, block_data: BlockData) -> None:
        """
        Attaches a copy of the passed block data to the item.

        Args:
            block_data (BlockData): the block data to attach to the block.

        Raises:
            ValueError: if the block_data is null or invalid for this item.
        """
        ...