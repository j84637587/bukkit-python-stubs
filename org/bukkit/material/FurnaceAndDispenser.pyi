from org.bukkit import Material
from org.bukkit.material import DirectionalContainer

"""
Represents a furnace or dispenser, two types of directional containers

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class FurnaceAndDispenser(DirectionalContainer):
    
    def __init__(self: "FurnaceAndDispenser", type: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self: "FurnaceAndDispenser", type: Material, data: bytes) -> None:
        ...

    def clone(self: "FurnaceAndDispenser") -> "FurnaceAndDispenser":
        ...