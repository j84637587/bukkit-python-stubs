from org.bukkit.block import BlockState
from org.bukkit.inventory.meta import ItemMeta
from typing import Protocol

class BlockStateMeta(ItemMeta, Protocol):
    """
    Interface for BlockStateMeta which extends ItemMeta.
    """

    def has_block_state(self) -> bool:
        """
        Returns whether the item has a block state currently
        attached to it.

        Returns:
            bool: whether a block state is already attached
        """
        ...

    def get_block_state(self) -> BlockState:
        """
        Returns the currently attached block state for this
        item or creates a new one if one doesn't exist.

        The state is a copy, it must be set back (or to another
        item) with set_block_state(org.bukkit.block.BlockState)

        Returns:
            BlockState: the attached state or a new state
        """
        ...

    def set_block_state(self, block_state: BlockState) -> None:
        """
        Attaches a copy of the passed block state to the item.

        Args:
            block_state (BlockState): the block state to attach to the block.

        Raises:
            IllegalArgumentException: if the blockState is null
            or invalid for this item.
        """
        ...