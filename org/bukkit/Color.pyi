from typing import Dict, List, Union

class Color:
    """
    A container for a color palette. This class is immutable; the set methods
    return a new color. The color names listed as fields are HTML4 standards,
    but subject to change.
    """
    BIT_MASK: int
    DEFAULT_ALPHA: int

    WHITE: 'Color'
    SILVER: 'Color'
    GRAY: 'Color'
    BLACK: 'Color'
    RED: 'Color'
    MAROON: 'Color'
    YELLOW: 'Color'
    OLIVE: 'Color'
    LIME: 'Color'
    GREEN: 'Color'
    AQUA: 'Color'
    TEAL: 'Color'
    BLUE: 'Color'
    NAVY: 'Color'
    FUCHSIA: 'Color'
    PURPLE: 'Color'
    ORANGE: 'Color'

    alpha: bytes
    red: bytes
    green: bytes
    blue: bytes

    @staticmethod
    def fromARGB(alpha: int, red: int, green: int, blue: int) -> 'Color': ...

    @staticmethod
    def fromRGB(red: int, green: int, blue: int) -> 'Color': ...

    @staticmethod
    def fromBGR(blue: int, green: int, red: int) -> 'Color': ...

    @staticmethod
    def fromRGB(rgb: int) -> 'Color': ...

    @staticmethod
    def fromARGB(argb: int) -> 'Color': ...

    @staticmethod
    def fromBGR(bgr: int) -> 'Color': ...

    def getAlpha(self) -> int: ...

    def setAlpha(self, alpha: int) -> 'Color': ...

    def getRed(self) -> int: ...

    def setRed(self, red: int) -> 'Color': ...

    def getGreen(self) -> int: ...

    def setGreen(self, green: int) -> 'Color': ...

    def getBlue(self) -> int: ...

    def setBlue(self, blue: int) -> 'Color': ...

    def asRGB(self) -> int: ...

    def asARGB(self) -> int: ...

    def asBGR(self) -> int: ...

    def mixDyes(self, colors: List['DyeColor']) -> 'Color': ...

    def mixColors(self, colors: List['Color']) -> 'Color': ...

    def __eq__(self, o: object) -> bool: ...

    def __hash__(self) -> int: ...

    def serialize(self) -> Dict[str, Union[int, str]]: ...

    @staticmethod
    def deserialize(map: Dict[str, Union[int, str]]) -> 'Color': ...

    def __str__(self) -> str: ...