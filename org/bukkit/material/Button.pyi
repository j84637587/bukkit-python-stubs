from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import SimpleAttachableMaterialData
from org.bukkit.material import Redstone

"""
Represents a button

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Button(SimpleAttachableMaterialData, Redstone):
    def __init__(self: "Button") -> None:
        ...

    def __init__(self: "Button", type: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "Button", type: Material, data: bytes) -> None:
        ...

    """
    Gets the current state of this Material, indicating if it's powered or
    unpowered

    @return true if powered, otherwise false
    """
    def is_powered(self: "Button") -> bool:
        ...

    """
    Sets the current state of this button

    @param bool whether or not the button is powered
    """
    def set_powered(self: "Button", bool: bool) -> None:
        ...

    """
    Gets the face that this block is attached on

    @return BlockFace attached to
    """
    def get_attached_face(self: "Button") -> BlockFace:
        ...

    """
    Sets the direction this button is pointing toward
    """
    def set_facing_direction(self: "Button", face: BlockFace) -> None:
        ...

    def __str__(self: "Button") -> str:
        ...

    def clone(self: "Button") -> "Button":
        ...