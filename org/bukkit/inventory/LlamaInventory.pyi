from org.bukkit.entity import Llama
from org.jetbrains.annotations import Nullable
from org.bukkit.inventory import AbstractHorseInventory
from org.bukkit.inventory import ItemStack

"""
An interface to the inventory of a {@link Llama}.
"""
class LlamaInventory(AbstractHorseInventory):

    """
    Gets the item in the llama's decor slot.

    @return: the decor item
    """
    def get_decor(self) -> Nullable[ItemStack]: ...

    """
    Sets the item in the llama's decor slot.

    @param stack: the new item
    """
    def set_decor(self, stack: Nullable[ItemStack]) -> None: ...