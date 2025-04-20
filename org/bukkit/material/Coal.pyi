from org.bukkit import CoalType
from org.bukkit import Material
from org.bukkit.material import MaterialData

"""
Represents the different types of coals.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Coal(MaterialData):
    def __init__(self) -> None:
        super().__init__(Material.LEGACY_COAL)

    def __init__(self, type: CoalType) -> None:
        self()
        self.set_type(type)

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
    Gets the current type of this coal

    @return CoalType of this coal
    """
    def get_type(self) -> CoalType:
        ...

    """
    Sets the type of this coal

    @param type New type of this coal
    """
    def set_type(self, type: CoalType) -> None:
        ...

    def __str__(self) -> str:
        ...

    def clone(self) -> 'Coal':
        ...