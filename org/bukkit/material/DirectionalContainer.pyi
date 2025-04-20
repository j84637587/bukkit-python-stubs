from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from typing import Type

"""
Represents a furnace or a dispenser.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class DirectionalContainer(MaterialData):

    def __init__(self, type: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None:
        ...

    def set_facing_direction(self, face: BlockFace) -> None:
        ...

    def get_facing(self) -> BlockFace:
        ...

    def __str__(self) -> str:
        ...

    def clone(self) -> Type['DirectionalContainer']:
        ...