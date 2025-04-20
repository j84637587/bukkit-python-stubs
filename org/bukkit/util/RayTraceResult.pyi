from typing import Optional

from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Entity
from org.bukkit.util import Vector

class RayTraceResult:
    """
    The hit result of a ray trace.
    <p>
    Only the hit position is guaranteed to always be available. The availability
    of the other attributes depends on what got hit and on the context in which
    the ray trace was performed.
    """

    def __init__(self, hit_position: Vector, hit_block: Optional[Block] = None, 
                 hit_block_face: Optional[BlockFace] = None, 
                 hit_entity: Optional[Entity] = None) -> None:
        ...

    def __init__(self, hit_position: Vector) -> None:
        ...

    def __init__(self, hit_position: Vector, hit_block_face: Optional[BlockFace]) -> None:
        ...

    def __init__(self, hit_position: Vector, hit_block: Optional[Block], 
                 hit_block_face: Optional[BlockFace]) -> None:
        ...

    def __init__(self, hit_position: Vector, hit_entity: Optional[Entity]) -> None:
        ...

    def __init__(self, hit_position: Vector, hit_entity: Optional[Entity], 
                 hit_block_face: Optional[BlockFace]) -> None:
        ...

    def get_hit_position(self) -> Vector:
        """
        Gets the exact position of the hit.

        @return: a copy of the exact hit position
        """
        ...

    def get_hit_block(self) -> Optional[Block]:
        """
        Gets the hit block.

        @return: the hit block, or <code>null</code> if not available
        """
        ...

    def get_hit_block_face(self) -> Optional[BlockFace]:
        """
        Gets the hit block face.

        @return: the hit block face, or <code>null</code> if not available
        """
        ...

    def get_hit_entity(self) -> Optional[Entity]:
        """
        Gets the hit entity.

        @return: the hit entity, or <code>null</code> if not available
        """
        ...

    def __hash__(self) -> int:
        ...

    def __eq__(self, obj: object) -> bool:
        ...

    def __str__(self) -> str:
        ...