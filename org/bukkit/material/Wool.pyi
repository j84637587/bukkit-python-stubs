from org.bukkit import DyeColor
from org.bukkit import Material
from org.bukkit.material import MaterialData
from org.bukkit.material import Colorable

"""
Represents a Wool/Cloth block
@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Wool(MaterialData, Colorable):
    def __init__(self: "Wool") -> None:
        super().__init__(Material.LEGACY_WOOL)

    def __init__(self: "Wool", color: DyeColor) -> None:
        self()
        self.setColor(color)

    def __init__(self: "Wool", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "Wool", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    Gets the current color of this dye

    @return DyeColor of this dye
    """
    def getColor(self: "Wool") -> DyeColor:
        ...

    """
    Sets the color of this dye

    @param color New color of this dye
    """
    def setColor(self: "Wool", color: DyeColor) -> None:
        ...

    def __str__(self: "Wool") -> str:
        ...

    def clone(self: "Wool") -> "Wool":
        ...