from org.bukkit.entity import Minecart
from org.bukkit.inventory import InventoryHolder
from org.bukkit.loot import Lootable

"""
Represents a Minecart with a Hopper inside it
"""
class HopperMinecart(Minecart, InventoryHolder, Lootable):
    
    """
    Checks whether or not this Minecart will pick up
    items into its inventory.

    @return true if the Minecart will pick up items
    """
    def is_enabled(self) -> bool: ...
    
    """
    Sets whether this Minecart will pick up items.

    @param enabled new enabled state
    """
    def set_enabled(self, enabled: bool) -> None: ...