from org.bukkit import Material
from org.bukkit.material import MaterialData
from org.bukkit.material import Redstone

class RedstoneWire(MaterialData, Redstone):
    """
    Represents redstone wire

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """

    def __init__(self: "RedstoneWire") -> None:
        super().__init__(Material.LEGACY_REDSTONE_WIRE)

    def __init__(self: "RedstoneWire", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "RedstoneWire", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    Gets the current state of this Material, indicating if it's powered or
    unpowered

    @return true if powered, otherwise false
    """
    def is_powered(self: "RedstoneWire") -> bool:
        return self.get_data() > 0

    def __str__(self: "RedstoneWire") -> str:
        return super().__str__() + " " + ("NOT " if not self.is_powered() else "") + "POWERED"

    def clone(self: "RedstoneWire") -> "RedstoneWire":
        return super().clone()