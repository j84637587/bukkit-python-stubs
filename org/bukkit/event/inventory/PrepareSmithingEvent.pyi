from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.inventory.InventoryView import InventoryView
from org.bukkit.inventory.ItemStack import ItemStack
from org.bukkit.inventory.SmithingInventory import SmithingInventory
from typing import Optional

class PrepareSmithingEvent(PrepareInventoryResultEvent):
    """
    Called when an item is put in a slot for upgrade by a Smithing Table.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, inventory: InventoryView, result: Optional[ItemStack]) -> None:
        super().__init__(inventory, result)

    def get_inventory(self) -> SmithingInventory:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...