from org.bukkit.entity import Boat
from org.bukkit.inventory import InventoryHolder
from org.bukkit.loot import Lootable

"""
A {@link Boat} with a chest.
"""
class ChestBoat(Boat, InventoryHolder, Lootable):
    pass