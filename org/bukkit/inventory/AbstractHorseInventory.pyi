from org.bukkit.entity import AbstractHorse
from org.jetbrains.annotations import Nullable
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import ItemStack

"""
An interface to the inventory of an {@link AbstractHorse}.
"""
class AbstractHorseInventory(Inventory):

    """
    Gets the item in the horse's saddle slot.

    @return: the saddle item
    @deprecated: llama's cannot have saddles
    """
        def get_saddle(self) -> ItemStack:
        ...

    """
    Sets the item in the horse's saddle slot.

    @param stack: the new item
    @deprecated: llama's cannot have saddles
    """
    def set_saddle(self, stack: Nullable[ItemStack]) -> None:
        ...