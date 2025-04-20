from org.bukkit.event.inventory import InventoryClickEvent
from org.bukkit.inventory import InventoryView, SmithingInventory
from org.bukkit.event.inventory import InventoryType
from org.bukkit.event.inventory import ClickType
from org.bukkit.event.inventory import InventoryAction
from typing import Literal

class SmithItemEvent(InventoryClickEvent):
    """
    Called when the recipe of an Item is completed inside a smithing table.
    """

    def __init__(self, view: InventoryView, type: InventoryType.SlotType, slot: int, click: ClickType, action: InventoryAction) -> None:
        ...

    def __init__(self, view: InventoryView, type: InventoryType.SlotType, slot: int, click: ClickType, action: InventoryAction, key: int) -> None:
        ...

    def get_inventory(self) -> SmithingInventory:
        ...