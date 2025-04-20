from org.bukkit import GrassSpecies
from org.bukkit import Material
from org.bukkit.material import MaterialData

"""
Represents the different types of long grasses.

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class LongGrass(MaterialData):
    def __init__(self: "LongGrass") -> None:
        super().__init__(Material.LEGACY_LONG_GRASS)

    def __init__(self: "LongGrass", species: GrassSpecies) -> None:
        self()
        self.setSpecies(species)

    def __init__(self: "LongGrass", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "LongGrass", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    Gets the current species of this grass

    @return GrassSpecies of this grass
    """
    def getSpecies(self: "LongGrass") -> GrassSpecies:
        return GrassSpecies.getByData(self.getData())

    """
    Sets the species of this grass

    @param species New species of this grass
    """
    def setSpecies(self: "LongGrass", species: GrassSpecies) -> None:
        self.setData(species.getData())

    def __str__(self: "LongGrass") -> str:
        return f"{self.getSpecies()} {super().__str__()}"

    def clone(self: "LongGrass") -> "LongGrass":
        return cast(LongGrass, super().clone())