from typing import Optional
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory import Recipe

class SmithingInventory(Inventory):
    """
    Interface to the inventory of a Smithing table.
    """

    def get_result(self) -> Optional[ItemStack]:
        """
        Check what item is in the result slot of this smithing table.

        Returns:
            the result item
        """
        ...

    def set_result(self, new_result: Optional[ItemStack]) -> None:
        """
        Set the item in the result slot of the smithing table.

        Args:
            new_result: the new result item
        """
        ...

    def get_recipe(self) -> Optional[Recipe]:
        """
        Get the current recipe formed on the smithing table, if any.

        Returns:
            the recipe, or None if the current contents don't match any recipe
        """
        ...