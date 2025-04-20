from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import DirectionalContainer

"""
Represents a chest

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Chest(DirectionalContainer):
    def __init__(self: "Chest") -> None:
        super().__init__(Material.LEGACY_CHEST)

    """
    Instantiate a chest facing in a particular direction.

    @param direction the direction the chest's lit opens towards
    """
    def __init__(self: "Chest", direction: BlockFace) -> None:
        self()
        self.setFacingDirection(direction)

    def __init__(self: "Chest", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self: "Chest", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    def clone(self: "Chest") -> "Chest":
        return super().clone()