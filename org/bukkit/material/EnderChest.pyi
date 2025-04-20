from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import DirectionalContainer

"""
Represents an ender chest

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class EnderChest(DirectionalContainer):
    
    def __init__(self: "EnderChest") -> None:
        super().__init__(Material.LEGACY_ENDER_CHEST)

    """
    Instantiate an ender chest facing in a particular direction.

    @param direction the direction the ender chest's lid opens towards
    """
    def __init__(self: "EnderChest", direction: BlockFace) -> None:
        self()
        self.setFacingDirection(direction)

    def __init__(self: "EnderChest", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self: "EnderChest", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    def clone(self: "EnderChest") -> "EnderChest":
        return super().clone()