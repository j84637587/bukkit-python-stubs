from org.bukkit.block.data import Bisected
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Openable
from org.bukkit.block.data import Powerable
from typing import Literal

class Door(Bisected, Directional, Openable, Powerable):
    """
    'hinge' indicates which hinge this door is attached to and will rotate around
    when opened.
    """

    def get_hinge(self) -> 'Hinge':
        """
        Gets the value of the 'hinge' property.

        Returns:
            Hinge: the 'hinge' value
        """
        ...

    def set_hinge(self, hinge: 'Hinge') -> None:
        """
        Sets the value of the 'hinge' property.

        Args:
            hinge (Hinge): the new 'hinge' value
        """
        ...

class Hinge:
    """
    The hinge of a door.
    """
    LEFT: Literal['LEFT']
    RIGHT: Literal['RIGHT']