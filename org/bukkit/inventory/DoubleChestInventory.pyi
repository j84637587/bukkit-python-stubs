from org.bukkit.block import DoubleChest
from org.bukkit.inventory import Inventory
from typing import Optional

class DoubleChestInventory(Inventory):
    """
    Interface to the inventory of a Double Chest.
    """

    def get_left_side(self) -> Inventory:
        """
        Get the left half of this double chest.

        Returns:
            The left side inventory
        """
        ...

    def get_right_side(self) -> Inventory:
        """
        Get the right side of this double chest.

        Returns:
            The right side inventory
        """
        ...

    def get_holder(self) -> Optional[DoubleChest]:
        ...