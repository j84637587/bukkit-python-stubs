from org.bukkit import Material
from org.bukkit.material import MaterialData
from org.bukkit.material import Redstone

"""
Represents a command block

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Command(MaterialData, Redstone):
    def __init__(self: "Command") -> None:
        super().__init__(Material.LEGACY_COMMAND)

    def __init__(self: "Command", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "Command", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    Gets the current state of this Material, indicating if it's powered or
    unpowered

    @return true if powered, otherwise false
    """
    def is_powered(self: "Command") -> bool:
        ...

    """
    Sets the current state of this Material

    @param bool
                whether or not the command block is powered
    """
    def set_powered(self: "Command", bool: bool) -> None:
        ...

    def __str__(self: "Command") -> str:
        ...

    def clone(self: "Command") -> "Command":
        ...