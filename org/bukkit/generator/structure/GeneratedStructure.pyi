from typing import Collection
from org.bukkit.persistence import PersistentDataHolder
from org.bukkit.util import BoundingBox
from org.bukkit.generator.structure import Structure
from org.bukkit.generator.structure import StructurePiece

class GeneratedStructure(PersistentDataHolder):
    """
    Represents a structure placed in the world.

    @see StructurePiece
    """

    def get_bounding_box(self) -> BoundingBox:
        """
        Gets the bounding box of this placed structure.

        @return bounding box of this placed structure
        """
        ...

    def get_structure(self) -> Structure:
        """
        Gets the structure that this PlacedStructure represents.

        @return the structure that this PlacedStructure represents
        """
        ...

    def get_pieces(self) -> Collection[StructurePiece]:
        """
        Gets all the {@link StructurePiece} that make up this PlacedStructure.

        @return a collection of all the StructurePieces
        """
        ...