from typing import Set
from org.bukkit.block.data import Directional
from org.jetbrains.annotations import NotNull

class ChiseledBookshelf(Directional):
    """
    Interface to the 'slot_0_occupied', 'slow_1_occupied' ... 'slot_5_occupied'
    flags on a bookshelf which indicate which slots are occupied rendered on the
    outside.
    <br>
    Block may have 0, 1... {@link #getMaximumOccupiedSlots()}-1 occupied slots.
    """

    def is_slot_occupied(self, slot: int) -> bool:
        """
        Checks if the following slot is occupied.

        :param slot: to check
        :return: if slot is occupied
        """
        ...

    def set_slot_occupied(self, slot: int, occupied: bool) -> None:
        """
        Sets whether the following slot is occupied.

        :param slot: to set
        :param occupied: book
        """
        ...

        def get_occupied_slots(self) -> Set[int]:
        """
        Get the indexes of all the occupied slots present on this block.

        :return: set of all occupied slots
        """
        ...

    def get_maximum_occupied_slots(self) -> int:
        """
        Get the maximum amount of slots on this block.

        :return: maximum occupied slots count
        """
        ...