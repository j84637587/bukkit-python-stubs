from org.bukkit.util import BoundingBox
from typing import Protocol

"""
Represents an individual part of a {@link GeneratedStructure}.

@see GeneratedStructure
"""
class StructurePiece(Protocol):

    """
    Gets the bounding box of this structure piece.

    @return: bounding box of this structure piece
    """
    def get_bounding_box(self) -> BoundingBox:
        ...