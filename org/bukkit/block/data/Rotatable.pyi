from org.bukkit.block import BlockFace
from org.bukkit.block.data import BlockData
from typing import Protocol

class Rotatable(Protocol):
    """
    'rotation' represents the current rotation of this block.
    """

    def get_rotation(self) -> BlockFace:
        """
        Gets the value of the 'rotation' property.

        Returns:
            BlockFace: the 'rotation' value
        """
        ...

    def set_rotation(self, rotation: BlockFace) -> None:
        """
        Sets the value of the 'rotation' property.

        Args:
            rotation (BlockFace): the new 'rotation' value
        """
        ...