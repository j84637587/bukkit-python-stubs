from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import SimpleAttachableMaterialData

"""
MaterialData for torches

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Torch(SimpleAttachableMaterialData):
    def __init__(self: "Torch") -> None:
        super().__init__(Material.LEGACY_TORCH)

    def __init__(self: "Torch", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "Torch", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    Gets the face that this block is attached on

    @return BlockFace attached to
    """
    def get_attached_face(self: "Torch") -> BlockFace:
        data: bytes = self.get_data()

        if data == 0x1:
            return BlockFace.WEST
        elif data == 0x2:
            return BlockFace.EAST
        elif data == 0x3:
            return BlockFace.NORTH
        elif data == 0x4:
            return BlockFace.SOUTH
        else:
            return BlockFace.DOWN

    def set_facing_direction(self: "Torch", face: BlockFace) -> None:
        data: bytes

        if face == BlockFace.EAST:
            data = 0x1
        elif face == BlockFace.WEST:
            data = 0x2
        elif face == BlockFace.SOUTH:
            data = 0x3
        elif face == BlockFace.NORTH:
            data = 0x4
        else:
            data = 0x5

        self.set_data(data)

    def clone(self: "Torch") -> "Torch":
        return super().clone()