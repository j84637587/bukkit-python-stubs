from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import Rails

"""
This is the superclass for the {@link DetectorRail} and {@link PoweredRail}
classes

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class ExtendedRails(Rails):
    def __init__(self: "ExtendedRails", type: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self: "ExtendedRails", type: Material, data: bytes) -> None:
        ...

    def is_curve(self: "ExtendedRails") -> bool:
        ...

    """
    {@inheritDoc}

    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def get_converted_data(self: "ExtendedRails") -> bytes:
        ...

    def set_direction(self: "ExtendedRails", face: BlockFace, is_on_slope: bool) -> None:
        ...

    def clone(self: "ExtendedRails") -> "ExtendedRails":
        ...