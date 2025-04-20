from org.bukkit import Material
from org.bukkit.material import ExtendedRails
from org.bukkit.material import PressureSensor

"""
Represents a detector rail

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class DetectorRail(ExtendedRails, PressureSensor):
    def __init__(self) -> None:
        super().__init__(Material.LEGACY_DETECTOR_RAIL)

    def __init__(self, type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None:
        super().__init__(type, data)

    def is_pressed(self) -> bool:
        ...

    def set_pressed(self, is_pressed: bool) -> None:
        ...

    def clone(self) -> 'DetectorRail':
        ...