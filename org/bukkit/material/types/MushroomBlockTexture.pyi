from typing import Dict, Optional
from org.bukkit.block import BlockFace

class MushroomBlockTexture:
    """
    Represents the different textured blocks of mushroom.
    """
    
    ALL_PORES: 'MushroomBlockTexture'
    CAP_NORTH_WEST: 'MushroomBlockTexture'
    CAP_NORTH: 'MushroomBlockTexture'
    CAP_NORTH_EAST: 'MushroomBlockTexture'
    CAP_WEST: 'MushroomBlockTexture'
    CAP_TOP: 'MushroomBlockTexture'
    CAP_EAST: 'MushroomBlockTexture'
    CAP_SOUTH_WEST: 'MushroomBlockTexture'
    CAP_SOUTH: 'MushroomBlockTexture'
    CAP_SOUTH_EAST: 'MushroomBlockTexture'
    STEM_SIDES: 'MushroomBlockTexture'
    ALL_CAP: 'MushroomBlockTexture'
    ALL_STEM: 'MushroomBlockTexture'
    
    BY_DATA: Dict[bytes, 'MushroomBlockTexture']
    BY_BLOCKFACE: Dict[Optional[BlockFace], 'MushroomBlockTexture']
    
    def __init__(self, data: int, cap_face: Optional[BlockFace]) -> None:
        """
        Initializes a MushroomBlockTexture with the given data and cap face.
        """
        ...

    def get_data(self) -> bytes:
        """
        Gets the associated data value representing this mushroom block face.

        Returns:
            A byte containing the data value of this mushroom block face
        """
        ...

    def get_cap_face(self) -> Optional[BlockFace]:
        """
        Gets the face that has cap texture.

        Returns:
            The cap face
        """
        ...

    @staticmethod
    def get_by_data(data: bytes) -> Optional['MushroomBlockTexture']:
        """
        Gets the MushroomBlockType with the given data value.

        Args:
            data: Data value to fetch

        Returns:
            The MushroomBlockTexture representing the given value, or
            None if it doesn't exist
        """
        ...

    @staticmethod
    def get_cap_by_face(face: Optional[BlockFace]) -> Optional['MushroomBlockTexture']:
        """
        Gets the MushroomBlockType with cap texture on the given block face.

        Args:
            face: the required block face with cap texture

        Returns:
            The MushroomBlockTexture representing the given block
            face, or None if it doesn't exist
        """
        ...

    @staticmethod
    def _initialize() -> None:
        """
        Initializes the static maps for MushroomBlockTexture.
        """
        ...