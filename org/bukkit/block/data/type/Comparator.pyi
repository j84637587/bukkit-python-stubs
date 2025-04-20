from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable
from typing import Literal

class Comparator(Directional, Powerable):
    """
    'mode' indicates what mode this comparator will operate in.
    """

    def get_mode(self) -> 'Mode':
        """
        Gets the value of the 'mode' property.

        Returns:
            Mode: the 'mode' value
        """
        ...

    def set_mode(self, mode: 'Mode') -> None:
        """
        Sets the value of the 'mode' property.

        Args:
            mode (Mode): the new 'mode' value
        """
        ...

class Mode:
    """
    The mode in which a comparator will operate in.
    """
    COMPARE: Literal['COMPARE'] = 'COMPARE'
    SUBTRACT: Literal['SUBTRACT'] = 'SUBTRACT'