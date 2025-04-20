from typing import Optional
from org.bukkit.Location import Location
from org.bukkit.World import World
from org.bukkit.inventory.DoubleChestInventory import DoubleChestInventory
from org.bukkit.inventory.Inventory import Inventory
from org.bukkit.inventory.InventoryHolder import InventoryHolder

class DoubleChest(InventoryHolder):
    """
    Represents a double chest.
    """

    def __init__(self: "DoubleChest", chest: DoubleChestInventory) -> None:
        ...

    def get_inventory(self: "DoubleChest") -> Inventory:
        ...

    def get_left_side(self: "DoubleChest") -> Optional[InventoryHolder]:
        ...

    def get_right_side(self: "DoubleChest") -> Optional[InventoryHolder]:
        ...

    def get_location(self: "DoubleChest") -> Location:
        ...

    def get_world(self: "DoubleChest") -> Optional[World]:
        ...

    def get_x(self: "DoubleChest") -> float:
        ...

    def get_y(self: "DoubleChest") -> float:
        ...

    def get_z(self: "DoubleChest") -> float:
        ...