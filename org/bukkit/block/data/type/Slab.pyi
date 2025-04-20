from org.bukkit.block.data import Waterlogged
from typing import Literal

class Slab(Waterlogged):
    """
    'type' represents what state the slab is in - either top, bottom, or a double
    slab occupying the full block.
    """

    def get_type(self) -> Type:
        """
        Gets the value of the 'type' property.

        Returns:
            Type: the 'type' value
        """
        ...

    def set_type(self, type: Type) -> None:
        """
        Sets the value of the 'type' property.

        Args:
            type (Type): the new 'type' value
        """
        ...

class Type:
    """
    The type of the slab.
    """
    TOP: Literal['TOP']
    BOTTOM: Literal['BOTTOM']
    DOUBLE: Literal['DOUBLE']