from org.bukkit.GrassSpecies import GrassSpecies
from org.bukkit.Material import Material
from org.bukkit.TreeSpecies import TreeSpecies
from org.bukkit.material.MaterialData import MaterialData
from org.bukkit.material.Tree import Tree
from org.bukkit.material.LongGrass import LongGrass

"""
Represents a flower pot.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class FlowerPot(MaterialData):

    """
    Default constructor for a flower pot.
    """
    def __init__(self) -> None: ...

    def __init__(self, type: Material) -> None: ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None: ...

    """
    Get the material in the flower pot

    @return material MaterialData for the block currently in the flower pot
        or null if empty
    """
    def get_contents(self) -> MaterialData: ...

    """
    Set the contents of the flower pot

    @param materialData MaterialData of the block to put in the flower pot.
    """
    def set_contents(self, materialData: MaterialData) -> None: ...

    def __str__(self) -> str: ...

    def clone(self) -> 'FlowerPot': ...