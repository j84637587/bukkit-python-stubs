# structure_rotation.pyi

from enum import Enum

class StructureRotation(Enum):
    """
    Represents how a Structure can be rotated.
    """
    NONE: StructureRotation
    CLOCKWISE_90: StructureRotation
    CLOCKWISE_180: StructureRotation
    COUNTERCLOCKWISE_90: StructureRotation