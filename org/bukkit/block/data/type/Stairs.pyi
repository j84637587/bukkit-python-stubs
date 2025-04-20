from org.bukkit.block.data import Bisected
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Waterlogged
from typing import Literal

class Stairs(Bisected, Directional, Waterlogged):
    """
    'shape' represents the texture and bounding box shape of these stairs.
    """

    def get_shape(self) -> 'Shape':
        """
        Gets the value of the 'shape' property.

        Returns:
            Shape: the 'shape' value
        """
        ...

    def set_shape(self, shape: 'Shape') -> None:
        """
        Sets the value of the 'shape' property.

        Args:
            shape (Shape): the new 'shape' value
        """
        ...

    class Shape:
        """
        The shape of a stair block - used for constructing corners.
        """
        STRAIGHT: Literal['STRAIGHT'] = 'STRAIGHT'
        INNER_LEFT: Literal['INNER_LEFT'] = 'INNER_LEFT'
        INNER_RIGHT: Literal['INNER_RIGHT'] = 'INNER_RIGHT'
        OUTER_LEFT: Literal['OUTER_LEFT'] = 'OUTER_LEFT'
        OUTER_RIGHT: Literal['OUTER_RIGHT'] = 'OUTER_RIGHT'