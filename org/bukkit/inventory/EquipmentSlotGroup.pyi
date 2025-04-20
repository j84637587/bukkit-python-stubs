from typing import Dict, Callable, Optional
from org.bukkit.inventory import EquipmentSlot
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

"""
Represents a group of {@link EquipmentSlot}.
"""
class EquipmentSlotGroup(Callable[[EquipmentSlot], bool]):

    BY_NAME: Dict[str, 'EquipmentSlotGroup'] = {}
    ANY: 'EquipmentSlotGroup'
    MAINHAND: 'EquipmentSlotGroup'
    OFFHAND: 'EquipmentSlotGroup'
    HAND: 'EquipmentSlotGroup'
    FEET: 'EquipmentSlotGroup'
    LEGS: 'EquipmentSlotGroup'
    CHEST: 'EquipmentSlotGroup'
    HEAD: 'EquipmentSlotGroup'
    ARMOR: 'EquipmentSlotGroup'
    SADDLE: 'EquipmentSlotGroup'

    def __init__(self, key: str, predicate: Callable[[EquipmentSlot], bool], example: EquipmentSlot) -> None:
        self.key: str = key
        self.predicate: Callable[[EquipmentSlot], bool] = predicate
        self.example: EquipmentSlot = example

        EquipmentSlotGroup.BY_NAME[key] = self

    def __call__(self, test: EquipmentSlot) -> bool:
        return self.predicate(test)

    def __str__(self) -> str:
        return self.key

    """
    Gets an {@link EquipmentSlot} which is an example of a slot in this
    group.

    @return an example slot
    @deprecated for internal compatibility use only
    """
        @Deprecated(since="1.20.5")
        def get_example(self) -> EquipmentSlot:
        return self.example

    """
    Gets the {@link EquipmentSlotGroup} corresponding to the given string.

    @param name group name
    @return associated group or null
    """
            @staticmethod
    def get_by_name(name: str) -> Optional['EquipmentSlotGroup']:
        Preconditions.checkArgument(name is not None, "Name cannot be null")

        return EquipmentSlotGroup.BY_NAME.get(name.lower())

    @staticmethod
    def get(key: str, slot: EquipmentSlot) -> 'EquipmentSlotGroup':
        return EquipmentSlotGroup.get(key, lambda test: test == slot, slot)

    @staticmethod
    def get(key: str, predicate: Callable[[EquipmentSlot], bool], example: EquipmentSlot) -> 'EquipmentSlotGroup':
        return EquipmentSlotGroup(key, predicate, example)