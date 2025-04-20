from org.bukkit.block import DecoratedPot
from org.jetbrains.annotations import Nullable
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import ItemStack

"""
Interface to the inventory of a DecoratedPot.
"""
class DecoratedPotInventory(Inventory):

    """
    Set the item stack in the decorated pot.

    @param item the new item stack
    """
    def set_item(self, item: Nullable[ItemStack]) -> None: ...

    """
    Get the item stack in the decorated pot.

    @return the current item stack
    """
        def get_item(self) -> Nullable[ItemStack]: ...

        def get_holder(self) -> Nullable[DecoratedPot]: ...