from typing import Optional
from .inventory import Inventory
from .inventory import ItemStack

class Campfire(TileState):
    """Represents a captured state of a campfire."""

    def get_size(self) -> int:
        """@return The size of the inventory
        @see Inventory#getSize()
        """
        ...

    def get_item(self, index: int) -> Optional[ItemStack]:
        """@param index The index of the Slot's ItemStack to return
        @return The ItemStack in the slot
        @see Inventory#getItem(int)
        """
        ...

    def set_item(self, index: int, item: Optional[ItemStack]) -> None:
        """@param index The index where to put the ItemStack
        @param item The ItemStack to set
        @see Inventory#setItem(int, org.bukkit.inventory.ItemStack)
        """
        ...

    def get_cook_time(self, index: int) -> int:
        """Get cook time.
        
        This is the amount of time the item has been cooking for.
        
        @param index item slot index
        @return Cook time
        """
        ...

    def set_cook_time(self, index: int, cook_time: int) -> None:
        """Set cook time.
        
        This is the amount of time the item has been cooking for.
        
        @param index item slot index
        @param cook_time Cook time
        """
        ...

    def get_cook_time_total(self, index: int) -> int:
        """Get cook time total.
        
        This is the amount of time the item is required to cook for.
        
        @param index item slot index
        @return Cook time total
        """
        ...

    def set_cook_time_total(self, index: int, cook_time_total: int) -> None:
        """Set cook time.
        
        This is the amount of time the item is required to cook for.
        
        @param index item slot index
        @param cook_time_total Cook time total
        """
        ...