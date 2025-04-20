from org.bukkit.block.data import BlockData
from typing import Literal, Protocol

class Jigsaw(Protocol):
    """'orientation' is the direction the block is facing."""

    def get_orientation(self) -> 'Orientation':
        """Gets the value of the 'orientation' property.

        Returns:
            Orientation: the 'orientation' value
        """
        ...

    def set_orientation(self, orientation: 'Orientation') -> None:
        """Sets the value of the 'orientation' property.

        Args:
            orientation (Orientation): the new 'orientation' value
        """
        ...

class Orientation:
    """The directions the Jigsaw can be oriented."""
    
    DOWN_EAST: Literal['DOWN_EAST']
    DOWN_NORTH: Literal['DOWN_NORTH']
    DOWN_SOUTH: Literal['DOWN_SOUTH']
    DOWN_WEST: Literal['DOWN_WEST']
    UP_EAST: Literal['UP_EAST']
    UP_NORTH: Literal['UP_NORTH']
    UP_SOUTH: Literal['UP_SOUTH']
    UP_WEST: Literal['UP_WEST']
    WEST_UP: Literal['WEST_UP']
    EAST_UP: Literal['EAST_UP']
    NORTH_UP: Literal['NORTH_UP']
    SOUTH_UP: Literal['SOUTH_UP']