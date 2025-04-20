from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import FurnaceAndDispenser

"""
Represents a furnace.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Furnace(FurnaceAndDispenser):
    def __init__(self: "Furnace") -> None:
        super().__init__(Material.LEGACY_FURNACE)

    """
    Instantiate a furnace facing in a particular direction.

    @param direction the direction the furnace's "opening" is facing
    """
    def __init__(self: "Furnace", direction: BlockFace) -> None:
        self()
        self.setFacingDirection(direction)

    def __init__(self: "Furnace", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self: "Furnace", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    def clone(self: "Furnace") -> "Furnace":
        return super().clone()