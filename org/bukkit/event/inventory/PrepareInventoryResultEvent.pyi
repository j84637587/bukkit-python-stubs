from org.bukkit.event.inventory import InventoryEvent
from org.bukkit.event import HandlerList
from org.bukkit.inventory import InventoryView, ItemStack
from typing import Optional

class PrepareInventoryResultEvent(InventoryEvent):
    """
    Called when an item is put in a slot and the result is calculated.
    """

    handlers: HandlerList = HandlerList()
    result: Optional[ItemStack]

    def __init__(self, inventory: InventoryView, result: Optional[ItemStack]) -> None:
        super().__init__(inventory)
        self.result = result

    """
    Get result item, may be null.

    @return: result item
    """
    def get_result(self) -> Optional[ItemStack]:
        ...

    """
    Set result item, may be null.

    @param result: result item
    """
    def set_result(self, result: Optional[ItemStack]) -> None:
        ...

    @Override
    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...