from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from org.bukkit.material import Directional

"""
Represents stairs.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Stairs(MaterialData, Directional):

    def __init__(self: "Stairs", type: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self: "Stairs", type: Material, data: bytes) -> None:
        ...

    """
    @return the direction the stairs ascend towards
    """
    def getAscendingDirection(self: "Stairs") -> BlockFace:
        ...

    """
    @return the direction the stairs descend towards
    """
    def getDescendingDirection(self: "Stairs") -> BlockFace:
        ...

    """
    Set the direction the stair part of the block is facing
    """
    def setFacingDirection(self: "Stairs", face: BlockFace) -> None:
        ...

    """
    @return the direction the stair part of the block is facing
    """
    def getFacing(self: "Stairs") -> BlockFace:
        ...

    """
    Test if step is inverted

    @return true if inverted (top half), false if normal (bottom half)
    """
    def isInverted(self: "Stairs") -> bool:
        ...

    """
    Set step inverted state

    @param inv - true if step is inverted (top half), false if step is
        normal (bottom half)
    """
    def setInverted(self: "Stairs", inv: bool) -> None:
        ...

    def __str__(self: "Stairs") -> str:
        ...

    def clone(self: "Stairs") -> "Stairs":
        ...