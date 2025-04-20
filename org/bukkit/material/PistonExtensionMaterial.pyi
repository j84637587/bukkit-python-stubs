from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from typing import Literal

"""
Material data for the piston extension block

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class PistonExtensionMaterial(MaterialData):
    def __init__(self: "PistonExtensionMaterial", type: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "PistonExtensionMaterial", type: Material, data: bytes) -> None:
        ...

    def set_facing_direction(self: "PistonExtensionMaterial", face: BlockFace) -> None:
        ...

    def get_facing(self: "PistonExtensionMaterial") -> BlockFace:
        ...

    """
    Checks if this piston extension is sticky, and returns true if so

    @return true if this piston is "sticky", or false
    """
    def is_sticky(self: "PistonExtensionMaterial") -> bool:
        ...

    """
    Sets whether or not this extension is sticky

    @param sticky true if sticky, otherwise false
    """
    def set_sticky(self: "PistonExtensionMaterial", sticky: bool) -> None:
        ...

    def get_attached_face(self: "PistonExtensionMaterial") -> BlockFace:
        ...

    def clone(self: "PistonExtensionMaterial") -> "PistonExtensionMaterial":
        ...