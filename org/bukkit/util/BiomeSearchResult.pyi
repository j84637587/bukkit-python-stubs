from org.bukkit import Location
from org.bukkit import World
from org.bukkit.block import Biome
from typing import Protocol

class BiomeSearchResult(Protocol):
    """
    Holds the result of searching for a biome.

    @see World.locateNearestBiome(Location, int, Biome...)
    @see World.locateNearestBiome(Location, int, int, int, Biome...)
    """

    def get_biome(self) -> Biome:
        """
        Return the biome which was found.

        @return: the found biome.
        """
        ...

    def get_location(self) -> Location:
        """
        Return the location of the biome.

        @return: the location the biome was found.
        """
        ...