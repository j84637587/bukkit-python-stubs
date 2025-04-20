from org.bukkit.block.data import BlockData
from org.jetbrains.annotations import NotNull
from typing import Literal

class Crafter(BlockData):
    """
    'orientation' is the direction the block is facing.
    <br>
    Similar to {@link Powerable}, 'triggered' indicates whether or not the
    dispenser is currently activated.
    <br>
    'crafting' is whether crafter's mouth is open and top is glowing.
    """

    def is_crafting(self) -> bool:
        """
        Gets the value of the 'crafting' property.

        @return: the 'crafting' value
        """
        ...

    def set_crafting(self, crafting: bool) -> None:
        """
        Sets the value of the 'crafting' property.

        @param crafting: the new 'crafting' value
        """
        ...

    def is_triggered(self) -> bool:
        """
        Gets the value of the 'triggered' property.

        @return: the 'triggered' value
        """
        ...

    def set_triggered(self, triggered: bool) -> None:
        """
        Sets the value of the 'triggered' property.

        @param triggered: the new 'triggered' value
        """
        ...

        def get_orientation(self) -> 'Orientation':
        """
        Gets the value of the 'orientation' property.

        @return: the 'orientation' value
        """
        ...

    def set_orientation(self, orientation: 'Orientation') -> None:
        """
        Sets the value of the 'orientation' property.

        @param orientation: the new 'orientation' value
        """
        ...

class Orientation:
    """
    The directions the Crafter can be oriented.
    """
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