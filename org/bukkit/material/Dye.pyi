from org.bukkit import DyeColor
from org.bukkit import Material
from org.bukkit.material import MaterialData
from typing import Any

"""
Represents dye

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Dye(MaterialData):
    def __init__(self: "Dye") -> None:
        super().__init__(Material.LEGACY_INK_SACK)

    def __init__(self: "Dye", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "Dye", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    @param color color of the dye
    """
    def __init__(self: "Dye", color: DyeColor) -> None:
        super().__init__(Material.LEGACY_INK_SACK, color.getDyeData())

    """
    Gets the current color of this dye

    @return DyeColor of this dye
    """
    def getColor(self: "Dye") -> DyeColor:
        ...

    """
    Sets the color of this dye

    @param color New color of this dye
    """
    def setColor(self: "Dye", color: DyeColor) -> None:
        ...

    def __str__(self: "Dye") -> str:
        ...

    def clone(self: "Dye") -> "Dye":
        ...