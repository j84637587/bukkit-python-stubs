from typing import Dict, Optional, List
from org.bukkit import ChatColor
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a bitmap font drawable to a map.
"""
class MapFont:
    chars: Dict[chr, 'CharacterSprite']
    height: int
    malleable: bool

    def __init__(self) -> None:
        ...

    """
    Set the sprite for a given character.

    @param ch The character to set the sprite for.
    @param sprite The CharacterSprite to set.
    @raises IllegalStateException if this font is static.
    """
    def set_char(self, ch: chr, sprite: 'CharacterSprite') -> None:
        ...

    """
    Get the sprite for a given character.

    @param ch The character to get the sprite for.
    @return The CharacterSprite associated with the character, or None if
        there is none.
    """
        def get_char(self, ch: chr) -> Optional['CharacterSprite']:
        ...

    """
    Get the width of the given text as it would be rendered using this
    font.

    @param text The text.
    @return The width in pixels.
    """
    def get_width(self, text: str) -> int:
        ...

    """
    Get the height of this font.

    @return The height of the font.
    """
    def get_height(self) -> int:
        ...

    """
    Check whether the given text is valid.

    @param text The text.
    @return True if the string contains only defined characters, false
        otherwise.
    """
    def is_valid(self, text: str) -> bool:
        ...


"""
Represents the graphics for a single character in a MapFont.
"""
class CharacterSprite:
    width: int
    height: int
    data: List[bool]

    def __init__(self, width: int, height: int, data: List[bool]) -> None:
        ...

    """
    Get the value of a pixel of the character.

    @param row The row, in the range [0,8).
    @param col The column, in the range [0,8).
    @return True if the pixel is solid, false if transparent.
    """
    def get(self, row: int, col: int) -> bool:
        ...

    """
    Get the width of the character sprite.

    @return The width of the character.
    """
    def get_width(self) -> int:
        ...

    """
    Get the height of the character sprite.

    @return The height of the character.
    """
    def get_height(self) -> int:
        ...