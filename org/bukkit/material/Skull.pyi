from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from typing import Literal

class Skull(MaterialData):
    """
    Represents a skull.

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """

    def __init__(self) -> None:
        super().__init__(Material.LEGACY_SKULL)

    """
    Instantiate a skull facing in a particular direction.

    @param direction the direction the skull's face is facing
    """
    def __init__(self, direction: BlockFace) -> None:
        self()
        self.set_facing_direction(direction)

    def __init__(self, type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: int) -> None:
        super().__init__(type, data)

    def set_facing_direction(self, face: BlockFace) -> None:
        data: int

        if face == BlockFace.SELF:
            data = 0x1
        elif face == BlockFace.NORTH:
            data = 0x2
        elif face == BlockFace.WEST:
            data = 0x4
        elif face == BlockFace.SOUTH:
            data = 0x3
        elif face == BlockFace.EAST:
            data = 0x5
        else:
            data = 0x1

        self.set_data(data.to_bytes(1, 'big'))

    def get_facing(self) -> BlockFace:
        data: int = self.get_data()

        if data == 0x1:
            return BlockFace.SELF
        elif data == 0x2:
            return BlockFace.NORTH
        elif data == 0x3:
            return BlockFace.SOUTH
        elif data == 0x4:
            return BlockFace.WEST
        elif data == 0x5:
            return BlockFace.EAST
        else:
            return BlockFace.SELF

    def __str__(self) -> str:
        return super().__str__() + " facing " + str(self.get_facing())

    def clone(self) -> 'Skull':
        return super().clone()