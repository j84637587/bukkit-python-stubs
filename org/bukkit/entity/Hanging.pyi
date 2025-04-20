from org.bukkit.block import BlockFace
from org.bukkit.material import Attachable
from org.bukkit.entity import Entity
from typing import Protocol

class Hanging(Protocol[Entity, Attachable]):
    """Represents a Hanging entity"""

    def set_facing_direction(self, face: BlockFace, force: bool) -> bool:
        """
        Sets the direction of the hanging entity, potentially overriding rules
        of placement. Note that if the result is not valid the object would
        normally drop as an item.

        Args:
            face: The new direction.
            force: Whether to force it.

        Returns:
            False if force was false and there was no block for it to
            attach to in order to face the given direction.
        """
        ...
