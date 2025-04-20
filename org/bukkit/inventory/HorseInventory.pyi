from typing import Optional
from org.bukkit.inventory import AbstractHorseInventory
from org.bukkit.inventory import ItemStack

class HorseInventory(AbstractHorseInventory):
    """
    An interface to the inventory of a Horse.
    """

    def get_saddle(self) -> Optional[ItemStack]:
        """
        Gets the item in the horse's saddle slot.

        Returns:
            Optional[ItemStack]: the saddle item
        """
        ...

    def set_saddle(self, stack: Optional[ItemStack]) -> None:
        """
        Sets the item in the horse's saddle slot.

        Args:
            stack (Optional[ItemStack]): the new item
        """
        ...

    def get_armor(self) -> Optional[ItemStack]:
        """
        Gets the item in the horse's armor slot.

        Returns:
            Optional[ItemStack]: the armor item
        """
        ...

    def set_armor(self, stack: Optional[ItemStack]) -> None:
        """
        Sets the item in the horse's armor slot.

        Args:
            stack (Optional[ItemStack]): the new item
        """
        ...