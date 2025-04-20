from org.bukkit import DyeColor
from typing import Protocol

"""
Tropical fish.
"""
class TropicalFish(Protocol):

    """
    Gets the color of the fish's pattern.

    @return: pattern color
    """
    def get_pattern_color(self) -> DyeColor:
        ...

    """
    Sets the color of the fish's pattern

    @param color: pattern color
    """
    def set_pattern_color(self, color: DyeColor) -> None:
        ...

    """
    Gets the color of the fish's body.

    @return: body color
    """
    def get_body_color(self) -> DyeColor:
        ...

    """
    Sets the color of the fish's body

    @param color: body color
    """
    def set_body_color(self, color: DyeColor) -> None:
        ...

    """
    Gets the fish's pattern.

    @return: pattern
    """
    def get_pattern(self) -> 'TropicalFish.Pattern':
        ...

    """
    Sets the fish's pattern

    @param pattern: new pattern
    """
    def set_pattern(self, pattern: 'TropicalFish.Pattern') -> None:
        ...

    """
    Enumeration of all different fish patterns. Refer to the
    <a href="https://minecraft.wiki/w/Fish">Minecraft Wiki</a>
    for pictures.
    """
    class Pattern:
        KOB: 'TropicalFish.Pattern'
        SUNSTREAK: 'TropicalFish.Pattern'
        SNOOPER: 'TropicalFish.Pattern'
        DASHER: 'TropicalFish.Pattern'
        BRINELY: 'TropicalFish.Pattern'
        SPOTTY: 'TropicalFish.Pattern'
        FLOPPER: 'TropicalFish.Pattern'
        STRIPEY: 'TropicalFish.Pattern'
        GLITTER: 'TropicalFish.Pattern'
        BLOCKFISH: 'TropicalFish.Pattern'
        BETTY: 'TropicalFish.Pattern'
        CLAYFISH: 'TropicalFish.Pattern'