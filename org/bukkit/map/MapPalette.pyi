from typing import Optional, Protocol, List
from java.awt import Color, Graphics2D, Image, BufferedImage
from com.google.common.base import Preconditions
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents the palette that map items use.
These fields are the base color ranges. Each entry corresponds to four
colors of varying shades with values entry to entry + 3.
"""
class MapPalette:
    colors: List[Color]

        @staticmethod
    def c(r: int, g: int, b: int) -> Color:
        ...

        @staticmethod
    def c(r: int, g: int, b: int, a: int) -> Color:
        ...

    @staticmethod
    def getDistance(c1: Color, c2: Color) -> float:
        ...

        @Deprecated(since="1.6.2")
    TRANSPARENT: int = 0

        @Deprecated(since="1.6.2")
    LIGHT_GREEN: int = 4

        @Deprecated(since="1.6.2")
    LIGHT_BROWN: int = 8

        @Deprecated(since="1.6.2")
    GRAY_1: int = 12

        @Deprecated(since="1.6.2")
    RED: int = 16

        @Deprecated(since="1.6.2")
    PALE_BLUE: int = 20

        @Deprecated(since="1.6.2")
    GRAY_2: int = 24

        @Deprecated(since="1.6.2")
    DARK_GREEN: int = 28

        @Deprecated(since="1.6.2")
    WHITE: int = 32

        @Deprecated(since="1.6.2")
    LIGHT_GRAY: int = 36

        @Deprecated(since="1.6.2")
    BROWN: int = 40

        @Deprecated(since="1.6.2")
    DARK_GRAY: int = 44

        @Deprecated(since="1.6.2")
    BLUE: int = 48

        @Deprecated(since="1.6.2")
    DARK_BROWN: int = 52

        @staticmethod
    def resizeImage(image: Optional[Image]) -> BufferedImage:
        ...

        @Deprecated(since="1.6.2")
    @staticmethod
    def imageToBytes(image: Image) -> byte:
        ...

    @Deprecated(since="1.6.2")
    @staticmethod
    def matchColor(r: int, g: int, b: int) -> int:
        ...

    @Deprecated(since="1.6.2")
    @staticmethod
    def matchColor(color: Color) -> int:
        ...

    @Deprecated(since="1.6.2")
        @staticmethod
    def getColor(index: int) -> Color:
        ...

    @staticmethod
    def setMapColorCache(mapColorCache: 'MapColorCache') -> None:
        ...

class MapColorCache(Protocol):
    def isCached(self) -> bool:
        ...

    @Deprecated(since="1.19")
    def matchColor(self, color: Color) -> int:
        ...