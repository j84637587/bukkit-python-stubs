from org.bukkit import Material
from org.bukkit.block import BlockFace
from typing import Optional

"""
Represents the cocoa plant

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class CocoaPlant(MaterialData, Directional, Attachable):

    class CocoaPlantSize:
        SMALL = ...
        MEDIUM = ...
        LARGE = ...

    def __init__(self) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self, type: Material, data: int) -> None:
        ...

    def __init__(self, sz: CocoaPlantSize) -> None:
        ...

    def __init__(self, sz: CocoaPlantSize, dir: BlockFace) -> None:
        ...

    """
    Get size of plant

    @return size
    """
    def getSize(self) -> CocoaPlantSize:
        ...

    """
    Set size of plant

    @param sz - size of plant
    """
    def setSize(self, sz: CocoaPlantSize) -> None:
        ...

    def getAttachedFace(self) -> BlockFace:
        ...

    def setFacingDirection(self, face: BlockFace) -> None:
        ...

    def getFacing(self) -> Optional[BlockFace]:
        ...

    def clone(self) -> 'CocoaPlant':
        ...

    def toString(self) -> str:
        ...