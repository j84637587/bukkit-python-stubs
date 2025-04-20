from org.bukkit.block.data import Ageable
from org.bukkit.block.data import Sapling
from typing import Literal

class Bamboo(Ageable, Sapling):
    """
    'leaves' represents the size of the leaves on this bamboo block.
    """

    def get_leaves(self) -> 'Leaves':
        """
        Gets the value of the 'leaves' property.

        Returns:
            Leaves: the 'leaves' value
        """
        ...

    def set_leaves(self, leaves: 'Leaves') -> None:
        """
        Sets the value of the 'leaves' property.

        Args:
            leaves (Leaves): the new 'leaves' value
        """
        ...

class Leaves:
    """
    Bamboo leaf size.
    """
    NONE: Literal['NONE']
    SMALL: Literal['SMALL']
    LARGE: Literal['LARGE']