from org.bukkit.block import BlockFace
from org.bukkit.material import Colorable
from org.bukkit.entity import Golem, Enemy
from typing import Protocol

class Shulker(Protocol, Golem, Colorable, Enemy):
    """
    Interface representing a Shulker entity.
    """

    def get_peek(self) -> float:
        """
        Gets the peek state of the shulker between 0.0 and 1.0.

        Returns:
            float: the peek state of the shulker between 0.0 and 1.0
        """
        ...

    def set_peek(self, value: float) -> None:
        """
        Sets the peek state of the shulker, should be in between 0.0 and 1.0.

        Args:
            value (float): peek state of the shulker, should be in between 0.0 and 1.0

        Raises:
            ValueError: thrown if the value exceeds the valid range in between of 0.0 and 1.0
        """
        ...

    def get_attached_face(self) -> BlockFace:
        """
        Gets the face to which the shulker is attached.

        Returns:
            BlockFace: the face to which the shulker is attached
        """
        ...

    def set_attached_face(self, face: BlockFace) -> None:
        """
        Sets the face to which the shulker is attached.

        Args:
            face (BlockFace): the face to attach the shulker to
        """
        ...