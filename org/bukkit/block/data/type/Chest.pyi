from org.bukkit.block.data import Directional
from org.bukkit.block.data import Waterlogged
from typing import Literal

class Chest(Directional, Waterlogged):
    """
    'type' represents which part of a double chest this block is, or if it is a
    single chest.
    """

    def get_type(self) -> 'Type':
        """
        Gets the value of the 'type' property.

        Returns:
            Type: the 'type' value
        """
        ...

    def set_type(self, type: 'Type') -> None:
        """
        Sets the value of the 'type' property.

        Args:
            type (Type): the new 'type' value
        """
        ...

    class Type:
        """
        Type of this chest block.
        NB: Left and right are relative to the chest itself, i.e opposite to what
        a player placing the appropriate block would see.
        """
        SINGLE: Literal['SINGLE'] = 'SINGLE'
        LEFT: Literal['LEFT'] = 'LEFT'
        RIGHT: Literal['RIGHT'] = 'RIGHT'