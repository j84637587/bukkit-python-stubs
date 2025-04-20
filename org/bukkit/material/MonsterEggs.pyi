from typing import List
from org.bukkit import Material
from org.bukkit.material import TexturedMaterial

"""
Represents the different types of monster eggs

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class MonsterEggs(TexturedMaterial):
    textures: List[Material]

    def __init__(self) -> None:
        ...

    def __init__(self, type: Material) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None:
        ...

    def get_textures(self) -> List[Material]:
        ...

    def clone(self) -> 'MonsterEggs':
        ...