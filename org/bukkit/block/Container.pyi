from typing import Protocol
from .nameable import Nameable
import org.bukkit.block_inventory_holder import BlockInventoryHolder
from .inventory import Inventory
from .tile_state import TileState
from .lockable import Lockable

class Container(Protocol[TileState, BlockInventoryHolder, Lockable, Nameable]):
    """Represents a captured state of a container block."""

    def get_inventory(self) -> Inventory:
        """
        Gets the inventory of the block represented by this block state.
        If the block was changed to a different type in the meantime, the
        returned inventory might no longer be valid.
        If this block state is not placed this will return the captured inventory
        snapshot instead.

        Returns:
            Inventory: the inventory
        """

    def get_snapshot_inventory(self) -> Inventory:
        """
        Gets the captured inventory snapshot of this container.
        The returned inventory is not linked to any block. Any modifications to
        the returned inventory will not be applied to the block represented by
        this block state up until update(boolean, boolean) has been
        called.

        Returns:
            Inventory: the captured inventory snapshot
        """