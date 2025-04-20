from typing import Optional, Protocol
from org.bukkit import Keyed, NamespacedKey, Registry, RegistryAware
from org.bukkit.util import OldEnum
from com.google.common.base import Preconditions
from com.google.common.collect import Lists

"""
Represents a cursor on a map.
"""
class MapCursor:
    x: int
    y: int
    direction: int
    visible: bool
    caption: Optional[str]
    type: 'MapCursor.Type'

    @Deprecated(since="1.6.2")
    def __init__(self, x: int, y: int, direction: int, type: int, visible: bool) -> None:
        ...

    def __init__(self, x: int, y: int, direction: int, type: 'MapCursor.Type', visible: bool) -> None:
        ...

    @Deprecated(since="1.13")
    def __init__(self, x: int, y: int, direction: int, type: int, visible: bool, caption: Optional[str]) -> None:
        ...

    def __init__(self, x: int, y: int, direction: int, type: 'MapCursor.Type', visible: bool, caption: Optional[str]) -> None:
        ...

    """
    Get the X position of this cursor.

    @return The X coordinate.
    """
    def get_x(self) -> int:
        ...

    """
    Get the Y position of this cursor.

    @return The Y coordinate.
    """
    def get_y(self) -> int:
        ...

    """
    Get the direction of this cursor.

    @return The facing of the cursor, from 0 to 15.
    """
    def get_direction(self) -> int:
        ...

    """
    Get the type of this cursor.

    @return The type (color/style) of the map cursor.
    """
    def get_type(self) -> 'MapCursor.Type':
        ...

    @Deprecated(since="1.6.2")
    def get_raw_type(self) -> int:
        ...

    """
    Get the visibility status of this cursor.

    @return True if visible, false otherwise.
    """
    def is_visible(self) -> bool:
        ...

    """
    Set the X position of this cursor.

    @param x The X coordinate.
    """
    def set_x(self, x: int) -> None:
        ...

    """
    Set the Y position of this cursor.

    @param y The Y coordinate.
    """
    def set_y(self, y: int) -> None:
        ...

    """
    Set the direction of this cursor.

    @param direction The facing of the cursor, from 0 to 15.
    """
    def set_direction(self, direction: int) -> None:
        ...

    """
    Set the type of this cursor.

    @param type The type (color/style) of the map cursor.
    """
    def set_type(self, type: 'MapCursor.Type') -> None:
        ...

    @Deprecated(since="1.6.2")
    def set_raw_type(self, type: int) -> None:
        ...

    """
    Set the visibility status of this cursor.

    @param visible True if visible.
    """
    def set_visible(self, visible: bool) -> None:
        ...

    """
    Gets the caption on this cursor.

    @return caption
    """
    def get_caption(self) -> Optional[str]:
        ...

    """
    Sets the caption on this cursor.

    @param caption new caption
    """
    def set_caption(self, caption: Optional[str]) -> None:
        ...


class Type(OldEnum, Keyed, RegistryAware, Protocol):
    PLAYER: 'Type'
    FRAME: 'Type'
    RED_MARKER: 'Type'
    BLUE_MARKER: 'Type'
    TARGET_X: 'Type'
    TARGET_POINT: 'Type'
    PLAYER_OFF_MAP: 'Type'
    PLAYER_OFF_LIMITS: 'Type'
    MANSION: 'Type'
    MONUMENT: 'Type'
    BANNER_WHITE: 'Type'
    BANNER_ORANGE: 'Type'
    BANNER_MAGENTA: 'Type'
    BANNER_LIGHT_BLUE: 'Type'
    BANNER_YELLOW: 'Type'
    BANNER_LIME: 'Type'
    BANNER_PINK: 'Type'
    BANNER_GRAY: 'Type'
    BANNER_LIGHT_GRAY: 'Type'
    BANNER_CYAN: 'Type'
    BANNER_PURPLE: 'Type'
    BANNER_BLUE: 'Type'
    BANNER_BROWN: 'Type'
    BANNER_GREEN: 'Type'
    BANNER_RED: 'Type'
    BANNER_BLACK: 'Type'
    RED_X: 'Type'
    VILLAGE_DESERT: 'Type'
    VILLAGE_PLAINS: 'Type'
    VILLAGE_SAVANNA: 'Type'
    VILLAGE_SNOWY: 'Type'
    VILLAGE_TAIGA: 'Type'
    JUNGLE_TEMPLE: 'Type'
    SWAMP_HUT: 'Type'
    TRIAL_CHAMBERS: 'Type'

    @staticmethod
    def get_type(key: str) -> 'Type':
        ...

    @Deprecated(since="1.21.4")
    def get_key(self) -> NamespacedKey:
        ...

    @Deprecated(since="1.6.2")
    def get_value(self) -> int:
        ...

    @Deprecated(since="1.6.2")
    @staticmethod
    def by_value(value: int) -> Optional['Type']:
        ...

    @Deprecated(since="1.21")
    @staticmethod
    def value_of(name: str) -> 'Type':
        ...

    @Deprecated(since="1.21")
    @staticmethod
    def values() -> list['Type']:
        ...