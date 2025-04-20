from typing import Literal
from org.bukkit.util import Vector

class BlockFace:
    NORTH: 'BlockFace'
    EAST: 'BlockFace'
    SOUTH: 'BlockFace'
    WEST: 'BlockFace'
    UP: 'BlockFace'
    DOWN: 'BlockFace'
    NORTH_EAST: 'BlockFace'
    NORTH_WEST: 'BlockFace'
    SOUTH_EAST: 'BlockFace'
    SOUTH_WEST: 'BlockFace'
    WEST_NORTH_WEST: 'BlockFace'
    NORTH_NORTH_WEST: 'BlockFace'
    NORTH_NORTH_EAST: 'BlockFace'
    EAST_NORTH_EAST: 'BlockFace'
    EAST_SOUTH_EAST: 'BlockFace'
    SOUTH_SOUTH_EAST: 'BlockFace'
    SOUTH_SOUTH_WEST: 'BlockFace'
    WEST_SOUTH_WEST: 'BlockFace'
    SELF: 'BlockFace'

    modX: int
    modY: int
    modZ: int

    def __init__(self, modX: int, modY: int, modZ: int) -> None:
        """Initialize BlockFace with modX, modY, modZ."""
        ...

    def __init__(self, face1: 'BlockFace', face2: 'BlockFace') -> None:
        """Initialize BlockFace with two other BlockFaces."""
        ...

    def getModX(self) -> int:
        """Get the amount of X-coordinates to modify to get the represented block.

        Returns:
            Amount of X-coordinates to modify
        """
        ...

    def getModY(self) -> int:
        """Get the amount of Y-coordinates to modify to get the represented block.

        Returns:
            Amount of Y-coordinates to modify
        """
        ...

    def getModZ(self) -> int:
        """Get the amount of Z-coordinates to modify to get the represented block.

        Returns:
            Amount of Z-coordinates to modify
        """
        ...

    def getDirection(self) -> Vector:
        """Gets the normal vector corresponding to this block face.

        Returns:
            the normal vector
        """
        ...

    def isCartesian(self) -> bool:
        """Returns true if this face is aligned with one of the unit axes in 3D
        Cartesian space (ie NORTH, SOUTH, EAST, WEST, UP, DOWN).

        Returns:
            Cartesian status
        """
        ...

    def getOppositeFace(self) -> 'BlockFace':
        """Get the opposite face of this BlockFace.

        Returns:
            The opposite BlockFace
        """
        ...