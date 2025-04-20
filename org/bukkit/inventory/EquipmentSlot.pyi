from typing import Callable
from org.bukkit.inventory.EquipmentSlotGroup import EquipmentSlotGroup
from org.jetbrains.annotations import ApiStatus, NotNull

class EquipmentSlot:
    HAND: 'EquipmentSlot'
    OFF_HAND: 'EquipmentSlot'
    FEET: 'EquipmentSlot'
    LEGS: 'EquipmentSlot'
    CHEST: 'EquipmentSlot'
    HEAD: 'EquipmentSlot'
    BODY: 'EquipmentSlot'
    SADDLE: 'EquipmentSlot'

    def __init__(self: 'EquipmentSlot', group: Callable[[], EquipmentSlotGroup]) -> None:
        """Initializes the EquipmentSlot with a group supplier."""
        ...

            def get_group(self: 'EquipmentSlot') -> EquipmentSlotGroup:
        """Gets the corresponding EquipmentSlotGroup for this slot.

        Returns:
            EquipmentSlotGroup: corresponding EquipmentSlotGroup
        """
        ...