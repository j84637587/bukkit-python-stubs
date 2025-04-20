from org.bukkit.block.data import Directional
from typing import Literal

class TechnicalPiston(Directional):
    """
    'type' represents the type of piston which this (technical) block corresponds
    to.
    """

    def get_type(self) -> 'Type':
        """
        Gets the value of the 'type' property.

        Returns:
            The 'type' value
        """
        ...

    def set_type(self, type: 'Type') -> None:
        """
        Sets the value of the 'type' property.

        Args:
            type: The new 'type' value
        """
        ...

    class Type:
        """
        Different piston variants.
        """
        NORMAL: Literal['NORMAL']
        STICKY: Literal['STICKY']