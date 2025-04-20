from typing import Optional
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import ItemStack

class BeaconInventory(Inventory):
    """Interface to the inventory of a Beacon."""

    def set_item(self, item: Optional[ItemStack]) -> None:
        """Set the item powering the beacon.

        Args:
            item: The new item
        """
        ...

    def get_item(self) -> Optional[ItemStack]:
        """Get the item powering the beacon.

        Returns:
            The current item.
        """
        ...