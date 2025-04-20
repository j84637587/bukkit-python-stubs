from typing import Collection
from org.bukkit.util import BoundingBox

class VoxelShape:
    """
    A shape made out of voxels.

    For example, used to represent the detailed collision shape of blocks.
    """

    def get_bounding_boxes(self) -> Collection[BoundingBox]:
        """
        Converts this shape into a collection of BoundingBox equivalent
        to the shape: a bounding box intersects with this block shape if it
        intersects with any of the shape's bounding boxes.

        @return shape converted to bounding boxes
        """
        ...

    def overlaps(self, other: BoundingBox) -> bool:
        """
        Checks if the given bounding box intersects this block shape.

        @param other bounding box to test
        @return true if other overlaps this, false otherwise
        """
        ...