from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import FurnaceAndDispenser

"""
Represents a dispenser.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Dispenser(FurnaceAndDispenser):
    def __init__(self: "Dispenser") -> None:
        super().__init__(Material.LEGACY_DISPENSER)

    def __init__(self: "Dispenser", direction: BlockFace) -> None:
        self()
        self.set_facing_direction(direction)

    def __init__(self: "Dispenser", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "Dispenser", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    def set_facing_direction(self: "Dispenser", face: BlockFace) -> None:
        data: bytes
        if face == BlockFace.DOWN:
            data = 0x0
        elif face == BlockFace.UP:
            data = 0x1
        elif face == BlockFace.NORTH:
            data = 0x2
        elif face == BlockFace.SOUTH:
            data = 0x3
        elif face == BlockFace.WEST:
            data = 0x4
        else:
            data = 0x5
        self.set_data(data)

    def get_facing(self: "Dispenser") -> BlockFace:
        data: int = self.get_data() & 0x7
        if data == 0x0:
            return BlockFace.DOWN
        elif data == 0x1:
            return BlockFace.UP
        elif data == 0x2:
            return BlockFace.NORTH
        elif data == 0x3:
            return BlockFace.SOUTH
        elif data == 0x4:
            return BlockFace.WEST
        else:
            return BlockFace.EAST

    def clone(self: "Dispenser") -> "Dispenser":
        return super().clone()