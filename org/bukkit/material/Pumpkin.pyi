from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from org.bukkit.material import Directional

"""
Represents a pumpkin.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Pumpkin(MaterialData, Directional):

    def __init__(self) -> None:
        ...

    """
    Instantiate a pumpkin facing in a particular direction.

    @param direction the direction the pumpkin's face is facing
    """
    def __init__(self, direction: BlockFace) -> None:
        ...

    def __init__(self, type: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None:
        ...

    def is_lit(self) -> bool:
        ...

    def set_facing_direction(self, face: BlockFace) -> None:
        ...

    def get_facing(self) -> BlockFace:
        ...

    def __str__(self) -> str:
        ...

    def clone(self) -> 'Pumpkin':
        ...