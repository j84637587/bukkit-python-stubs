from typing import Set
from org.bukkit.block import BlockFace
from org.bukkit.block.data import BlockData

"""
This class encompasses the 'north', 'east', 'south', 'west', 'up', 'down'
boolean flags which are used to set which faces of the block textures are
displayed on.
<br>
Some blocks may not be able to have faces on all directions, use
{@link #getAllowedFaces()} to get all possible faces for this block. It is
not valid to call any methods on non-allowed faces.
"""
class MultipleFacing(BlockData):

    """
    Checks if this block has the specified face enabled.

    @param face to check
    @return if face is enabled
    """
    def has_face(self, face: BlockFace) -> bool: ...

    """
    Set whether this block has the specified face enabled.

    @param face to set
    @param has the face
    """
    def set_face(self, face: BlockFace, has: bool) -> None: ...

    """
    Get all of the faces which are enabled on this block.

    @return all faces enabled
    """
    def get_faces(self) -> Set[BlockFace]: ...

    """
    Gets all of this faces which may be set on this block.

    @return all allowed faces
    """
    def get_allowed_faces(self) -> Set[BlockFace]: ...