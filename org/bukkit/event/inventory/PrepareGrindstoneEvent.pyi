from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.inventory.GrindstoneInventory import GrindstoneInventory
from org.bukkit.inventory.InventoryView import InventoryView
from org.bukkit.inventory.ItemStack import ItemStack
from typing import Optional

class PrepareGrindstoneEvent(PrepareInventoryResultEvent):
    """
    Called when an item is put in a slot for repair or unenchanting in a grindstone.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, inventory: InventoryView, result: Optional[ItemStack]) -> None:
        super().__init__(inventory, result)

    def getInventory(self) -> GrindstoneInventory:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...