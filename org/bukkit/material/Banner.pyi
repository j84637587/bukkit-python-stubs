from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from typing import Optional

"""
@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Banner(MaterialData):
    def __init__(self) -> None:
        super().__init__(Material.LEGACY_BANNER)

    def __init__(self, type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None:
        super().__init__(type, data)

    def is_wall_banner(self) -> bool:
        return self.get_item_type() == Material.LEGACY_WALL_BANNER

    def get_attached_face(self) -> Optional[BlockFace]:
        if self.is_wall_banner():
            data = self.get_data()

            if data == 0x2:
                return BlockFace.SOUTH
            elif data == 0x3:
                return BlockFace.NORTH
            elif data == 0x4:
                return BlockFace.EAST
            elif data == 0x5:
                return BlockFace.WEST

            return None
        else:
            return BlockFace.DOWN

    def get_facing(self) -> Optional[BlockFace]:
        data = self.get_data()

        if not self.is_wall_banner():
            if data == 0x0:
                return BlockFace.SOUTH
            elif data == 0x1:
                return BlockFace.SOUTH_SOUTH_WEST
            elif data == 0x2:
                return BlockFace.SOUTH_WEST
            elif data == 0x3:
                return BlockFace.WEST_SOUTH_WEST
            elif data == 0x4:
                return BlockFace.WEST
            elif data == 0x5:
                return BlockFace.WEST_NORTH_WEST
            elif data == 0x6:
                return BlockFace.NORTH_WEST
            elif data == 0x7:
                return BlockFace.NORTH_NORTH_WEST
            elif data == 0x8:
                return BlockFace.NORTH
            elif data == 0x9:
                return BlockFace.NORTH_NORTH_EAST
            elif data == 0xA:
                return BlockFace.NORTH_EAST
            elif data == 0xB:
                return BlockFace.EAST_NORTH_EAST
            elif data == 0xC:
                return BlockFace.EAST
            elif data == 0xD:
                return BlockFace.EAST_SOUTH_EAST
            elif data == 0xE:
                return BlockFace.SOUTH_EAST
            elif data == 0xF:
                return BlockFace.SOUTH_SOUTH_EAST

            return None
        else:
            return self.get_attached_face().get_opposite_face()

    def set_facing_direction(self, face: BlockFace) -> None:
        data: bytes

        if self.is_wall_banner():
            if face == BlockFace.NORTH:
                data = 0x2
            elif face == BlockFace.SOUTH:
                data = 0x3
            elif face == BlockFace.WEST:
                data = 0x4
            else:
                data = 0x5
        else:
            if face == BlockFace.SOUTH:
                data = 0x0
            elif face == BlockFace.SOUTH_SOUTH_WEST:
                data = 0x1
            elif face == BlockFace.SOUTH_WEST:
                data = 0x2
            elif face == BlockFace.WEST_SOUTH_WEST:
                data = 0x3
            elif face == BlockFace.WEST:
                data = 0x4
            elif face == BlockFace.WEST_NORTH_WEST:
                data = 0x5
            elif face == BlockFace.NORTH_WEST:
                data = 0x6
            elif face == BlockFace.NORTH_NORTH_WEST:
                data = 0x7
            elif face == BlockFace.NORTH:
                data = 0x8
            elif face == BlockFace.NORTH_NORTH_EAST:
                data = 0x9
            elif face == BlockFace.NORTH_EAST:
                data = 0xA
            elif face == BlockFace.EAST_NORTH_EAST:
                data = 0xB
            elif face == BlockFace.EAST:
                data = 0xC
            elif face == BlockFace.EAST_SOUTH_EAST:
                data = 0xD
            elif face == BlockFace.SOUTH_SOUTH_EAST:
                data = 0xF
            else:
                data = 0xE

        self.set_data(data)

    def __str__(self) -> str:
        return super().__str__() + " facing " + str(self.get_facing())

    def clone(self) -> 'Banner':
        return super().clone()