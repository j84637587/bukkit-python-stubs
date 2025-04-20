from org.bukkit.inventory import CrafterInventory
from org.bukkit.inventory import InventoryView
from typing import Protocol

class CrafterView(InventoryView, Protocol):
    """
    An instance of {@link InventoryView} which provides extra methods related to
    crafter view data.
    """

    def get_top_inventory(self) -> CrafterInventory:
        """
        @return: the top inventory
        """
        ...

    def is_slot_disabled(self, slot: int) -> bool:
        """
        Checks if the given crafter slot is disabled.

        @param slot: the slot to check
        @return: true if the slot is disabled otherwise false
        """
        ...

    def is_powered(self) -> bool:
        """
        Checks whether or not this crafter view is powered.

        @return: true if the crafter is powered
        """
        ...

    def set_slot_disabled(self, slot: int, disabled: bool) -> None:
        """
        Sets the status of the crafter slot.

        @param slot: the slot to set the status of
        @param disabled: true if the slot should be disabled otherwise false
        """
        ...