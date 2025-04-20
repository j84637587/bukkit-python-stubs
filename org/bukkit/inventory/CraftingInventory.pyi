from typing import Optional, List
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory import Recipe

class CraftingInventory(Inventory):
    """
    Interface to the crafting inventories
    """

    def get_result(self) -> Optional[ItemStack]:
        """
        Check what item is in the result slot of this crafting inventory.

        Returns:
            The result item.
        """
        ...

    def get_matrix(self) -> List[Optional[ItemStack]]:
        """
        Get the contents of the crafting matrix.

        Returns:
            The contents. Individual entries may be null.
        """
        ...

    def set_result(self, new_result: Optional[ItemStack]) -> None:
        """
        Set the item in the result slot of the crafting inventory.

        Args:
            new_result: The new result item.
        """
        ...

    def set_matrix(self, contents: List[Optional[ItemStack]]) -> None:
        """
        Replace the contents of the crafting matrix

        Args:
            contents: The new contents. Individual entries may be null.

        Raises:
            IllegalArgumentException: if the length of contents is greater
            than the size of the crafting matrix.
        """
        ...

    def get_recipe(self) -> Optional[Recipe]:
        """
        Get the current recipe formed on the crafting inventory, if any.

        Returns:
            The recipe, or null if the current contents don't match any
            recipe.
        """
        ...