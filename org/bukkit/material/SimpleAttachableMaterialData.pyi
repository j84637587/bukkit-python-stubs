from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from org.bukkit.material import Attachable
from typing import Optional

"""
Simple utility class for attachable MaterialData subclasses.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class SimpleAttachableMaterialData(MaterialData, Attachable):
    
    def __init__(self, type: Material, direction: BlockFace) -> None:
        """
        Initializes a SimpleAttachableMaterialData with the specified type and direction.
        """
        ...

    def __init__(self, type: Material) -> None:
        """
        Initializes a SimpleAttachableMaterialData with the specified type.
        """
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None:
        ...
    
    def getFacing(self) -> Optional[BlockFace]:
        """
        Returns the BlockFace that this material is facing.
        """
        ...
    
    def __str__(self) -> str:
        """
        Returns a string representation of this material data.
        """
        ...
    
    def clone(self) -> 'SimpleAttachableMaterialData':
        """
        Clones this SimpleAttachableMaterialData.
        """
        ...