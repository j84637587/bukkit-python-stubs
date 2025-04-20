from org.bukkit.Material import Material
from org.bukkit.block import BrewingStand
from org.jetbrains.annotations import Nullable
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import ItemStack

"""
Interface to the inventory of a Brewing Stand.
"""
class BrewerInventory(Inventory):

    """
    Get the current ingredient for brewing.

    @return The ingredient.
    """
    def get_ingredient(self) -> Nullable[ItemStack]: ...

    """
    Set the current ingredient for brewing.

    @param ingredient The ingredient
    """
    def set_ingredient(self, ingredient: Nullable[ItemStack]) -> None: ...

    """
    Get the current fuel for brewing.

    @return The fuel
    """
    def get_fuel(self) -> Nullable[ItemStack]: ...

    """
    Set the current fuel for brewing. Generally only
    {@link Material#BLAZE_POWDER} will be of use.

    @param fuel The fuel
    """
    def set_fuel(self, fuel: Nullable[ItemStack]) -> None: ...

    @Override
    """
    Get the holder of the inventory.

    @return The holder.
    """
    def get_holder(self) -> Nullable[BrewingStand]: ...