from org.bukkit import Material
from org.bukkit.material import ExtendedRails
from org.bukkit.material import Redstone

class PoweredRail(ExtendedRails, Redstone):
    """
    Represents a powered rail

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """

    def __init__(self: "PoweredRail") -> None:
        ...

    def __init__(self: "PoweredRail", type: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "PoweredRail", type: Material, data: bytes) -> None:
        ...

    def is_powered(self: "PoweredRail") -> bool:
        ...

    """
    Set whether this PoweredRail should be powered or not.

    @param isPowered whether or not the rail is powered
    """
    def set_powered(self: "PoweredRail", is_powered: bool) -> None:
        ...

    def clone(self: "PoweredRail") -> "PoweredRail":
        ...