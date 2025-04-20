from org.bukkit import Material
from org.bukkit.material import MaterialData
from org.bukkit.material import PressureSensor

"""
Represents a pressure plate

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class PressurePlate(MaterialData, PressureSensor):
    def __init__(self: "PressurePlate") -> None:
        super().__init__(Material.LEGACY_WOOD_PLATE)

    def __init__(self: "PressurePlate", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self: "PressurePlate", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    def is_pressed(self: "PressurePlate") -> bool:
        ...

    def __str__(self: "PressurePlate") -> str:
        ...

    def clone(self: "PressurePlate") -> "PressurePlate":
        ...