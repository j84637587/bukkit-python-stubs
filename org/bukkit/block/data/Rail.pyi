from typing import Set
from org.bukkit.block.data.Waterlogged import Waterlogged
from org.jetbrains.annotations import NotNull

"""
'shape' represents the current layout of a minecart rail.
<br>
Some types of rail may not be able to be laid out in all shapes, use
:get_shapes: to get those applicable to this block.
"""
class Rail(Waterlogged):

    """
    Gets the value of the 'shape' property.

    @return: the 'shape' value
    """
        def get_shape(self) -> 'Shape':
        ...

    """
    Sets the value of the 'shape' property.

    @param shape: the new 'shape' value
    """
    def set_shape(self, shape: 'Shape') -> None:
        ...

    """
    Gets the shapes which are applicable to this block.

    @return: the allowed 'shape' values
    """
        def get_shapes(self) -> Set['Shape']:
        ...


    """
    The different types of shapes a rail block can occupy.
    """
    class Shape:
        """
        The rail runs flat along the north/south (Z) axis.
        """
        NORTH_SOUTH = ...

        """
        The rail runs flat along the east/west (X) axis.
        """
        EAST_WEST = ...

        """
        The rail ascends in the east (positive X) direction.
        """
        ASCENDING_EAST = ...

        """
        The rail ascends in the west (negative X) direction.
        """
        ASCENDING_WEST = ...

        """
        The rail ascends in the north (negative Z) direction.
        """
        ASCENDING_NORTH = ...

        """
        The rail ascends in the south (positive Z) direction.
        """
        ASCENDING_SOUTH = ...

        """
        The rail forms a curve connecting the south and east faces of the
        block.
        """
        SOUTH_EAST = ...

        """
        The rail forms a curve connecting the south and west faces of the
        block.
        """
        SOUTH_WEST = ...

        """
        The rail forms a curve connecting the north and west faces of the
        block.
        """
        NORTH_WEST = ...

        """
        The rail forms a curve connecting the north and east faces of the
        block.
        """
        NORTH_EAST = ...