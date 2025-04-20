from typing import Set
from org.bukkit.block.BlockFace import BlockFace
from org.bukkit.block.data.BlockData import BlockData
from org.jetbrains.annotations import NotNull

"""
'facing' represents the face towards which the block is pointing.
<br>
Some blocks may not be able to face in all directions, use
{@link #getFaces()} to get all possible directions for this block.
"""
class Directional(BlockData):
    """
    Gets the value of the 'facing' property.

    @return the 'facing' value
    """
        def get_facing(self) -> BlockFace: ...

    """
    Sets the value of the 'facing' property.

    @param facing the new 'facing' value
    """
    def set_facing(self, facing: BlockFace) -> None: ...

    """
    Gets the faces which are applicable to this block.

    @return the allowed 'facing' values
    """
        def get_faces(self) -> Set[BlockFace]: ...