from org.bukkit.inventory import Inventory
from org.bukkit.inventory import InventoryHolder
from org.bukkit.inventory import Merchant
from org.jetbrains.annotations import NotNull
from typing import Protocol

class AbstractVillager(Protocol):
    """
    Represents a villager NPC
    """

        def get_inventory(self) -> Inventory:
        """
        Gets this villager's inventory.
        Note that this inventory is not the Merchant inventory, rather, it is the
        items that a villager might have collected (from harvesting crops, etc.)
        """
        ...