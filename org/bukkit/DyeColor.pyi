from typing import Optional, Dict
from org.bukkit import Color

class DyeColor:
    """
    All supported color values for dyes and cloth
    """
    WHITE: 'DyeColor'
    ORANGE: 'DyeColor'
    MAGENTA: 'DyeColor'
    LIGHT_BLUE: 'DyeColor'
    YELLOW: 'DyeColor'
    LIME: 'DyeColor'
    PINK: 'DyeColor'
    GRAY: 'DyeColor'
    LIGHT_GRAY: 'DyeColor'
    CYAN: 'DyeColor'
    PURPLE: 'DyeColor'
    BLUE: 'DyeColor'
    BROWN: 'DyeColor'
    GREEN: 'DyeColor'
    RED: 'DyeColor'
    BLACK: 'DyeColor'
    woolData: bytes
    dyeData: bytes
    color: Color
    firework: Color
    BY_WOOL_DATA: Dict[bytes, 'DyeColor']
    BY_DYE_DATA: Dict[bytes, 'DyeColor']
    BY_COLOR: Dict[Color, 'DyeColor']
    BY_FIREWORK: Dict[Color, 'DyeColor']

    def __init__(self, woolData: int, dyeData: int, color: Color, firework: Color) -> None:
        """
        Constructor for DyeColor
        """
        pass

    def getWoolData(self) -> bytes:
        """
        Gets the associated wool data value representing this color.
        """
        pass

    def getDyeData(self) -> bytes:
        """
        Gets the associated dye data value representing this color.
        """
        pass

    def getColor(self) -> Color:
        """
        Gets the color that this dye represents.
        """
        pass

    def getFireworkColor(self) -> Color:
        """
        Gets the firework color that this dye represents.
        """
        pass

    @staticmethod
    def getByWoolData(data: bytes) -> Optional['DyeColor']:
        """
        Gets the DyeColor with the given wool data value.
        """
        pass

    @staticmethod
    def getByDyeData(data: bytes) -> Optional['DyeColor']:
        """
        Gets the DyeColor with the given dye data value.
        """
        pass

    @staticmethod
    def getByColor(color: Color) -> Optional['DyeColor']:
        """
        Gets the DyeColor with the given color value.
        """
        pass

    @staticmethod
    def getByFireworkColor(color: Color) -> Optional['DyeColor']:
        """
        Gets the DyeColor with the given firework color value.
        """
        pass

    @staticmethod
    def legacyValueOf(name: Optional[str]) -> 'DyeColor':
        """
        Gets the DyeColor for the given name, possibly doing legacy transformations.
        """
        pass