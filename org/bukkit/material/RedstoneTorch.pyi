from org.bukkit import Material
from org.bukkit.material import Torch
from org.bukkit.material import Redstone

class RedstoneTorch(Torch, Redstone):
    """
    Represents a redstone torch

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """

    def __init__(self: "RedstoneTorch") -> None:
        ...

    def __init__(self: "RedstoneTorch", type: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "RedstoneTorch", type: Material, data: bytes) -> None:
        ...

    """
    Gets the current state of this Material, indicating if it's powered or
    unpowered

    @return true if powered, otherwise false
    """
    def isPowered(self: "RedstoneTorch") -> bool:
        ...

    def __str__(self: "RedstoneTorch") -> str:
        ...

    def clone(self: "RedstoneTorch") -> "RedstoneTorch":
        ...