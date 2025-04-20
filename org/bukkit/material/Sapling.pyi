from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.material import Wood

"""
Represents the different types of Tree block that face a direction.

@see Material.LEGACY_SAPLING

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Sapling(Wood):
    DEFAULT_SPECIES: TreeSpecies

    """
    Constructs a sapling.
    """
    def __init__(self: "Sapling") -> None:
        ...

    """
    Constructs a sapling of the given tree species.

    @param species the species of the sapling
    """
    def __init__(self: "Sapling", species: TreeSpecies) -> None:
        ...

    """
    Constructs a sapling of the given tree species and if is it instant
    growable

    @param species the species of the tree block
    @param isInstantGrowable true if the Sapling should grow when next ticked with bonemeal
    """
    def __init__(self: "Sapling", species: TreeSpecies, isInstantGrowable: bool) -> None:
        ...

    """
    Constructs a sapling of the given type.

    @param type the type of tree block
    """
    def __init__(self: "Sapling", type: Material) -> None:
        ...

    """
    Constructs a sapling of the given type and tree species.

    @param type the type of sapling
    @param species the species of the sapling
    """
    def __init__(self: "Sapling", type: Material, species: TreeSpecies) -> None:
        ...

    """
    Constructs a sapling of the given type and tree species and if is it
    instant growable

    @param type the type of sapling
    @param species the species of the sapling
    @param isInstantGrowable true if the Sapling should grow when next ticked
    with bonemeal
    """
    def __init__(self: "Sapling", type: Material, species: TreeSpecies, isInstantGrowable: bool) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.9")
    def __init__(self: "Sapling", type: Material, data: bytes) -> None:
        ...

    """
    Checks if the Sapling would grow when next ticked with bonemeal

    @return true if the Sapling would grow when next ticked with bonemeal
    """
    def isInstantGrowable(self: "Sapling") -> bool:
        ...

    """
    Set whether this sapling will grow when next ticked with bonemeal

    @param isInstantGrowable true if the Sapling should grow when next ticked
    with bonemeal
    """
    def setIsInstantGrowable(self: "Sapling", isInstantGrowable: bool) -> None:
        ...

    """
    @return a string representation of the sapling
    """
    def __str__(self: "Sapling") -> str:
        ...

    """
    @return a clone of this sapling
    """
    def clone(self: "Sapling") -> "Sapling":
        ...