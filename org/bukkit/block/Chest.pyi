from typing import Protocol
from .inventory import Inventory
from .loot import Lootable
from .container import Container
from .lidded import Lidded

class Chest(Protocol[Container, Lootable, Lidded]):
    """Represents a captured state of a chest."""

    def get_block_inventory(self) -> Inventory:
        """
        Gets the inventory of the chest block represented by this block state.
        If the chest is a double chest, it returns just the portion of the
        inventory linked to the half of the chest corresponding to this block state.
        If the block was changed to a different type in the meantime, the
        returned inventory might no longer be valid.
        If this block state is not placed this will return the captured
        inventory snapshot instead.

        Returns:
            Inventory: the inventory
        """