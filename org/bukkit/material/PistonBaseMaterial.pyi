from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from typing import Literal

"""
Material data for the piston base block

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class PistonBaseMaterial(MaterialData):

    def __init__(self: "PistonBaseMaterial", type: Material) -> None:
        ...

    """
    Constructs a PistonBaseMaterial.

    @param type the material type to use
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self: "PistonBaseMaterial", type: Material, data: bytes) -> None:
        ...

    def set_facing_direction(self: "PistonBaseMaterial", face: BlockFace) -> None:
        ...

    def get_facing(self: "PistonBaseMaterial") -> BlockFace:
        ...

    def is_powered(self: "PistonBaseMaterial") -> bool:
        ...

    """
    Sets the current state of this piston

    @param powered true if the piston is extended {@literal &} powered, or false
    """
    def set_powered(self: "PistonBaseMaterial", powered: bool) -> None:
        ...

    """
    Checks if this piston base is sticky, and returns true if so

    @return true if this piston is "sticky", or false
    """
    def is_sticky(self: "PistonBaseMaterial") -> bool:
        ...

    def clone(self: "PistonBaseMaterial") -> "PistonBaseMaterial":
        ...