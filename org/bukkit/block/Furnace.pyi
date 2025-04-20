from typing import Dict, TypeVar
from org.bukkit.inventory import CookingRecipe, FurnaceInventory
from org.jetbrains.annotations import NotNull

T = TypeVar('T', bound=CookingRecipe)

class Furnace:
    """
    Represents a captured state of a furnace.
    """

    def get_burn_time(self) -> int:
        """
        Get burn time.

        Returns:
            Burn time
        """
        ...

    def set_burn_time(self, burn_time: int) -> None:
        """
        Set burn time.

        A burn time greater than 0 will cause this block to be lit, whilst a time
        less than 0 will extinguish it.

        Args:
            burn_time: Burn time
        """
        ...

    def get_cook_time(self) -> int:
        """
        Get cook time.

        This is the amount of time the item has been cooking for.

        Returns:
            Cook time
        """
        ...

    def set_cook_time(self, cook_time: int) -> None:
        """
        Set cook time.

        This is the amount of time the item has been cooking for.

        Args:
            cook_time: Cook time
        """
        ...

    def get_cook_time_total(self) -> int:
        """
        Get cook time total.

        This is the amount of time the item is required to cook for.

        Returns:
            Cook time total
        """
        ...

    def set_cook_time_total(self, cook_time_total: int) -> None:
        """
        Set cook time.

        This is the amount of time the item is required to cook for.

        Args:
            cook_time_total: Cook time total
        """
        ...

        def get_recipes_used(self) -> Dict[T, int]:
        """
        Get the recipes used in this furnace.

        Note: These recipes used are reset when the result item is
        manually taken from the furnace.

        Returns:
            An immutable map with the recipes used and the times used
        """
        ...

        def get_inventory(self) -> FurnaceInventory:
        ...

        def get_snapshot_inventory(self) -> FurnaceInventory:
        ...