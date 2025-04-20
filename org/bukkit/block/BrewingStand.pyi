from typing import Protocol
from org.bukkit.inventory import BrewerInventory

class BrewingStand(Protocol):
    """
    Represents a captured state of a brewing stand.
    """

    def get_brewing_time(self) -> int:
        """
        How much time is left in the brewing cycle.

        Returns:
            Brew Time
        """
        ...

    def set_brewing_time(self, brew_time: int) -> None:
        """
        Set the time left before brewing completes.

        Args:
            brew_time: Brewing time
        """
        ...

    def get_fuel_level(self) -> int:
        """
        Get the level of current fuel for brewing.

        Returns:
            The fuel level
        """
        ...

    def set_fuel_level(self, level: int) -> None:
        """
        Set the level of current fuel for brewing.

        Args:
            level: fuel level
        """
        ...

    def get_inventory(self) -> BrewerInventory:
        ...
    
    def get_snapshot_inventory(self) -> BrewerInventory:
        ...