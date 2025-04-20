from typing import Protocol
from org.bukkit.inventory import Inventory

class InventoryHolder(Protocol):
    """
    Get the object's inventory.
    """

    def get_inventory(self) -> Inventory:
        """
        Get the object's inventory.

        Returns:
            The inventory.
        """
        ...