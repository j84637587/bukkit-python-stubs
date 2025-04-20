from typing import Optional
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import ItemStack

class EnchantingInventory(Inventory):
    """
    Interface to the inventory of an Enchantment Table.
    """

    def set_item(self, item: Optional[ItemStack]) -> None:
        """
        Set the item being enchanted.

        :param item: The new item
        """
        ...

    def get_item(self) -> Optional[ItemStack]:
        """
        Get the item being enchanted.

        :return: The current item.
        """
        ...

    def set_secondary(self, item: Optional[ItemStack]) -> None:
        """
        Set the secondary item being used for the enchant.

        :param item: The new item
        """
        ...

    def get_secondary(self) -> Optional[ItemStack]:
        """
        Get the secondary item being used for the enchant.

        :return: The second item
        """
        ...