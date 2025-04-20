from typing import Protocol
from org.bukkit.inventory import BlockInventoryHolder, ChiseledBookshelfInventory
from org.bukkit.util import Vector
from typing import Optional

class ChiseledBookshelf(Protocol, BlockInventoryHolder):
    """
    Represents a captured state of a chiseled bookshelf.
    """

    def get_last_interacted_slot(self) -> int:
        """
        Gets the last interacted inventory slot.

        Returns:
            int: the last interacted slot
        """
        ...

    def set_last_interacted_slot(self, last_interacted_slot: int) -> None:
        """
        Sets the last interacted inventory slot.

        Args:
            last_interacted_slot (int): the new last interacted slot
        """
        ...

    def get_inventory(self) -> ChiseledBookshelfInventory:
        """
        Returns:
            ChiseledBookshelfInventory: inventory
        """
        ...

    def get_snapshot_inventory(self) -> ChiseledBookshelfInventory:
        """
        Returns:
            ChiseledBookshelfInventory: snapshot inventory
        """
        ...

    def get_slot(self, position: Vector) -> int:
        """
        Gets the appropriate slot based on a vector relative to this block.
        Will return -1 if the given vector is not within the bounds of any slot.

        The supplied vector should only contain components with values between 0.0
        and 1.0, inclusive.

        Args:
            position (Vector): a vector relative to this block

        Returns:
            int: the slot under the given vector or -1
        """
        ...