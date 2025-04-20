from org.bukkit.block import BlockFace
from typing import Protocol

class Directional(Protocol):
    """
    Interface for directional blocks.
    """

    def set_facing_direction(self, face: BlockFace) -> None:
        """
        Sets the direction that this block is facing in.

        :param face: The facing direction
        """
        ...

    def get_facing(self) -> BlockFace:
        """
        Gets the direction this block is facing.

        :return: the direction this block is facing
        """
        ...