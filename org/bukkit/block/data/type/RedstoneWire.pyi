from typing import Set
from org.bukkit.block import BlockFace
from org.bukkit.block.data import AnaloguePowerable
from org.jetbrains.annotations import NotNull

"""
'north', 'east', 'south', 'west' represent the types of connections this
redstone wire has to adjacent blocks.
"""
class RedstoneWire(AnaloguePowerable):
    """
    Checks the type of connection on the specified face.

    @param face to check
    @return connection type
    """
        def get_face(self, face: BlockFace) -> 'RedstoneWire.Connection':
        ...

    """
    Sets the type of connection on the specified face.

    @param face to set
    @param connection the connection type
    """
    def set_face(self, face: BlockFace, connection: 'RedstoneWire.Connection') -> None:
        ...

    """
    Gets all of this faces which may be set on this block.

    @return all allowed faces
    """
        def get_allowed_faces(self) -> Set[BlockFace]:
        ...


    class Connection:
        """
        The wire travels up the side of the block adjacent to this face.
        """
        UP = ...

        """
        The wire travels flat from this face and into the adjacent block.
        """
        SIDE = ...

        """
        The wire does not connect in this direction.
        """
        NONE = ...