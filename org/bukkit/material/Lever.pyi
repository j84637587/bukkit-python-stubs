from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import SimpleAttachableMaterialData
from org.bukkit.material import Redstone

"""
Represents a lever

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Lever(SimpleAttachableMaterialData, Redstone):
    def __init__(self: "Lever") -> None:
        super().__init__(Material.LEGACY_LEVER)

    def __init__(self: "Lever", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "Lever", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    Gets the current state of this Material, indicating if it's powered or
    unpowered

    @return true if powered, otherwise false
    """
    def is_powered(self: "Lever") -> bool:
        ...

    """
    Set this lever to be powered or not.

    @param isPowered whether the lever should be powered or not
    """
    def set_powered(self: "Lever", is_powered: bool) -> None:
        ...

    """
    Gets the face that this block is attached on

    @return BlockFace attached to
    """
    def get_attached_face(self: "Lever") -> BlockFace:
        ...

    """
    Sets the direction this lever is pointing in
    """
    def set_facing_direction(self: "Lever", face: BlockFace) -> None:
        ...

    def __str__(self: "Lever") -> str:
        ...

    def clone(self: "Lever") -> "Lever":
        ...