from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.material import Wood

"""
Represents the different types of leaf block that may be permanent or can
decay when too far from a log.

@see Material.LEGACY_LEAVES
@see Material.LEGACY_LEAVES_2

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Leaves(Wood):
    DEFAULT_TYPE: Material = Material.LEGACY_LEAVES
    DEFAULT_DECAYABLE: bool = True

    """
    Constructs a leaf block.
    """
    def __init__(self: "Leaves") -> None:
        ...

    """
    Constructs a leaf block of the given tree species.

    @param species the species of the wood block
    """
    def __init__(self: "Leaves", species: TreeSpecies) -> None:
        ...

    """
    Constructs a leaf block of the given tree species and flag for whether
    this leaf block will disappear when too far from a log.

    @param species the species of the wood block
    @param isDecayable whether the block is permanent or can disappear
    """
    def __init__(self: "Leaves", species: TreeSpecies, isDecayable: bool) -> None:
        ...

    """
    Constructs a leaf block of the given type.

    @param type the type of leaf block
    """
    def __init__(self: "Leaves", type: Material) -> None:
        ...

    """
    Constructs a leaf block of the given type and tree species.

    @param type the type of leaf block
    @param species the species of the wood block
    """
    def __init__(self: "Leaves", type: Material, species: TreeSpecies) -> None:
        ...

    """
    Constructs a leaf block of the given type and tree species and flag for
    whether this leaf block will disappear when too far from a log.

    @param type the type of leaf block
    @param species the species of the wood block
    @param isDecayable whether the block is permanent or can disappear
    """
    def __init__(self: "Leaves", type: Material, species: TreeSpecies, isDecayable: bool) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self: "Leaves", type: Material, data: bytes) -> None:
        ...

    """
    Checks if this leaf block is in the process of decaying

    @return true if the leaf block is in the process of decaying
    """
    def isDecaying(self: "Leaves") -> bool:
        ...

    """
    Set whether this leaf block is in the process of decaying

    @param isDecaying whether the block is decaying or not
    """
    def setDecaying(self: "Leaves", isDecaying: bool) -> None:
        ...

    """
    Checks if this leaf block is permanent or can decay when too far from a
    log

    @return true if the leaf block is permanent or can decay when too far
    from a log
    """
    def isDecayable(self: "Leaves") -> bool:
        ...

    """
    Set whether this leaf block will disappear when too far from a log

    @param isDecayable whether the block is permanent or can disappear
    """
    def setDecayable(self: "Leaves", isDecayable: bool) -> None:
        ...

    def __str__(self: "Leaves") -> str:
        ...

    def clone(self: "Leaves") -> "Leaves":
        ...