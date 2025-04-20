from typing import List, Optional
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory.meta import ItemMeta

class CrossbowMeta(ItemMeta):
    """
    Interface for CrossbowMeta.
    """

    def has_charged_projectiles(self) -> bool:
        """
        Returns whether the item has any charged projectiles.

        Returns:
            bool: whether charged projectiles are present
        """
        ...

    def get_charged_projectiles(self) -> List[ItemStack]:
        """
        Returns an immutable list of the projectiles charged on this item.

        Returns:
            List[ItemStack]: charged projectiles
        """
        ...

    def set_charged_projectiles(self, projectiles: Optional[List[ItemStack]]) -> None:
        """
        Sets the projectiles charged on this item.

        Removes all projectiles when given None.

        Args:
            projectiles (Optional[List[ItemStack]]): the projectiles to set

        Raises:
            IllegalArgumentException: if one of the projectiles is not an
            arrow or firework rocket
        """
        ...

    def add_charged_projectile(self, item: ItemStack) -> None:
        """
        Adds a charged projectile to this item.

        Args:
            item (ItemStack): projectile

        Raises:
            IllegalArgumentException: if the projectile is not an arrow or
            firework rocket
        """
        ...