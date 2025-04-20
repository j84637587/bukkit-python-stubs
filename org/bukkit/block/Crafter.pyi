from typing import Protocol
from org.bukkit.loot import Lootable
from org.jetbrains.annotations import ApiStatus

class Crafter(Protocol[Lootable]):
    """Represents a captured state of a crafter."""

    def get_crafting_ticks(self) -> int:
        """
        Gets the number of ticks which this block will remain in the crafting
        state for.

        Returns:
            number of ticks remaining
        """
        ...

    def set_crafting_ticks(self, ticks: int) -> None:
        """
        Sets the number of ticks which this block will remain in the crafting
        state for.

        Args:
            ticks: number of ticks remaining
        """
        ...

    def is_slot_disabled(self, slot: int) -> bool:
        """
        Gets whether the slot at the specified index is disabled and will not
        have items placed in it.

        Args:
            slot: slot index

        Returns:
            disabled status
        """
        ...

    def set_slot_disabled(self, slot: int, disabled: bool) -> None:
        """
        Sets whether the slot at the specified index is disabled and will not
        have items placed in it.

        Args:
            slot: slot index
            disabled: disabled status
        """
        ...

    def is_triggered(self) -> bool:
        """
        Gets whether this Crafter is powered.

        Returns:
            powered status
        """
        ...

    def set_triggered(self, triggered: bool) -> None:
        """
        Sets whether this Crafter is powered.

        Args:
            triggered: powered status
        """
        ...
