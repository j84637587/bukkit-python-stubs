from org.bukkit.inventory import ItemStack
from org.jetbrains.annotations import NotNull

"""
Represents a sized fireball.
"""
class SizedFireball(Fireball):

    """
    Gets the display ItemStack.

    @return display ItemStack
    """
        def get_display_item(self) -> ItemStack: ...

    """
    Sets the display ItemStack for the fireball.

    @param item the ItemStack to display
    """
    def set_display_item(self, item: ItemStack) -> None: ...