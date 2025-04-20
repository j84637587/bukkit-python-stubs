from typing import Dict, Any, Optional

from org.bukkit.Location import Location
from org.bukkit.block.Block import Block
from org.bukkit.block.BlockFace import BlockFace
from org.bukkit.configuration.serialization.ConfigurationSerializable import ConfigurationSerializable
from org.bukkit.configuration.serialization.SerializableAs import SerializableAs
from org.jetbrains.annotations import NotNull, Nullable

@SerializableAs("BoundingBox")
class BoundingBox(ConfigurationSerializable):
    """
    A mutable axis aligned bounding box (AABB).
    This basically represents a rectangular box (specified by minimum and maximum
    corners) that can for example be used to describe the position and extents of
    an object (such as an entity, block, or rectangular region) in 3D space. Its
    edges and faces are parallel to the axes of the cartesian coordinate system.
    The bounding box may be degenerate (one or more sides having the length 0).
    Because bounding boxes are mutable, storing them long term may be dangerous
    if they get modified later. If you want to keep around a bounding box, it may
    be wise to call {@link #clone()} in order to get a copy.
    """

    @staticmethod
        def of(corner1: 'Vector', corner2: 'Vector') -> 'BoundingBox':
        """
        Creates a new bounding box using the coordinates of the given vectors as
        corners.

        @param corner1 the first corner
        @param corner2 the second corner
        @return the bounding box
        """
        ...

    @staticmethod
        def of(corner1: Location, corner2: Location) -> 'BoundingBox':
        """
        Creates a new bounding box using the coordinates of the given locations
        as corners.

        @param corner1 the first corner
        @param corner2 the second corner
        @return the bounding box
        """
        ...

    @staticmethod
        def of(corner1: Block, corner2: Block) -> 'BoundingBox':
        """
        Creates a new bounding box using the coordinates of the given blocks as
        corners.
        The bounding box will be sized to fully contain both blocks.

        @param corner1 the first corner block
        @param corner2 the second corner block
        @return the bounding box
        """
        ...

    @staticmethod
        def of(block: Block) -> 'BoundingBox':
        """
        Creates a new 1x1x1 sized bounding box containing the given block.

        @param block the block
        @return the bounding box
        """
        ...

    @staticmethod
        def of(center: 'Vector', x: float, y: float, z: float) -> 'BoundingBox':
        """
        Creates a new bounding box using the given center and extents.

        @param center the center
        @param x 1/2 the size of the bounding box along the x axis
        @param y 1/2 the size of the bounding box along the y axis
        @param z 1/2 the size of the bounding box along the z axis
        @return the bounding box
        """
        ...

    @staticmethod
        def of(center: Location, x: float, y: float, z: float) -> 'BoundingBox':
        """
        Creates a new bounding box using the given center and extents.

        @param center the center
        @param x 1/2 the size of the bounding box along the x axis
        @param y 1/2 the size of the bounding box along the y axis
        @param z 1/2 the size of the bounding box along the z axis
        @return the bounding box
        """
        ...

    def __init__(self, x1: float = 0.0, y1: float = 0.0, z1: float = 0.0, x2: float = 0.0, y2: float = 0.0, z2: float = 0.0) -> None:
        """
        Creates a new bounding box from the given corner coordinates.

        @param x1 the first corner's x value
        @param y1 the first corner's y value
        @param z1 the first corner's z value
        @param x2 the second corner's x value
        @param y2 the second corner's y value
        @param z2 the second corner's z value
        """
        ...

        def resize(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> 'BoundingBox':
        """
        Resizes this bounding box.

        @param x1 the first corner's x value
        @param y1 the first corner's y value
        @param z1 the first corner's z value
        @param x2 the second corner's x value
        @param y2 the second corner's y value
        @param z2 the second corner's z value
        @return this bounding box (resized)
        """
        ...

    def getMinX(self) -> float:
        """Gets the minimum x value."""
        ...

    def getMinY(self) -> float:
        """Gets the minimum y value."""
        ...

    def getMinZ(self) -> float:
        """Gets the minimum z value."""
        ...

        def getMin(self) -> 'Vector':
        """Gets the minimum corner as vector."""
        ...

    def getMaxX(self) -> float:
        """Gets the maximum x value."""
        ...

    def getMaxY(self) -> float:
        """Gets the maximum y value."""
        ...

    def getMaxZ(self) -> float:
        """Gets the maximum z value."""
        ...

        def getMax(self) -> 'Vector':
        """Gets the maximum corner as vector."""
        ...

    def getWidthX(self) -> float:
        """Gets the width of the bounding box in the x direction."""
        ...

    def getWidthZ(self) -> float:
        """Gets the width of the bounding box in the z direction."""
        ...

    def getHeight(self) -> float:
        """Gets the height of the bounding box."""
        ...

    def getVolume(self) -> float:
        """Gets the volume of the bounding box."""
        ...

    def getCenterX(self) -> float:
        """Gets the x coordinate of the center of the bounding box."""
        ...

    def getCenterY(self) -> float:
        """Gets the y coordinate of the center of the bounding box."""
        ...

    def getCenterZ(self) -> float:
        """Gets the z coordinate of the center of the bounding box."""
        ...

        def getCenter(self) -> 'Vector':
        """Gets the center of the bounding box."""
        ...

        def copy(self, other: 'BoundingBox') -> 'BoundingBox':
        """Copies another bounding box."""
        ...

        def expand(self, negativeX: float, negativeY: float, negativeZ: float, positiveX: float, positiveY: float, positiveZ: float) -> 'BoundingBox':
        """
        Expands this bounding box by the given values in the corresponding
        directions.
        Negative values will shrink the bounding box in the corresponding
        direction. Shrinking will be limited to the point where the affected
        opposite faces would meet if the they shrank at uniform speeds.

        @param negativeX the amount of expansion in the negative x direction
        @param negativeY the amount of expansion in the negative y direction
        @param negativeZ the amount of expansion in the negative z direction
        @param positiveX the amount of expansion in the positive x direction
        @param positiveY the amount of expansion in the positive y direction
        @param positiveZ the amount of expansion in the positive z direction
        @return this bounding box (now expanded)
        """
        ...

        def expand(self, x: float, y: float, z: float) -> 'BoundingBox':
        """Expands this bounding box uniformly by the given values in both positive and negative directions."""
        ...

        def expand(self, expansion: 'Vector') -> 'BoundingBox':
        """Expands this bounding box uniformly by the given values in both positive and negative directions."""
        ...

        def expand(self, expansion: float) -> 'BoundingBox':
        """Expands this bounding box uniformly by the given value in all directions."""
        ...

        def expand(self, dirX: float, dirY: float, dirZ: float, expansion: float) -> 'BoundingBox':
        """Expands this bounding box in the specified direction."""
        ...

        def expand(self, direction: 'Vector', expansion: float) -> 'BoundingBox':
        """Expands this bounding box in the specified direction."""
        ...

        def expand(self, blockFace: BlockFace, expansion: float) -> 'BoundingBox':
        """Expands this bounding box in the direction specified by the given block face."""
        ...

        def expandDirectional(self, dirX: float, dirY: float, dirZ: float) -> 'BoundingBox':
        """Expands this bounding box in the specified direction."""
        ...

        def expandDirectional(self, direction: 'Vector') -> 'BoundingBox':
        """Expands this bounding box in the specified direction."""
        ...

        def union(self, posX: float, posY: float, posZ: float) -> 'BoundingBox':
        """Expands this bounding box to contain (or border) the specified position."""
        ...

        def union(self, position: 'Vector') -> 'BoundingBox':
        """Expands this bounding box to contain (or border) the specified position."""
        ...

        def union(self, position: Location) -> 'BoundingBox':
        """Expands this bounding box to contain (or border) the specified position."""
        ...

        def union(self, other: 'BoundingBox') -> 'BoundingBox':
        """Expands this bounding box to contain both this and the given bounding box."""
        ...

        def intersection(self, other: 'BoundingBox') -> 'BoundingBox':
        """Resizes this bounding box to represent the intersection of this and the given bounding box."""
        ...

        def shift(self, shiftX: float, shiftY: float, shiftZ: float) -> 'BoundingBox':
        """Shifts this bounding box by the given amounts."""
        ...

        def shift(self, shift: 'Vector') -> 'BoundingBox':
        """Shifts this bounding box by the given amounts."""
        ...

        def shift(self, shift: Location) -> 'BoundingBox':
        """Shifts this bounding box by the given amounts."""
        ...

    def overlaps(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float) -> bool:
        """Checks if this bounding box overlaps with the given bounding box."""
        ...

    def overlaps(self, other: 'BoundingBox') -> bool:
        """Checks if this bounding box overlaps with the given bounding box."""
        ...

    def overlaps(self, min: 'Vector', max: 'Vector') -> bool:
        """Checks if this bounding box overlaps with the bounding box that is defined by the given corners."""
        ...

    def contains(self, x: float, y: float, z: float) -> bool:
        """Checks if this bounding box contains the specified position."""
        ...

    def contains(self, position: 'Vector') -> bool:
        """Checks if this bounding box contains the specified position."""
        ...

    def contains(self, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float) -> bool:
        """Checks if this bounding box fully contains the given bounding box."""
        ...

    def contains(self, other: 'BoundingBox') -> bool:
        """Checks if this bounding box fully contains the given bounding box."""
        ...

    def contains(self, min: 'Vector', max: 'Vector') -> bool:
        """Checks if this bounding box fully contains the bounding box that is defined by the given corners."""
        ...

        def rayTrace(self, start: 'Vector', direction: 'Vector', maxDistance: float) -> Optional['RayTraceResult']:
        """
        Calculates the intersection of this bounding box with the specified line
        segment.
        Intersections at edges and corners yield one of the affected block faces
        as hit result, but it is not defined which of them.

        @param start the start position
        @param direction the ray direction
        @param maxDistance the maximum distance
        @return the ray trace hit result, or <code>null</code> if there is no hit
        """
        ...

    def hashCode(self) -> int:
        """Overrides hashCode method."""
        ...

    def equals(self, obj: Any) -> bool:
        """Overrides equals method."""
        ...

    def toString(self) -> str:
        """Overrides toString method."""
        ...

        def clone(self) -> 'BoundingBox':
        """Creates a copy of this bounding box."""
        ...

        def serialize(self) -> Dict[str, Any]:
        """Serializes this bounding box."""
        ...

        @staticmethod
    def deserialize(args: Dict[str, Any]) -> 'BoundingBox':
        """Deserializes a bounding box from the given arguments."""
        ...