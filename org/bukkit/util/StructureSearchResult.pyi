from org.bukkit import Location
from org.bukkit import World
from org.bukkit.generator.structure import Structure
from org.bukkit.generator.structure import StructureType
from typing import Protocol

class StructureSearchResult(Protocol):
    """
    Holds the result of searching for a structure.

    @see World.locateNearestStructure(Location, Structure, int, bool)
    @see World.locateNearestStructure(Location, StructureType, int, bool)
    """

    def get_structure(self) -> Structure:
        """
        Return the structure which was found.

        @return: the found structure.
        """
        ...

    def get_location(self) -> Location:
        """
        Return the location of the structure.

        @return: the location the structure was found.
        """
        ...