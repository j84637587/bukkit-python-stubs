from org.bukkit.block.data import Bisected
from org.bukkit.block.data import Directional
from typing import Literal

class Bed(Directional):
    """
    Similar to {@link Bisected}, 'part' denotes which half of the bed this block
    corresponds to.
    <br>
    'occupied' property is a quick flag to check if a player is currently
    sleeping in this bed block.
    """

    def get_part(self) -> 'Part':
        """
        Gets the value of the 'part' property.

        Returns:
            Part: the 'part' value
        """
        ...

    def set_part(self, part: 'Part') -> None:
        """
        Sets the value of the 'part' property.

        Args:
            part (Part): the new 'part' value
        """
        ...

    def is_occupied(self) -> bool:
        """
        Gets the value of the 'occupied' property.

        Returns:
            bool: the 'occupied' value
        """
        ...


class Part:
    """
    Horizontal half of a bed.
    """
    HEAD: Literal['HEAD']
    FOOT: Literal['FOOT']