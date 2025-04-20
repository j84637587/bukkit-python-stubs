from org.bukkit.block import BlockFace
from org.bukkit.block.data import Waterlogged
from typing import Protocol, Type

class Wall(Waterlogged, Protocol):
    """
    This class encompasses the 'north', 'east', 'south', 'west', height flags
    which are used to set the height of a wall.

    'up' denotes whether the well has a center post.
    """

    def is_up(self) -> bool:
        """
        Gets the value of the 'up' property.

        @return: the 'up' value
        """
        ...

    def set_up(self, up: bool) -> None:
        """
        Sets the value of the 'up' property.

        @param up: the new 'up' value
        """
        ...

    def get_height(self, face: BlockFace) -> 'Height':
        """
        Gets the height of the specified face.

        @param face: to check
        @return: if face is enabled
        """
        ...

    def set_height(self, face: BlockFace, height: 'Height') -> None:
        """
        Set the height of the specified face.

        @param face: to set
        @param height: the height
        """
        ...

class Height:
    """
    The different heights a face of a wall may have.
    """
    NONE: Type['Height']
    LOW: Type['Height']
    TALL: Type['Height']