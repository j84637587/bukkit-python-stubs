from org.bukkit import Material
from org.bukkit import SandstoneType
from org.bukkit.material import MaterialData

"""
Represents the different types of sandstone.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Sandstone(MaterialData):
    def __init__(self: "Sandstone") -> None:
        ...

    def __init__(self: "Sandstone", type: SandstoneType) -> None:
        ...

    def __init__(self: "Sandstone", type: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "Sandstone", type: Material, data: int) -> None:
        ...

    """
    Gets the current type of this sandstone

    @return SandstoneType of this sandstone
    """
    def get_type(self: "Sandstone") -> SandstoneType:
        ...

    """
    Sets the type of this sandstone

    @param type New type of this sandstone
    """
    def set_type(self: "Sandstone", type: SandstoneType) -> None:
        ...

    def __str__(self: "Sandstone") -> str:
        ...

    def clone(self: "Sandstone") -> "Sandstone":
        ...