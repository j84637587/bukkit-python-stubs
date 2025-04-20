from typing import Set
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material.types import MushroomBlockTexture

"""
Represents a huge mushroom block with certain combinations of faces set to
cap, pores or stem.

@see Material.LEGACY_HUGE_MUSHROOM_1
@see Material.LEGACY_HUGE_MUSHROOM_2

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Mushroom:
    NORTH_LIMIT: int
    SOUTH_LIMIT: int
    EAST_WEST_LIMIT: int
    EAST_REMAINDER: int
    WEST_REMAINDER: int
    NORTH_SOUTH_MOD: int
    EAST_WEST_MOD: int

    """
    Constructs a brown/red mushroom block with all sides set to pores.

    @param shroom A brown or red mushroom material type.

    @see Material.LEGACY_HUGE_MUSHROOM_1
    @see Material.LEGACY_HUGE_MUSHROOM_2
    """
    def __init__(self, shroom: Material) -> None: ...

    """
    Constructs a brown/red mushroom cap block with the specified face or
    faces set to cap texture.

    Setting any of the four sides will also set the top to cap.

    To set two side faces at once use e.g. north-west.

    Specify self to set all six faces at once.

    @param shroom A brown or red mushroom material type.
    @param capFace The face or faces to set to mushroom cap texture.

    @see Material.LEGACY_HUGE_MUSHROOM_1
    @see Material.LEGACY_HUGE_MUSHROOM_2
    @see BlockFace
    """
    def __init__(self, shroom: Material, capFace: BlockFace) -> None: ...

    """
    Constructs a brown/red mushroom block with the specified textures.

    @param shroom A brown or red mushroom material type.
    @param texture The textured mushroom faces.

    @see Material.LEGACY_HUGE_MUSHROOM_1
    @see Material.LEGACY_HUGE_MUSHROOM_2
    """
    def __init__(self, shroom: Material, texture: MushroomBlockTexture) -> None: ...

    """
    @param shroom the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self, shroom: Material, data: bytes) -> None: ...

    """
    @return Whether this is a mushroom stem.
    """
    def isStem(self) -> bool: ...

    """
    Sets this to be a mushroom stem.

    @see MushroomBlockTexture.STEM_SIDES
    @see MushroomBlockTexture.ALL_STEM

    @deprecated Use
    {@link #setBlockTexture(org.bukkit.material.types.MushroomBlockTexture)}
    with {@link MushroomBlockTexture.STEM_SIDES } or
    {@link MushroomBlockTexture.ALL_STEM}
    """
    @Deprecated(since="1.9")
    def setStem(self) -> None: ...

    """
    Gets the mushroom texture of this block.

    @return The mushroom texture of this block
    """
    def getBlockTexture(self) -> MushroomBlockTexture: ...

    """
    Sets the mushroom texture of this block.

    @param texture The mushroom texture to set
    """
    def setBlockTexture(self, texture: MushroomBlockTexture) -> None: ...

    """
    Checks whether a face of the block is painted with cap texture.

    @param face The face to check.
    @return True if it is painted.
    """
    def isFacePainted(self, face: BlockFace) -> bool: ...

    """
    Set a face of the block to be painted or not. Note that due to the
    nature of how the data is stored, setting a face painted or not is not
    guaranteed to leave the other faces unchanged.

    @param face The face to paint or unpaint.
    @param painted True if you want to paint it, false if you want the
        pores to show.

    @deprecated Use MushroomBlockType cap options
    """
    @Deprecated(since="1.9")
    def setFacePainted(self, face: BlockFace, painted: bool) -> None: ...

    """
    @return A set of all faces that are currently painted (an empty set if
        it is a stem)
    """
    def getPaintedFaces(self) -> Set[BlockFace]: ...

    def __str__(self) -> str: ...

    def clone(self) -> 'Mushroom': ...