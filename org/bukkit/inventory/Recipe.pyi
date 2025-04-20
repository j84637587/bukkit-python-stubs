from org.bukkit.inventory import ItemStack
from typing import Protocol

class Recipe(Protocol):
    """Represents some type of crafting recipe."""

    def get_result(self) -> ItemStack:
        """Get the result of this recipe.

        Returns:
            ItemStack: The result stack
        """