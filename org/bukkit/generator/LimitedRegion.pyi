from typing import List
from org.bukkit import Location
from org.bukkit import RegionAccessor
from org.bukkit.block import BlockState

class LimitedRegion(RegionAccessor):
    """
    A limited region is used in world generation for features which are
    going over a chunk. For example, trees or ores.

    Use {@link #getBuffer()} to know how much you can go beyond the central
    chunk. The buffer zone may or may not be already populated.

    The coordinates are <b>absolute</b> from the world origin.
    """

    def get_buffer(self) -> int:
        """
        Gets the buffer around the central chunk which is accessible.
        The returned value is in normal world coordinate scale.
        <p>
        For example: If the method returns 16 you have a working area of 48x48.

        @return The buffer in X and Z direction
        """
        ...

    def is_in_region(self, location: Location) -> bool:
        """
        Checks if the given {@link Location} is in the region.

        @param location the location to check
        @return true if the location is in the region, otherwise false.
        """
        ...

    def is_in_region(self, x: int, y: int, z: int) -> bool:
        """
        Checks if the given coordinates are in the region.

        @param x X-coordinate to check
        @param y Y-coordinate to check
        @param z Z-coordinate to check
        @return true if the coordinates are in the region, otherwise false.
        """
        ...

    def get_tile_entities(self) -> List[BlockState]:
        """
        Gets a list of all tile entities in the limited region including the
        buffer zone.

        @return a list of tile entities.
        """
        ...