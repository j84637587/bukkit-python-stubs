from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData

"""
Represents minecart rails.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Rails(MaterialData):

    def __init__(self) -> None:
        super().__init__(Material.LEGACY_RAILS)

    def __init__(self, type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    @return the whether this track is set on a slope
    """
    def is_on_slope(self) -> bool:
        d: bytes = self.get_converted_data()
        return (d == 0x2 or d == 0x3 or d == 0x4 or d == 0x5)

    """
    @return the whether this track is set as a curve
    """
    def is_curve(self) -> bool:
        d: bytes = self.get_converted_data()
        return (d == 0x6 or d == 0x7 or d == 0x8 or d == 0x9)

    """
    @return the direction these tracks are set
        <p>
        Note that tracks are bidirectional and that the direction returned
        is the ascending direction if the track is set on a slope. If it is
        set as a curve, the corner of the track is returned.
    """
    def get_direction(self) -> BlockFace:
        d: bytes = self.get_converted_data()
        if d == 0x0:
            return BlockFace.SOUTH
        elif d == 0x1:
            return BlockFace.EAST
        elif d == 0x2:
            return BlockFace.EAST
        elif d == 0x3:
            return BlockFace.WEST
        elif d == 0x4:
            return BlockFace.NORTH
        elif d == 0x5:
            return BlockFace.SOUTH
        elif d == 0x6:
            return BlockFace.NORTH_WEST
        elif d == 0x7:
            return BlockFace.NORTH_EAST
        elif d == 0x8:
            return BlockFace.SOUTH_EAST
        elif d == 0x9:
            return BlockFace.SOUTH_WEST

    def __str__(self) -> str:
        return super().__str__() + " facing " + str(self.get_direction()) + ( " on a curve" if self.is_curve() else (" on a slope" if self.is_on_slope() else ""))

    """
    Return the data without the extended properties used by {@link
    PoweredRail} and {@link DetectorRail}. Overridden in {@link
    ExtendedRails}

    @return the data without the extended part
    @deprecated Magic value
    """
    def get_converted_data(self) -> bytes:
        return self.get_data()

    """
    Set the direction of these tracks
    <p>
    Note that tracks are bidirectional and that the direction returned is
    the ascending direction if the track is set on a slope. If it is set as
    a curve, the corner of the track should be supplied.

    @param face the direction the track should be facing
    @param is_on_slope whether or not the track should be on a slope
    """
    def set_direction(self, face: BlockFace, is_on_slope: bool) -> None:
        if face == BlockFace.EAST:
            self.set_data(bytes(0x2 if is_on_slope else 0x1))
        elif face == BlockFace.WEST:
            self.set_data(bytes(0x3 if is_on_slope else 0x1))
        elif face == BlockFace.NORTH:
            self.set_data(bytes(0x4 if is_on_slope else 0x0))
        elif face == BlockFace.SOUTH:
            self.set_data(bytes(0x5 if is_on_slope else 0x0))
        elif face == BlockFace.NORTH_WEST:
            self.set_data(bytes(0x6))
        elif face == BlockFace.NORTH_EAST:
            self.set_data(bytes(0x7))
        elif face == BlockFace.SOUTH_EAST:
            self.set_data(bytes(0x8))
        elif face == BlockFace.SOUTH_WEST:
            self.set_data(bytes(0x9))

    def clone(self) -> 'Rails':
        return super().clone()