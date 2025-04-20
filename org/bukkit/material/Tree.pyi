from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.block import BlockFace
from org.bukkit.material import Wood

"""
Represents the different types of Tree block that face a direction.

@see Material.LEGACY_LOG
@see Material.LEGACY_LOG_2

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Tree(Wood):
    DEFAULT_TYPE: Material
    DEFAULT_DIRECTION: BlockFace

    """
    Constructs a tree block.
    """
    def __init__(self) -> None: ...

    """
    Constructs a tree block of the given tree species.

    @param species the species of the tree block
    """
    def __init__(self, species: TreeSpecies) -> None: ...

    """
    Constructs a tree block of the given tree species, and facing the given
    direction.

    @param species the species of the tree block
    @param dir the direction the tree block is facing
    """
    def __init__(self, species: TreeSpecies, dir: BlockFace) -> None: ...

    """
    Constructs a tree block of the given type.

    @param type the type of tree block
    """
    def __init__(self, type: Material) -> None: ...

    """
    Constructs a tree block of the given type and tree species.

    @param type the type of tree block
    @param species the species of the tree block
    """
    def __init__(self, type: Material, species: TreeSpecies) -> None: ...

    """
    Constructs a tree block of the given type and tree species, and facing
    the given direction.

    @param type the type of tree block
    @param species the species of the tree block
    @param dir the direction the tree block is facing
    """
    def __init__(self, type: Material, species: TreeSpecies, dir: BlockFace) -> None: ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self, type: Material, data: bytes) -> None: ...

    """
    Get direction of the log

    @return one of:
    <ul>
    <li>BlockFace.TOP for upright (default)
    <li>BlockFace.NORTH (east-west)
    <li>BlockFace.WEST (north-south)
    <li>BlockFace.SELF (directionless)
    </ul>
    """
    def getDirection(self) -> BlockFace: ...

    """
    Set direction of the log

    @param dir - direction of end of log (BlockFace.SELF for no direction)
    """
    def setDirection(self, dir: BlockFace) -> None: ...

    def __str__(self) -> str: ...

    def clone(self) -> 'Tree': ...