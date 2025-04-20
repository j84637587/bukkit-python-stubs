from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.material import MaterialData
from typing import Literal

class Wood(MaterialData):
    """
    Represents wood blocks of different species.

    @see Material.LEGACY_WOOD
    @see Material.LEGACY_SAPLING
    @see Material.LEGACY_WOOD_DOUBLE_STEP

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """
    DEFAULT_TYPE: Material = Material.LEGACY_WOOD
    DEFAULT_SPECIES: TreeSpecies = TreeSpecies.GENERIC

    def __init__(self: 'Wood') -> None:
        """
        Constructs a wood block.
        """
        ...

    def __init__(self: 'Wood', species: TreeSpecies) -> None:
        """
        Constructs a wood block of the given tree species.

        @param species the species of the wood block
        """
        ...

    def __init__(self: 'Wood', type: Material) -> None:
        """
        Constructs a wood block of the given type.

        @param type the type of wood block
        """
        ...

    def __init__(self: 'Wood', type: Material, species: TreeSpecies) -> None:
        """
        Constructs a wood block of the given type and tree species.

        @param type the type of wood block
        @param species the species of the wood block
        """
        ...

    @Deprecated(since="1.9")
    def __init__(self: 'Wood', type: Material, data: int) -> None:
        """
        @param type the type
        @param data the raw data value
        @deprecated Magic value
        """
        ...

    def getSpecies(self: 'Wood') -> TreeSpecies:
        """
        Gets the current species of this wood block

        @return TreeSpecies of this wood block
        """
        ...

    @staticmethod
    def getSpeciesType(type: Material, species: TreeSpecies) -> Material:
        """
        Correct the block type for certain species-type combinations.

        @param type The desired type
        @param species The required species
        @return The actual type for this species given the desired type
        """
        ...

    def setSpecies(self: 'Wood', species: TreeSpecies) -> None:
        """
        Sets the species of this wood block

        @param species New species of this wood block
        """
        ...

    def __str__(self: 'Wood') -> str:
        """
        @return String representation of the wood block
        """
        ...

    def clone(self: 'Wood') -> 'Wood':
        """
        @return A clone of this wood block
        """
        ...