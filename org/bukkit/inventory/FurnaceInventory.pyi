from org.bukkit.inventory import Inventory
from org.bukkit.block import Furnace
from org.jetbrains.annotations import Nullable
from org.bukkit.inventory import ItemStack

"""
Interface to the inventory of a Furnace.
"""
class FurnaceInventory(Inventory):

    """
    Get the current item in the result slot.

    @return The item
    """
    def get_result(self) -> Nullable[ItemStack]: ...

    """
    Get the current fuel.

    @return The item
    """
    def get_fuel(self) -> Nullable[ItemStack]: ...

    """
    Get the item currently smelting.

    @return The item
    """
    def get_smelting(self) -> Nullable[ItemStack]: ...

    """
    Set the current fuel.

    @param stack The item
    """
    def set_fuel(self, stack: Nullable[ItemStack]) -> None: ...

    """
    Set the current item in the result slot.

    @param stack The item
    """
    def set_result(self, stack: Nullable[ItemStack]) -> None: ...

    """
    Set the item currently smelting.

    @param stack The item
    """
    def set_smelting(self, stack: Nullable[ItemStack]) -> None: ...

    """
    @return The holder of the inventory.
    """
    def get_holder(self) -> Nullable[Furnace]: ...