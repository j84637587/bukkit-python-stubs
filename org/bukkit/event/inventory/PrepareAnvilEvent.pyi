from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.inventory.AnvilInventory import AnvilInventory
from org.bukkit.inventory.ItemStack import ItemStack
from org.bukkit.inventory.view.AnvilView import AnvilView
from typing import Optional

class PrepareAnvilEvent(PrepareInventoryResultEvent):
    """
    Called when an item is put in a slot for repair by an anvil.
    """

    handlers: HandlerList

    def __init__(self, inventory: AnvilView, result: Optional[ItemStack]) -> None:
        ...

    def get_inventory(self) -> AnvilInventory:
        ...

    def get_view(self) -> AnvilView:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...