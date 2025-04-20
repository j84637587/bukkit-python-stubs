from org.bukkit.block import BlockFace
from typing import Protocol

class Attachable(Protocol):
    """Indicates that a block can be attached to another block"""

    def get_attached_face(self) -> BlockFace:
        """Gets the face that this block is attached on

        Returns:
            BlockFace: attached to
        """
        ...