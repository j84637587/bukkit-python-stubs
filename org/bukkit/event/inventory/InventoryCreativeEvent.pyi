from org.bukkit.event.inventory import InventoryClickEvent
from org.bukkit.event.inventory import InventoryType
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import ItemStack
from typing import Any
from typing import Optional

class InventoryCreativeEvent(InventoryClickEvent):
    """
    This event is called when a player in creative mode puts down or picks up
    an item in their inventory / hotbar and when they drop items from their
    Inventory while in creative mode.
    """

    def __init__(self, what: InventoryView, type: InventoryType.SlotType, slot: int, newItem: ItemStack) -> None:
        ...

        def get_cursor(self) -> ItemStack:
        ...

    def set_cursor(self, item: ItemStack) -> None:
        ...