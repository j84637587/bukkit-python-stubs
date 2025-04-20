from org.bukkit.entity import Minecart
from org.bukkit.inventory import InventoryHolder
from org.bukkit.loot import Lootable

"""
Represents a minecart with a chest. These types of {@link Minecart
minecarts} have their own inventory that can be accessed using methods
from the {@link InventoryHolder} interface.
"""
class StorageMinecart(Minecart, InventoryHolder, Lootable):
    pass