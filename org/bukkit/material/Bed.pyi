from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from org.bukkit.material import Directional

"""
Represents a bed.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Bed(MaterialData, Directional):
    """
    Default constructor for a bed.
    """
    def __init__(self) -> None: ...

    """
    Instantiate a bed facing in a particular direction.

    @param direction the direction the bed's head is facing
    """
    def __init__(self, direction: BlockFace) -> None: ...

    def __init__(self, type: Material) -> None: ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None: ...

    """
    Determine if this block represents the head of the bed

    @return true if this is the head of the bed, false if it is the foot
    """
    def is_head_of_bed(self) -> bool: ...

    """
    Configure this to be either the head or the foot of the bed

    @param is_head_of_bed True to make it the head.
    """
    def set_head_of_bed(self, is_head_of_bed: bool) -> None: ...

    """
    Set which direction the head of the bed is facing. Note that this will
    only affect one of the two blocks the bed is made of.
    """
    def set_facing_direction(self, face: BlockFace) -> None: ...

    """
    Get the direction that this bed's head is facing toward

    @return the direction the head of the bed is facing
    """
    def get_facing(self) -> BlockFace: ...

    def __str__(self) -> str: ...

    def clone(self) -> 'Bed': ...