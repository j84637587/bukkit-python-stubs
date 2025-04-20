from typing import List
from org.bukkit import Material
from org.bukkit.material import TexturedMaterial

"""
Represents the different types of steps.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Step(TexturedMaterial):
    textures: List[Material] = []

    def __init__(self) -> None:
        super().__init__(Material.LEGACY_STEP)

    def __init__(self, type: Material) -> None:
        super().__init__(Material.LEGACY_STEP if type in self.textures else type)
        if type in self.textures:
            self.setMaterial(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self, type: Material, data: bytes) -> None:
        super().__init__(type, data)

    def getTextures(self) -> List[Material]:
        return self.textures

    """
    Test if step is inverted

    @return true if inverted (top half), false if normal (bottom half)
    """
    def isInverted(self) -> bool:
        return (self.getData() & 0x8) != 0

    """
    Set step inverted state

    @param inv - true if step is inverted (top half), false if step is
        normal (bottom half)
    """
    def setInverted(self, inv: bool) -> None:
        dat = self.getData() & 0x7
        if inv:
            dat |= 0x8
        self.setData(bytes(dat))

    """
    {@inheritDoc}

    @deprecated Magic value
    """
    @Deprecated(since="1.20.5")
    def getTextureIndex(self) -> int:
        return self.getData() & 0x7

    """
    {@inheritDoc}

    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def setTextureIndex(self, idx: int) -> None:
        self.setData(bytes((self.getData() & 0x8) | idx))

    def clone(self) -> 'Step':
        return super().clone()

    def __str__(self) -> str:
        return super().__str__() + ("inverted" if self.isInverted() else "")