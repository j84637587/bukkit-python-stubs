from typing import List
from org.bukkit import Material

"""
Represents textured materials like steps and smooth bricks

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class TexturedMaterial(MaterialData):

    def __init__(self, m: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self, type: Material, data: bytes) -> None:
        ...

    """
    Retrieve a list of possible textures. The first element of the list
    will be used as a default.

    @return a list of possible textures for this block
    """
    def getTextures(self) -> List[Material]:
        ...

    """
    Gets the current Material this block is made of

    @return Material of this block
    """
    def getMaterial(self) -> Material:
        ...

    """
    Sets the material this block is made of

    @param material
            New material of this block
    """
    def setMaterial(self, material: Material) -> None:
        ...

    """
    Get material index from data

    @return index of data in textures list
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def getTextureIndex(self) -> int:
        ...

    """
    Set material index

    @param idx - index of data in textures list
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def setTextureIndex(self, idx: int) -> None:
        ...

    def __str__(self) -> str:
        ...

    def clone(self) -> 'TexturedMaterial':
        ...