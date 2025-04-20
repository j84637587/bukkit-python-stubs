from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import SimpleAttachableMaterialData

"""
Represents Ladder data

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Ladder(SimpleAttachableMaterialData):
    def __init__(self: "Ladder") -> None:
        super().__init__(Material.LEGACY_LADDER)

    def __init__(self: "Ladder", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "Ladder", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    Gets the face that this block is attached on

    @return BlockFace attached to
    """
    def get_attached_face(self: "Ladder") -> BlockFace:
        data: bytes = self.get_data()

        if data == 0x2:
            return BlockFace.SOUTH
        elif data == 0x3:
            return BlockFace.NORTH
        elif data == 0x4:
            return BlockFace.EAST
        elif data == 0x5:
            return BlockFace.WEST

        return None

    """
    Sets the direction this ladder is facing
    """
    def set_facing_direction(self: "Ladder", face: BlockFace) -> None:
        data: bytes = 0x0

        if face == BlockFace.SOUTH:
            data = 0x2
        elif face == BlockFace.NORTH:
            data = 0x3
        elif face == BlockFace.EAST:
            data = 0x4
        elif face == BlockFace.WEST:
            data = 0x5

        self.set_data(data)

    def clone(self: "Ladder") -> "Ladder":
        return super().clone()