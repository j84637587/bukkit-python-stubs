from org.bukkit.inventory import ItemStack
from typing import Protocol

class ThrowableProjectile(Protocol):
    """
    Interface for throwable projectiles.
    """

    def get_item(self) -> ItemStack:
        """
        Gets the ItemStack the thrown projectile will display.

        Returns:
            The thrown item display ItemStack.
        """
        ...

    def set_item(self, item: ItemStack) -> None:
        """
        Sets the display ItemStack for the thrown projectile.

        Args:
            item: ItemStack set to be displayed.
        """
        ...